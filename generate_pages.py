"""Page generators for all static pages."""
from generate import (
    head, nav, footer, breadcrumb, cta_section, faq_section, org_schema,
    write_page, PHONE, PHONE_HREF, EMAIL, DOMAIN, COLORS
)

# ---------------------------------------------------------------------------
# Service page template (matches live site ProductPage.tsx)
# ---------------------------------------------------------------------------

def service_page(filename, data):
    """Generate a service/product page from a data dict."""
    d = data
    accent = d.get("accent_color", "#0088ff")
    faqs = [(q["question"], q["answer"]) for q in d.get("faqs", [])]
    hero_img = d.get("hero_image", "")
    hero_img_webp = d.get("hero_image_webp", "")

    # Benefits list (2-column grid like live site)
    benefits_html = ""
    for b in d.get("benefits", {}).get("items", []):
        benefits_html += f'''          <li class="flex items-start gap-3">
            <svg class="h-6 w-6 shrink-0" style="color:{accent}" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
            <span class="text-gray-600">{b}</span>
          </li>\n'''

    # Features grid (rounded icon containers like live site)
    features_html = ""
    for f in d.get("features", {}).get("items", []):
        features_html += f'''        <div class="rounded-xl border border-gray-200 bg-white p-8">
          <div class="mb-5 inline-flex h-12 w-12 items-center justify-center rounded-full" style="background-color:{accent}15;color:{accent}">
            <svg class="h-6 w-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/></svg>
          </div>
          <h3 class="font-serif text-xl font-bold mb-3">{f["title"]}</h3>
          <p class="text-gray-500 leading-relaxed">{f["description"]}</p>
        </div>\n'''

    # Stats
    stats_html = ""
    for s in d.get("proof_stats", {}).get("items", []):
        stats_html += f'''        <div class="rounded-xl border border-gray-200 bg-gray-50 p-6 text-center">
          <div class="font-serif text-4xl font-bold mb-2" style="color:{accent}">{s["stat"]}</div>
          <div class="text-sm text-gray-500">{s["label"]}</div>
        </div>\n'''

    # Process steps
    process_html = ""
    for s in d.get("process", {}).get("steps", []):
        process_html += f'''        <div class="flex gap-6">
          <div class="flex h-12 w-12 shrink-0 items-center justify-center rounded-lg font-serif text-2xl font-bold text-white" style="background-color:{accent}">{s["number"]}</div>
          <div>
            <h3 class="text-xl font-bold mb-2">{s["title"]}</h3>
            <p class="text-gray-500">{s["description"]}</p>
          </div>
        </div>\n'''

    seo_title = d.get("seo_meta_title", d["title"]) + " | Savvy Dealer"
    seo_desc = d.get("seo_meta_description", d.get("hero_description", ""))
    canonical = filename.replace(".html", "")

    # Hero image HTML
    hero_section = ""
    if hero_img:
        hero_section = f'''
    <!-- Hero -->
    <section class="relative flex min-h-[85vh] items-center justify-center overflow-hidden px-6 py-20 sm:px-8 lg:px-12">
      <picture class="absolute inset-0 z-0">
        {f'<source srcset="{hero_img_webp}" type="image/webp">' if hero_img_webp else ''}
        <img src="{hero_img}" alt="{d["title"]}" class="h-full w-full object-cover" loading="eager" fetchpriority="high">
      </picture>
      <div class="absolute inset-0 z-0" style="background:linear-gradient(to bottom, rgba(0,0,0,0.7), rgba(0,0,0,0.5))"></div>
      <div class="relative z-10 max-w-7xl mx-auto text-center">
        <div class="mx-auto max-w-5xl space-y-8">
          <div class="inline-flex items-center gap-2 rounded-full border border-white/20 bg-white/10 px-5 py-2.5 text-sm backdrop-blur-md">
            <span class="font-medium text-white">{d.get("badge", "")}</span>
          </div>
          <h1 class="font-serif text-4xl font-bold leading-tight text-white sm:text-5xl lg:text-6xl">{d["title"]}</h1>
          <p class="mx-auto max-w-3xl text-xl text-white/90 sm:text-2xl">{d["subtitle"]}</p>
          <p class="mx-auto max-w-3xl text-lg text-white/80">{d.get("hero_description", "")}</p>
          <div class="flex flex-col items-center justify-center gap-4 pt-4 sm:flex-row sm:gap-6">
            <a href="/book" class="inline-flex items-center justify-center min-h-[56px] w-full sm:w-auto rounded-full bg-white/95 px-10 text-base font-semibold text-[#0088ff] backdrop-blur-sm hover:bg-white transition">Request Free Audit</a>
            <a href="tel:{PHONE_HREF}" class="inline-flex items-center justify-center min-h-[56px] w-full sm:w-auto rounded-full border border-white/20 bg-white/10 px-10 text-base font-semibold text-white backdrop-blur-sm hover:bg-white/20 transition">Call {PHONE}</a>
          </div>
        </div>
      </div>
    </section>'''
    else:
        hero_section = f'''
    <!-- Hero -->
    <section class="relative flex min-h-[85vh] items-center justify-center overflow-hidden px-6 py-20 sm:px-8 lg:px-12" style="background:linear-gradient(135deg, #0a2540 0%, #1e3a5f 50%, {accent} 100%)">
      <div class="relative z-10 max-w-7xl mx-auto text-center">
        <div class="mx-auto max-w-5xl space-y-8">
          <div class="inline-flex items-center gap-2 rounded-full border border-white/20 bg-white/10 px-5 py-2.5 text-sm backdrop-blur-md">
            <span class="font-medium text-white">{d.get("badge", "")}</span>
          </div>
          <h1 class="font-serif text-4xl font-bold leading-tight text-white sm:text-5xl lg:text-6xl">{d["title"]}</h1>
          <p class="mx-auto max-w-3xl text-xl text-white/90 sm:text-2xl">{d["subtitle"]}</p>
          <p class="mx-auto max-w-3xl text-lg text-white/80">{d.get("hero_description", "")}</p>
          <div class="flex flex-col items-center justify-center gap-4 pt-4 sm:flex-row sm:gap-6">
            <a href="/book" class="inline-flex items-center justify-center min-h-[56px] w-full sm:w-auto rounded-full bg-white/95 px-10 text-base font-semibold text-[#0088ff] backdrop-blur-sm hover:bg-white transition">Request Free Audit</a>
            <a href="tel:{PHONE_HREF}" class="inline-flex items-center justify-center min-h-[56px] w-full sm:w-auto rounded-full border border-white/20 bg-white/10 px-10 text-base font-semibold text-white backdrop-blur-sm hover:bg-white/20 transition">Call {PHONE}</a>
          </div>
        </div>
      </div>
    </section>'''

    content = f'''{head(seo_title, seo_desc, canonical)}
{nav()}
  <main class="flex-1">
{breadcrumb([("Home", "/"), ("Products", "/products"), (d["title"], None)])}
{hero_section}

    <!-- Benefits -->
    <section class="py-24">
      <div class="max-w-7xl mx-auto px-6 sm:px-8 lg:px-12">
        <h2 class="font-serif text-3xl sm:text-4xl font-bold mb-12 text-center">{d.get("benefits", {}).get("title", "Why Choose Us")}</h2>
        <ul class="grid gap-4 md:grid-cols-2">
{benefits_html}        </ul>
      </div>
    </section>

    <!-- Features -->
    <section class="bg-gray-50 py-24">
      <div class="max-w-7xl mx-auto px-6 sm:px-8 lg:px-12">
        <div class="mb-12 text-center">
          <h2 class="font-serif text-3xl sm:text-4xl font-bold mb-4">{d.get("features", {}).get("title", "Features")}</h2>
          <p class="mx-auto max-w-2xl text-lg text-gray-500">{d.get("features", {}).get("description", "")}</p>
        </div>
        <div class="grid gap-8 md:grid-cols-2 lg:grid-cols-3">
{features_html}        </div>
      </div>
    </section>

    <!-- Stats -->
    <section class="py-24">
      <div class="max-w-7xl mx-auto px-6 sm:px-8 lg:px-12">
        <h2 class="font-serif text-3xl sm:text-4xl font-bold text-center mb-12">{d.get("proof_stats", {}).get("title", "By The Numbers")}</h2>
        <div class="grid gap-8 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4">
{stats_html}        </div>
      </div>
    </section>

    <!-- Process -->
    <section class="bg-gray-50 py-24">
      <div class="max-w-7xl mx-auto px-6 sm:px-8 lg:px-12">
        <h2 class="font-serif text-3xl sm:text-4xl font-bold mb-12 text-center">{d.get("process", {}).get("title", "Our Process")}</h2>
        <div class="mx-auto max-w-4xl space-y-8">
{process_html}        </div>
      </div>
    </section>

{faq_section(faqs) if faqs else ""}
{cta_section(d.get("cta", {}).get("title", "Ready to Dominate Your Market?"), d.get("cta", {}).get("description", ""))}
  </main>
{footer()}'''
    write_page(filename, content)


# ---------------------------------------------------------------------------
# Service page data
# ---------------------------------------------------------------------------

