"""Page generators for all static pages."""
from generate import (
    head, nav, footer, breadcrumb, cta_section, faq_section, org_schema,
    write_page, PHONE, PHONE_HREF, EMAIL, DOMAIN
)

# ---------------------------------------------------------------------------
# Service page template
# ---------------------------------------------------------------------------

def service_page(filename, data):
    """Generate a service/product page from a data dict."""
    d = data
    accent = d.get("accent_color", "#2563eb")
    faqs = [(q["question"], q["answer"]) for q in d.get("faqs", [])]

    # Benefits list
    benefits_html = ""
    for b in d.get("benefits", {}).get("items", []):
        benefits_html += f'          <li class="flex items-start gap-3"><svg class="w-5 h-5 text-green-500 mt-0.5 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg><span>{b}</span></li>\n'

    # Features grid
    features_html = ""
    for f in d.get("features", {}).get("items", []):
        features_html += f'''        <div class="bg-white rounded-xl p-6 shadow-sm border border-gray-100">
          <h3 class="text-lg font-semibold text-gray-900 mb-2">{f["title"]}</h3>
          <p class="text-gray-600 text-sm">{f["description"]}</p>
        </div>\n'''

    # Stats
    stats_html = ""
    for s in d.get("proof_stats", {}).get("items", []):
        stats_html += f'''        <div class="text-center">
          <div class="text-3xl font-bold text-blue-600">{s["stat"]}</div>
          <div class="text-sm text-gray-600 mt-1">{s["label"]}</div>
        </div>\n'''

    # Process steps
    process_html = ""
    for s in d.get("process", {}).get("steps", []):
        process_html += f'''        <div class="flex gap-4">
          <div class="w-10 h-10 rounded-full bg-blue-600 text-white flex items-center justify-center font-bold shrink-0">{s["number"]}</div>
          <div>
            <h3 class="font-semibold text-gray-900">{s["title"]}</h3>
            <p class="text-gray-600 text-sm mt-1">{s["description"]}</p>
          </div>
        </div>\n'''

    seo_title = d.get("seo_meta_title", d["title"]) + " | Savvy Dealer"
    seo_desc = d.get("seo_meta_description", d.get("hero_description", ""))
    canonical = filename.replace(".html", "")

    content = f'''{head(seo_title, seo_desc, canonical)}
{nav()}
  <main class="flex-1">
{breadcrumb([("Home", "/"), ("Products", "/products"), (d["title"], None)])}

    <!-- Hero -->
    <section class="hero-bg text-white py-20 px-4">
      <div class="max-w-6xl mx-auto">
        <span class="inline-block bg-white/10 text-blue-200 text-sm font-medium px-3 py-1 rounded-full mb-4">{d.get("badge", "")}</span>
        <h1 class="text-4xl md:text-5xl font-extrabold mb-4">{d["title"]}</h1>
        <p class="text-xl text-blue-100 mb-4">{d["subtitle"]}</p>
        <p class="text-blue-200 max-w-3xl mb-8">{d.get("hero_description", "")}</p>
        <div class="flex flex-col sm:flex-row gap-4">
          <a href="/book" class="inline-flex items-center justify-center px-8 py-3 bg-white text-blue-900 font-semibold rounded-full hover:bg-blue-50 transition">Request Free Audit</a>
          <a href="tel:{PHONE_HREF}" class="inline-flex items-center justify-center px-8 py-3 border-2 border-white text-white font-semibold rounded-full hover:bg-white/10 transition">Call {PHONE}</a>
        </div>
      </div>
    </section>

    <!-- Benefits -->
    <section class="py-16 px-4">
      <div class="max-w-6xl mx-auto">
        <h2 class="text-3xl font-bold text-gray-900 mb-8">{d.get("benefits", {}).get("title", "Why Choose Us")}</h2>
        <ul class="grid md:grid-cols-2 gap-4">
{benefits_html}        </ul>
      </div>
    </section>

    <!-- Features -->
    <section class="py-16 px-4 bg-gray-50">
      <div class="max-w-6xl mx-auto">
        <h2 class="text-3xl font-bold text-gray-900 mb-4">{d.get("features", {}).get("title", "Features")}</h2>
        <p class="text-gray-600 mb-8 max-w-3xl">{d.get("features", {}).get("description", "")}</p>
        <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
{features_html}        </div>
      </div>
    </section>

    <!-- Stats -->
    <section class="py-16 px-4">
      <div class="max-w-4xl mx-auto">
        <h2 class="text-3xl font-bold text-center text-gray-900 mb-8">{d.get("proof_stats", {}).get("title", "By The Numbers")}</h2>
        <div class="grid grid-cols-2 md:grid-cols-4 gap-8">
{stats_html}        </div>
      </div>
    </section>

    <!-- Process -->
    <section class="py-16 px-4 bg-gray-50">
      <div class="max-w-3xl mx-auto">
        <h2 class="text-3xl font-bold text-gray-900 mb-8">{d.get("process", {}).get("title", "Our Process")}</h2>
        <div class="space-y-6">
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
    content = f'''{head("Savvy Dealer - Digital Marketing for Automotive Dealerships", "Expert digital marketing for car dealerships. Facebook Ads, PPC, SEO/GEO optimization, and AI-powered dealer websites. We don't outspend the competition - we outsmart them.", "")}
{nav()}
  <main class="flex-1">
    <!-- Hero -->
    <section class="hero-bg text-white py-24 px-4">
      <div class="max-w-6xl mx-auto text-center">
        <span class="inline-block bg-white/10 text-blue-200 text-sm font-medium px-4 py-1.5 rounded-full mb-6">Digital Marketing for Auto Dealers</span>
        <h1 class="text-4xl md:text-6xl font-extrabold mb-6">The Savvy Dealer Difference</h1>
        <p class="text-xl md:text-2xl text-blue-100 mb-8 max-w-3xl mx-auto">We partner with dealers who know that <strong>leads aren't created - they're captured.</strong></p>
        <div class="flex flex-col sm:flex-row gap-4 justify-center">
          <a href="/book" class="inline-flex items-center justify-center px-8 py-3 bg-white text-blue-900 font-semibold rounded-full hover:bg-blue-50 transition text-lg">Request Free Audit</a>
          <a href="tel:{PHONE_HREF}" class="inline-flex items-center justify-center px-8 py-3 border-2 border-white text-white font-semibold rounded-full hover:bg-white/10 transition text-lg">Call {PHONE}</a>
        </div>
      </div>
    </section>

    <!-- About / How We Drive Sales -->
    <section class="py-20 px-4">
      <div class="max-w-6xl mx-auto">
        <h2 class="text-3xl md:text-4xl font-bold text-gray-900 mb-6">How We Drive Your Sales</h2>
        <p class="text-lg text-gray-600 mb-8 max-w-3xl">By aligning our SEO and GEO (Generative Engine Optimization) strategies, we ensure your dealership doesn't just compete - it <strong>appears first and performs faster</strong> wherever shoppers are searching, from Google to ChatGPT.</p>
        <div class="grid md:grid-cols-2 gap-4 mb-8">
          <div class="flex items-start gap-3"><svg class="w-5 h-5 text-green-500 mt-0.5 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg><span>Counter competitor tactics effectively</span></div>
          <div class="flex items-start gap-3"><svg class="w-5 h-5 text-green-500 mt-0.5 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg><span>Dominate in search and generative AI results</span></div>
          <div class="flex items-start gap-3"><svg class="w-5 h-5 text-green-500 mt-0.5 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg><span>AI-optimized websites that convert</span></div>
          <div class="flex items-start gap-3"><svg class="w-5 h-5 text-green-500 mt-0.5 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg><span>Transparent reporting you can trust</span></div>
        </div>
        <p class="text-lg font-semibold text-gray-900">We don't outspend the competition - <strong>we outsmart them.</strong></p>
      </div>
    </section>

    <!-- Testimonials -->
    <section class="py-20 px-4 bg-gray-50">
      <div class="max-w-6xl mx-auto">
        <h2 class="text-3xl font-bold text-center text-gray-900 mb-2">What Dealers are Saying</h2>
        <p class="text-center text-gray-600 mb-12">Consistent performance improvements and trusted partnerships</p>
        <div class="grid md:grid-cols-3 gap-8">
          <div class="bg-white rounded-xl p-6 shadow-sm border border-gray-100">
            <p class="text-gray-600 text-sm mb-4">"Savvy Dealer nailed the essentials: a high-performing website, marketing that delivers results, consistent service, and reporting that makes decisions obvious. The outcome is steady, consistent performance improvements across traffic quality, conversions, and paid efficiency."</p>
            <p class="font-semibold text-gray-900">Josh Mead</p>
            <p class="text-sm text-gray-500">General Manager, Brighton Ford</p>
          </div>
          <div class="bg-white rounded-xl p-6 shadow-sm border border-gray-100">
            <p class="text-gray-600 text-sm mb-4">"We've been working with Savvy Dealer for over a year, and Savvy Dealer has been a major contributor for Banner Fords success. Our website is faster and converts better, and we see consistent performance improvements across SEO and paid media."</p>
            <p class="font-semibold text-gray-900">Greg Jones</p>
            <p class="text-sm text-gray-500">General Manager, Banner Ford</p>
          </div>
          <div class="bg-white rounded-xl p-6 shadow-sm border border-gray-100">
            <p class="text-gray-600 text-sm mb-4">"Savvy Dealer is the ideal partner for our dealerships. Month after month we see consistent performance improvements across website conversions, SEO visibility, and paid media. Attribution is clear, budgets are transparent."</p>
            <p class="font-semibold text-gray-900">David Blake</p>
            <p class="text-sm text-gray-500">General Manager, Lake Powell Ford and Alamo Ford</p>
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
    <section class="hero-bg text-white py-20 px-4">
      <div class="max-w-6xl mx-auto">
        <h1 class="text-4xl md:text-5xl font-extrabold mb-4">We Don't Outspend the Competition</h1>
        <p class="text-2xl text-blue-100 mb-4">We Outsmart Them</p>
        <p class="text-blue-200 max-w-3xl">Savvy Dealer was founded on a simple principle: automotive dealerships deserve digital marketing that actually drives sales, not just impressions. We combine deep industry expertise with data-driven strategies to help dealers win in an increasingly competitive market.</p>
      </div>
    </section>

    <section class="py-16 px-4">
      <div class="max-w-6xl mx-auto grid md:grid-cols-2 gap-12">
        <div>
          <h2 class="text-2xl font-bold text-gray-900 mb-4">Our Mission</h2>
          <p class="text-gray-600">To empower automotive dealerships with marketing strategies that focus on ready-to-buy shoppers, transparent ROI metrics, and measurable results. We believe in building backwards from the sale, optimizing for conversations and test drives - not vanity metrics.</p>
        </div>
        <div>
          <h2 class="text-2xl font-bold text-gray-900 mb-4">What Sets Us Apart</h2>
          <ul class="space-y-3">
            <li class="flex items-start gap-3"><span class="font-semibold text-blue-600">High-intent focus:</span> We target shoppers who are ready now, not "someday"</li>
            <li class="flex items-start gap-3"><span class="font-semibold text-blue-600">Transparent metrics:</span> Simple, human-readable KPIs that matter</li>
            <li class="flex items-start gap-3"><span class="font-semibold text-blue-600">Agile execution:</span> Twice-monthly cadence to pivot against competitors</li>
            <li class="flex items-start gap-3"><span class="font-semibold text-blue-600">Real content:</span> No AI-generated fluff - just substance that ranks</li>
          </ul>
        </div>
      </div>
    </section>

    <section class="py-16 px-4 bg-gray-50">
      <div class="max-w-6xl mx-auto">
        <h2 class="text-3xl font-bold text-center text-gray-900 mb-12">Our Team</h2>
        <div class="grid md:grid-cols-3 lg:grid-cols-5 gap-8">
          <div class="text-center"><div class="w-24 h-24 bg-gray-200 rounded-full mx-auto mb-3"></div><h3 class="font-semibold">Adam Gillrie</h3><p class="text-sm text-gray-500">Director</p></div>
          <div class="text-center"><div class="w-24 h-24 bg-gray-200 rounded-full mx-auto mb-3"></div><h3 class="font-semibold">Nick Chivinski</h3><p class="text-sm text-gray-500">VP of Sales</p></div>
          <div class="text-center"><div class="w-24 h-24 bg-gray-200 rounded-full mx-auto mb-3"></div><h3 class="font-semibold">David Frost</h3><p class="text-sm text-gray-500">CTO</p></div>
          <div class="text-center"><div class="w-24 h-24 bg-gray-200 rounded-full mx-auto mb-3"></div><h3 class="font-semibold">Emily Shultz</h3><p class="text-sm text-gray-500">Head of Operations</p></div>
          <div class="text-center"><div class="w-24 h-24 bg-gray-200 rounded-full mx-auto mb-3"></div><h3 class="font-semibold">Lucas Terwilliger</h3><p class="text-sm text-gray-500">Strategist</p></div>
        </div>
      </div>
    </section>

    <section class="py-16 px-4">
      <div class="max-w-6xl mx-auto">
        <h2 class="text-3xl font-bold text-center text-gray-900 mb-12">Our Values</h2>
        <div class="grid md:grid-cols-3 gap-8">
          <div class="text-center"><h3 class="text-xl font-semibold mb-2">Results-Driven</h3><p class="text-gray-600">Every campaign is built to drive real conversations, test drives, and sales - not just traffic.</p></div>
          <div class="text-center"><h3 class="text-xl font-semibold mb-2">Partnership</h3><p class="text-gray-600">We're an extension of your team, meeting twice monthly to plan and pivot based on market conditions.</p></div>
          <div class="text-center"><h3 class="text-xl font-semibold mb-2">Innovation</h3><p class="text-gray-600">From AI-optimized websites to attribution intelligence, we stay ahead of the automotive marketing curve.</p></div>
        </div>
      </div>
    </section>

