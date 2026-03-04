const express = require('express');
const path = require('path');
const crypto = require('crypto');
const compression = require('compression');
const app = express();

// --- Compression ---
app.use(compression());

// --- Security headers ---
app.use((req, res, next) => {
  res.setHeader('X-Content-Type-Options', 'nosniff');
  res.setHeader('X-Frame-Options', 'DENY');
  res.setHeader('Referrer-Policy', 'strict-origin-when-cross-origin');
  res.setHeader('Permissions-Policy', 'geolocation=(), microphone=(), camera=()');
  res.setHeader('Content-Security-Policy', [
    "default-src 'self'",
    "script-src 'self' 'unsafe-inline' https://www.google.com/recaptcha/ https://www.gstatic.com/recaptcha/ https://www.googletagmanager.com",
    "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com",
    "font-src 'self' https://fonts.gstatic.com",
    "img-src 'self' data: https://www.googletagmanager.com",
    "connect-src 'self' https://www.google.com https://www.googletagmanager.com https://region1.google-analytics.com",
    "frame-src https://www.google.com/recaptcha/ https://www.googletagmanager.com",
  ].join('; '));
  if (req.get('x-forwarded-proto') === 'https') {
    res.setHeader('Strict-Transport-Security', 'max-age=31536000; includeSubDomains');
  }
  next();
});

// --- HTTPS redirect (Cloud Run) ---
app.use((req, res, next) => {
  if (process.env.NODE_ENV === 'production' && req.get('x-forwarded-proto') && req.get('x-forwarded-proto') !== 'https') {
    return res.redirect(301, `https://${req.get('host')}${req.url}`);
  }
  next();
});

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// --- Blocked IPs ---
const BLOCKED_IPS = new Set([
  '80.94.95.173',
]);

app.use((req, res, next) => {
  const clientIp = req.headers['x-forwarded-for']?.split(',')[0]?.trim() || req.ip;
  if (BLOCKED_IPS.has(clientIp)) {
    console.warn(`[Blocked] Rejected request from banned IP ${clientIp}`);
    return res.status(403).end();
  }
  next();
});

// --- Legacy redirects ---
const REDIRECTS = {
  '/why-us': '/',
  '/home': '/',
  '/free-audit': '/book',
  '/automotive-seo': '/dealer-seo',
  '/nada': '/nada-show',
  '/contact': '/book',
  '/will-fords-separating-of-the-ev-business-be-cancer-for-ford-dealers': '/blog',
  '/how-dealers-should-evaluate-marketing-roi-and-agencies-12-practical-moves': '/blog',
  '/how-to-add-a-user-to-your-google-my-business': '/blog',
  '/yelp-content-review-filter': '/blog',
  '/savvy-dealer-tampa-floridas-newest-google-partner': '/blog',
  '/auto-market-insights-september-15th-2025': '/blog',
  '/how-to-add-a-user-to-your-facebook-business-page': '/blog',
  '/how-to-add-a-user-to-your-google-search-console': '/blog',
  '/car-dealership-inventory-on-google': '/vehicle-ads',
  '/reclaim-your-': '/blog',
  '/reclaim-your': '/blog',
  '/embed': '/',
  '/google-vehicle-ads': '/vehicle-ads',
};

app.use((req, res, next) => {
  const target = REDIRECTS[req.path];
  if (target) {
    return res.redirect(301, target + (req.query && Object.keys(req.query).length ? '?' + new URLSearchParams(req.query).toString() : ''));
  }
  // Prefix-based redirects
  if (req.path.startsWith('/embed/')) return res.redirect(301, '/');
  if (req.path.startsWith('/testimonial/')) return res.redirect(301, '/case-studies');
  next();
});

// --- Form token (proves browser loaded the page) ---
const FORM_TOKEN_SECRET = process.env.FORM_TOKEN_SECRET || crypto.randomBytes(32).toString('hex');
const FORM_TOKEN_MAX_AGE_MS = 30 * 60 * 1000; // 30 minutes