SERVICE_PAGES = {
    "facebook-ads.html": {
        "hero_image": "/images/Professional_hero_background_image_8c13e03a.png",
        "hero_image_webp": "/images/Professional_hero_background_image_8c13e03a.webp",
        "badge": "Social Media Advertising",
        "title": "Facebook Advertising For Auto Dealers",
        "subtitle": "Cost-Effective Lead Generation That Works While You Sleep",
        "hero_description": "7 out of 10 U.S. adults use Facebook. They're scrolling during commercials, in bed, even in your competitor's showroom. Reach them with hand-built, high-performing ads that target your current inventory.",
        "accent_color": "#FF4081",
        "seo_meta_title": "Facebook Advertising for Auto Dealers",
        "seo_meta_description": "Hand-built, high-performing Facebook ads that target your current inventory. Starting at $300/month. Capture leads while your competitors sleep.",
        "benefits": {
            "title": "Why Facebook Advertising Works for Dealerships",
            "items": [
                "7 out of 10 U.S. adults actively use Facebook",
                "World's third-most visited website",
                "Average user clicks 12 ads per month",
                "One of the most cost-effective advertising platforms",
                "Customers scroll throughout the day - capture their attention anytime",
                "Target customers even while they're at competitor dealerships",
                "Dynamic inventory advertising with hundreds of vehicles",
                "Management starting at just $300/month plus ad spend",
            ]
        },
        "features": {
            "title": "Our Proven Facebook Advertising Approach",
            "description": "We don't just run ads - we build strategic campaigns that perform. Our unique methodology focuses on perfecting performance before scaling.",
            "items": [
                {"title": "Build Backwards Methodology", "description": "We perfect ad performance scores with Facebook first, then scale. Unlike competitors who mass-produce ads and struggle to improve later."},
                {"title": "Organic-Style Ads", "description": "Our ads feel like organic posts, not spam. This prevents users from blocking your content and increases engagement rates."},
                {"title": "Dynamic Inventory Targeting", "description": "Advertise hundreds of vehicles simultaneously with dynamic targeting that focuses on current inventory that drives traffic."},
                {"title": "Constant Ad Rotation", "description": "We continuously rotate ads and inventory to prevent ad fatigue and maintain peak performance throughout your campaign."},
                {"title": "Complete Tracking Integration", "description": "Google Analytics, Facebook Pixel, and phone tracking provide complete visibility into campaign performance."},
                {"title": "Flexible OEM Compliance", "description": "We prioritize what performs best for your dealership first, then adapt to OEM requirements. Collaborative decision-making always."},
            ]
        },
        "proof_stats": {
            "title": "Facebook Advertising By The Numbers",
            "items": [
                {"stat": "70%", "label": "of U.S. adults use Facebook"},
                {"stat": "12", "label": "ads clicked per user monthly"},
                {"stat": "$300", "label": "minimum management fee/mo"},
                {"stat": "#3", "label": "most visited website globally"},
            ]
        },
        "process": {
            "title": "How We Build Your Facebook Campaign",
            "steps": [
                {"number": "1", "title": "Free Audit & Strategy", "description": "We diagnose why existing campaigns aren't performing and build a custom strategy."},
                {"number": "2", "title": "Perfect Performance First", "description": "Using our 'build backwards' approach, we perfect ad performance scores before scaling spend."},
                {"number": "3", "title": "Launch Dynamic Inventory Ads", "description": "Deploy ads targeting hundreds of vehicles simultaneously, focusing on inventory that drives traffic."},
                {"number": "4", "title": "Monitor, Rotate, Optimize", "description": "Continuous monitoring with constant ad and inventory rotation prevents fatigue and maintains peak performance."},
            ]
        },
        "cta": {"title": "Ready to Capture More Leads from Facebook?", "description": "Get a free audit of your current Facebook advertising and discover why your campaigns may not be targeting the right inventory."},
        "faqs": [
            {"question": "How much does Facebook advertising cost for car dealerships?", "answer": "Our Facebook advertising management starts at $300/month plus your ad spend budget. Most dealerships see effective results with ad budgets ranging from $1,000-$5,000/month depending on market size and goals."},
            {"question": "How do Facebook ads target car buyers?", "answer": "We use dynamic inventory targeting to show your actual vehicles to people actively shopping for cars. Our ads target based on demographics, interests, behaviors, and location."},
            {"question": "Why do Facebook ads look like organic posts?", "answer": "Ads that feel like organic content get higher engagement and prevent users from blocking your dealership. Our organic-style approach keeps your ads visible and effective long-term."},
            {"question": "How quickly will I see results from Facebook ads?", "answer": "Most dealerships see initial leads within the first week. We use our build backwards methodology to perfect ad performance before scaling."},
            {"question": "Can you advertise my specific inventory on Facebook?", "answer": "Yes! Our dynamic inventory ads showcase hundreds of your vehicles simultaneously. As inventory changes, ads automatically update to feature your current stock."},
        ]
    },
    "dealer-seo.html": {
        "hero_image": "/images/Professional_hero_background_image_8c13e03a.png",
        "hero_image_webp": "/images/Professional_hero_background_image_8c13e03a.webp",
        "badge": "Search Engine Optimization",
        "title": "Dealer SEO + GEO Strategy",
        "subtitle": "Appear First in Google AND ChatGPT",
        "hero_description": "By aligning our SEO and GEO (Generative Engine Optimization) strategies, we ensure your dealership doesn't just compete - it appears first and performs faster wherever shoppers are searching, from Google to ChatGPT.",
        "accent_color": "#00E676",
        "seo_meta_title": "Dealer SEO + GEO Strategy - Appear First in Google AND ChatGPT",
        "seo_meta_description": "Combined SEO and GEO ensures your dealership appears first in traditional Google search AND AI-powered results from ChatGPT, Gemini, and Perplexity.",
        "benefits": {
            "title": "SEO + GEO: The New Standard For Dealer Visibility",
            "items": [
                "Appear in AI-generated answers from ChatGPT, Google Gemini, and Perplexity",
                "Dominate traditional Google search results with proven SEO",
                "85% of car buyers research online before purchasing",
                "Answer-first content optimized for AI recommendations",
                "Original, Google-friendly content creation for organic growth",
                "Combined SEO/SEM management for maximum visibility",
                "75%+ of shoppers expected to use AI tools by end of 2025",
                "National keyword rankings for brand search terms",
            ]
        },
        "features": {
            "title": "Dual Optimization Strategy",
            "description": "Traditional SEO gets you ranked on Google. GEO ensures AI chatbots recommend your dealership when buyers ask questions. Together, they create complete search dominance.",
            "items": [
                {"title": "Generative Engine Optimization (GEO)", "description": "Optimize your content to appear in AI-generated answers from ChatGPT, Google Gemini, Perplexity, and other LLMs that car buyers trust."},
                {"title": "Traditional SEO Excellence", "description": "Proven search engine optimization strategies that deliver rankings, traffic, and leads from Google and Bing search results."},
                {"title": "Answer-First Content", "description": "AI loves clarity. We structure content to directly answer buyer questions, then add context - exactly what LLMs and search engines want."},
                {"title": "Conversational Long-Tail Keywords", "description": "Target specific buyer questions like 'best electric SUVs for winter driving' instead of generic terms."},
                {"title": "Local Authority Building", "description": "Create hyper-local content addressing community-specific questions. AI prioritizes relevant, helpful answers tied to location."},
                {"title": "Schema Markup Optimization", "description": "Perfect your schema.org markup so AI tools accurately represent your dealership."},
            ]
        },
        "proof_stats": {
            "title": "SEO + GEO Impact",
            "items": [
                {"stat": "85%", "label": "of buyers research online"},
                {"stat": "75%+", "label": "will use AI tools by 2025"},
                {"stat": "66%", "label": "traffic increase (client)"},
                {"stat": "100%", "label": "Google-friendly content"},
            ]
        },
        "process": {
            "title": "Our SEO + GEO Process",
            "steps": [
                {"number": "1", "title": "Audit & AI Visibility Check", "description": "Analyze current search rankings AND test how your dealership appears in AI-generated responses."},
                {"number": "2", "title": "Content Strategy Development", "description": "Build answer-first content targeting conversational buyer questions. Optimize schema markup."},
                {"number": "3", "title": "Implementation & Optimization", "description": "Deploy optimized content, perfect schema.org markup, and build local authority."},
                {"number": "4", "title": "Monitor & Refine", "description": "Track rankings in Google AND visibility in AI-generated answers. Continuously refine."},
            ]
        },
        "cta": {"title": "Ready to Dominate Both Google AND AI Search?", "description": "Discover how our combined SEO + GEO strategy ensures your dealership appears first wherever car buyers are searching."},
        "faqs": [
            {"question": "What is GEO (Generative Engine Optimization)?", "answer": "GEO is optimization for AI-powered search tools like ChatGPT, Google Gemini, and Perplexity. As more car buyers use AI to research vehicles, GEO ensures your dealership appears in AI-generated recommendations."},
            {"question": "How is SEO different from GEO?", "answer": "SEO focuses on ranking in traditional search engines. GEO optimizes content so AI chatbots recommend your dealership. Together, they ensure visibility wherever buyers search."},
            {"question": "How long does SEO take to show results?", "answer": "Most dealerships see measurable improvements in 3-6 months, with significant results in 6-12 months. We focus on quick wins first while building long-term authority."},
            {"question": "Do car dealerships need local SEO?", "answer": "Absolutely. 85% of car buyers research online before visiting. Local SEO ensures you appear in 'near me' searches and Google Maps."},
            {"question": "What is schema markup for auto dealers?", "answer": "Schema markup is structured data that helps search engines understand your dealership. We implement AutoDealer schema, vehicle inventory markup, and local business data."},
        ]
    },
    "ppc-ads.html": {
        "hero_image": "/images/Professional_hero_background_image_8c13e03a.png",
        "hero_image_webp": "/images/Professional_hero_background_image_8c13e03a.webp",
        "badge": "Paid Search Advertising",
        "title": "PPC & SEM Advertising For Auto Dealers",
        "subtitle": "We Dominate Markets. We Don't Share Them.",
        "hero_description": "90% search term-to-keyword match. Your ads align with what you're selling - not AI-generated junk like headlight repair kits. We route competitor traffic to your dealership with exclusive market control.",
        "accent_color": "#FF6B35",
        "seo_meta_title": "PPC & SEM Advertising for Auto Dealers - Market Dominance Strategy",
        "seo_meta_description": "90% search term-to-keyword match. Exclusive market control with competitor keyword intelligence. We dominate your market - no shared visibility.",
        "benefits": {
            "title": "Strategic Market Dominance Through Precision Targeting",
            "items": [
                "90% search term-to-keyword match - your ads align with what you sell",
                "Competitor keyword intelligence from unique campaign structure",
                "Exclusive market control - we don't take competing dealers in your market",
                "Expert traffic routing from competitors to your dealership",
                "Market share dominance, not shared visibility",
                "See what competitors bid on at the keyword level",
                "No AI-generated junk ads for headlight repair kits",
                "Strategic exclusivity ensures we work for you, not your competition",
            ]
        },
        "features": {
            "title": "Precision Targeting Meets Strategic Market Control",
            "description": "Our unique campaign structure gives you competitor intelligence at the keyword level while ensuring 90% search term-to-keyword match.",
            "items": [
                {"title": "90% Search Term Match", "description": "Your ads align with what you're actually selling. No AI-generated garbage. Precision targeting that converts."},
                {"title": "Competitor Keyword Intelligence", "description": "See what your competitors bid on at the keyword level. Our unique campaign structure reveals their strategy."},
                {"title": "Exclusive Market Control", "description": "We don't take competing dealerships in your market. Period. Your success is our only focus."},
                {"title": "Expert Traffic Routing", "description": "We're experts at routing competitor traffic to your dealership through strategic bidding and targeting."},
                {"title": "Market Share Dominance", "description": "We dominate market share in our markets - we don't share it. Strategic exclusivity means you own your territory."},
                {"title": "Campaign Structure Advantage", "description": "Proprietary campaign architecture enables real-time competitor analysis and precision adjustments."},
            ]
        },
        "proof_stats": {
            "title": "Market Dominance Metrics",
            "items": [
                {"stat": "90%", "label": "search term-to-keyword match"},
                {"stat": "100%", "label": "market exclusivity guarantee"},
                {"stat": "Keyword", "label": "level competitor intelligence"},
                {"stat": "Zero", "label": "competing dealers in market"},
            ]
        },
        "process": {
            "title": "How We Dominate Your Market",
            "steps": [
                {"number": "1", "title": "Market Exclusivity Review", "description": "We verify no competing dealerships in your market before engagement."},
                {"number": "2", "title": "Competitor Intelligence Mapping", "description": "Identify competitor keywords at granular level using our unique campaign structure."},
                {"number": "3", "title": "Precision Campaign Build", "description": "90% search term-to-keyword match architecture with precision targeting that converts."},
                {"number": "4", "title": "Traffic Routing & Dominance", "description": "Deploy strategic bidding to route competitor traffic to you. Continuous optimization."},
            ]
        },
        "cta": {"title": "Ready to Own Your Market?", "description": "Discover how our exclusive market approach and 90% precision matching can route competitor traffic to your dealership."},
        "faqs": [
            {"question": "What is the search term-to-keyword match rate?", "answer": "Most agencies achieve 50-70%. Savvy Dealer maintains 90%, ensuring your ads align with what you're selling."},
            {"question": "How do you handle competitor keywords?", "answer": "Our unique campaign structure provides competitor keyword intelligence at the keyword level, letting us strategically route their traffic to you."},
            {"question": "Do you work with multiple dealers in the same market?", "answer": "No. We offer exclusive market control. We don't take competing dealerships in your market. Period."},
            {"question": "What makes dealer PPC different from regular PPC?", "answer": "Automotive PPC requires inventory-level precision, understanding of buying cycles, and conquest strategies for competitor traffic."},
            {"question": "How do you prevent wasted ad spend?", "answer": "Through precise keyword matching, aggressive negative keyword management, and inventory-aligned campaigns."},
        ]
    },
    "vehicle-ads.html": {
        "hero_image": "/images/Professional_hero_background_image_8c13e03a.png",
        "hero_image_webp": "/images/Professional_hero_background_image_8c13e03a.webp",
        "badge": "Vehicle Listing Ads",
        "title": "Stop Setting Your VLA Budget on Fire",
        "subtitle": "Get a Free Waste Audit & Reclaim Thousands in Wasted Ad Spend",
        "hero_description": "Are your Vehicle Ads just funding Google's banner ad network? Dealers are wasting thousands every month on low-intent clicks from Performance Max. We'll show you exactly where your budget is going - and how to fix it.",
        "seo_meta_title": "Google Vehicle Ads (VLA) Management - Stop Wasting Your Budget",
        "seo_meta_description": "Stop wasting thousands on Performance Max display ads. Expert VLA management that focuses your budget on high-intent Google Search and Shopping placements.",
        "benefits": {
            "title": "The Performance Max Problem",
            "items": [
                "VLAs now run through Google's 'black box' Performance Max system",
                "Your ads appear on millions of low-value banner websites",
                "Most agencies 'set it and forget it' - letting Google waste your budget",
                "Algorithm finds the cheapest clicks, not the best leads",
                "Your click numbers look good, but VSRs don't budge",
                "You're paying for 'brand awareness' instead of capturing leads",
                "Thousands wasted monthly on the Google Display Network",
                "No transparency into where your budget actually goes",
            ]
        },
        "features": {
            "title": "What Sets Our VLA Management Apart",
            "description": "We don't 'set and forget.' We actively fight the black box to make your VLA budget work for you.",
            "items": [
                {"title": "Aggressive Spend Containment", "description": "We actively minimize budget waste on the Google Display Network and force your ad dollars to compete where it matters: high-intent Google Search and Shopping."},
                {"title": "Meticulous Feed Optimization", "description": "The single most important factor in VLA success. We meticulously clean, optimize, and manage your feed for every vehicle."},
                {"title": "Total Google Domination", "description": "Our VLA strategy works with your Google Business Profile and PPC campaigns for an impenetrable 'Google Domination' effect."},
                {"title": "High-Intent Focus", "description": "Your VLA budget should capture high-intent shoppers at the bottom of the funnel, not fund Google's banner network."},
                {"title": "Transparent Reporting", "description": "We show you exactly where your budget is going. Plain English reporting that reveals waste and demonstrates value."},
                {"title": "Budget Recapture Strategy", "description": "We identify and eliminate thousands in monthly waste, then reallocate to high-performing placements."},
            ]
        },
        "proof_stats": {
            "title": "Stop Guessing. Start Capturing.",
            "items": [
                {"stat": "$1000s", "label": "wasted monthly on display ads"},
                {"stat": "0%", "label": "transparency from 'black box'"},
                {"stat": "100%", "label": "feed optimization per vehicle"},
                {"stat": "3x", "label": "coverage: paid + organic + maps"},
            ]
        },
        "process": {
            "title": "Get Your Free VLA Waste Audit",
            "steps": [
                {"number": "1", "title": "Free Waste Analysis", "description": "We analyze your current VLA or Performance Max campaign and show you where your budget is being wasted."},
                {"number": "2", "title": "Clear Action Plan", "description": "Receive a detailed plan to capture more high-intent shoppers. No obligation. No sales pitch. Just data."},
                {"number": "3", "title": "Feed Optimization", "description": "We meticulously clean and optimize your inventory feed - perfect pricing, high-res photos, complete attributes."},
                {"number": "4", "title": "Active Campaign Management", "description": "We actively manage campaigns to minimize Display Network waste and maximize Search and Shopping placements."},
            ]
        },
        "cta": {"title": "Stop Funding Google's Banner Network", "description": "Get a free waste audit and discover exactly how much of your VLA budget is disappearing into low-value clicks."},
        "faqs": [
            {"question": "What are Google Vehicle Listing Ads (VLA)?", "answer": "Google VLAs display your actual inventory with photos, prices, and details directly in Google Search and Shopping results for high-intent car shoppers."},
            {"question": "Why is my VLA budget going to the Display Network?", "answer": "VLAs run through Performance Max which often sends budget to low-value banner placements. Without active management, the algorithm finds cheapest clicks, not best leads."},
            {"question": "How do you prevent VLA budget waste?", "answer": "We use aggressive spend containment strategies to minimize Display Network waste and force budget toward high-intent placements."},
            {"question": "How important is the inventory feed?", "answer": "The data feed is the single most important factor in VLA success. We meticulously optimize every vehicle listing."},
            {"question": "How do VLAs work with other Google advertising?", "answer": "Our VLA strategy integrates with your Google Business Profile and PPC campaigns for a 'Google Domination' effect across all placements."},
        ]
    },
    "dealer-websites.html": {
        "hero_image": "/images/Professional_hero_background_image_8c13e03a.png",
        "hero_image_webp": "/images/Professional_hero_background_image_8c13e03a.webp",
        "badge": "Website Solutions",
        "title": "AI-Optimized Dealer Websites",
        "subtitle": "Built For Performance, Not Politics",
        "hero_description": "SEO-first architecture with lightning-fast load times. Our custom dealer websites deliver 2x the traffic of average dealer sites while meeting Google's Core Web Vitals - without OEM restrictions holding you back.",
        "seo_meta_title": "AI-Optimized Dealer Websites - Built For Performance",
        "seo_meta_description": "SEO-first dealer websites with lightning-fast load times. Meet Google Core Web Vitals. Deliver 2x average traffic. No OEM restrictions.",
        "benefits": {
            "title": "Why Our Dealer Websites Outperform",
            "items": [
                "SEO-first architecture optimized for search from day one",
                "Lightning-fast load times meeting Google Core Web Vitals",
                "2x traffic compared to average dealer websites",
                "Mobile-optimized responsive design across all devices",
                "No OEM restrictions - built for your needs first",
                "Custom features requested by sales managers get implemented",
                "Built-in SEO on every page for maximum visibility",
                "Direct inventory system integrations",
            ]
        },
        "features": {
            "title": "Built For Performance",
            "description": "Born out of frustration with large website providers who couldn't keep up with Google's evolving requirements.",
            "items": [
                {"title": "Lightning-Fast Performance", "description": "Optimized to meet Google's Core Web Vitals standards. Fast page loads improve search rankings and conversion rates."},
                {"title": "SEO-First Architecture", "description": "Every page is built with search optimization in mind. SEO is fundamental to our design approach."},
                {"title": "2x Average Traffic", "description": "Our websites consistently deliver double the traffic of average dealer sites through superior optimization."},
                {"title": "No OEM Restrictions", "description": "We build what performs best for your dealership first, then adapt to OEM requirements."},
                {"title": "Dealer-Driven Features", "description": "Features requested by actual sales managers and internet managers get implemented."},
                {"title": "Mobile-First Design", "description": "Fully responsive design optimized for mobile devices where most car buyers research."},
            ]
        },
        "proof_stats": {
            "title": "Website Performance Stats",
            "items": [
                {"stat": "2x", "label": "traffic vs average dealer sites"},
                {"stat": "100%", "label": "Core Web Vitals optimized"},
                {"stat": "66%", "label": "traffic increase (client result)"},
                {"stat": "100%", "label": "mobile-optimized responsive"},
            ]
        },
        "process": {
            "title": "Our Website Development Process",
            "steps": [
                {"number": "1", "title": "Discovery & Requirements", "description": "We understand your dealership needs, inventory systems, and OEM requirements."},
                {"number": "2", "title": "SEO-First Development", "description": "Build your website with search optimization and Core Web Vitals as fundamental priorities."},
                {"number": "3", "title": "Integration & Testing", "description": "Connect inventory systems, test across devices, and optimize load times."},
                {"number": "4", "title": "Launch & Optimize", "description": "Deploy your website and continuously optimize based on performance data."},
            ]
        },
        "cta": {"title": "Ready For a Website That Actually Performs?", "description": "Discover how our SEO-first dealer websites deliver double the traffic while meeting Google's Core Web Vitals."},
        "faqs": [
            {"question": "What makes a dealer website SEO-optimized?", "answer": "Fast load times, proper schema markup, mobile responsiveness, clean URL structures, and content architecture designed for search engines."},
            {"question": "How fast should a dealership website load?", "answer": "Google recommends under 2.5 seconds for LCP. Our dealer websites consistently score in the 'Good' range for all Core Web Vitals."},
            {"question": "Do I need OEM approval?", "answer": "We build sites that prioritize performance first, then adapt to OEM requirements when needed."},
            {"question": "Can I request custom features?", "answer": "Absolutely. Unlike template solutions, we build custom features based on what your sales team actually needs."},
            {"question": "How does website speed affect car sales?", "answer": "53% of mobile users abandon sites that take over 3 seconds to load. Fast websites keep shoppers engaged."},
        ]
    },
    "fully-managed-marketing.html": {
        "hero_image": "/images/Fully_managed_marketing_orange_theme_c07bcc36.png",
        "hero_image_webp": "/images/Fully_managed_marketing_orange_theme_c07bcc36.webp",
        "badge": "Premium Service",
        "title": "Complete Automotive Marketing Solution",
        "subtitle": "Focus on selling cars. We'll handle everything else.",
        "hero_description": "From co-op management to vendor coordination, website optimization to ROI tracking - we deliver comprehensive white-glove service that eliminates hassles and maximizes results.",
        "seo_meta_title": "Fully Managed Marketing - Complete Automotive Marketing Solution",
        "seo_meta_description": "Focus on selling cars while we handle everything. Co-op management, vendor coordination, website optimization, SEO, PPC, social media, design, and ROI tracking.",
        "benefits": {
            "title": "Everything You Need",
            "items": [
                "Single point of contact for all marketing needs",
                "Co-op advertising management and optimization",
                "Complete 3rd party vendor coordination",
                "Website management and continuous optimization",
                "SEO and GEO (Generative Engine Optimization)",
                "SEM/PPC campaign management across all platforms",
                "Facebook and social media advertising",
                "Professional graphic design and creative services",
                "Comprehensive ROI tracking and transparent reporting",
                "Dedicated account manager who knows your business",
                "Quarterly strategy sessions to stay ahead",
                "No vendor juggling - we coordinate everything",
            ]
        },
        "features": {
            "title": "White-Glove Service",
            "description": "One team, one strategy, one report. No more conflicting advice from multiple vendors.",
            "items": [
                {"title": "Single Source of Truth", "description": "One team, one strategy, one report. No more conflicting advice from multiple vendors."},
                {"title": "Co-op Mastery", "description": "We maximize every dollar of your co-op funds, handling compliance, documentation, and strategy."},
                {"title": "Vendor Wrangling", "description": "Stop playing middleman between your website provider, inventory feed, CRM, and other vendors."},
                {"title": "Website Excellence", "description": "Continuous optimization of your dealer website - speed, SEO, conversions, content, and user experience."},
                {"title": "Multi-Channel Mastery", "description": "Expert management of SEO, GEO, PPC, Facebook Ads, and emerging channels."},
                {"title": "Performance Accountability", "description": "Clear attribution from click to close, with transparent reporting on what's working."},
            ]
        },
        "proof_stats": {
            "title": "By The Numbers",
            "items": [
                {"stat": "8+", "label": "Services included"},
                {"stat": "1", "label": "Dedicated account manager"},
                {"stat": "100%", "label": "Co-op fund maximization"},
                {"stat": "Monthly", "label": "Performance reports"},
            ]
        },
        "process": {
            "title": "How It Works",
            "steps": [
                {"number": "1", "title": "Comprehensive Audit & Discovery", "description": "Deep dive into your current marketing ecosystem, vendor relationships, and competitive landscape."},
                {"number": "2", "title": "Strategic Roadmap Development", "description": "Custom 90-day plan prioritizing quick wins while building long-term advantage."},
                {"number": "3", "title": "Seamless Takeover & Optimization", "description": "We handle all vendor transitions, account migrations, and system integrations."},
                {"number": "4", "title": "Ongoing Management & Reporting", "description": "Continuous optimization with monthly reporting and quarterly strategy sessions."},
            ]
        },
        "cta": {"title": "Ready to Simplify Your Marketing?", "description": "Get a comprehensive audit showing exactly where you're leaving money on the table."},
        "faqs": [
            {"question": "What does fully managed marketing include?", "answer": "Website management, SEO/GEO optimization, paid advertising (Facebook, Google, VLA), co-op management, creative production, analytics reporting, and strategic consulting."},
            {"question": "How do you handle co-op advertising?", "answer": "We manage the entire co-op process - from planning campaigns that qualify for reimbursement to submitting documentation and tracking approvals."},
            {"question": "What kind of ROI can I expect?", "answer": "Clients typically see 2-3x return on ad spend. We provide transparent attribution reporting so you can see which campaigns drive sales."},
            {"question": "Do I need to hire a marketing person?", "answer": "No. Our fully managed service replaces the need for an in-house marketing team."},
            {"question": "How often will I hear from you?", "answer": "Monthly performance reports and strategy calls. Direct access to your account manager for urgent matters."},
        ]
    },
}