{cta_section("Ready to Work Together?", "Let's discuss how Savvy Dealer can help your dealership dominate your market")}
  </main>
{footer()}'''
    write_page("about.html", content)


def generate_products():
    products = [
        ("Fully Managed Marketing", "Premium Service", "White-glove service that handles everything - co-op management, vendor coordination, website, SEO, SEM, Facebook ads, design, and ROI tracking.", "/fully-managed-marketing"),
        ("Facebook Ads", "Capture Traffic / Drive Sales", "Hand-built Facebook Ads that lead the industry in performance. We hand-select vehicles for maximum results.", "/facebook-ads"),
        ("Dealer SEO + GEO", "Fuel Long-Term Site Growth", "SEO + GEO optimization that positions your dealership first in traditional search and AI-powered results.", "/dealer-seo"),
        ("PPC Ads", "Turbocharge Your PPC", "Industry-leading Google and Bing Ad campaigns that focus on your in-stock inventory.", "/ppc-ads"),
        ("Vehicle Ads", "Stop Wasting Your VLA Budget", "Reclaim thousands wasted on Google's Display Network. Expert Performance Max management.", "/vehicle-ads"),
        ("Dealer Websites", "Dominate Your Online Market", "SEO-first website architecture that accelerates your digital marketing efforts.", "/dealer-websites"),
        ("Independent Dealer Websites", "Built For Your Business", "Premium websites for independent dealers and buy-here-pay-here lots. No franchise fees.", "/independent-dealer-websites"),
        ("Anti-Dashboard AI", "Coming Soon", "AI-powered attribution and analytics that transforms how you measure marketing success.", "/anti-dashboard"),
    ]
    cards_html = ""
    for name, subtitle, desc, url in products:
        cards_html += f'''        <div class="bg-white rounded-xl p-6 shadow-sm border border-gray-100 hover:shadow-md transition">
          <h3 class="text-xl font-semibold text-gray-900 mb-1">{name}</h3>
          <p class="text-sm text-blue-600 font-medium mb-3">{subtitle}</p>
          <p class="text-gray-600 text-sm mb-4">{desc}</p>
          <a href="{url}" class="text-blue-600 font-medium text-sm hover:underline">Learn More &rarr;</a>
        </div>\n'''

    content = f'''{head("Savvy Product Suite - Automotive Marketing Solutions | Savvy Dealer", "Comprehensive suite of automotive marketing products. Facebook Ads, PPC, SEO/GEO, dealer websites, and AI-powered tools.", "products")}
{nav()}
  <main class="flex-1">
{breadcrumb([("Home", "/"), ("Products", None)])}
    <section class="hero-bg text-white py-20 px-4">
      <div class="max-w-6xl mx-auto text-center">
        <h1 class="text-4xl md:text-5xl font-extrabold mb-4">Savvy Product Suite</h1>
        <p class="text-lg text-blue-200 max-w-3xl mx-auto">At Savvy Dealer, we customize our marketing packages to meet your needs, not ours. Our comprehensive suite of products works together to counter competitor tactics and dominate in both search and generative AI results.</p>
      </div>
    </section>

    <section class="py-16 px-4">
      <div class="max-w-6xl mx-auto">
        <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
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
    <section class="py-20 px-4">
      <div class="max-w-2xl mx-auto">
        <h1 class="text-4xl font-extrabold text-gray-900 mb-4 text-center">Request a Free Audit</h1>
        <p class="text-gray-600 text-center mb-8">Fill out the form below and we'll analyze your digital presence and show you exactly how we can help.</p>
        <form data-ajax action="/api/schedule-demo" class="space-y-5">
          <div><label for="name" class="block text-sm font-medium text-gray-700 mb-1">Name *</label><input type="text" id="name" name="name" required class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"></div>
          <div><label for="email" class="block text-sm font-medium text-gray-700 mb-1">Email *</label><input type="email" id="email" name="email" required class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"></div>
          <div><label for="phone" class="block text-sm font-medium text-gray-700 mb-1">Phone *</label><input type="tel" id="phone" name="phone" required class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"></div>
          <div><label for="dealership" class="block text-sm font-medium text-gray-700 mb-1">Dealership</label><input type="text" id="dealership" name="dealership" class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"></div>
          <div><label for="message" class="block text-sm font-medium text-gray-700 mb-1">Tell us about your goals</label><textarea id="message" name="message" rows="4" class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"></textarea></div>
          <button type="submit" class="w-full bg-blue-600 text-white py-3 px-6 rounded-lg font-semibold hover:bg-blue-700 transition text-lg">Submit Request</button>
        </form>
        <p class="text-center text-sm text-gray-500 mt-6">Or call us directly: <a href="tel:{PHONE_HREF}" class="text-blue-600 font-semibold">{PHONE}</a></p>
      </div>
    </section>
  </main>
{footer()}'''
    write_page("book.html", content)


def generate_404():
    content = f'''{head("Page Not Found - Savvy Dealer", "The page you're looking for doesn't exist.", "404")}
{nav()}
  <main class="flex-1">
    <section class="py-32 px-4 text-center">
      <h1 class="text-6xl font-extrabold text-gray-300 mb-4">404</h1>
      <h2 class="text-2xl font-bold text-gray-900 mb-4">Page Not Found</h2>
      <p class="text-gray-600 mb-8">The page you're looking for doesn't exist or has been moved.</p>
      <a href="/" class="inline-flex items-center px-6 py-3 bg-blue-600 text-white font-semibold rounded-full hover:bg-blue-700 transition">Back to Home</a>
    </section>
  </main>
{footer()}'''
    write_page("404.html", content)


def generate_visibility_audit():
    content = f'''{head("AI Visibility Audit - Check Your Dealership | Savvy Dealer", "Check how visible your dealership is to AI search engines like ChatGPT and Perplexity.", "visibility-audit")}
{nav()}
  <main class="flex-1">
{breadcrumb([("Home", "/"), ("Visibility Audit", None)])}
    <section class="py-20 px-4 text-center">
      <div class="max-w-3xl mx-auto">
        <h1 class="text-4xl font-extrabold text-gray-900 mb-4">AI Visibility Audit</h1>
        <p class="text-lg text-gray-600 mb-8">Check how visible your dealership is to AI search engines like ChatGPT, Perplexity, and Google AI Overviews.</p>
        <a href="https://ai-compatible-v3-185609396182.us-central1.run.app" target="_blank" rel="noopener" class="inline-flex items-center px-8 py-4 bg-blue-600 text-white font-semibold rounded-full hover:bg-blue-700 transition text-lg">Run Your Free AI Visibility Audit &rarr;</a>
        <p class="text-sm text-gray-500 mt-4">Free tool - no login required</p>
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
    <section class="hero-bg text-white py-24 px-4 text-center">
      <div class="max-w-4xl mx-auto">
        <span class="inline-block bg-white/10 text-blue-200 text-sm font-medium px-4 py-1.5 rounded-full mb-6">Coming Soon</span>
        <h1 class="text-4xl md:text-5xl font-extrabold mb-4">Anti-Dashboard AI</h1>
        <p class="text-xl text-blue-100 mb-8">Something big is coming. AI will transform automotive attribution and analytics. Be among the first to see how.</p>
        <a href="/book" class="inline-flex items-center px-8 py-3 bg-white text-blue-900 font-semibold rounded-full hover:bg-blue-50 transition">Schedule a Preview</a>
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
    <section class="hero-bg text-white py-20 px-4">
      <div class="max-w-4xl mx-auto text-center">
        <span class="inline-block bg-white/10 text-blue-200 text-sm font-medium px-4 py-1.5 rounded-full mb-6">Exclusive Early Access</span>
        <h1 class="text-4xl md:text-5xl font-extrabold mb-4">Not Going to NADA? See What Everyone Else Will Be Talking About First</h1>
        <p class="text-lg text-blue-200 mb-8">Get early access to Savvy Dealer's new Anti-Dashboard Dashboard and upcoming dealer marketing tools before they are introduced at NADA.</p>
        <a href="/book" class="inline-flex items-center px-8 py-3 bg-white text-blue-900 font-semibold rounded-full hover:bg-blue-50 transition">Schedule Your Early Access Demo</a>
      </div>
    </section>
    <section class="py-16 px-4">
      <div class="max-w-3xl mx-auto prose prose-lg">
        <p>Not everyone can make it to NADA, and that should not put you behind. Savvy Dealer is preparing to introduce a new way for dealers to measure digital marketing success, along with tools designed for AI-ready visibility, smarter spend, and clearer reporting.</p>
        <p>Before this is shown publicly at NADA, a limited number of dealers are being given a private preview. <strong>This is your opportunity to see what is coming before the rest of the industry.</strong></p>
        <h2>What You'll Get With an Early Preview</h2>
        <ul>
          <li>A private walkthrough of the Anti-Dashboard Dashboard</li>
          <li>Insight into new reporting and attribution concepts before public release</li>
          <li>An overview of Savvy Dealer's AI-ready website and SEO strategies</li>
          <li>A look at how smarter paid search and social campaigns are built to convert</li>
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
    <section class="hero-bg text-white py-20 px-4">
      <div class="max-w-6xl mx-auto text-center">
        <span class="inline-block bg-white/10 text-blue-200 text-sm font-medium px-4 py-1.5 rounded-full mb-4">Booth 6760N | February 4-6, 2026 | Las Vegas</span>
        <h1 class="text-4xl md:text-5xl font-extrabold mb-4">Why Visit Savvy Dealer at NADA Show 2026</h1>
        <p class="text-lg text-blue-200 mb-8">Get exclusive access to our Anti-Dashboard, master GEO before your competitors, and discover strategies from top-performing dealers.</p>
        <a href="/book" class="inline-flex items-center px-8 py-3 bg-white text-blue-900 font-semibold rounded-full hover:bg-blue-50 transition">Lock in Your Strategy Session</a>
      </div>
    </section>
    <section class="py-16 px-4">
      <div class="max-w-6xl mx-auto">
        <h2 class="text-3xl font-bold text-center mb-12">Proven Results From Real Dealers</h2>
        <div class="grid md:grid-cols-4 gap-8 text-center">
          <div><div class="text-3xl font-bold text-blue-600">+838%</div><div class="text-sm text-gray-600">Verified Users (Banner Chevy)</div></div>
          <div><div class="text-3xl font-bold text-blue-600">+340%</div><div class="text-sm text-gray-600">VDP Views (Banner Chevy)</div></div>
          <div><div class="text-3xl font-bold text-blue-600">+47%</div><div class="text-sm text-gray-600">Conversions (Brighton Ford)</div></div>
          <div><div class="text-3xl font-bold text-blue-600">-32%</div><div class="text-sm text-gray-600">Cost Per Lead (Lake Powell Ford)</div></div>
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
    <section class="hero-bg text-white py-20 px-4">
      <div class="max-w-6xl mx-auto">
        <span class="inline-block bg-white/10 text-blue-200 text-sm font-medium px-3 py-1 rounded-full mb-4">Independent Dealer Solutions</span>
        <h1 class="text-4xl md:text-5xl font-extrabold mb-4">Independent Dealer Websites With SEO & GEO Built In</h1>
        <p class="text-blue-200 max-w-3xl mb-8">Get a lightning-fast, mobile-first dealer website modeled after our highest-performing dealers, with SEO and GEO baked in - without giving up control of your domain or your data.</p>
        <div class="flex flex-col sm:flex-row gap-4">
          <a href="/book" class="inline-flex items-center justify-center px-8 py-3 bg-white text-blue-900 font-semibold rounded-full hover:bg-blue-50 transition">Book a 15-Minute Demo</a>
        </div>
      </div>
    </section>

    <section class="py-16 px-4">
      <div class="max-w-6xl mx-auto">
        <h2 class="text-3xl font-bold mb-8">Why Most Independent Dealer Websites Leave Money on the Table</h2>
        <div class="grid md:grid-cols-2 gap-6">
          <div class="bg-red-50 border border-red-100 rounded-xl p-6"><h3 class="font-semibold text-red-800 mb-2">Slow on mobile</h3><p class="text-gray-600 text-sm">When your site takes too long to load, shoppers bounce before they ever see your inventory.</p></div>
          <div class="bg-red-50 border border-red-100 rounded-xl p-6"><h3 class="font-semibold text-red-800 mb-2">Hard for Google and AI</h3><p class="text-gray-600 text-sm">Generic templates and messy URL structures make it hard for Google and AI engines to find you.</p></div>
          <div class="bg-red-50 border border-red-100 rounded-xl p-6"><h3 class="font-semibold text-red-800 mb-2">You don't really own it</h3><p class="text-gray-600 text-sm">With some providers, your website lives on their subdomain. If you leave, you fight over your domain.</p></div>
          <div class="bg-red-50 border border-red-100 rounded-xl p-6"><h3 class="font-semibold text-red-800 mb-2">Weak conversion paths</h3><p class="text-gray-600 text-sm">Buried phone numbers and hard-to-tap buttons mean traffic doesn't turn into leads.</p></div>
        </div>
      </div>
    </section>

    <section class="py-16 px-4 bg-gray-50">
      <div class="max-w-6xl mx-auto">
        <h2 class="text-3xl font-bold mb-4">What's Included</h2>
        <p class="text-gray-600 mb-8">Everything is built around one goal: help independent and BHPH dealers turn more visitors into real opportunities.</p>
        <div class="grid md:grid-cols-2 gap-8">
          <div class="bg-white rounded-xl p-6 border border-gray-100"><h3 class="font-semibold text-lg mb-2">High-Converting Dealer Website</h3><p class="text-gray-600 text-sm">Clean SRP/VDP structure, clear CTAs, inventory-focused design. You keep your domain.</p></div>
          <div class="bg-white rounded-xl p-6 border border-gray-100"><h3 class="font-semibold text-lg mb-2">SEO Built In From Day One</h3><p class="text-gray-600 text-sm">Search-friendly URLs, structured data, smart internal linking.</p></div>
          <div class="bg-white rounded-xl p-6 border border-gray-100"><h3 class="font-semibold text-lg mb-2">GEO - Generative Engine Optimization</h3><p class="text-gray-600 text-sm">Machine-readable signals so AI assistants can find and recommend your store.</p></div>
          <div class="bg-white rounded-xl p-6 border border-gray-100"><h3 class="font-semibold text-lg mb-2">Mobile-First and Lightning Fast</h3><p class="text-gray-600 text-sm">Performance-minded templates, mobile-first layouts, fewer bounces.</p></div>
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
        feat_badge = '<span class="bg-blue-100 text-blue-700 text-xs px-2 py-0.5 rounded-full">Featured</span>' if featured else ""
        cards += f'''        <div class="bg-white rounded-xl p-6 shadow-sm border border-gray-100 hover:shadow-md transition">
          <div class="flex items-center gap-2 mb-3"><span class="bg-gray-100 text-gray-700 text-xs px-2 py-0.5 rounded-full">{badge}</span><span class="text-xs text-gray-500">{readtime}</span>{feat_badge}</div>
          <h3 class="text-lg font-semibold text-gray-900 mb-2">{title}</h3>
          <p class="text-gray-600 text-sm mb-4">{desc}</p>
          <a href="{url}" class="text-blue-600 font-medium text-sm hover:underline">Read Guide &rarr;</a>
        </div>\n'''

    content = f'''{head("Dealer Marketing Resources - Free Guides & Playbooks | Savvy Dealer", "In-depth guides, playbooks, and strategies to help your dealership win in digital marketing.", "resources")}
{nav()}
  <main class="flex-1">
{breadcrumb([("Home", "/"), ("Resources", None)])}
    <section class="hero-bg text-white py-20 px-4 text-center">
      <div class="max-w-4xl mx-auto">
        <span class="inline-block bg-white/10 text-blue-200 text-sm font-medium px-4 py-1.5 rounded-full mb-6">Free Resources</span>
        <h1 class="text-4xl md:text-5xl font-extrabold mb-4">Dealer Marketing Resources</h1>
        <p class="text-lg text-blue-200">In-depth guides, playbooks, and strategies to help your dealership win in digital marketing. No fluff - just actionable insights.</p>
      </div>
    </section>
    <section class="py-16 px-4">
      <div class="max-w-6xl mx-auto">
        <div class="grid md:grid-cols-2 gap-6">
{cards}        </div>
      </div>
    </section>
{cta_section()}
  </main>
{footer()}'''
    write_page("resources/index.html", content)

    # Resource guide placeholder pages (content is very long - we'll generate simplified versions)
    for slug, title, desc in [
        ("seo-guide", "The Complete Dealership SEO Guide for 2025", "Future-proof strategies to dominate search rankings, drive organic traffic, and capture more leads."),
        ("facebook-ads-playbook", "2026 Facebook Ads Playbook for Dealerships", "Advanced strategies for inventory-based automotive advertising on Meta platforms."),
        ("geo-guide", "The Complete Guide to Generative Engine Optimization for Car Dealers", "How to get your dealership cited in AI search engines like ChatGPT, Perplexity, and Google AI Overviews."),
        ("reputation-guide", "The Dealership Reputation Guide", "How to build, manage, and protect your online reputation."),
    ]:
        content = f'''{head(f"{title} | Savvy Dealer", desc, f"resources/{slug}")}
{nav()}
  <main class="flex-1">
{breadcrumb([("Home", "/"), ("Resources", "/resources"), (title, None)])}
    <section class="hero-bg text-white py-20 px-4">
      <div class="max-w-4xl mx-auto text-center">
        <h1 class="text-3xl md:text-4xl font-extrabold mb-4">{title}</h1>
        <p class="text-lg text-blue-200">{desc}</p>
      </div>
    </section>
    <section class="py-16 px-4">
      <div class="max-w-3xl mx-auto prose prose-lg">
        <p class="text-gray-600">This guide is being migrated to the new platform. Check back soon for the complete content.</p>
        <p class="text-gray-600">In the meantime, <a href="/book" class="text-blue-600 hover:underline">request a free audit</a> to discuss your dealership's strategy.</p>
      </div>
    </section>
{cta_section()}
  </main>
{footer()}'''
        write_page(f"resources/{slug}.html", content)

    # Case Studies
    content = f'''{head("Case Studies - Dealerships Winning with Savvy Dealer", "From improved website performance to crystal-clear attribution, see how we help dealerships drive measurable results.", "case-studies")}
{nav()}
  <main class="flex-1">
{breadcrumb([("Home", "/"), ("Case Studies", None)])}
    <div class="bg-blue-600 text-white text-center py-3 px-4 text-sm">
      <a href="/case-studies/ai-compatibility" class="hover:underline font-medium">84% of Dealer Websites Are Invisible to AI -- See the Full Study &rarr;</a>
    </div>
    <section class="hero-bg text-white py-20 px-4">
      <div class="max-w-6xl mx-auto text-center">
        <span class="inline-block bg-white/10 text-blue-200 text-sm font-medium px-4 py-1.5 rounded-full mb-4">Real Results</span>
        <h1 class="text-4xl md:text-5xl font-extrabold mb-4">Dealerships Winning with Savvy Dealer</h1>
        <p class="text-lg text-blue-200">From improved website performance to crystal-clear attribution, see how we help dealerships drive measurable results.</p>
      </div>
    </section>
    <section class="py-16 px-4">
      <div class="max-w-6xl mx-auto space-y-12">
        <!-- Banner Chevrolet -->
        <div class="bg-white rounded-xl p-8 shadow-sm border border-gray-100">
          <div class="flex items-center gap-2 mb-4"><h2 class="text-2xl font-bold">Banner Chevrolet</h2><span class="text-sm text-gray-500">New Orleans, LA</span></div>
          <p class="text-gray-600 mb-6">Slow mobile experience with weak Core Web Vitals suppressed organic and paid performance. Disjointed paid media limited reach and efficiency.</p>
          <div class="grid md:grid-cols-4 gap-6 mb-6">
            <div class="text-center bg-green-50 rounded-lg p-4"><div class="text-2xl font-bold text-green-600">+838%</div><div class="text-sm text-gray-600">Verified Users YoY</div></div>
            <div class="text-center bg-green-50 rounded-lg p-4"><div class="text-2xl font-bold text-green-600">+340%</div><div class="text-sm text-gray-600">VDP Views YoY</div></div>
            <div class="text-center bg-green-50 rounded-lg p-4"><div class="text-2xl font-bold text-green-600">&lt;1.5s</div><div class="text-sm text-gray-600">Mobile LCP</div></div>
            <div class="text-center bg-green-50 rounded-lg p-4"><div class="text-2xl font-bold text-green-600">-25%</div><div class="text-sm text-gray-600">Media Spend YoY</div></div>
          </div>
          <blockquote class="border-l-4 border-blue-600 pl-4 italic text-gray-600">"After moving to Savvy Dealer and unifying our SEO, Google Ads, and Meta strategy, our results took off."<br><span class="not-italic font-semibold text-gray-900">- Greg Jones, General Manager</span></blockquote>
        </div>
        <!-- Brighton Ford -->
        <div class="bg-white rounded-xl p-8 shadow-sm border border-gray-100">
          <div class="flex items-center gap-2 mb-4"><h2 class="text-2xl font-bold">Brighton Ford</h2><span class="text-sm text-gray-500">Brighton, CO</span></div>
          <p class="text-gray-600 mb-6">Needed consistent marketing performance and better ROI visibility across all digital channels.</p>
          <div class="grid md:grid-cols-4 gap-6 mb-6">
            <div class="text-center bg-green-50 rounded-lg p-4"><div class="text-2xl font-bold text-green-600">+47%</div><div class="text-sm text-gray-600">Conversions</div></div>
            <div class="text-center bg-green-50 rounded-lg p-4"><div class="text-2xl font-bold text-green-600">+62%</div><div class="text-sm text-gray-600">Quality Traffic</div></div>
            <div class="text-center bg-green-50 rounded-lg p-4"><div class="text-2xl font-bold text-green-600">+38%</div><div class="text-sm text-gray-600">Paid Media Efficiency</div></div>
            <div class="text-center bg-green-50 rounded-lg p-4"><div class="text-2xl font-bold text-green-600">+54%</div><div class="text-sm text-gray-600">SEO Visibility</div></div>
          </div>
          <blockquote class="border-l-4 border-blue-600 pl-4 italic text-gray-600">"Savvy Dealer nailed the essentials: a high-performing website, marketing that delivers results, consistent service."<br><span class="not-italic font-semibold text-gray-900">- Josh Mead, General Manager</span></blockquote>
        </div>
        <!-- Lake Powell & Alamo -->
        <div class="bg-white rounded-xl p-8 shadow-sm border border-gray-100">
          <div class="flex items-center gap-2 mb-4"><h2 class="text-2xl font-bold">Lake Powell Ford & Alamo Ford</h2><span class="text-sm text-gray-500">Page, AZ & San Antonio, TX</span></div>
          <p class="text-gray-600 mb-6">Managing marketing across two distinct markets with different competition levels and customer demographics.</p>
          <div class="grid md:grid-cols-4 gap-6 mb-6">
            <div class="text-center bg-green-50 rounded-lg p-4"><div class="text-2xl font-bold text-green-600">+68%</div><div class="text-sm text-gray-600">Lead Volume</div></div>
            <div class="text-center bg-green-50 rounded-lg p-4"><div class="text-2xl font-bold text-green-600">-32%</div><div class="text-sm text-gray-600">Cost Per Lead</div></div>
            <div class="text-center bg-green-50 rounded-lg p-4"><div class="text-2xl font-bold text-green-600">+44%</div><div class="text-sm text-gray-600">Appointment Rate</div></div>
            <div class="text-center bg-green-50 rounded-lg p-4"><div class="text-2xl font-bold text-green-600">+100%</div><div class="text-sm text-gray-600">Attribution Clarity</div></div>
          </div>
          <blockquote class="border-l-4 border-blue-600 pl-4 italic text-gray-600">"Month after month we see consistent performance improvements. Attribution is clear, budgets are transparent."<br><span class="not-italic font-semibold text-gray-900">- David Blake, General Manager</span></blockquote>
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
    <section class="hero-bg text-white py-20 px-4">
      <div class="max-w-6xl mx-auto text-center">
        <h1 class="text-4xl md:text-5xl font-extrabold mb-6">84% of Dealer Websites Are Invisible to AI</h1>
        <div class="grid md:grid-cols-4 gap-6 mt-8">
          <div><div class="text-4xl font-bold">84%</div><div class="text-blue-200 text-sm">Failing AI compatibility</div></div>
          <div><div class="text-4xl font-bold">48%</div><div class="text-blue-200 text-sm">Actively blocking AI</div></div>
          <div><div class="text-4xl font-bold">34</div><div class="text-blue-200 text-sm">Average score / 100</div></div>
          <div><div class="text-4xl font-bold">14%</div><div class="text-blue-200 text-sm">Passing (B or higher)</div></div>
        </div>
      </div>
    </section>
    <section class="py-16 px-4">
      <div class="max-w-3xl mx-auto prose prose-lg">
        <h2>The Two-Part Problem</h2>
        <p><strong>Part 1: Access.</strong> 48% of dealer websites block AI crawlers via robots.txt, CloudFlare, or HTTP-level blocking.</p>
        <p><strong>Part 2: Optimization.</strong> Even sites that allow AI access often lack structured data. 31% have zero LocalBusiness schema.</p>
        <h2>What This Means For Your Dealership</h2>
        <p>If your website is invisible to AI search engines like ChatGPT, Perplexity, and Google AI Overviews, you're losing potential customers who never even know you exist.</p>
        <p class="text-center mt-8"><a href="/visibility-audit" class="inline-flex items-center px-8 py-3 bg-blue-600 text-white font-semibold rounded-full hover:bg-blue-700 transition no-underline">Check Your Website Free &rarr;</a></p>
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