app.get('/api/form-token', (req, res) => {
  const timestamp = Date.now().toString();
  const sig = crypto.createHmac('sha256', FORM_TOKEN_SECRET).update(timestamp).digest('hex');
  res.json({ token: `${timestamp}.${sig}` });
});

function isValidFormToken(token) {
  if (!token || typeof token !== 'string') return false;
  const parts = token.split('.');
  if (parts.length !== 2) return false;
  const [timestamp, sig] = parts;
  const expected = crypto.createHmac('sha256', FORM_TOKEN_SECRET).update(timestamp).digest('hex');
  if (!crypto.timingSafeEqual(Buffer.from(sig, 'hex'), Buffer.from(expected, 'hex'))) return false;
  const age = Date.now() - parseInt(timestamp, 10);
  if (age < 0 || age > FORM_TOKEN_MAX_AGE_MS) return false;
  return true;
}

// --- IP rate limiting ---
const RATE_LIMIT_WINDOW_MS = 10 * 60 * 1000; // 10 minutes
const RATE_LIMIT_MAX = 5; // More form types than TLP
const ipSubmissions = new Map();

function isRateLimited(ip) {
  const now = Date.now();
  const record = ipSubmissions.get(ip);
  if (!record) {
    ipSubmissions.set(ip, { count: 1, windowStart: now });
    return false;
  }
  if (now - record.windowStart > RATE_LIMIT_WINDOW_MS) {
    ipSubmissions.set(ip, { count: 1, windowStart: now });
    return false;
  }
  record.count++;
  if (record.count > RATE_LIMIT_MAX) {
    console.warn(`[RateLimit] IP ${ip} exceeded ${RATE_LIMIT_MAX} submissions in ${RATE_LIMIT_WINDOW_MS / 60000} min`);
    return true;
  }
  return false;
}

setInterval(() => {
  const cutoff = Date.now() - RATE_LIMIT_WINDOW_MS;
  for (const [ip, record] of ipSubmissions) {
    if (record.windowStart < cutoff) ipSubmissions.delete(ip);
  }
}, 15 * 60 * 1000);

// --- reCAPTCHA verification ---
const RECAPTCHA_SCORE_THRESHOLD = 0.3;

async function verifyRecaptcha(token, expectedAction) {
  const secretKey = process.env.RECAPTCHA_SECRET_KEY;
  if (!secretKey) {
    console.warn('[reCAPTCHA] No secret key configured, skipping verification');
    return true;
  }
  if (!token) {
    console.warn('[reCAPTCHA] No token provided, deferring to honeypot check');
    return true;
  }
  try {
    const resp = await fetch('https://www.google.com/recaptcha/api/siteverify', {
      method: 'POST',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      body: `secret=${secretKey}&response=${token}`,
    });
    const data = await resp.json();
    console.log(`[reCAPTCHA] success=${data.success} score=${data.score} action=${data.action}`);
    if (!data.success) {
      console.warn('[reCAPTCHA] Verification failed, allowing submission (fail open). Errors:', data['error-codes']);
      return true;
    }
    if (data.score !== undefined && data.score < RECAPTCHA_SCORE_THRESHOLD) {
      console.warn(`[reCAPTCHA] Score too low (${data.score}), rejecting as likely bot`);
      return false;
    }
    return true;
  } catch (err) {
    console.error('[reCAPTCHA] Error (allowing submission):', err.message);
    return true;
  }
}

// --- Honeypot check ---
function isHoneypotFilled(body) {
  if (body.website && body.website.trim() !== '') {
    console.warn('[Honeypot] Bot detected - hidden field filled:', body.website);
    return true;
  }
  return false;
}

// --- Resend email ---
const FROM_EMAIL = process.env.FROM_EMAIL || 'contact@savvydealer.ai';
const TO_EMAIL = process.env.TO_EMAIL || 'support@savvydealer.com';
const TO_EMAILS = TO_EMAIL.split(',').map(e => e.trim());