# ---------------------------------------------------------------------------
# Non-service pages
# ---------------------------------------------------------------------------

def generate_home():
    # Products for alternating grid (matches Home.tsx features section)
    products = [
        ("Fully Managed Marketing", "Complete Marketing Solution", "White-glove service that handles everything - co-op management, vendor coordination, website, SEO, SEM, Facebook ads, design, and ROI tracking.", "/fully-managed-marketing", "#FF6B35", "Fully_managed_marketing_orange_theme_c07bcc36", "Sparkles"),
        ("Dealer Websites", "AI-Optimized Dealer Websites", "SEO-first website architecture with lightning-fast load times, meeting Core Web Vitals and built for both human visitors and AI crawlers.", "/dealer-websites", "#0088FF", "Dealer_Websites_blue_theme_2aaf45c2", "Globe"),
        ("Dealer SEO + GEO", "Search + AI Optimization", "Combined SEO and Generative Engine Optimization for visibility in Google AND AI-powered search like ChatGPT, Perplexity, and Gemini.", "/dealer-seo", "#00E676", "SEO_green_theme_1cae63d8", "Search"),
        ("Facebook Ads", "Social Media Advertising", "Hand-built, high-performing Facebook ads targeting current dealer inventory. Starting at $300/month.", "/facebook-ads", "#FF4081", "Facebook_Ads_pink_theme_3fd45300", "Facebook"),
        ("PPC Ads", "Pay-Per-Click Advertising", "90% search term-to-keyword match with exclusive market control and competitor keyword intelligence.", "/ppc-ads", "#FF6B35", "PPC_Ads_orange_theme_7bcb5a76", "TrendingUp"),
        ("Vehicle Ads", "Vehicle Listing Ads", "Expert Performance Max management that eliminates budget waste on Google's Display Network.", "/vehicle-ads", "#00D4D4", "Vehicle_Ads_teal_theme_1273b0d6", "Car"),
    ]

    products_html = ""
    for i, (name, badge, desc, url, color, img_base, icon) in enumerate(products):
        is_reversed = i % 2 == 1
        order_img = "order-1 lg:order-2" if not is_reversed else "order-1 lg:order-1"
        order_text = "order-2 lg:order-1" if not is_reversed else "order-2 lg:order-2"

        products_html += f'''
    <section class="py-24">
      <div class="max-w-7xl mx-auto px-6 sm:px-8 lg:px-12">
        <div class="grid items-center gap-12 lg:grid-cols-2">
          <div class="{order_text}">
            <div class="inline-flex items-center gap-3 rounded-full border border-gray-200 px-4 py-2 mb-6">
              <span class="text-sm font-semibold uppercase tracking-wide text-gray-500">{badge}</span>
            </div>
            <h2 class="font-serif text-4xl font-bold leading-tight sm:text-5xl mb-6">{name}</h2>
            <p class="text-lg sm:text-xl text-gray-500 mb-8">{desc}</p>
            <div class="flex flex-col gap-4 pt-4 sm:flex-row sm:gap-6">
              <a href="{url}" class="inline-flex items-center justify-center min-h-[48px] rounded-full px-8 bg-[#0088ff] text-white font-semibold hover:bg-[#0077e6] transition">Learn More</a>
              <a href="/book" class="inline-flex items-center justify-center min-h-[48px] rounded-full px-8 border border-gray-200 text-gray-900 font-semibold hover:bg-gray-50 transition">Request Audit</a>
            </div>
          </div>
          <div class="{order_img}">
            <div class="relative overflow-hidden rounded-3xl">
              <picture>
                <source srcset="/images/{img_base}.webp" type="image/webp">
                <img src="/images/{img_base}.png" alt="{name}" class="h-full w-full object-cover" loading="lazy">
              </picture>
              <div class="absolute inset-0" style="background:linear-gradient(135deg, {color} 0%, transparent 100%);opacity:0.1"></div>
            </div>
          </div>
        </div>
      </div>
    </section>\n'''

    content = f'''{head("Savvy Dealer - Digital Marketing for Automotive Dealerships", "Expert digital marketing for car dealerships. Facebook Ads, PPC, SEO/GEO optimization, and AI-powered dealer websites. We don't outspend the competition - we outsmart them.", "")}
{nav()}
  <main class="flex-1">
    <!-- Hero -->
    <section class="relative flex min-h-screen items-center justify-center overflow-hidden">
      <picture class="absolute inset-0 z-0">
        <source srcset="/images/Automotive_dealership_hero_image_d17995ec.webp" type="image/webp">
        <img src="/images/Automotive_dealership_hero_image_d17995ec.png" alt="Automotive dealership" class="h-full w-full object-cover" loading="eager" fetchpriority="high">
      </picture>
      <div class="absolute inset-0 z-0 bg-gradient-to-b from-black/50 via-black/30 to-black/50"></div>
      <div class="relative z-10 max-w-7xl mx-auto px-6 py-32 text-center sm:px-8 lg:px-12">
        <div class="mx-auto max-w-5xl space-y-10">
          <div class="inline-flex items-center gap-2 rounded-full border border-white/20 bg-white/10 px-5 py-2.5 text-sm backdrop-blur-md">
            <svg class="h-4 w-4 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 3v4M3 5h4M6 17v4m-2-2h4m5-16l2.286 6.857L21 12l-5.714 2.143L13 21l-2.286-6.857L5 12l5.714-2.143L13 3z"/></svg>
            <span class="font-medium text-white">Digital Marketing for Auto Dealers</span>
          </div>
          <h1 class="font-serif text-6xl font-bold leading-[1.1] tracking-tight text-white sm:text-7xl lg:text-8xl">The Savvy Dealer<br>Difference</h1>
          <p class="mx-auto max-w-3xl text-xl text-white/90 sm:text-2xl">We partner with dealers who know that <strong class="text-white">leads aren't created - they're captured.</strong></p>
          <div class="flex flex-col items-center justify-center gap-4 pt-4 sm:flex-row sm:gap-6">
            <a href="/book" class="inline-flex items-center gap-2 min-h-[56px] w-full sm:w-auto rounded-full bg-white/95 px-10 text-base font-semibold text-[#0088ff] backdrop-blur-sm hover:bg-white transition">
              Request Free Audit
              <svg class="h-5 w-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
            </a>
            <a href="tel:{PHONE_HREF}" class="inline-flex items-center justify-center min-h-[56px] w-full sm:w-auto rounded-full border border-white/20 bg-white/10 px-10 text-base font-semibold text-white backdrop-blur-sm hover:bg-white/20 transition">Call {PHONE}</a>
          </div>
        </div>
      </div>
    </section>

    <!-- Products Section Header -->
    <section class="overflow-hidden">
      <div class="py-32 text-center">
        <div class="mx-auto max-w-4xl px-6 sm:px-8">
          <h2 class="font-serif text-5xl sm:text-6xl font-bold mb-6">Savvy Product Suite</h2>
          <p class="text-xl sm:text-2xl text-gray-500">Customized marketing that outsmart the competition</p>
        </div>
      </div>
    </section>

    <!-- Product Grid (alternating layout) -->
{products_html}

    <!-- View All Products -->
    <section class="pb-24 text-center">
      <a href="/products" class="inline-flex items-center gap-2 min-h-[48px] rounded-full px-8 border border-gray-200 text-gray-900 font-semibold hover:bg-gray-50 transition">
        View All Products
        <svg class="h-5 w-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
      </a>
    </section>

    <!-- About Section -->
    <section class="bg-gray-50 py-32">
      <div class="max-w-7xl mx-auto px-6 sm:px-8 lg:px-12">
        <div class="grid items-center gap-16 lg:grid-cols-2">
          <div class="order-2 lg:order-1">
            <h2 class="font-serif text-4xl font-bold leading-tight sm:text-5xl mb-8">How We Drive Your Sales</h2>
            <p class="text-xl text-gray-500 mb-8">By aligning our SEO and GEO strategies, we ensure your dealership doesn't just compete - it <strong class="text-gray-900">appears first and performs faster</strong> wherever shoppers are searching.</p>
            <div class="space-y-4 mb-8">
              <div class="flex items-start gap-4"><svg class="h-6 w-6 shrink-0 text-[#0088ff]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg><span class="text-lg text-gray-500">Counter competitor tactics effectively</span></div>
              <div class="flex items-start gap-4"><svg class="h-6 w-6 shrink-0 text-[#0088ff]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg><span class="text-lg text-gray-500">Dominate in search and generative AI results</span></div>
              <div class="flex items-start gap-4"><svg class="h-6 w-6 shrink-0 text-[#0088ff]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg><span class="text-lg text-gray-500">AI-optimized websites that convert</span></div>
              <div class="flex items-start gap-4"><svg class="h-6 w-6 shrink-0 text-[#0088ff]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg><span class="text-lg text-gray-500">Transparent reporting you can trust</span></div>
            </div>
            <p class="text-xl font-semibold mb-8">We don't outspend the competition - <span class="text-[#0088ff]">we outsmart them.</span></p>
            <a href="/about" class="inline-flex items-center justify-center min-h-[48px] rounded-full px-8 bg-[#0088ff] text-white font-semibold hover:bg-[#0077e6] transition">Learn More About Us</a>
          </div>
          <div class="order-1 lg:order-2">
            <img src="/images/Feature_section_workspace_image_6c209941.png" alt="Savvy Dealer workspace" class="rounded-3xl" loading="lazy">
          </div>
        </div>
      </div>
    </section>

    <!-- Testimonials -->
    <section class="py-32">
      <div class="max-w-7xl mx-auto px-6 sm:px-8 lg:px-12">
        <div class="mb-20 text-center">
          <h2 class="font-serif text-4xl sm:text-5xl font-bold mb-4">What Dealers are Saying</h2>
          <p class="text-xl text-gray-500">Consistent performance improvements and trusted partnerships</p>
        </div>
        <div class="grid gap-8 md:grid-cols-2 lg:grid-cols-3">
          <div class="rounded-xl border border-gray-200 p-8">
            <p class="text-lg text-gray-500 italic leading-relaxed mb-8">&ldquo;Savvy Dealer nailed the essentials: a high-performing website, marketing that delivers results, consistent service, and reporting that makes decisions obvious. The outcome is steady, consistent performance improvements across traffic quality, conversions, and paid efficiency.&rdquo;</p>
            <div class="border-t pt-6">
              <p class="font-semibold text-lg">Josh Mead</p>
              <p class="text-gray-500">General Manager</p>
              <p class="font-medium text-[#0088ff]">Brighton Ford</p>
            </div>
          </div>
          <div class="rounded-xl border border-gray-200 p-8">
            <p class="text-lg text-gray-500 italic leading-relaxed mb-8">&ldquo;We've been working with Savvy Dealer for over a year, and Savvy Dealer has been a major contributor for Banner Fords success. Our website is faster and converts better, and we see consistent performance improvements across SEO and paid media.&rdquo;</p>
            <div class="border-t pt-6">
              <p class="font-semibold text-lg">Greg Jones</p>
              <p class="text-gray-500">General Manager</p>
              <p class="font-medium text-[#0088ff]">Banner Ford</p>
            </div>
          </div>
          <div class="rounded-xl border border-gray-200 p-8">
            <p class="text-lg text-gray-500 italic leading-relaxed mb-8">&ldquo;Savvy Dealer is the ideal partner for our dealerships. Month after month we see consistent performance improvements across website conversions, SEO visibility, and paid media. Attribution is clear, budgets are transparent.&rdquo;</p>
            <div class="border-t pt-6">
              <p class="font-semibold text-lg">David Blake</p>
              <p class="text-gray-500">General Manager</p>
              <p class="font-medium text-[#0088ff]">Lake Powell Ford &amp; Alamo Ford</p>
            </div>
          </div>
        </div>
      </div>
    </section>

{cta_section()}
{org_schema()}
  </main>
{footer()}'''
    write_page("index.html", content)


