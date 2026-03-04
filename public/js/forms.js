// Form submission handler for Savvy Dealer
// Sends form data to API endpoints via fetch

// Fetch form token (proves browser loaded the page)
let _formToken = null;
fetch('/api/form-token').then(r => r.json()).then(d => { _formToken = d.token; }).catch(() => {});

document.addEventListener('DOMContentLoaded', function() {
  // Inject honeypot field into all ajax forms
  document.querySelectorAll('form[data-ajax]').forEach(function(form) {
    if (!form.querySelector('input[name="website"]')) {
      var hp = document.createElement('div');
      hp.style.display = 'none';
      hp.setAttribute('aria-hidden', 'true');
      hp.innerHTML = '<input type="text" name="website" tabindex="-1" autocomplete="off">';
      form.appendChild(hp);
    }
  });

  document.querySelectorAll('form[data-ajax]').forEach(function(form) {
    form.addEventListener('submit', async function(e) {
      e.preventDefault();

      var btn = form.querySelector('button[type="submit"]');
      var originalText = btn.textContent;
      btn.textContent = 'Sending...';
      btn.disabled = true;

      var formData = new FormData(form);
      var data = Object.fromEntries(formData.entries());
      var endpoint = form.getAttribute('action') || '/api/lead-form';

      // Add form token
      if (_formToken) data.formToken = _formToken;

      // Add source page
      data.sourcePage = window.location.pathname;

      // Add reCAPTCHA token if available
      if (typeof grecaptcha !== 'undefined') {
        try {
          var siteKey = form.dataset.recaptchaSiteKey || document.querySelector('meta[name="recaptcha-site-key"]')?.content;
          if (siteKey) {
            var token = await grecaptcha.execute(siteKey, { action: 'lead_form_submit' });
            data.recaptchaToken = token;
          }
        } catch (err) {
          console.warn('reCAPTCHA failed, submitting without:', err);
        }
      }

      try {
        var resp = await fetch(endpoint, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(data),
        });
        var result = await resp.json();

        if (resp.ok && result.success) {
          form.innerHTML = '<div class="text-center py-8"><div class="text-4xl mb-4">&#10003;</div><h3 class="text-2xl font-bold text-green-600 mb-2">Thank You!</h3><p class="text-gray-600">' + (result.message || 'We will contact you shortly.') + '</p><p class="text-gray-500 text-sm mt-4">Or call us now: <a href="tel:8135013229" class="text-blue-600 font-semibold">(813) 501-3229</a></p></div>';
        } else {
          btn.textContent = originalText;
          btn.disabled = false;
          alert(result.error || 'Something went wrong. Please call us at (813) 501-3229.');
        }
      } catch (err) {
        btn.textContent = originalText;
        btn.disabled = false;
        alert('Unable to send. Please call us directly at (813) 501-3229.');
      }
    });
  });
});