async function sendEmail({ subject, html, replyTo }) {
  const apiKey = process.env.RESEND_API_KEY;
  if (!apiKey) {
    console.warn('[Email] No Resend API key, skipping');
    return { success: false, error: 'Email not configured' };
  }
  try {
    const resp = await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${apiKey}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        from: FROM_EMAIL,
        to: TO_EMAILS,
        subject,
        html,
        reply_to: replyTo,
      }),
    });
    const result = await resp.json();
    console.log(`[Email] Sent: ${result.id || 'ok'}`);
    return { success: true };
  } catch (err) {
    console.error('[Email] Error:', err.message);
    return { success: false, error: err.message };
  }
}

// --- Shared form validation middleware ---
function formGuard(req, res, next) {
  const { formToken } = req.body;
  const clientIp = req.headers['x-forwarded-for']?.split(',')[0]?.trim() || req.ip;

  if (!isValidFormToken(formToken)) {
    console.warn(`[FormToken] Invalid or missing form token from ${clientIp}`);
    return res.status(403).json({ error: 'Submission rejected' });
  }
  if (isRateLimited(clientIp)) {
    return res.status(429).json({ error: 'Too many submissions. Please try again later.' });
  }
  if (isHoneypotFilled(req.body)) {
    return res.status(403).json({ error: 'Submission rejected' });
  }
  next();
}

// --- API Routes ---

// Lead form (global contact/CTA form)
app.post('/api/lead-form', formGuard, async (req, res) => {
  const { recaptchaToken, name, email, phone, dealership, message, sourcePage } = req.body;

  const isHuman = await verifyRecaptcha(recaptchaToken, 'lead_form_submit');
  if (!isHuman) return res.status(403).json({ error: 'reCAPTCHA verification failed' });

  const result = await sendEmail({
    subject: `New Lead: ${name} - ${dealership || 'General Inquiry'}`,
    html: `
      <h2>New Lead from SavvyDealer.com</h2>
      <p><strong>Name:</strong> ${name || 'N/A'}</p>
      <p><strong>Email:</strong> ${email || 'N/A'}</p>
      <p><strong>Phone:</strong> ${phone || 'N/A'}</p>
      ${dealership ? `<p><strong>Dealership:</strong> ${dealership}</p>` : ''}
      ${message ? `<p><strong>Message:</strong></p><p>${message}</p>` : ''}
      ${sourcePage ? `<p><strong>Source Page:</strong> ${sourcePage}</p>` : ''}
      <hr><p style="color:#666;font-size:12px;">Submitted from savvydealer.com</p>
    `,
    replyTo: email,
  });

  if (result.success) {
    res.json({ success: true, message: 'Thank you! We will be in touch shortly.' });
  } else {
    res.status(500).json({ error: 'Failed to send message. Please try again.' });
  }
});

// Quick text (minimal fields)
app.post('/api/quick-text', formGuard, async (req, res) => {
  const { recaptchaToken, firstName, phone, message, sourcePage } = req.body;

  const isHuman = await verifyRecaptcha(recaptchaToken, 'lead_form_submit');
  if (!isHuman) return res.status(403).json({ error: 'reCAPTCHA verification failed' });

  const result = await sendEmail({
    subject: `Quick Text: ${firstName}`,
    html: `
      <h2>Quick Text from SavvyDealer.com</h2>
      <p><strong>Name:</strong> ${firstName || 'N/A'}</p>
      <p><strong>Phone:</strong> ${phone || 'N/A'}</p>
      ${message ? `<p><strong>Message:</strong></p><p>${message}</p>` : ''}
      ${sourcePage ? `<p><strong>Source Page:</strong> ${sourcePage}</p>` : ''}
      <hr><p style="color:#666;font-size:12px;">Submitted from savvydealer.com</p>
    `,
  });

  if (result.success) {
    res.json({ success: true, message: 'Thanks! We will text you back shortly.' });
  } else {
    res.status(500).json({ error: 'Failed to send message. Please try again.' });
  }
});