def generate_about():
    content = f'''{head("About Savvy Dealer - Automotive Digital Marketing Experts", "Founded on a simple principle: automotive dealerships deserve digital marketing that actually drives sales, not just impressions.", "about")}
{nav()}
  <main class="flex-1">
{breadcrumb([("Home", "/"), ("About", None)])}
    <section class="relative flex min-h-[70vh] items-center justify-center overflow-hidden px-6 py-20 sm:px-8 lg:px-12" style="background:linear-gradient(135deg, #0a2540 0%, #1e3a5f 50%, #0088ff 100%)">
      <div class="relative z-10 max-w-7xl mx-auto text-center">
        <div class="mx-auto max-w-5xl space-y-8">
          <h1 class="font-serif text-4xl font-bold leading-tight text-white sm:text-5xl lg:text-6xl">We Don't Outspend the Competition</h1>
          <p class="text-2xl text-white/90 font-semibold">We Outsmart Them</p>
          <p class="mx-auto max-w-3xl text-lg text-white/80">Savvy Dealer was founded on a simple principle: automotive dealerships deserve digital marketing that actually drives sales, not just impressions. We combine deep industry expertise with data-driven strategies to help dealers win in an increasingly competitive market.</p>
        </div>
      </div>
    </section>

    <section class="py-24 px-6 sm:px-8 lg:px-12">
      <div class="max-w-7xl mx-auto grid md:grid-cols-2 gap-16">
        <div>
          <h2 class="font-serif text-3xl font-bold text-gray-900 mb-6">Our Mission</h2>
          <p class="text-gray-500 text-lg leading-relaxed">To empower automotive dealerships with marketing strategies that focus on ready-to-buy shoppers, transparent ROI metrics, and measurable results. We believe in building backwards from the sale, optimizing for conversations and test drives - not vanity metrics.</p>
        </div>
        <div>
          <h2 class="font-serif text-3xl font-bold text-gray-900 mb-6">What Sets Us Apart</h2>
          <ul class="space-y-4">
            <li class="flex items-start gap-3"><span class="font-semibold text-[#0088ff]">High-intent focus:</span> <span class="text-gray-500">We target shoppers who are ready now, not "someday"</span></li>
            <li class="flex items-start gap-3"><span class="font-semibold text-[#0088ff]">Transparent metrics:</span> <span class="text-gray-500">Simple, human-readable KPIs that matter</span></li>
            <li class="flex items-start gap-3"><span class="font-semibold text-[#0088ff]">Agile execution:</span> <span class="text-gray-500">Twice-monthly cadence to pivot against competitors</span></li>
            <li class="flex items-start gap-3"><span class="font-semibold text-[#0088ff]">Real content:</span> <span class="text-gray-500">No AI-generated fluff - just substance that ranks</span></li>
          </ul>
        </div>
      </div>
    </section>

    <section class="py-24 px-6 sm:px-8 lg:px-12 bg-gray-50">
      <div class="max-w-7xl mx-auto">
        <h2 class="font-serif text-3xl sm:text-4xl font-bold text-center text-gray-900 mb-16">Our Team</h2>
        <div class="grid md:grid-cols-3 lg:grid-cols-5 gap-8">
          <div class="text-center"><div class="w-24 h-24 bg-gray-200 rounded-full mx-auto mb-4"></div><h3 class="font-semibold text-lg">Adam Gillrie</h3><p class="text-sm text-gray-500">Director</p></div>
          <div class="text-center"><div class="w-24 h-24 bg-gray-200 rounded-full mx-auto mb-4"></div><h3 class="font-semibold text-lg">Nick Chivinski</h3><p class="text-sm text-gray-500">VP of Sales</p></div>
          <div class="text-center"><div class="w-24 h-24 bg-gray-200 rounded-full mx-auto mb-4"></div><h3 class="font-semibold text-lg">David Frost</h3><p class="text-sm text-gray-500">CTO</p></div>
          <div class="text-center"><div class="w-24 h-24 bg-gray-200 rounded-full mx-auto mb-4"></div><h3 class="font-semibold text-lg">Emily Shultz</h3><p class="text-sm text-gray-500">Head of Operations</p></div>
          <div class="text-center"><div class="w-24 h-24 bg-gray-200 rounded-full mx-auto mb-4"></div><h3 class="font-semibold text-lg">Lucas Terwilliger</h3><p class="text-sm text-gray-500">Strategist</p></div>
        </div>
      </div>
    </section>

    <section class="py-24 px-6 sm:px-8 lg:px-12">
      <div class="max-w-7xl mx-auto">
        <h2 class="font-serif text-3xl sm:text-4xl font-bold text-center text-gray-900 mb-16">Our Values</h2>
        <div class="grid md:grid-cols-3 gap-12">
          <div class="text-center"><h3 class="font-serif text-xl font-bold mb-3">Results-Driven</h3><p class="text-gray-500">Every campaign is built to drive real conversations, test drives, and sales - not just traffic.</p></div>
          <div class="text-center"><h3 class="font-serif text-xl font-bold mb-3">Partnership</h3><p class="text-gray-500">We're an extension of your team, meeting twice monthly to plan and pivot based on market conditions.</p></div>
          <div class="text-center"><h3 class="font-serif text-xl font-bold mb-3">Innovation</h3><p class="text-gray-500">From AI-optimized websites to attribution intelligence, we stay ahead of the automotive marketing curve.</p></div>
        </div>
      </div>
    </section>

{cta_section("Ready to Work Together?", "Let's discuss how Savvy Dealer can help your dealership dominate your market")}
  </main>
{footer()}'''
    write_page("about.html", content)


def generate_products():
    products = [
        ("Fully Managed Marketing", "Premium Service", "White-glove service that handles everything - co-op management, vendor coordination, website, SEO, SEM, Facebook ads, design, and ROI tracking.", "/fully-managed-marketing", "#FF6B35"),
        ("Facebook Ads", "Capture Traffic / Drive Sales", "Hand-built Facebook Ads that lead the industry in performance. We hand-select vehicles for maximum results.", "/facebook-ads", "#FF4081"),
        ("Dealer SEO + GEO", "Fuel Long-Term Site Growth", "SEO + GEO optimization that positions your dealership first in traditional search and AI-powered results.", "/dealer-seo", "#00E676"),
        ("PPC Ads", "Turbocharge Your PPC", "Industry-leading Google and Bing Ad campaigns that focus on your in-stock inventory.", "/ppc-ads", "#FF6B35"),
        ("Vehicle Ads", "Stop Wasting Your VLA Budget", "Reclaim thousands wasted on Google's Display Network. Expert Performance Max management.", "/vehicle-ads", "#00D4D4"),
        ("Dealer Websites", "Dominate Your Online Market", "SEO-first website architecture that accelerates your digital marketing efforts.", "/dealer-websites", "#0088FF"),
        ("Independent Dealer Websites", "Built For Your Business", "Premium websites for independent dealers and buy-here-pay-here lots. No franchise fees.", "/independent-dealer-websites", "#20B2AA"),
        ("Anti-Dashboard AI", "Coming Soon", "AI-powered attribution and analytics that transforms how you measure marketing success.", "/anti-dashboard", "#9D4EDD"),
    ]
    cards_html = ""
    for name, subtitle, desc, url, color in products:
        cards_html += f'''        <div class="rounded-xl border border-gray-200 p-8 hover:shadow-lg transition">
          <div class="mb-4 inline-flex h-10 w-10 items-center justify-center rounded-lg" style="background-color:{color}20;color:{color}">
            <svg class="h-5 w-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/></svg>
          </div>
          <h3 class="font-serif text-xl font-bold text-gray-900 mb-1">{name}</h3>
          <p class="text-sm font-medium mb-3" style="color:{color}">{subtitle}</p>
          <p class="text-gray-500 text-sm mb-6">{desc}</p>
          <a href="{url}" class="text-[#0088ff] font-medium text-sm hover:underline">Learn More &rarr;</a>
        </div>\n'''

    content = f'''{head("Savvy Product Suite - Automotive Marketing Solutions | Savvy Dealer", "Comprehensive suite of automotive marketing products. Facebook Ads, PPC, SEO/GEO, dealer websites, and AI-powered tools.", "products")}
{nav()}
  <main class="flex-1">
{breadcrumb([("Home", "/"), ("Products", None)])}
    <section class="relative flex min-h-[60vh] items-center justify-center overflow-hidden px-6 py-20 sm:px-8 lg:px-12" style="background:linear-gradient(135deg, #0a2540 0%, #1e3a5f 50%, #0088ff 100%)">
      <div class="relative z-10 max-w-7xl mx-auto text-center">
        <div class="mx-auto max-w-4xl space-y-6">
          <h1 class="font-serif text-4xl font-bold leading-tight text-white sm:text-5xl lg:text-6xl">Savvy Product Suite</h1>
          <p class="text-xl text-white/80 max-w-3xl mx-auto">At Savvy Dealer, we customize our marketing packages to meet your needs, not ours. Our comprehensive suite of products works together to counter competitor tactics and dominate in both search and generative AI results.</p>
        </div>
      </div>
    </section>

    <section class="py-24 px-6 sm:px-8 lg:px-12">
      <div class="max-w-7xl mx-auto">
        <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
{cards_html}        </div>
      </div>
    </section>

{cta_section()}
  </main>
{footer()}'''
    write_page("products.html", content)