// Schedule demo (book a demo form)
app.post('/api/schedule-demo', formGuard, async (req, res) => {
  const { recaptchaToken, name, email, phone, dealership, date, time, sourcePage } = req.body;

  const isHuman = await verifyRecaptcha(recaptchaToken, 'lead_form_submit');
  if (!isHuman) return res.status(403).json({ error: 'reCAPTCHA verification failed' });

  const result = await sendEmail({
    subject: `Demo Request: ${name} - ${dealership || 'Unknown Dealership'}`,
    html: `
      <h2>New Demo Request from SavvyDealer.com</h2>
      <p><strong>Name:</strong> ${name || 'N/A'}</p>
      <p><strong>Email:</strong> ${email || 'N/A'}</p>
      <p><strong>Phone:</strong> ${phone || 'N/A'}</p>
      ${dealership ? `<p><strong>Dealership:</strong> ${dealership}</p>` : ''}
      ${date ? `<p><strong>Preferred Date:</strong> ${date}</p>` : ''}
      ${time ? `<p><strong>Preferred Time:</strong> ${time}</p>` : ''}
      ${sourcePage ? `<p><strong>Source Page:</strong> ${sourcePage}</p>` : ''}
      <hr><p style="color:#666;font-size:12px;">Submitted from savvydealer.com</p>
    `,
    replyTo: email,
  });

  if (result.success) {
    res.json({ success: true, message: 'Demo request received! We will confirm your time shortly.' });
  } else {
    res.status(500).json({ error: 'Failed to send request. Please try again.' });
  }
});

// Independent dealer demo request
app.post('/api/indie-demo-request', formGuard, async (req, res) => {
  const { recaptchaToken, name, email, phone, dealership, preferredDay, preferredTime, sourcePage } = req.body;

  const isHuman = await verifyRecaptcha(recaptchaToken, 'lead_form_submit');
  if (!isHuman) return res.status(403).json({ error: 'reCAPTCHA verification failed' });

  const result = await sendEmail({
    subject: `Indie Demo Request: ${name} - ${dealership || 'Independent Dealer'}`,
    html: `
      <h2>Independent Dealer Demo Request</h2>
      <p><strong>Name:</strong> ${name || 'N/A'}</p>
      <p><strong>Email:</strong> ${email || 'N/A'}</p>
      <p><strong>Phone:</strong> ${phone || 'N/A'}</p>
      ${dealership ? `<p><strong>Dealership:</strong> ${dealership}</p>` : ''}
      ${preferredDay ? `<p><strong>Preferred Day:</strong> ${preferredDay}</p>` : ''}
      ${preferredTime ? `<p><strong>Preferred Time:</strong> ${preferredTime}</p>` : ''}
      ${sourcePage ? `<p><strong>Source Page:</strong> ${sourcePage}</p>` : ''}
      <hr><p style="color:#666;font-size:12px;">Submitted from savvydealer.com</p>
    `,
    replyTo: email,
  });

  if (result.success) {
    res.json({ success: true, message: 'Demo request received! We will be in touch soon.' });
  } else {
    res.status(500).json({ error: 'Failed to send request. Please try again.' });
  }
});

// --- Static files ---
app.use(express.static(path.join(__dirname, 'public'), {
  extensions: ['html'],
  index: 'index.html',
  maxAge: '1d',
  setHeaders: (res, filePath) => {
    if (filePath.endsWith('.html')) {
      res.setHeader('Cache-Control', 'public, max-age=3600');
    }
  },
}));

// Clean URLs fallback - try .html extension
app.get('*', (req, res) => {
  const filePath = path.join(__dirname, 'public', req.path + '.html');
  res.sendFile(filePath, (err) => {
    if (err) {
      res.status(404).sendFile(path.join(__dirname, 'public', '404.html'), (err2) => {
        if (err2) res.status(404).send('Page not found');
      });
    }
  });
});

// --- Global error handler ---
app.use((err, req, res, next) => {
  console.error('[Server] Unhandled error:', err.message);
  res.status(500).json({ error: 'Internal server error' });
});

process.on('unhandledRejection', (reason) => {
  console.error('[Server] Unhandled rejection:', reason);
});

const PORT = process.env.PORT || 8080;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