def generate_book():
    content = f'''{head("Book a Demo - Savvy Dealer", "Schedule a demo with Savvy Dealer. See how we help dealerships dominate their market with AI-optimized marketing.", "book")}
{nav()}
  <main class="flex-1">
{breadcrumb([("Home", "/"), ("Book a Demo", None)])}
    <section class="py-24 px-6 sm:px-8 lg:px-12">
      <div class="max-w-2xl mx-auto">
        <h1 class="font-serif text-4xl sm:text-5xl font-bold text-gray-900 mb-4 text-center">Request a Free Audit</h1>
        <p class="text-gray-500 text-center text-lg mb-10">Fill out the form below and we'll analyze your digital presence and show you exactly how we can help.</p>
        <form data-ajax action="/api/schedule-demo" class="space-y-5">
          <div><label for="name" class="block text-sm font-medium text-gray-700 mb-1">Name *</label><input type="text" id="name" name="name" required class="w-full px-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-[#0088ff] focus:border-[#0088ff] outline-none"></div>
          <div><label for="email" class="block text-sm font-medium text-gray-700 mb-1">Email *</label><input type="email" id="email" name="email" required class="w-full px-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-[#0088ff] focus:border-[#0088ff] outline-none"></div>
          <div><label for="phone" class="block text-sm font-medium text-gray-700 mb-1">Phone *</label><input type="tel" id="phone" name="phone" required class="w-full px-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-[#0088ff] focus:border-[#0088ff] outline-none"></div>
          <div><label for="dealership" class="block text-sm font-medium text-gray-700 mb-1">Dealership</label><input type="text" id="dealership" name="dealership" class="w-full px-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-[#0088ff] focus:border-[#0088ff] outline-none"></div>
          <div><label for="message" class="block text-sm font-medium text-gray-700 mb-1">Tell us about your goals</label><textarea id="message" name="message" rows="4" class="w-full px-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-[#0088ff] focus:border-[#0088ff] outline-none"></textarea></div>
          <button type="submit" class="w-full bg-[#0088ff] text-white py-3 px-6 rounded-full font-semibold hover:bg-[#0077e6] transition text-lg min-h-[48px]">Submit Request</button>
        </form>
        <p class="text-center text-sm text-gray-500 mt-8">Or call us directly: <a href="tel:{PHONE_HREF}" class="text-[#0088ff] font-semibold">{PHONE}</a></p>
      </div>
    </section>
  </main>
{footer()}'''
    write_page("book.html", content)


def generate_404():
    content = f'''{head("Page Not Found - Savvy Dealer", "The page you're looking for doesn't exist.", "404")}
{nav()}
  <main class="flex-1">
    <section class="py-32 px-6 sm:px-8 text-center">
      <h1 class="font-serif text-8xl font-bold text-gray-200 mb-6">404</h1>
      <h2 class="font-serif text-3xl font-bold text-gray-900 mb-4">Page Not Found</h2>
      <p class="text-gray-500 text-lg mb-10">The page you're looking for doesn't exist or has been moved.</p>
      <a href="/" class="inline-flex items-center justify-center min-h-[48px] px-8 bg-[#0088ff] text-white font-semibold rounded-full hover:bg-[#0077e6] transition">Back to Home</a>
    </section>
  </main>
{footer()}'''
    write_page("404.html", content)


def generate_visibility_audit():
    content = f'''{head("AI Visibility Audit - Check Your Dealership | Savvy Dealer", "Check how visible your dealership is to AI search engines like ChatGPT and Perplexity.", "visibility-audit")}
{nav()}
  <main class="flex-1">
{breadcrumb([("Home", "/"), ("Visibility Audit", None)])}
    <section class="py-32 px-6 sm:px-8 text-center">
      <div class="max-w-3xl mx-auto">
        <h1 class="font-serif text-4xl sm:text-5xl font-bold text-gray-900 mb-6">AI Visibility Audit</h1>
        <p class="text-xl text-gray-500 mb-10">Check how visible your dealership is to AI search engines like ChatGPT, Perplexity, and Google AI Overviews.</p>
        <a href="https://ai-compatible-v3-185609396182.us-central1.run.app" target="_blank" rel="noopener" class="inline-flex items-center justify-center min-h-[56px] px-10 bg-[#0088ff] text-white font-semibold rounded-full hover:bg-[#0077e6] transition text-lg">Run Your Free AI Visibility Audit &rarr;</a>
        <p class="text-sm text-gray-500 mt-6">Free tool - no login required</p>
      </div>
    </section>
{cta_section()}
  </main>
{footer()}'''
    write_page("visibility-audit.html", content)


def generate_anti_dashboard():
    content = f'''{head("Anti-Dashboard AI - Coming Soon | Savvy Dealer", "AI-powered attribution and analytics that transforms how you measure automotive marketing success.", "anti-dashboard")}
{nav()}
  <main class="flex-1">
{breadcrumb([("Home", "/"), ("Products", "/products"), ("Anti-Dashboard AI", None)])}
    <section class="relative flex min-h-[70vh] items-center justify-center overflow-hidden px-6 py-20 sm:px-8 lg:px-12" style="background:linear-gradient(135deg, #0a2540 0%, #1e3a5f 50%, #9D4EDD 100%)">
      <div class="relative z-10 max-w-7xl mx-auto text-center">
        <div class="mx-auto max-w-4xl space-y-8">
          <div class="inline-flex items-center gap-2 rounded-full border border-white/20 bg-white/10 px-5 py-2.5 text-sm backdrop-blur-md">
            <span class="font-medium text-white">Coming Soon</span>
          </div>
          <h1 class="font-serif text-4xl font-bold leading-tight text-white sm:text-5xl lg:text-6xl">Anti-Dashboard AI</h1>
          <p class="mx-auto max-w-3xl text-xl text-white/90">Something big is coming. AI will transform automotive attribution and analytics. Be among the first to see how.</p>
          <a href="/book" class="inline-flex items-center justify-center min-h-[56px] rounded-full bg-white/95 px-10 text-base font-semibold text-[#9D4EDD] backdrop-blur-sm hover:bg-white transition">Schedule a Preview</a>
        </div>
      </div>
    </section>
  </main>
{footer()}'''
    write_page("anti-dashboard.html", content)


def generate_simple_pages():
    """Generate early-access, nada-show, case-studies, independent-dealer-websites, resources, legal pages."""

    # Early Access
    content = f'''{head("Early Access - Savvy Dealer", "Get early access to Savvy Dealer's new Anti-Dashboard and upcoming dealer marketing tools.", "early-access")}
{nav()}
  <main class="flex-1">
{breadcrumb([("Home", "/"), ("Early Access", None)])}
    <section class="relative flex min-h-[60vh] items-center justify-center overflow-hidden px-6 py-20 sm:px-8 lg:px-12" style="background:linear-gradient(135deg, #0a2540 0%, #1e3a5f 50%, #9D4EDD 100%)">
      <div class="relative z-10 max-w-7xl mx-auto text-center">
        <div class="mx-auto max-w-4xl space-y-8">
          <div class="inline-flex items-center gap-2 rounded-full border border-white/20 bg-white/10 px-5 py-2.5 text-sm backdrop-blur-md">
            <span class="font-medium text-white">Exclusive Early Access</span>
          </div>
          <h1 class="font-serif text-4xl font-bold leading-tight text-white sm:text-5xl lg:text-6xl">Not Going to NADA? See What Everyone Else Will Be Talking About First</h1>
          <p class="mx-auto max-w-3xl text-lg text-white/80">Get early access to Savvy Dealer's new Anti-Dashboard Dashboard and upcoming dealer marketing tools before they are introduced at NADA.</p>
          <a href="/book" class="inline-flex items-center justify-center min-h-[56px] rounded-full bg-white/95 px-10 text-base font-semibold text-[#0088ff] backdrop-blur-sm hover:bg-white transition">Schedule Your Early Access Demo</a>
        </div>
      </div>
    </section>
    <section class="py-24 px-6 sm:px-8 lg:px-12">
      <div class="max-w-3xl mx-auto">
        <p class="text-gray-500 text-lg leading-relaxed mb-6">Not everyone can make it to NADA, and that should not put you behind. Savvy Dealer is preparing to introduce a new way for dealers to measure digital marketing success, along with tools designed for AI-ready visibility, smarter spend, and clearer reporting.</p>
        <p class="text-gray-500 text-lg leading-relaxed mb-8">Before this is shown publicly at NADA, a limited number of dealers are being given a private preview. <strong class="text-gray-900">This is your opportunity to see what is coming before the rest of the industry.</strong></p>
        <h2 class="font-serif text-3xl font-bold mb-6">What You'll Get With an Early Preview</h2>
        <ul class="space-y-4 text-gray-500 text-lg">
          <li class="flex items-start gap-3"><svg class="h-6 w-6 shrink-0 text-[#0088ff]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>A private walkthrough of the Anti-Dashboard Dashboard</li>
          <li class="flex items-start gap-3"><svg class="h-6 w-6 shrink-0 text-[#0088ff]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>Insight into new reporting and attribution concepts before public release</li>
          <li class="flex items-start gap-3"><svg class="h-6 w-6 shrink-0 text-[#0088ff]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>An overview of Savvy Dealer's AI-ready website and SEO strategies</li>
          <li class="flex items-start gap-3"><svg class="h-6 w-6 shrink-0 text-[#0088ff]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>A look at how smarter paid search and social campaigns are built to convert</li>
        </ul>
      </div>
    </section>
{cta_section("Get Early Access Before NADA", "Savvy Dealer will introduce this publicly at NADA. You can see it now.")}
  </main>
{footer()}'''
    write_page("early-access.html", content)

    # NADA Show
    content = f'''{head("NADA Show 2026 - Booth 6760N | Savvy Dealer", "Visit Savvy Dealer at NADA Show 2026, Booth 6760N. See our Anti-Dashboard, master GEO, and discover strategies from top-performing dealers.", "nada-show")}
{nav()}
  <main class="flex-1">
{breadcrumb([("Home", "/"), ("NADA Show 2026", None)])}
    <section class="relative flex min-h-[60vh] items-center justify-center overflow-hidden px-6 py-20 sm:px-8 lg:px-12" style="background:linear-gradient(135deg, #0a2540 0%, #1e3a5f 50%, #0088ff 100%)">
      <div class="relative z-10 max-w-7xl mx-auto text-center">
        <div class="mx-auto max-w-5xl space-y-8">
          <div class="inline-flex items-center gap-2 rounded-full border border-white/20 bg-white/10 px-5 py-2.5 text-sm backdrop-blur-md">
            <span class="font-medium text-white">Booth 6760N | February 4-6, 2026 | Las Vegas</span>
          </div>
          <h1 class="font-serif text-4xl font-bold leading-tight text-white sm:text-5xl lg:text-6xl">Why Visit Savvy Dealer at NADA Show 2026</h1>
          <p class="mx-auto max-w-3xl text-lg text-white/80">Get exclusive access to our Anti-Dashboard, master GEO before your competitors, and discover strategies from top-performing dealers.</p>
          <a href="/book" class="inline-flex items-center justify-center min-h-[56px] rounded-full bg-white/95 px-10 text-base font-semibold text-[#0088ff] backdrop-blur-sm hover:bg-white transition">Lock in Your Strategy Session</a>
        </div>
      </div>
    </section>
    <section class="py-24 px-6 sm:px-8 lg:px-12">
      <div class="max-w-7xl mx-auto">
        <h2 class="font-serif text-3xl sm:text-4xl font-bold text-center mb-16">Proven Results From Real Dealers</h2>
        <div class="grid md:grid-cols-4 gap-8 text-center">
          <div class="rounded-xl border border-gray-200 p-6"><div class="font-serif text-4xl font-bold text-[#0088ff]">+838%</div><div class="text-sm text-gray-500 mt-2">Verified Users (Banner Chevy)</div></div>
          <div class="rounded-xl border border-gray-200 p-6"><div class="font-serif text-4xl font-bold text-[#0088ff]">+340%</div><div class="text-sm text-gray-500 mt-2">VDP Views (Banner Chevy)</div></div>
          <div class="rounded-xl border border-gray-200 p-6"><div class="font-serif text-4xl font-bold text-[#0088ff]">+47%</div><div class="text-sm text-gray-500 mt-2">Conversions (Brighton Ford)</div></div>
          <div class="rounded-xl border border-gray-200 p-6"><div class="font-serif text-4xl font-bold text-[#0088ff]">-32%</div><div class="text-sm text-gray-500 mt-2">Cost Per Lead (Lake Powell Ford)</div></div>
        </div>
      </div>
    </section>
{cta_section("See You at Booth 6760N", "Don't miss this opportunity to transform your dealership's digital marketing strategy.")}
  </main>
{footer()}'''
    write_page("nada-show.html", content)

    # Independent Dealer Websites (custom layout, not standard service)
    content = f'''{head("Independent Dealer Websites with SEO & GEO | Savvy Dealer", "Lightning-fast, mobile-first dealer websites for independent stores with built-in SEO and GEO.", "independent-dealer-websites")}
{nav()}
  <main class="flex-1">
{breadcrumb([("Home", "/"), ("Products", "/products"), ("Independent Dealer Websites", None)])}
    <section class="relative flex min-h-[70vh] items-center justify-center overflow-hidden px-6 py-20 sm:px-8 lg:px-12" style="background:linear-gradient(135deg, #0a2540 0%, #1e3a5f 50%, #20B2AA 100%)">
      <div class="relative z-10 max-w-7xl mx-auto text-center">
        <div class="mx-auto max-w-5xl space-y-8">
          <div class="inline-flex items-center gap-2 rounded-full border border-white/20 bg-white/10 px-5 py-2.5 text-sm backdrop-blur-md">
            <span class="font-medium text-white">Independent Dealer Solutions</span>
          </div>
          <h1 class="font-serif text-4xl font-bold leading-tight text-white sm:text-5xl lg:text-6xl">Independent Dealer Websites With SEO & GEO Built In</h1>
          <p class="mx-auto max-w-3xl text-lg text-white/80">Get a lightning-fast, mobile-first dealer website modeled after our highest-performing dealers, with SEO and GEO baked in - without giving up control of your domain or your data.</p>
          <a href="/book" class="inline-flex items-center justify-center min-h-[56px] rounded-full bg-white/95 px-10 text-base font-semibold text-[#20B2AA] backdrop-blur-sm hover:bg-white transition">Book a 15-Minute Demo</a>
        </div>
      </div>
    </section>

    <section class="py-24 px-6 sm:px-8 lg:px-12">
      <div class="max-w-7xl mx-auto">
        <h2 class="font-serif text-3xl sm:text-4xl font-bold mb-12">Why Most Independent Dealer Websites Leave Money on the Table</h2>
        <div class="grid md:grid-cols-2 gap-8">
          <div class="bg-red-50 border border-red-100 rounded-xl p-8"><h3 class="font-semibold text-red-800 mb-3">Slow on mobile</h3><p class="text-gray-500">When your site takes too long to load, shoppers bounce before they ever see your inventory.</p></div>
          <div class="bg-red-50 border border-red-100 rounded-xl p-8"><h3 class="font-semibold text-red-800 mb-3">Hard for Google and AI</h3><p class="text-gray-500">Generic templates and messy URL structures make it hard for Google and AI engines to find you.</p></div>
          <div class="bg-red-50 border border-red-100 rounded-xl p-8"><h3 class="font-semibold text-red-800 mb-3">You don't really own it</h3><p class="text-gray-500">With some providers, your website lives on their subdomain. If you leave, you fight over your domain.</p></div>
          <div class="bg-red-50 border border-red-100 rounded-xl p-8"><h3 class="font-semibold text-red-800 mb-3">Weak conversion paths</h3><p class="text-gray-500">Buried phone numbers and hard-to-tap buttons mean traffic doesn't turn into leads.</p></div>
        </div>
      </div>
    </section>

    <section class="py-24 px-6 sm:px-8 lg:px-12 bg-gray-50">
      <div class="max-w-7xl mx-auto">
        <h2 class="font-serif text-3xl sm:text-4xl font-bold mb-4">What's Included</h2>
        <p class="text-gray-500 text-lg mb-12">Everything is built around one goal: help independent and BHPH dealers turn more visitors into real opportunities.</p>
        <div class="grid md:grid-cols-2 gap-8">
          <div class="bg-white rounded-xl p-8 border border-gray-200"><h3 class="font-semibold text-lg mb-3">High-Converting Dealer Website</h3><p class="text-gray-500">Clean SRP/VDP structure, clear CTAs, inventory-focused design. You keep your domain.</p></div>
          <div class="bg-white rounded-xl p-8 border border-gray-200"><h3 class="font-semibold text-lg mb-3">SEO Built In From Day One</h3><p class="text-gray-500">Search-friendly URLs, structured data, smart internal linking.</p></div>
          <div class="bg-white rounded-xl p-8 border border-gray-200"><h3 class="font-semibold text-lg mb-3">GEO - Generative Engine Optimization</h3><p class="text-gray-500">Machine-readable signals so AI assistants can find and recommend your store.</p></div>
          <div class="bg-white rounded-xl p-8 border border-gray-200"><h3 class="font-semibold text-lg mb-3">Mobile-First and Lightning Fast</h3><p class="text-gray-500">Performance-minded templates, mobile-first layouts, fewer bounces.</p></div>
        </div>
      </div>
    </section>

{faq_section([
    ("Is this only for franchise dealers?", "No. This package is specifically designed for independent and BHPH dealers."),
    ("Is there a long-term contract?", "No long-term contract required. We earn your business every month with results."),
    ("Can I keep my existing inventory provider?", "In most cases, yes. We'll review your current setup and connect it."),
    ("What if I'm on a $99 website now?", "Part of our discovery process is reviewing your current setup and safely migrating you without losing your domain or search history."),
    ("Can you migrate me off a marketplace-style site?", "Yes. We'll map your key pages and inventory so you don't lose the equity you've built."),
])}
{cta_section("Give Your Independent Store a Website That Can Actually Win Online", "No long-term contract. Built specifically for independent and BHPH dealers.")}
  </main>
{footer()}'''
    write_page("independent-dealer-websites.html", content)

    # Resources hub
    resources = [
        ("The Complete Guide to Generative Engine Optimization for Car Dealers", "2026 Guide", "15 min read", "How to get your dealership cited in AI search engines like ChatGPT, Perplexity, and Google AI Overviews.", "/resources/geo-guide", True),
        ("The Complete Dealership SEO Guide for 2025", "2025 Guide", "45 min read", "Future-proof strategies to dominate search rankings, drive organic traffic, and capture more leads.", "/resources/seo-guide", True),
        ("2026 Facebook Ads Playbook for Dealerships", "2026 Playbook", "20 min read", "Advanced strategies for inventory-based automotive advertising on Meta platforms.", "/resources/facebook-ads-playbook", True),
        ("The Dealership Reputation Guide", "Practical Guide", "15 min read", "How to build, manage, and protect your online reputation.", "/resources/reputation-guide", False),
    ]
    cards = ""
    for title, badge, readtime, desc, url, featured in resources:
        feat_badge = '<span class="bg-[#0088ff]/10 text-[#0088ff] text-xs px-2.5 py-1 rounded-full font-medium">Featured</span>' if featured else ""
        cards += f'''        <div class="rounded-xl border border-gray-200 p-8 hover:shadow-lg transition">
          <div class="flex items-center gap-2 mb-4"><span class="bg-gray-100 text-gray-700 text-xs px-2.5 py-1 rounded-full font-medium">{badge}</span><span class="text-xs text-gray-500">{readtime}</span>{feat_badge}</div>
          <h3 class="font-serif text-xl font-bold text-gray-900 mb-3">{title}</h3>
          <p class="text-gray-500 mb-6">{desc}</p>
          <a href="{url}" class="text-[#0088ff] font-medium hover:underline">Read Guide &rarr;</a>
        </div>\n'''

    content = f'''{head("Dealer Marketing Resources - Free Guides & Playbooks | Savvy Dealer", "In-depth guides, playbooks, and strategies to help your dealership win in digital marketing.", "resources")}
{nav()}
  <main class="flex-1">
{breadcrumb([("Home", "/"), ("Resources", None)])}
    <section class="relative flex min-h-[60vh] items-center justify-center overflow-hidden px-6 py-20 sm:px-8 lg:px-12" style="background:linear-gradient(135deg, #0a2540 0%, #1e3a5f 50%, #0088ff 100%)">
      <div class="relative z-10 max-w-7xl mx-auto text-center">
        <div class="mx-auto max-w-4xl space-y-6">
          <div class="inline-flex items-center gap-2 rounded-full border border-white/20 bg-white/10 px-5 py-2.5 text-sm backdrop-blur-md">
            <span class="font-medium text-white">Free Resources</span>
          </div>
          <h1 class="font-serif text-4xl font-bold leading-tight text-white sm:text-5xl lg:text-6xl">Dealer Marketing Resources</h1>
          <p class="text-xl text-white/80">In-depth guides, playbooks, and strategies to help your dealership win in digital marketing. No fluff - just actionable insights.</p>
        </div>
      </div>
    </section>
    <section class="py-24 px-6 sm:px-8 lg:px-12">
      <div class="max-w-7xl mx-auto">
        <div class="grid md:grid-cols-2 gap-8">
{cards}        </div>
      </div>
    </section>
{cta_section()}
  </main>
{footer()}'''
    write_page("resources/index.html", content)

    # Resource guide pages (full content in generate_resources.py)
    from generate_resources import generate_all_resources
    generate_all_resources()

    # Case Studies
    content = f'''{head("Case Studies - Dealerships Winning with Savvy Dealer", "From improved website performance to crystal-clear attribution, see how we help dealerships drive measurable results.", "case-studies")}
{nav()}
  <main class="flex-1">
{breadcrumb([("Home", "/"), ("Case Studies", None)])}
    <div class="bg-[#0088ff] text-white text-center py-3 px-6 text-sm">
      <a href="/case-studies/ai-compatibility" class="hover:underline font-medium">84% of Dealer Websites Are Invisible to AI -- See the Full Study &rarr;</a>
    </div>
    <section class="relative flex min-h-[60vh] items-center justify-center overflow-hidden px-6 py-20 sm:px-8 lg:px-12" style="background:linear-gradient(135deg, #0a2540 0%, #1e3a5f 50%, #0088ff 100%)">
      <div class="relative z-10 max-w-7xl mx-auto text-center">
        <div class="mx-auto max-w-4xl space-y-6">
          <div class="inline-flex items-center gap-2 rounded-full border border-white/20 bg-white/10 px-5 py-2.5 text-sm backdrop-blur-md">
            <span class="font-medium text-white">Real Results</span>
          </div>
          <h1 class="font-serif text-4xl font-bold leading-tight text-white sm:text-5xl lg:text-6xl">Dealerships Winning with Savvy Dealer</h1>
          <p class="text-xl text-white/80">From improved website performance to crystal-clear attribution, see how we help dealerships drive measurable results.</p>
        </div>
      </div>
    </section>
    <section class="py-24 px-6 sm:px-8 lg:px-12">
      <div class="max-w-7xl mx-auto space-y-12">
        <!-- Banner Chevrolet -->
        <div class="rounded-xl border border-gray-200 p-8">
          <div class="flex items-center gap-3 mb-4"><h2 class="font-serif text-2xl font-bold">Banner Chevrolet</h2><span class="text-sm text-gray-500">New Orleans, LA</span></div>
          <p class="text-gray-500 mb-8">Slow mobile experience with weak Core Web Vitals suppressed organic and paid performance. Disjointed paid media limited reach and efficiency.</p>
          <div class="grid md:grid-cols-4 gap-6 mb-8">
            <div class="text-center bg-green-50 rounded-xl p-6"><div class="font-serif text-3xl font-bold text-green-600">+838%</div><div class="text-sm text-gray-500 mt-1">Verified Users YoY</div></div>
            <div class="text-center bg-green-50 rounded-xl p-6"><div class="font-serif text-3xl font-bold text-green-600">+340%</div><div class="text-sm text-gray-500 mt-1">VDP Views YoY</div></div>
            <div class="text-center bg-green-50 rounded-xl p-6"><div class="font-serif text-3xl font-bold text-green-600">&lt;1.5s</div><div class="text-sm text-gray-500 mt-1">Mobile LCP</div></div>
            <div class="text-center bg-green-50 rounded-xl p-6"><div class="font-serif text-3xl font-bold text-green-600">-25%</div><div class="text-sm text-gray-500 mt-1">Media Spend YoY</div></div>
          </div>
          <blockquote class="border-l-4 border-[#0088ff] pl-6 italic text-gray-500">&ldquo;After moving to Savvy Dealer and unifying our SEO, Google Ads, and Meta strategy, our results took off.&rdquo;<br><span class="not-italic font-semibold text-gray-900 mt-2 block">- Greg Jones, General Manager</span></blockquote>
        </div>
        <!-- Brighton Ford -->
        <div class="rounded-xl border border-gray-200 p-8">
          <div class="flex items-center gap-3 mb-4"><h2 class="font-serif text-2xl font-bold">Brighton Ford</h2><span class="text-sm text-gray-500">Brighton, CO</span></div>
          <p class="text-gray-500 mb-8">Needed consistent marketing performance and better ROI visibility across all digital channels.</p>
          <div class="grid md:grid-cols-4 gap-6 mb-8">
            <div class="text-center bg-green-50 rounded-xl p-6"><div class="font-serif text-3xl font-bold text-green-600">+47%</div><div class="text-sm text-gray-500 mt-1">Conversions</div></div>
            <div class="text-center bg-green-50 rounded-xl p-6"><div class="font-serif text-3xl font-bold text-green-600">+62%</div><div class="text-sm text-gray-500 mt-1">Quality Traffic</div></div>
            <div class="text-center bg-green-50 rounded-xl p-6"><div class="font-serif text-3xl font-bold text-green-600">+38%</div><div class="text-sm text-gray-500 mt-1">Paid Media Efficiency</div></div>
            <div class="text-center bg-green-50 rounded-xl p-6"><div class="font-serif text-3xl font-bold text-green-600">+54%</div><div class="text-sm text-gray-500 mt-1">SEO Visibility</div></div>
          </div>
          <blockquote class="border-l-4 border-[#0088ff] pl-6 italic text-gray-500">&ldquo;Savvy Dealer nailed the essentials: a high-performing website, marketing that delivers results, consistent service.&rdquo;<br><span class="not-italic font-semibold text-gray-900 mt-2 block">- Josh Mead, General Manager</span></blockquote>
        </div>
        <!-- Lake Powell & Alamo -->
        <div class="rounded-xl border border-gray-200 p-8">
          <div class="flex items-center gap-3 mb-4"><h2 class="font-serif text-2xl font-bold">Lake Powell Ford & Alamo Ford</h2><span class="text-sm text-gray-500">Page, AZ & San Antonio, TX</span></div>
          <p class="text-gray-500 mb-8">Managing marketing across two distinct markets with different competition levels and customer demographics.</p>
          <div class="grid md:grid-cols-4 gap-6 mb-8">
            <div class="text-center bg-green-50 rounded-xl p-6"><div class="font-serif text-3xl font-bold text-green-600">+68%</div><div class="text-sm text-gray-500 mt-1">Lead Volume</div></div>
            <div class="text-center bg-green-50 rounded-xl p-6"><div class="font-serif text-3xl font-bold text-green-600">-32%</div><div class="text-sm text-gray-500 mt-1">Cost Per Lead</div></div>
            <div class="text-center bg-green-50 rounded-xl p-6"><div class="font-serif text-3xl font-bold text-green-600">+44%</div><div class="text-sm text-gray-500 mt-1">Appointment Rate</div></div>
            <div class="text-center bg-green-50 rounded-xl p-6"><div class="font-serif text-3xl font-bold text-green-600">+100%</div><div class="text-sm text-gray-500 mt-1">Attribution Clarity</div></div>
          </div>
          <blockquote class="border-l-4 border-[#0088ff] pl-6 italic text-gray-500">&ldquo;Month after month we see consistent performance improvements. Attribution is clear, budgets are transparent.&rdquo;<br><span class="not-italic font-semibold text-gray-900 mt-2 block">- David Blake, General Manager</span></blockquote>
        </div>
      </div>
    </section>
{cta_section("Ready to See Similar Results?", "Let's discuss your dealership's specific challenges and build a strategy to drive measurable performance improvements.")}
  </main>
{footer()}'''
    write_page("case-studies.html", content)

    # AI Compatibility Study
    content = f'''{head("84% of Dealer Websites Are Invisible to AI | Savvy Dealer", "Our research found 84% of dealer websites are failing AI compatibility. 48% actively block AI crawlers.", "case-studies/ai-compatibility")}
{nav()}
  <main class="flex-1">
{breadcrumb([("Home", "/"), ("Case Studies", "/case-studies"), ("AI Compatibility Study", None)])}
    <section class="relative flex min-h-[60vh] items-center justify-center overflow-hidden px-6 py-20 sm:px-8 lg:px-12" style="background:linear-gradient(135deg, #0a2540 0%, #1e3a5f 50%, #0088ff 100%)">
      <div class="relative z-10 max-w-7xl mx-auto text-center">
        <h1 class="font-serif text-4xl font-bold leading-tight text-white sm:text-5xl lg:text-6xl mb-12">84% of Dealer Websites Are Invisible to AI</h1>
        <div class="grid md:grid-cols-4 gap-8">
          <div class="rounded-xl border border-white/20 bg-white/10 p-6 backdrop-blur-sm"><div class="font-serif text-4xl font-bold text-white">84%</div><div class="text-white/70 text-sm mt-2">Failing AI compatibility</div></div>
          <div class="rounded-xl border border-white/20 bg-white/10 p-6 backdrop-blur-sm"><div class="font-serif text-4xl font-bold text-white">48%</div><div class="text-white/70 text-sm mt-2">Actively blocking AI</div></div>
          <div class="rounded-xl border border-white/20 bg-white/10 p-6 backdrop-blur-sm"><div class="font-serif text-4xl font-bold text-white">34</div><div class="text-white/70 text-sm mt-2">Average score / 100</div></div>
          <div class="rounded-xl border border-white/20 bg-white/10 p-6 backdrop-blur-sm"><div class="font-serif text-4xl font-bold text-white">14%</div><div class="text-white/70 text-sm mt-2">Passing (B or higher)</div></div>
        </div>
      </div>
    </section>
    <section class="py-24 px-6 sm:px-8 lg:px-12">
      <div class="max-w-3xl mx-auto">
        <h2 class="font-serif text-3xl font-bold mb-6">The Two-Part Problem</h2>
        <p class="text-gray-500 text-lg leading-relaxed mb-4"><strong class="text-gray-900">Part 1: Access.</strong> 48% of dealer websites block AI crawlers via robots.txt, CloudFlare, or HTTP-level blocking.</p>
        <p class="text-gray-500 text-lg leading-relaxed mb-10"><strong class="text-gray-900">Part 2: Optimization.</strong> Even sites that allow AI access often lack structured data. 31% have zero LocalBusiness schema.</p>
        <h2 class="font-serif text-3xl font-bold mb-6">What This Means For Your Dealership</h2>
        <p class="text-gray-500 text-lg leading-relaxed mb-4">If your website is invisible to AI search engines like ChatGPT, Perplexity, and Google AI Overviews, you're losing potential customers who never even know you exist.</p>
        <p class="text-center mt-10"><a href="/visibility-audit" class="inline-flex items-center justify-center min-h-[56px] px-10 bg-[#0088ff] text-white font-semibold rounded-full hover:bg-[#0077e6] transition">Check Your Website Free &rarr;</a></p>
      </div>
    </section>
{cta_section()}
  </main>
{footer()}'''
    write_page("case-studies/ai-compatibility.html", content)

    # Privacy Policy
    content = f'''{head("Privacy Policy | Savvy Dealer", "Savvy Dealer privacy policy. Learn how we collect, use, and protect your personal information.", "privacy-policy")}
{nav()}
  <main class="flex-1">
{breadcrumb([("Home", "/"), ("Privacy Policy", None)])}
    <section class="py-16 px-4">
      <div class="max-w-3xl mx-auto prose prose-lg">
        <h1>Privacy Policy</h1>
        <p class="text-sm text-gray-500">Last Updated: 9/20/2024</p>
        <p>Your privacy is paramount to us. As you engage with our services, both on our website and at our physical locations, we want you to be confident in how we manage and protect your personal information.</p>
        <h2>Notice of Collection</h2>
        <p>In the past 12 months, we have collected categories of personal information including names, addresses, contact details, vehicle preferences, and other information voluntarily submitted through online forms or chat functionality.</p>
        <h2>Purpose of Collection</h2>
        <p>We collect this information to provide you with a tailored website experience, process sales, offer post-sales services, respond to your inquiries, and support your use of our website and related services.</p>
        <h2>Cookies and Similar Technologies</h2>
        <p>We utilize cookies and similar technologies to enhance your online experience, analyze our website's performance, and tailor content and advertisements to your preferences.</p>
        <h2>Information Disclosure</h2>
        <p>We may share your information for service enhancement with trusted partners, legal imperatives, business dynamics such as mergers, business partners for expanded services, and agents who execute tasks on our behalf.</p>
        <h2>Children's Information</h2>
        <p>Our platforms are not targeted at children under the age of 16. We do not intentionally gather personal information from those under 16.</p>
        <h2>Contact Us</h2>
        <p>Questions about this Privacy Policy? Contact us at <a href="mailto:{EMAIL}">{EMAIL}</a> or call <a href="tel:{PHONE_HREF}">{PHONE}</a>.</p>
      </div>
    </section>
  </main>
{footer()}'''
    write_page("privacy-policy.html", content)

    # End User Agreement
    content = f'''{head("End User Agreement | Savvy Dealer", "Savvy Dealer end user agreement governing use of products and services.", "end-user-agreement")}
{nav()}
  <main class="flex-1">
{breadcrumb([("Home", "/"), ("End User Agreement", None)])}
    <section class="py-16 px-4">
      <div class="max-w-3xl mx-auto prose prose-lg">
        <h1>End User Agreement</h1>
        <p>The customer signing the Savvy Dealer Subscription Agreement agrees that Customer's use of any products or services offered by Savvy Dealer, Inc. will be subject to these standard terms and conditions.</p>
        <h2>1. Agreement and Services</h2>
        <p>This Agreement governs Customer's use of all Services ordered from Savvy Dealer. Subject to Customer's payment of applicable Fees, Savvy Dealer will provide the Services identified in each Invoice.</p>
        <h2>2. Access to Services</h2>
        <p>Savvy Dealer grants Customer a non-exclusive, non-transferable, limited license to access and use the Services solely for the purpose of enhancing, managing, and displaying data relating to motor vehicles.</p>
        <h2>3. Data Rights</h2>
        <p>Customer retains ownership of all Inventory Data and Performance/Transaction Data. Customer grants Savvy Dealer license to use this data for service delivery and improvement purposes.</p>
        <h2>4. Term and Termination</h2>
        <p>Customer may terminate with 90 days' written notice. Savvy Dealer may terminate with 30 days' notice. All unpaid fees become immediately due upon termination.</p>
        <h2>5. Fees and Payment</h2>
        <p>Payments are due monthly in advance. Late payments may bear interest at 1.5% per month. All amounts paid are non-refundable.</p>
        <h2>Contact</h2>
        <p>Questions? Contact us at <a href="mailto:{EMAIL}">{EMAIL}</a> or call <a href="tel:{PHONE_HREF}">{PHONE}</a>.</p>
      </div>
    </section>
  </main>
{footer()}'''
    write_page("end-user-agreement.html", content)


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------

def generate_all_pages():
    print("Generating pages...")

    # Home
    generate_home()

    # Service pages
    for filename, data in SERVICE_PAGES.items():
        service_page(filename, data)

    # Other pages
    generate_about()
    generate_products()
    generate_book()
    generate_404()
    generate_visibility_audit()
    generate_anti_dashboard()
    generate_simple_pages()

    print(f"  Pages complete!")
