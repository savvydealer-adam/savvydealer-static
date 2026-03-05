"""Generate full resource guide pages."""
from generate import (
    head, nav, footer, breadcrumb, cta_section, faq_section,
    write_page, DOMAIN
)


def _guide_page(slug, title, desc, badge, read_time, updated, body_html,
                faqs=None, cta_title=None, cta_desc=None):
    """Shared template for long-form resource guide pages."""
    faq_html = faq_section(faqs) if faqs else ""
    ct = cta_title or "Ready to Dominate Your Market?"
    cd = cta_desc or "See how Savvy Dealer can transform your dealership's digital marketing."
    schema = '{"@context":"https://schema.org","@type":"Article","headline":"' + title + '","publisher":{"@type":"Organization","name":"Savvy Dealer","url":"' + DOMAIN + '"}}'

    content = f'''{head(f"{title} | Savvy Dealer", desc, f"resources/{slug}", og_type="article")}
{nav()}
  <main class="flex-1">
{breadcrumb([("Home", "/"), ("Resources", "/resources"), (title[:50] + "..." if len(title) > 50 else title, None)])}
    <section class="relative flex min-h-[50vh] items-center justify-center overflow-hidden px-6 py-20 sm:px-8 lg:px-12" style="background:linear-gradient(135deg, #0a2540 0%, #1e3a5f 50%, #0088ff 100%)">
      <div class="relative z-10 max-w-7xl mx-auto text-center">
        <div class="mx-auto max-w-4xl space-y-6">
          <div class="inline-flex items-center gap-2 rounded-full border border-white/20 bg-white/10 px-5 py-2.5 text-sm backdrop-blur-md">
            <span class="font-medium text-white">{badge}</span>
          </div>
          <h1 class="font-serif text-3xl font-bold leading-tight text-white sm:text-4xl lg:text-5xl">{title}</h1>
          <p class="text-lg text-white/80">{desc}</p>
          <div class="flex items-center justify-center gap-4 text-sm text-white/60">
            <span>{read_time}</span>
            <span>Updated: {updated}</span>
          </div>
        </div>
      </div>
    </section>
    <article class="py-24 px-6 sm:px-8 lg:px-12">
      <div class="max-w-3xl mx-auto">
{body_html}
      </div>
    </article>
{faq_html}
    <script type="application/ld+json">{schema}</script>
{cta_section(ct, cd)}
  </main>
{footer()}'''
    write_page(f"resources/{slug}.html", content)


def _h2(text):
    return f'        <h2 class="text-2xl font-bold mt-12 mb-4 text-gray-900">{text}</h2>'


def _h3(text):
    return f'        <h3 class="text-xl font-semibold mt-8 mb-3 text-gray-900">{text}</h3>'


def _h4(text):
    return f'        <h4 class="text-lg font-semibold mt-6 mb-2 text-gray-900">{text}</h4>'


def _p(text):
    return f'        <p class="text-gray-700 leading-relaxed my-4">{text}</p>'


def _ul(items):
    li = "\n".join(f'          <li>{item}</li>' for item in items)
    return f'        <ul class="list-disc pl-6 space-y-2 my-4 text-gray-700">\n{li}\n        </ul>'


def _ol(items):
    li = "\n".join(f'          <li>{item}</li>' for item in items)
    return f'        <ol class="list-decimal pl-6 space-y-2 my-4 text-gray-700">\n{li}\n        </ol>'


def _callout(text, color="blue"):
    return f'        <div class="bg-{color}-50 border-l-4 border-{color}-600 p-4 my-6 rounded-r-lg"><p class="text-{color}-900 text-sm font-medium">{text}</p></div>'


def _key_takeaway(text):
    return f'        <div class="bg-amber-50 border-l-4 border-amber-500 p-4 my-6 rounded-r-lg"><p class="text-amber-900 text-sm"><strong>KEY TAKEAWAY:</strong> {text}</p></div>'


def _key_insight(text):
    return f'        <div class="bg-emerald-50 border-l-4 border-emerald-500 p-4 my-6 rounded-r-lg"><p class="text-emerald-900 text-sm"><strong>KEY INSIGHT:</strong> {text}</p></div>'


def _table(headers, rows):
    th = "".join(f'<th class="text-left py-2 px-4 border-b border-gray-200 text-sm font-semibold text-gray-900">{h}</th>' for h in headers)
    body = ""
    for row in rows:
        cells = "".join(f'<td class="py-2 px-4 border-b border-gray-100 text-sm text-gray-700">{c}</td>' for c in row)
        body += f"<tr>{cells}</tr>"
    return f'''        <div class="overflow-x-auto my-6">
          <table class="w-full border-collapse">
            <thead><tr>{th}</tr></thead>
            <tbody>{body}</tbody>
          </table>
        </div>'''


def _stats_row(stats):
    """Stats as colored cards."""
    cards = ""
    for stat, label in stats:
        cards += f'<div class="text-center bg-gray-50 rounded-xl p-6 border border-gray-200"><div class="font-serif text-2xl font-bold text-[#0088ff]">{stat}</div><div class="text-sm text-gray-500 mt-1">{label}</div></div>'
    return f'        <div class="grid md:grid-cols-{len(stats)} gap-4 my-6">{cards}</div>'


# ===================================================================
# SEO GUIDE
# ===================================================================

def generate_seo_guide():
    body = "\n".join([
        _p("Search engine optimization has undergone a dramatic transformation over the past several years. The strategies that worked in 2020 or even 2023 may no longer be effective\u2014and some could actually hurt your rankings. Understanding the current SEO landscape is essential before diving into specific tactics."),
        _p("For dealerships, these changes present both challenges and opportunities. While the rules have become more complex, they also favor businesses that genuinely serve their customers well. If your dealership provides excellent service and valuable information, modern SEO allows you to demonstrate that to search engines more effectively than ever before."),

        # Section 1
        _h2("1. The SEO Landscape in 2025 \u2014 What's Changed"),
        _h3("The Shift from Keywords to Intent"),
        _p("The days of stuffing keywords into content and watching rankings climb are long gone. Google's algorithms have become sophisticated enough to understand the meaning behind searches, not just the words themselves. This semantic understanding means you need to focus on answering questions and solving problems, not just including specific phrases."),
        _callout("<strong>What This Means for Dealerships:</strong> Instead of creating separate pages targeting \u2018used trucks,\u2019 \u2018pre-owned trucks,\u2019 and \u2018second-hand trucks,\u2019 focus on creating comprehensive, helpful content about your used truck inventory. Google understands these terms are related and will rank helpful content for all relevant variations."),
        _h3("The Rise of AI in Search"),
        _p("Artificial intelligence now powers both sides of the search equation. Google uses AI to better understand queries and content, while new AI-powered search tools like ChatGPT, Perplexity, and Google's AI Overviews are changing how consumers discover businesses."),
        _p("This dual AI presence means dealerships must optimize for both traditional search rankings and AI-generated recommendations. A strategy that ignores either avenue leaves significant opportunity on the table."),
        _h3("User Experience as a Ranking Factor"),
        _p("Google has made clear that user experience directly impacts rankings. Core Web Vitals\u2014metrics measuring load speed, interactivity, and visual stability\u2014are now official ranking factors. Sites that frustrate users with slow load times or janky interfaces will struggle to rank, regardless of their content quality."),
        _key_takeaway("Modern SEO success requires a holistic approach combining great content, technical excellence, and outstanding user experience. There are no shortcuts or tricks\u2014only genuine quality and strategic optimization."),

        # Section 2
        _h2("2. Understanding Google's Core Algorithm Updates"),
        _p("Google updates its search algorithms hundreds of times per year, but certain major updates have fundamentally changed how rankings work. Understanding these updates helps you align your strategy with what Google rewards\u2014and avoid practices that could trigger penalties."),
        _h3("The Helpful Content Update"),
        _p("Launched in 2022 and continuously refined, the Helpful Content Update targets content created primarily for search engines rather than humans. This update fundamentally changed content strategy for many industries, including automotive retail."),
        _h4("Content That Gets Demoted"),
        _ul([
            "Content that answers questions people aren't actually asking",
            "Pages that exist solely to rank for keywords without providing value",
            "Aggregated content that doesn't add original insight or analysis",
            "Content that leaves readers needing to search again for better information",
            "AI-generated content published without human review or added value",
        ]),
        _h4("Content That Gets Rewarded"),
        _ul([
            "Original information, research, or analysis",
            "Comprehensive coverage that doesn't leave important questions unanswered",
            "Content that demonstrates real expertise and experience",
            "Pages that satisfy the reader without requiring additional searches",
            "Content created for a specific audience with genuine intent to help",
        ]),
        _h3("Core Updates and Their Impact"),
        _p("Google releases several broad core updates annually. These updates don't target specific sites or tactics but rather refine how Google assesses overall content quality. Sites may see significant ranking changes after core updates\u2014either positive or negative."),
        _callout("<strong>How to Respond to Core Updates:</strong> If your rankings drop after a core update, resist the urge to make reactive changes. Instead, honestly assess whether your content truly serves users as well as competing content. Focus on improving quality rather than trying to reverse-engineer what changed."),
        _key_takeaway("The best protection against algorithm updates is building a website that genuinely serves users well. Sites focused on quality rarely suffer significant losses from algorithm changes\u2014they usually benefit."),

        # Section 3
        _h2("3. E-E-A-T \u2014 The Foundation of Modern SEO"),
        _p("E-E-A-T stands for <strong>Experience, Expertise, Authoritativeness, and Trustworthiness</strong>. While not a direct ranking factor, E-E-A-T represents the qualities Google's algorithms are designed to identify and reward. Understanding and demonstrating these qualities is essential for sustainable SEO success."),
        _table(["Pillar", "What It Means", "For Dealerships"], [
            ["Experience", "First-hand knowledge of a topic", "Include author bios highlighting automotive experience, share behind-the-scenes content"],
            ["Expertise", "Deep knowledge of your subject matter", "A service manager's maintenance explanations carry more weight than generic content"],
            ["Authoritativeness", "Being recognized as a go-to source", "Earn backlinks from respected publications, display certifications"],
            ["Trustworthiness", "The most important factor", "Display real reviews, provide transparent pricing, use HTTPS, respond to feedback"],
        ]),
        _key_takeaway("E-E-A-T isn't something you optimize for directly\u2014it's a framework for understanding what makes content valuable. Focus on genuinely being experienced, expert, authoritative, and trustworthy, and your SEO will benefit naturally."),

        # Section 4
        _h2("4. Local SEO \u2014 Your Dealership's Competitive Edge"),
        _p("Local SEO is perhaps the most important SEO discipline for dealerships. Unlike e-commerce businesses competing nationally, most of your customers come from a defined geographic area. Dominating local search results can transform your business by capturing customers at the exact moment they're looking for what you offer."),
        _h3("Why Local SEO Matters"),
        _p("Consider how people actually search for dealerships. Queries like \u2018Honda dealer near me,\u2019 \u2018used cars in [city],\u2019 and \u2018car dealerships open now\u2019 all carry strong local intent. These searchers aren't casually browsing\u2014they're actively looking to buy, often within the next few days."),
        _callout("<strong>The Local Pack Advantage:</strong> Google's local pack\u2014the map-based results that appear for local searches\u2014gets significant click-through rates. Appearing in this prime real estate puts your dealership in front of high-intent customers before they even see organic results."),
        _h3("Local Search Ranking Factors"),
        _table(["Factor", "Description"], [
            ["Relevance", "How well your business matches the search query"],
            ["Distance", "Physical proximity to the searcher's location"],
            ["Prominence", "How well-known and reputable your business is"],
            ["Reviews", "Quantity, quality, and recency of customer reviews"],
            ["Website Quality", "Traditional SEO signals from your website"],
        ]),
        _h3("The Local SEO Ecosystem"),
        _p("Local SEO isn't just about your website\u2014it's about your entire online presence. Google gathers information about your business from numerous sources and uses this collective data to determine rankings."),
        _ul([
            "Google Business Profile (formerly Google My Business)",
            "Local citations across directories and platforms",
            "Customer reviews on Google and other platforms",
            "Locally-focused website content",
            "Local backlinks from community sources",
            "Social media presence and engagement",
        ]),
        _key_takeaway("Local SEO success requires consistent effort across multiple platforms. A strong Google Business Profile alone isn't enough\u2014you need a cohesive strategy that reinforces your local presence everywhere potential customers might look."),

        # Section 5
        _h2("5. Google Business Profile Optimization"),
        _p("Your Google Business Profile (GBP) is arguably the single most important asset for local SEO. It controls how your dealership appears in Google Maps, the local pack, and knowledge panels. A fully optimized profile significantly increases your visibility and click-through rates."),
        _h3("Profile Optimization Checklist"),
        _ul([
            "Complete every section of your profile with accurate information",
            "Add high-quality photos of your lot, showroom, and team",
            "Select all relevant categories (primary + secondary)",
            "Add services offered with detailed descriptions",
            "Keep business hours updated, including holiday schedules",
            "Write a compelling business description with keywords",
            "Enable messaging and Q&A features",
            "Post weekly updates about inventory, promotions, and events",
            "Respond to all reviews within 24-48 hours",
        ]),

        # Section 6
        _h2("6. Local Citations & NAP Consistency"),
        _p("A citation is any online mention of your dealership's name, address, and phone number (NAP). Citations appear on business directories, social platforms, apps, and websites. Consistent and accurate citations help Google verify your business information and improve local rankings."),
        _callout("<strong>Critical Rule:</strong> Your NAP must be exactly the same everywhere it appears online. \u201c123 Main Street\u201d is different from \u201c123 Main St.\u201d in Google's eyes. Inconsistencies confuse search engines and can hurt your rankings."),
        _h3("Priority Citation Sources for Dealerships"),
        _ul([
            "<strong>Automotive-specific:</strong> Cars.com, AutoTrader, CarGurus, Edmunds, DealerRater",
            "<strong>Major directories:</strong> Yelp, Yellow Pages, BBB, Apple Maps, Bing Places",
            "<strong>Social platforms:</strong> Facebook, Instagram, LinkedIn, X (Twitter)",
            "<strong>Local sources:</strong> Chamber of Commerce, local news sites, community directories",
        ]),

        # Section 7
        _h2("7. Creating Locally Relevant Content"),
        _p("Content that speaks to your specific community signals relevance to both users and search engines. Generic content that could apply to any dealership anywhere won't help you dominate local search."),
        _h3("Local Content Ideas"),
        _ul([
            'City-specific buying guides (e.g., "Best Cars for [City] Winters")',
            "Local event sponsorships and community involvement coverage",
            "Neighborhood spotlights and local driving tips",
            "Staff profiles highlighting local connections",
            "Customer success stories from your community",
        ]),

        # Section 8
        _h2("8. Mobile-First Indexing"),
        _p("Google now primarily uses the mobile version of your website for indexing and ranking. If your site doesn't work well on phones, you're invisible to a majority of car shoppers\u2014and to Google."),
        _stats_row([("70%+", "Car research on mobile"), ("53%", "Users abandon slow mobile sites"), ("3 sec", "Max mobile load time")]),
        _h3("Mobile Optimization Essentials"),
        _ul([
            "Responsive design that adapts to all screen sizes",
            "Touch-friendly navigation with appropriately sized buttons",
            "Click-to-call phone numbers throughout the site",
            "Mobile-optimized forms with minimal required fields",
            "Fast-loading images with proper compression",
        ]),

        # Section 9
        _h2("9. Site Speed Optimization"),
        _p("Page speed is a confirmed ranking factor and directly impacts user experience. A one-second delay in page load time can result in 7% fewer conversions. For dealerships, this translates directly to lost leads and sales."),
        _h3("Core Web Vitals Explained"),
        _table(["Metric", "What It Measures", "Target"], [
            ["Largest Contentful Paint (LCP)", "Loading performance", "Under 2.5 seconds"],
            ["Interaction to Next Paint (INP)", "Interactivity", "Under 200 milliseconds"],
            ["Cumulative Layout Shift (CLS)", "Visual stability", "Under 0.1"],
        ]),
        _h3("Speed Optimization Tactics"),
        _ul([
            "Compress and optimize all images (WebP format recommended)",
            "Implement lazy loading for below-the-fold content",
            "Minimize and combine CSS and JavaScript files",
            "Use a content delivery network (CDN)",
            "Enable browser caching and server compression",
        ]),

        # Section 10
        _h2("10. Content Optimization"),
        _p("Content remains the foundation of SEO, but what constitutes \u201cgood content\u201d has evolved dramatically. Today's successful content must satisfy user intent, demonstrate expertise, and provide genuine value that competitors don't offer."),
        _ul([
            "<strong>Answer the question completely:</strong> Don't leave readers needing to search elsewhere",
            "<strong>Add unique value:</strong> Include original insights, data, or perspectives",
            "<strong>Structure for scanning:</strong> Use headers, bullets, and visual breaks",
            "<strong>Keep it current:</strong> Update content regularly with fresh information",
            "<strong>Optimize naturally:</strong> Include keywords where they fit naturally, not forced",
        ]),

        # Section 11
        _h2("11. Understanding Search Intent"),
        _p("Search intent is the reason behind a search query. Understanding whether someone wants to learn, find, or buy determines what content will satisfy their needs\u2014and what Google will rank."),
        _table(["Intent Type", "Example Query", "Strategy"], [
            ["Informational", '"How much does an oil change cost?"', "Create helpful guides, FAQ pages, educational content"],
            ["Navigational", '"ABC Toyota hours"', "Ensure your business info is accurate and easy to find"],
            ["Commercial", '"Best SUVs for families 2025"', "Create comparison content and buying guides"],
            ["Transactional", '"Used Honda Civic for sale near me"', "Optimize inventory pages with clear CTAs"],
        ]),

        # Section 12
        _h2("12. Schema Markup & Structured Data"),
        _p("Schema markup is code that helps search engines understand your content better. For dealerships, proper schema can enhance your search listings with rich snippets, star ratings, pricing, and availability information."),
        _h3("Essential Schema Types for Dealerships"),
        _ul([
            "<strong>LocalBusiness/AutoDealer:</strong> Business information, hours, location",
            "<strong>Vehicle:</strong> Individual vehicle listings with specs and pricing",
            "<strong>Review/AggregateRating:</strong> Customer reviews and ratings",
            "<strong>FAQPage:</strong> Common questions and answers",
            "<strong>Service:</strong> Service department offerings",
        ]),

        # Section 13
        _h2("13. Building Quality Backlinks"),
        _p("Backlinks remain one of Google's most important ranking factors. Quality matters far more than quantity\u2014a single link from a respected local news site is worth more than hundreds of links from low-quality directories."),
        _h3("Link Building Strategies for Dealerships"),
        _ul([
            "<strong>Community involvement:</strong> Sponsor local events, charities, and sports teams",
            "<strong>Local press:</strong> Share newsworthy stories with local media",
            "<strong>Manufacturer programs:</strong> Ensure proper links from OEM dealer locators",
            "<strong>Industry associations:</strong> Join dealer associations with member directories",
            "<strong>Content partnerships:</strong> Guest post on automotive and local blogs",
        ]),
        _callout("<strong>Warning:</strong> Avoid purchasing links or participating in link schemes. Google actively penalizes these practices, and recovery can take months or years.", "red"),

        # Section 14
        _h2("14. Voice Search Optimization"),
        _p('Voice search continues to grow, with more people using Siri, Alexa, and Google Assistant to find local businesses. Voice queries tend to be longer, more conversational, and often question-based.'),
        _ul([
            "Target long-tail, conversational keywords",
            "Create FAQ content answering common questions directly",
            "Ensure your Google Business Profile is fully optimized",
            'Focus on local "near me" style queries',
            "Improve site speed for featured snippet positioning",
        ]),

        # Section 15
        _h2("15. AI Search & Generative Engine Optimization (GEO)"),
        _p("AI-powered search tools like ChatGPT, Perplexity, and Google's AI Overviews represent the next frontier of search. These platforms synthesize information from multiple sources to provide direct answers rather than links."),
        _callout('<strong>The GEO Opportunity:</strong> When someone asks an AI assistant "What\'s the best dealership for first-time buyers in [your city]?", the AI synthesizes multiple sources and provides a direct recommendation. Getting cited in these answers can drive significant traffic and trust.'),
        _ul([
            "Create comprehensive, authoritative content on key topics",
            "Build a strong review profile across multiple platforms",
            "Establish thought leadership through consistent, quality content",
            "Ensure structured data is properly implemented",
        ]),

        # Section 16
        _h2("16. User Engagement Signals"),
        _p("While Google doesn't confirm engagement metrics as direct ranking factors, evidence strongly suggests that how users interact with your site influences rankings. Sites that engage visitors tend to rank better."),
        _ul([
            "<strong>Click-through rate:</strong> Compelling titles and meta descriptions",
            "<strong>Time on site:</strong> Engaging, valuable content that holds attention",
            "<strong>Pages per session:</strong> Clear navigation and internal linking",
            "<strong>Bounce rate:</strong> Meeting user expectations with relevant content",
            "<strong>Return visits:</strong> Building loyalty through consistent value",
        ]),

        # Section 17
        _h2("17. Video SEO for Dealerships"),
        _p("Video content is increasingly important for both engagement and rankings. YouTube is the second-largest search engine, and video results often appear prominently in Google search."),
        _ul([
            "Vehicle walkarounds and feature highlights",
            "Customer testimonials and success stories",
            "Service department tips and maintenance guides",
            "Dealership tours and staff introductions",
            "Local community involvement and events",
        ]),

        # Section 18
        _h2("18. Technical SEO Fundamentals"),
        _p("Technical SEO ensures search engines can efficiently crawl, understand, and index your website. Even great content won't rank if technical issues prevent Google from accessing it."),
        _h3("Technical SEO Checklist"),
        _ul([
            "Implement SSL certificate (HTTPS) across entire site",
            "Create and submit XML sitemap to Google Search Console",
            "Optimize robots.txt to allow proper crawling",
            "Fix broken links (404 errors) and redirect chains",
            "Implement canonical tags to prevent duplicate content",
            "Ensure proper heading hierarchy (H1, H2, H3)",
            "Optimize URL structure for readability and keywords",
            "Enable browser caching and compression",
            "Implement proper 301 redirects for changed URLs",
            "Monitor Core Web Vitals and fix issues",
        ]),

        # Section 19
        _h2("19. SEO Tools & Resources"),
        _h3("Free Tools"),
        _ul([
            "<strong>Google Search Console</strong> \u2014 Monitor search performance",
            "<strong>Google Analytics 4</strong> \u2014 Track website traffic and behavior",
            "<strong>Google PageSpeed Insights</strong> \u2014 Analyze site speed",
            "<strong>Google Business Profile</strong> \u2014 Manage local presence",
            "<strong>Bing Webmaster Tools</strong> \u2014 Monitor Bing search performance",
        ]),
        _h3("Premium Tools"),
        _ul([
            "<strong>SEMrush</strong> \u2014 Comprehensive SEO suite",
            "<strong>Ahrefs</strong> \u2014 Backlink analysis and keyword research",
            "<strong>Moz Pro</strong> \u2014 Domain authority and rank tracking",
            "<strong>Screaming Frog</strong> \u2014 Technical SEO auditing",
            "<strong>BrightLocal</strong> \u2014 Local SEO management",
        ]),

        # Section 20
        _h2("20. Your 90-Day SEO Action Plan"),
        _p("Implementing everything at once is overwhelming. This 90-day plan prioritizes actions by impact and helps you build momentum."),
        _h3("Days 1\u201330: Foundation Phase"),
        _ul([
            "Claim and fully optimize Google Business Profile",
            "Set up Google Search Console and Analytics",
            "Fix critical technical issues (HTTPS, broken links, site speed)",
            "Audit and correct NAP consistency across top 20 citations",
            "Implement review generation strategy",
        ]),
        _h3("Days 31\u201360: Content & Local Phase"),
        _ul([
            "Create or optimize key landing pages for each service",
            "Develop 5 pieces of locally-focused content",
            "Implement schema markup across key pages",
            "Build citations on automotive-specific platforms",
            "Start local link building outreach",
        ]),
        _h3("Days 61\u201390: Optimization & Expansion Phase"),
        _ul([
            "Analyze results and adjust strategy based on data",
            "Create video content for key inventory/services",
            "Expand content strategy based on search performance",
            "Implement GEO optimization strategies",
            "Plan ongoing monthly SEO activities",
        ]),
        _key_takeaway("SEO is a marathon, not a sprint. Consistent, quality effort over time will yield far better results than any quick-fix tactics. Focus on genuinely serving your customers well, and the rankings will follow."),
    ])

    faqs = [
        ("How long does SEO take to work for car dealerships?",
         "Most dealerships see measurable improvements in 3-6 months, with significant results in 6-12 months. Local SEO improvements like Google Business Profile optimization can show results faster, often within weeks."),
        ("What is E-E-A-T and why does it matter for dealer SEO?",
         "E-E-A-T stands for Experience, Expertise, Authoritativeness, and Trustworthiness. Google uses these signals to evaluate content quality. For dealerships, demonstrating expertise through helpful content and building trust through reviews directly impacts rankings."),
        ("How important is mobile optimization for dealer websites?",
         "Critical. Google uses mobile-first indexing, meaning your mobile site determines rankings. Over 60% of car research happens on mobile devices. A slow or poorly optimized mobile experience hurts both rankings and conversions."),
        ("What is local SEO for car dealerships?",
         "Local SEO optimizes your dealership to appear in location-based searches like 'car dealers near me' and Google Maps results. It includes Google Business Profile optimization, local citations, reviews management, and locally-focused content."),
        ("How do I improve my dealership's Google Business Profile?",
         "Complete every field, add high-quality photos regularly, respond to all reviews, post updates weekly, ensure NAP consistency across the web, and use relevant categories. Active profiles with engagement signals rank higher in local results."),
    ]

    _guide_page(
        "seo-guide",
        "The Complete Dealership SEO Guide for 2025",
        "Future-proof strategies to dominate search rankings, drive organic traffic, and capture more leads.",
        "2025 Complete SEO Guide", "45 min read", "December 2025",
        body, faqs,
        "Need Expert Help With Your SEO Strategy?",
        "Our team specializes in automotive SEO. Let us audit your current presence and show you exactly where the opportunities are."
    )


# ===================================================================
# FACEBOOK ADS PLAYBOOK
# ===================================================================

def generate_facebook_ads_playbook():
    body = "\n".join([
        _p("Meta has become the highest-intent social channel for in-market auto shoppers. With Marketplace visibility, AI-driven placements, and first-party CRM integrations, Facebook remains the only platform where dealerships can launch VIN-level, dynamic, retail-ready vehicle ads at scale\u2014while still layering on human-built creative that Marketplace prefers."),
        _p("This playbook details the 2026 best practices your dealership needs to dominate Meta with inventory-based ads."),

        # Section 1
        _h2("1. The 2026 Meta Landscape for Automotive"),
        _h3("What Changed in 2026"),
        _ol([
            "<strong>Marketplace Vehicle Distribution</strong> \u2014 Now prioritizes human-structured listing data over feed-only automated ads",
            "<strong>Advantage+ Creative Expansion</strong> \u2014 Meta can auto-optimize text, cropping, backgrounds, and CTAs\u2014but automotive results still perform best when fed structured inventory plus manual descriptions",
            "<strong>AI Lookalikes</strong> \u2014 Auto-refresh weekly to reduce audience fatigue",
            "<strong>On-Platform Lead Flows</strong> \u2014 Meta Instant Forms + Messenger Threads convert at 2\u20134x the rate of website VDP visits",
            "<strong>Inventory Availability Signals</strong> \u2014 Mileage, days-on-lot, price reductions, EV incentives now enhance ad ranking",
        ]),

        # Section 2
        _h2("2. Inventory Architecture: The Foundation"),
        _p("Your inventory feed is the backbone of every Meta campaign. Without clean, comprehensive data, even the best creative and targeting will underperform."),
        _h3("Required Data Fields"),
        _ul([
            "VIN",
            "Body Style and Trim",
            "Price + Price History",
            "Mileage",
            "OEM Packages and Key Features",
            "20\u201330 high-resolution images",
            "Stock Number",
            "Dealer Address and Geo Pins",
        ]),
        _callout("<strong>Meta Image Quality Update:</strong> Meta now reads image EXIF data and applies clarity scoring. Dealerships with high-resolution, properly lit photos see 15\u201325% lower CPM compared to blurry or dark images."),
        _h3("Recommended Optional Enhancements"),
        _p("Meta now scores feeds using Auto Quality Signals:"),
        _ul([
            '<strong>Reconditioned Features:</strong> "New Tires", "Fresh Brakes", "Service Completed"',
            '<strong>Dealer Value Props:</strong> "Lifetime Warranty", "Free Home Delivery"',
            "<strong>Fuel Savings:</strong> Hybrid/EV comparisons",
            "<strong>Payment Estimates:</strong> Monthly payment calculations",
        ]),
        _callout("<strong>Why Human-Built Marketplace Listings Win:</strong> Marketplace ranks human-authored listings higher than automated feed ads. Manual listing creation provides better search placement, more buyer messages, lower CPM, and reduced duplicate flagging.", "green"),

        # Section 3
        _h2("3. Creative Frameworks That Win in 2026"),
        _h3("Campaign Architecture: Hybrid Approach"),
        _p("The three-pillar approach consistently outperforms standalone catalog ads. Each pillar serves a distinct purpose: Marketplace drives conversations, DVA handles scale, and Brand+Offer reinforces your value proposition."),
        _table(["Pillar", "Type", "Output"], [
            ["Human-Built", "Marketplace Listings", "High-intent messages"],
            ["Dynamic Vehicle Ads", "VIN-Level Automation", "Retargeting + Acquisition"],
            ["Brand + Offer", "OEM Incentives", "Dealer differentiators"],
        ]),
        _h3("Human-Built Vehicle Ad Structure"),
        _ol([
            "<strong>Title</strong> \u2014 Year + Make + Model + Key Benefit",
            "<strong>First Lines</strong> \u2014 Feature-driven copy (avoid generic templates)",
            "<strong>Condition Notes</strong> \u2014 Mention reconditioning details that build trust",
            '<strong>Call-To-Action</strong> \u2014 "Message for availability" (algorithm prefers conversational intent)',
        ]),
        _h3("Photo Order (Optimal Sequence)"),
        _ol([
            "Front Quarter (Hero shot)",
            "Interior (Cockpit)",
            "Rear Seats (Space)",
            "Features (Highlights)",
            "Packages (OEM adds)",
            "Details (Condition)",
        ]),

        # Section 4
        _h2("4. Audience Strategy"),
        _h3("Core Audiences (Always Running)"),
        _ul([
            "Auto In-Market AI Audience",
            "15\u201330 mile radius geo-zones",
            "Catalog Retargeting (VDP views)",
        ]),
        _h3("High-Intent Custom (CRM-Based)"),
        _ul([
            "CRM Uploads (ADF/XML/CSV)",
            "Past buyers (1\u20136 years)",
            "Service customers",
        ]),
        _h3("Lookalike Layers (Priority Ranking)"),
        _ol([
            "Messenger Conversations",
            "Lead Form Starters",
            "Service Customers",
            "High-Equity Owners",
            "EV Shoppers (for EV dealers)",
        ]),

        # Section 5
        _h2("5. Campaign Types and Structures"),
        _table(["Campaign Type", "Goal", "Best For"], [
            ["Marketplace + Human Listings", "Drive high-intent message conversations", "Used inventory, trucks, older units"],
            ["Advantage+ Catalog Ads", "VIN-specific ads to active shoppers", "New inventory, high-volume, price drops"],
            ["Hybrid Architecture", "Full-funnel coverage", "All dealerships (recommended)"],
        ]),

        # Section 6
        _h2("6. Messaging Frameworks and Copy Templates"),
        _h3("Used Inventory (Most Effective)"),
        _ul([
            '"Clean Carfax + New Tires"',
            '"Fully Serviced, Ready Today"',
            '"Financing for all credit levels\u2014fast approvals."',
            '"Message for availability\u2014units move fast."',
        ]),
        _h3("Trade-In Acquisition"),
        _ul([
            '"We\'ll buy your car even if you don\'t buy from us."',
            '"Get your instant offer\u2014paid same day."',
            '"Overbook value for select models."',
        ]),

        # Section 7
        _h2("7. Lead Capture Optimization"),
        _table(["Method", "Best For", "Tips"], [
            ["Instant Forms", "Volume", "Keep to 8 fields max, use conditional questions, enable Higher Intent Mode"],
            ["Messenger Threads", "Appointment Conversion", "Availability confirmation, price range auto-reply, trade-in + appointment flow"],
        ]),

        # Section 8
        _h2("8. Marketplace Optimization Best Practices"),
        _h3("Listing Rotation Strategy"),
        _ul([
            "Refresh listings every 7\u201310 days",
            "Remove sold vehicles immediately",
            "Cycle top performers back into rotation",
        ]),
        _h3("Behavioral Ranking Signals"),
        _p("Marketplace now evaluates: Response time, Conversation quality, Price fairness scoring, and Listing completeness."),

        # Section 9
        _h2("9. Analytics and KPI Benchmarks"),
        _h3("Lead Metrics by Source"),
        _table(["Lead Source", "Cost Per Lead (CPL)"], [
            ["Messenger", "$8\u2013$18"],
            ["Instant Form", "$12\u2013$30"],
            ["Website VDP", "$25\u2013$80"],
        ]),
        _stats_row([("$8\u2013$18", "Messenger CPL"), ("$12\u2013$30", "Form CPL"), ("$25\u2013$80", "VDP CPL")]),

        # Section 10
        _h2("10. Compliance and Ad Policy Guardrails"),
        _p("Meta auto-reviews every vehicle ad. Avoid these common violations:"),
        _ul([
            'Claims like "guaranteed approval"',
            "VIN in primary text (keep in feed only)",
            "All-caps shouting",
            "Odometer dishonesty",
            "AI-generated fake features or misrepresentations",
        ]),

        # Section 11
        _h2("11. Execution Checklist"),
        _h3("Before Launch"),
        _ul(["Clean, updated feed", "Image audit (10+ photos/unit)", "Tracking tags working", "Offline CRM event upload"]),
        _h3("Weekly"),
        _ul(["Rotate Marketplace listings", "Remove sold units", "Refresh creative variations", "Review aged units"]),
        _h3("Monthly"),
        _ul(["Analyze VIN-level performance", "Rebuild Lookalikes", "Resync CRM audiences", "Review attribution/ROAS"]),

        # Section 12
        _h2("12. Add-On Strategies for Competitive Dealerships"),
        _ol([
            "<strong>EV-Specific Campaign Layer</strong> \u2014 Highlight charging costs, federal incentives, and local rebates.",
            "<strong>Spanish-Language Creative</strong> \u2014 Near-native copy nets 15\u201335% lower CPL in bilingual markets.",
            "<strong>Service-to-Sales Funnels</strong> \u2014 Leverage service history to target upgrade opportunities.",
            "<strong>Regional Market Dominance</strong> \u2014 Run VIN-level conquest campaigns targeting competitor shoppers.",
        ]),
    ])

    faqs = [
        ("What is VIN-level dynamic advertising on Facebook?",
         "VIN-level dynamic ads automatically pull individual vehicle data from your inventory feed to create personalized ads for each car in stock. They show the exact vehicle, price, and details to shoppers based on their browsing behavior and interests."),
        ("How do I get my inventory into Facebook Marketplace?",
         "You need to set up a catalog in Meta Commerce Manager, connect an inventory feed (via partner integration or direct upload), and apply for Marketplace vehicle listing eligibility. Most dealers use feed management tools to automate this process."),
        ("What budget should dealerships spend on Facebook Ads?",
         "Most successful dealerships allocate $3,000-$10,000+ monthly on Meta advertising. Start with a test budget around $1,500-$2,000 to optimize campaigns before scaling. Focus on ROAS and cost-per-lead metrics rather than just spend."),
        ("Which performs better: Marketplace or traditional Facebook ads?",
         "Both have different strengths. Marketplace captures high-intent shoppers actively searching for vehicles with 2-4x higher conversion rates. Traditional ads excel at brand awareness and retargeting. Most dealerships should run both simultaneously."),
        ("How do I track Facebook ad conversions for my dealership?",
         "Install the Meta Pixel on your website, set up the Conversions API for server-side tracking, define custom conversion events (lead forms, VDP views, phone calls), and connect your CRM for offline conversion tracking to measure actual sales."),
    ]

    _guide_page(
        "facebook-ads-playbook",
        "2026 Facebook Ads Playbook for Dealerships",
        "Advanced strategies for inventory-based automotive advertising on Meta platforms.",
        "2026 Meta Advertising Playbook", "20 min read", "January 2026",
        body, faqs,
        "Ready to Dominate Meta Ads?",
        "Our team manages Facebook and Instagram campaigns for dealerships across the country. Let us show you what's possible with a properly structured Meta strategy."
    )


# ===================================================================
# GEO GUIDE
# ===================================================================

def generate_geo_guide():
    body = "\n".join([
        _p("The way car buyers find dealerships is changing faster than any shift we've seen since the rise of Google itself. By 2026, an estimated 15% of all organic traffic to websites will come from AI search platforms\u2014and that number is climbing every month. If your dealership isn't optimized for these new \u201canswer engines,\u201d you're invisible to a growing segment of in-market shoppers."),
        _p('This guide breaks down exactly what Generative Engine Optimization (GEO) means for automotive retail, why it matters right now, and the specific steps your dealership needs to take to show up when customers ask AI assistants questions like "What\'s the best Toyota dealer near me?" or "Where can I find a reliable used truck under $25,000?"'),

        # Section 1
        _h2("1. What Is Generative Engine Optimization?"),
        _p("Generative Engine Optimization\u2014or GEO\u2014is the practice of structuring your dealership's digital presence so that AI-powered platforms cite you in their answers. Unlike traditional SEO, where you're competing for a spot on a list of ten blue links, GEO is about becoming the answer that an AI synthesizes from across the web."),
        _p("The term was formally introduced by researchers at Princeton University in late 2023, and by 2025, it had become a standard component of digital marketing strategy. For car dealers, GEO represents the most significant shift in how customers discover businesses since mobile search overtook desktop."),
        _callout('Traditional SEO asks "How do I rank higher on a list?" GEO asks "How do I become the source an AI trusts enough to quote?"'),
        _p('Think of it this way: when someone asks ChatGPT "What\'s the best dealership for first-time buyers in [your city]?", the AI doesn\'t show them a search results page. It synthesizes information from dozens of sources and provides a direct answer\u2014often naming specific businesses. If you\'re not optimized for this new reality, your competitors will be the ones getting mentioned.'),

        # Section 2
        _h2("2. How AI Search Differs from Traditional Google Search"),
        _p("Understanding the fundamental differences between traditional search and AI-powered search is critical for any dealer who wants to stay competitive. The mechanics are completely different\u2014and so are the optimization strategies."),
        _h3("The Critical Shift: From Rankings to Citations"),
        _p("In traditional SEO, your goal was to rank on page one. In GEO, your goal is to be cited\u2014to be one of the sources the AI trusts enough to reference when forming its answer. This is a fundamentally different game with different rules."),
        _table(["Traditional SEO", "Generative Engine Optimization"], [
            ["Compete for 10 organic positions", "Compete to be cited in a single answer"],
            ["Optimize for keywords", "Optimize for entity recognition and authority"],
            ["Click-through rate matters most", "Citation frequency is the key metric"],
            ["Meta descriptions drive clicks", "Structured data drives AI comprehension"],
            ["Backlink quantity important", "Source authority and topical relevance matter more"],
        ]),

        # Section 3
        _h2("3. Why This Matters for Car Dealers\u2014Right Now"),
        _p("The automotive industry is particularly vulnerable to this shift because car buying is research-intensive. Customers ask complex, conversational questions that AI is specifically designed to answer:"),
        _ul([
            '"What\'s the most reliable dealership in [city] for used trucks?"',
            '"Which dealer has the best financing options for first-time buyers?"',
            '"Where should I buy a Honda Civic in [region] if I want good service after the sale?"',
            '"What dealers near me don\'t charge over MSRP?"',
        ]),
        _p("These aren't keyword searches\u2014they're questions. And increasingly, customers are asking them directly to ChatGPT, Perplexity, or Google's AI Overviews instead of typing fragmented keywords into a search bar."),
        _stats_row([("14.5%", "Projected AI traffic share by late 2026"), ("12.8%", "Searches triggering AI Overviews"), ("10.4", "Avg. sources cited per ChatGPT response")]),

        # Section 4
        _h2("4. The 7-Step GEO Framework for Dealerships"),
        _p("Based on the latest research and best practices emerging in the industry, here's a practical framework for optimizing your dealership's presence in AI search results."),

        _h3("Step 1: Build an AI-Readable Website Foundation"),
        _p("AI crawlers evaluate your content differently than traditional search bots. They're looking for semantic clarity, structured data, and content that can be easily parsed and extracted. Start with these technical fundamentals:"),
        _ol([
            "<strong>Implement comprehensive schema markup.</strong> Use LocalBusiness, AutoDealer, Product, Review, and FAQ schemas. This gives AI engines structured data they can parse directly.",
            "<strong>Create clear content hierarchies.</strong> Use proper heading structures (H1 \u2192 H2 \u2192 H3) that make your content's organization obvious to AI parsers.",
            "<strong>Optimize page speed and Core Web Vitals.</strong> Fast, technically sound sites are more likely to be crawled thoroughly and cited accurately.",
            "<strong>Ensure mobile excellence.</strong> AI training data increasingly comes from mobile-first indexing; poor mobile experiences hurt your citation potential.",
        ]),

        _h3("Step 2: Create Authority-Building Content"),
        _p("AI engines prioritize content that demonstrates expertise, experience, authoritativeness, and trustworthiness (E-E-A-T). For dealerships, this means going beyond basic inventory listings:"),
        _ul([
            'Develop comprehensive buying guides specific to your market. Instead of generic content, create guides like "The Complete Guide to Buying a Truck in [Your Region]: Weather Considerations, Best Models, and Local Dealer Comparison."',
            "Publish transparent pricing information when possible. AI engines frequently cite sources that provide clear, verifiable data.",
            'Feature real expertise. Include named authors with credentials. A service article written by "John Smith, ASE-Certified Master Technician" carries more weight than anonymous content.',
        ]),

        _h3("Step 3: Dominate Your Reputation Ecosystem"),
        _p("AI engines synthesize information from multiple sources\u2014your website is just one input. Reviews, forum discussions, and third-party mentions all influence whether you get cited."),
        _p("Research shows that platforms like Reddit appear heavily in AI responses for both Perplexity and Google's AI features. Wikipedia content accounts for nearly half of ChatGPT's top citations. This means your reputation across the entire web matters."),
        _callout("<strong>Action Item:</strong> Monitor and actively respond to reviews on Google, DealerRater, and Cars.com. Encourage satisfied customers to share their experiences on Reddit's local and automotive subreddits. These discussions become training data for AI models.", "green"),

        _h3("Step 4: Optimize for Conversational Queries"),
        _p("Traditional keyword research focuses on search volume and competition. GEO requires understanding the natural language questions customers actually ask AI assistants."),
        _p('Start by asking AI engines questions about your own market: "What\'s the best Honda dealer in [your city]?" "Where should I buy a used car in [your region]?" See what sources get cited and what information gets included. Then create content that directly addresses these query patterns.'),
        _p("Structure your content to answer questions completely. AI engines look for comprehensive, self-contained answers they can extract and synthesize. Pages that thoroughly address a topic are more likely to be cited than thin content that requires users to look elsewhere."),

        _h3("Step 5: Build Entity Recognition"),
        _p("AI engines work by recognizing and connecting entities\u2014people, places, businesses, and concepts. The more clearly your dealership is established as a distinct, authoritative entity, the more likely you are to be cited."),
        _p("Ensure your dealership's name, address, and phone number (NAP) are consistent across every platform. Claim and optimize all relevant business profiles: Google Business Profile, Apple Maps, Bing Places, and automotive directories. Create content that explicitly connects your dealership to your market, brands you sell, and services you provide."),

        _h3("Step 6: Leverage Multi-Platform Content Distribution"),
        _p("Your website alone won't win at GEO. AI engines cite information from wherever they find authority\u2014and different platforms carry different weight with different AI systems."),
        _ul([
            "Google's AI tends to favor established high-authority domains.",
            "Perplexity shows strong preference for Reddit discussions and community-generated content.",
            "ChatGPT heavily weights Wikipedia and academic or well-cited sources.",
        ]),
        _p("This means your content strategy needs to extend beyond your own site. Contribute to industry publications. Ensure your dealership has accurate Wikipedia mentions if you qualify. Engage authentically in relevant Reddit communities."),

        _h3("Step 7: Measure What Matters"),
        _p("Traditional SEO metrics like rankings and click-through rates don't capture GEO performance. New metrics are emerging:"),
        _ul([
            "<strong>AI Visibility Score:</strong> How often does your dealership appear in AI responses for target queries?",
            "<strong>Citation Frequency:</strong> When your dealership is mentioned, how prominent is the citation?",
            "<strong>Share of AI Voice:</strong> What percentage of AI answers in your market mention your dealership versus competitors?",
            "<strong>Sentiment in Citations:</strong> When AI mentions you, is the context positive, neutral, or negative?",
        ]),
        _p("Tools are emerging to track these metrics, and manual monitoring (regularly querying AI engines about your market) provides valuable qualitative insight."),

        # Section 5
        _h2("5. What Happens If You Wait?"),
        _p("AI search visibility has winner-take-most dynamics. Once an AI engine identifies trusted sources in a category, it tends to reinforce those choices across related queries. Early movers who establish authority create compounding advantages that late adopters struggle to overcome."),
        _p("The dealerships that begin optimizing for GEO now will build the authority signals and citation history that AI engines reward. Those who wait will find themselves fighting for visibility against competitors who have already established themselves as the trusted sources in their market."),

        # Section 6
        _h2("6. The Bottom Line"),
        _p("Generative Engine Optimization isn't replacing traditional SEO\u2014it's adding a new layer of competition. The most successful dealerships in 2026 and beyond will be those that master both: maintaining strong traditional search presence while building the authority, structure, and multi-platform reputation that earns citations in AI-generated answers."),
        _p("The question isn't whether AI search will impact your dealership's digital marketing\u2014it's whether you'll be one of the dealers getting recommended or one of the dealers getting overlooked."),
    ])

    faqs = [
        ("What is Generative Engine Optimization (GEO)?",
         "GEO is the practice of optimizing your content to appear in AI-generated answers from tools like ChatGPT, Google Gemini, Perplexity, and Claude. As more car buyers use AI to research vehicles, GEO ensures your dealership gets recommended in these conversations."),
        ("How is GEO different from traditional SEO?",
         "Traditional SEO optimizes for search engine rankings and clicks. GEO optimizes for AI recommendations and citations. SEO focuses on keywords; GEO focuses on being the authoritative answer to questions AI tools are asked."),
        ("Why do car dealers need GEO in 2026?",
         "Over 75% of car shoppers are expected to use AI tools during their research by end of 2025. If your dealership isn't optimized for AI search, you're invisible to a growing segment of buyers who ask ChatGPT 'where should I buy a car?'"),
        ("How do I get my dealership recommended by ChatGPT?",
         "Focus on creating authoritative, well-structured content that directly answers buyer questions. Use proper schema markup, build citations from trusted sources, and ensure your business information is consistent across the web."),
        ("Can I do GEO myself or do I need an agency?",
         "Basic GEO practices can be implemented in-house, but comprehensive optimization requires expertise in content strategy, technical markup, and understanding how different AI models source information. An experienced agency can accelerate results significantly."),
    ]

    _guide_page(
        "geo-guide",
        "The Complete Guide to Generative Engine Optimization for Car Dealers",
        "How to get your dealership cited in AI search engines like ChatGPT, Perplexity, and Google AI Overviews.",
        "2026 Automotive Marketing Guide", "15 min read", "February 2026",
        body, faqs,
        "Ready to Get Started with GEO?",
        "Let's discuss how Savvy Dealer can help your dealership get cited in AI search results."
    )


# ===================================================================
# REPUTATION GUIDE
# ===================================================================

def generate_reputation_guide():
    body = "\n".join([
        _h2("Introduction: Why Reputation Is Everything"),
        _p("Your dealership's online reputation is arguably your most valuable marketing asset. In an era where 95% of car buyers use digital channels during their research and nearly 90% read online reviews before visiting a dealership, your reputation directly determines how many customers walk through your doors."),
        _p("Unlike advertising, which stops working the moment you stop paying, a strong reputation compounds over time. Every positive review, every satisfied customer, and every professional interaction builds equity that continues generating leads for years. Conversely, a damaged reputation can take years to repair and cost countless lost opportunities in the meantime."),
        _p("This guide provides a practical framework for building, managing, and protecting your dealership's online reputation across three core areas: review management, social proof, and customer feedback systems."),
        _key_insight("Dealerships with a 4.5+ star rating receive 270% more leads than those with ratings below 4.0. Every tenth of a point in your rating affects your bottom line."),

        # Section 1
        _h2("Section 1: Managing Online Reviews"),
        _p("Online reviews are the foundation of your digital reputation. They influence local search rankings, shape first impressions, and often determine whether a potential customer contacts you or your competitor. Effective review management requires a proactive strategy for generating reviews and a thoughtful approach to responding to them."),

        _h3("Why Reviews Matter More Than Ever"),
        _p("Reviews impact your dealership in three critical ways that compound on each other."),
        _table(["Impact Area", "Why It Matters"], [
            ["Local SEO", "Google prioritizes businesses with recent, positive reviews in local results. Review quantity, quality, and recency all influence your local pack ranking."],
            ["Trust Building", "88% of consumers trust online reviews as much as personal recommendations. For many customers, reviews are their first impression of your dealership."],
            ["AI Discovery", "AI search tools like ChatGPT heavily weight review sentiment when recommending businesses. Strong reviews increase your visibility in AI-generated responses."],
        ]),

        _h3("Building a Review Generation System"),
        _p("The best review strategies don't leave reviews to chance\u2014they systematically create opportunities for satisfied customers to share their experiences."),

        _h4("The Right Time to Ask"),
        _p("Timing dramatically affects whether customers leave reviews and what they say. Ask at moments of peak satisfaction:"),
        _ul([
            "Immediately after vehicle delivery (the excitement is highest)",
            "After a successful service appointment",
            "When a customer expresses gratitude or compliments your team",
            "Following resolution of a concern (turning negatives into positives)",
            "After milestone interactions (first service, warranty work, repeat purchase)",
        ]),

        _h4("Making It Easy"),
        _p("Every friction point between your request and the completed review costs you responses. Remove barriers ruthlessly:"),
        _ul([
            "Send direct links to your Google review page (not your general profile)",
            "Use QR codes on receipts, business cards, and service paperwork",
            "Send SMS requests with one-tap links (higher conversion than email)",
            "Include review links in email signatures",
            "Display review platform options prominently in waiting areas",
        ]),

        _h4("Review Platform Priority"),
        _table(["Platform", "Priority", "Why"], [
            ["Google", "Essential", "Biggest SEO impact, most visibility"],
            ["Facebook", "High", "Social proof, shareability"],
            ["DealerRater", "High", "Industry-specific, buyer-focused"],
            ["Cars.com", "Medium", "Reaches active shoppers"],
            ["Yelp", "Medium", "General visibility, service focus"],
        ]),

        _h3("The Art of Responding to Reviews"),
        _p("How you respond to reviews matters as much as the reviews themselves. Potential customers read your responses to gauge how you treat people."),

        _h4("Responding to Positive Reviews"),
        _ul([
            "Thank the customer by name (personalization matters)",
            "Reference something specific from their review",
            "Mention the team member who helped them (if appropriate)",
            "Invite them back for future needs",
            "Keep it genuine\u2014avoid templated responses",
        ]),

        _h4("Responding to Negative Reviews"),
        _ul([
            "Respond quickly (within 24 hours if possible)",
            "Stay calm and professional\u2014never defensive",
            "Acknowledge their frustration and apologize",
            "Take responsibility where appropriate",
            "Offer to resolve the issue offline",
        ]),

        _callout('<strong>Example Positive Response:</strong> "Thank you so much, Sarah! We\'re thrilled to hear that Marcus made your F-150 purchase such a smooth experience. We know you\'ll love it on those weekend camping trips you mentioned. See you at your first service appointment!"', "green"),
        _callout('<strong>Example Negative Response:</strong> "David, I\'m truly sorry your service experience didn\'t meet our standards. This isn\'t the level of care we strive for. I\'d like to personally make this right. Please call me directly at [number]\u2014I\'m committed to resolving this for you. \u2014 [Name], Service Director"', "blue"),

        _key_insight("53% of customers expect businesses to respond to negative reviews within a week. 45% say they're more likely to visit a business that responds to negative reviews constructively."),

        # Section 2
        _h2("Section 2: Social Proof and Trust Signals"),
        _p("Social proof\u2014evidence that others have had positive experiences with your dealership\u2014is one of the most powerful psychological influences on purchasing decisions. Strategic deployment of social proof across your digital presence can significantly increase conversion rates."),

        _h3("Types of Social Proof That Convert"),
        _table(["Type", "Best Used For"], [
            ["Customer Reviews", "General trust building, SEO benefits, answering common concerns"],
            ["Testimonials", "Highlighting specific experiences, emotional connection, featured placement"],
            ["Case Studies", "Demonstrating problem-solving, complex sales, commercial accounts"],
            ["Trust Badges", "Instant credibility, third-party validation, reducing purchase anxiety"],
            ["Social Media", "Real-time engagement, community building, humanizing your brand"],
            ["Media Mentions", "Authority building, local recognition, differentiation"],
        ]),

        _h3("Customer Testimonials That Work"),
        _p("Effective testimonials are specific, relatable, and address the concerns potential customers have. Generic praise doesn't move the needle."),

        _h4("Elements of Powerful Testimonials"),
        _ul([
            'Specific details about the experience (not just "great service")',
            "The problem or concern they had before coming to you",
            "How your dealership solved their problem",
            'Emotional language that resonates ("peace of mind," "stress-free")',
            "Real names and photos (with permission) for authenticity",
            'Results or outcomes ("saved $3,000," "got approved after other rejections")',
        ]),

        _callout('<strong>Weak:</strong> "Great dealership, would recommend!"<br><br><strong>Strong:</strong> "After being turned down by two other dealers for financing, Mike at ABC Motors found a program that got me approved at a payment I could actually afford. He never made me feel embarrassed about my credit situation. I\'ve already sent my brother here." \u2014 Jennifer M., Tampa'),

        _h4("Video Testimonials"),
        _p("Video testimonials are significantly more impactful than text. They're harder to fake, more emotionally engaging, and perform well across platforms."),
        _ul([
            "Capture them during vehicle delivery (peak excitement)",
            "Keep them short (60-90 seconds maximum)",
            "Coach but don't script (authenticity matters)",
            "Include the vehicle in the shot when possible",
            "Get written permission for marketing use",
        ]),

        _h3("Trust Badges and Certifications"),
        _p("Trust badges provide instant credibility by associating your dealership with recognized authorities. Display them prominently but don't overdo it."),
        _ul([
            "Manufacturer certifications (Certified Pre-Owned, Elite Dealer status)",
            "Better Business Bureau accreditation and rating",
            "Industry awards (Dealer of the Year, Customer Service Excellence)",
            "Google Partner or verified review badges",
            "Community awards and recognitions",
            "Years in business (longevity signals stability)",
        ]),

        _h3("Strategic Placement of Social Proof"),
        _table(["Location", "Best Social Proof Elements"], [
            ["Homepage", "Overall rating, featured testimonials, trust badges, awards"],
            ["Vehicle Pages", "Model-specific reviews, buyer testimonials for that vehicle type"],
            ["Service Pages", "Service testimonials, certifications, warranty information"],
            ["Contact/Form Pages", "Trust badges, recent reviews, response time promises"],
            ["Financing Pages", "Approval success stories, credit-rebuilding testimonials"],
        ]),

        _key_insight("Pages with testimonials convert 34% better than those without. Video testimonials can increase conversion rates by up to 80%."),

        # Section 3
        _h2("Section 3: Customer Feedback Systems"),
        _p("Reviews and testimonials capture moments in time. A systematic feedback program creates ongoing dialogue with customers, enabling continuous improvement and building lasting relationships that drive retention and referrals."),

        _h3("Why Feedback Loops Matter"),
        _ul([
            "Identify problems before they become public complaints",
            "Understand what customers actually value (not what you assume)",
            "Create opportunities to recover unhappy customers",
            "Generate data for process improvements",
            "Show customers their opinions matter (builds loyalty)",
            "Identify your best team members and practices",
        ]),

        _h3("Building an Effective Feedback System"),
        _p("A good feedback system captures input at key touchpoints without overwhelming customers."),

        _h4("Key Feedback Touchpoints"),
        _table(["Touchpoint", "Timing", "Method"], [
            ["Post-Purchase", "24-48 hours after delivery", "Email survey or SMS"],
            ["Post-Service", "Same day or next day", "SMS or quick email"],
            ["30-Day Follow-Up", "30 days post-purchase", "Phone call or detailed survey"],
            ["Annual Check-In", "Purchase anniversary", "Email with service reminder"],
        ]),

        _h4("Survey Best Practices"),
        _ul([
            "Keep it short (3-5 questions for quick surveys, 10 max for detailed)",
            "Include at least one open-ended question for detailed feedback",
            "Use Net Promoter Score (NPS) for tracking over time",
            "Mobile-optimize all surveys (most will be completed on phones)",
            "Personalize with customer name and specific details",
            "Follow up on negative responses immediately",
        ]),

        _h3("Closing the Feedback Loop"),
        _p("Collecting feedback without acting on it is worse than not collecting it at all. Customers notice when their input goes into a void."),

        _h4("The Complete Feedback Cycle"),
        _ol([
            "<strong>Collect</strong> \u2014 Gather feedback through surveys, calls, and interactions",
            "<strong>Analyze</strong> \u2014 Identify patterns, common issues, and opportunities",
            "<strong>Act</strong> \u2014 Implement changes based on what you learn",
            "<strong>Communicate</strong> \u2014 Tell customers how their feedback shaped improvements",
            "<strong>Measure</strong> \u2014 Track whether changes improved customer satisfaction",
        ]),

        _callout('<strong>Communication Example:</strong> "Based on customer feedback, we\'ve extended our service department hours to 7 PM on weekdays. Thank you for helping us serve you better!"', "green"),

        _h3("Turning Feedback into Retention"),
        _h4("Recovery Strategies for Negative Feedback"),
        _ul([
            "Contact unhappy customers within 24 hours (manager level)",
            "Listen fully before responding or defending",
            "Offer meaningful resolution (not just apologies)",
            "Follow up after resolution to confirm satisfaction",
            "Invite them to update their review if appropriate",
        ]),

        _h4("Loyalty Program Integration"),
        _p("Connect feedback participation to your loyalty initiatives:"),
        _ul([
            "Reward customers who complete surveys (service discounts, gift cards)",
            "Create VIP programs for highly engaged customers",
            "Send personalized offers based on feedback preferences",
            "Invite top advocates to exclusive events",
            "Recognize referrals that come from satisfied customers",
        ]),

        _key_insight("Customers whose complaints are resolved quickly and well become more loyal than customers who never had a problem. A recovered customer has a 70% chance of doing business with you again."),

        # Checklist
        _h2("Quick Reference: Reputation Management Checklist"),
        _p("Use this checklist to audit and improve your dealership's reputation management efforts."),

        _h3("Daily Activities"),
        _ul([
            "Monitor new reviews across all platforms",
            "Respond to any new reviews (positive and negative)",
            "Check social media for mentions or comments",
            "Follow up on negative feedback from surveys",
        ]),
        _h3("Weekly Activities"),
        _ul([
            "Review feedback survey responses and identify patterns",
            "Update Google Business Profile with fresh content/photos",
            "Share positive reviews/testimonials on social media",
            "Capture video testimonials from satisfied customers",
        ]),
        _h3("Monthly Activities"),
        _ul([
            "Calculate overall rating trends across platforms",
            "Review and update testimonials on website",
            "Analyze NPS scores and customer satisfaction metrics",
            "Meet with team to discuss feedback insights and improvements",
            "Benchmark against competitor ratings",
        ]),

        # Conclusion
        _h2("Conclusion: Reputation as a Competitive Advantage"),
        _p("Your online reputation isn't just a marketing metric\u2014it's a reflection of how well you serve customers and a predictor of future success. Dealerships with strong reputations enjoy higher conversion rates, better search visibility, increased customer loyalty, and ultimately, greater profitability."),
        _p("Building a strong reputation isn't complicated, but it does require consistency. The dealerships that win are those that make reputation management a daily priority rather than an occasional project. They systematically generate reviews, thoughtfully respond to feedback, and continuously improve based on what customers tell them."),
        _p("Start with the fundamentals: respond to every review, ask satisfied customers to share their experiences, and create systems that surface problems before they become public complaints. As these habits become ingrained, your reputation will steadily improve\u2014and so will your results."),
        _p("Remember: every interaction is an opportunity to build your reputation. Make each one count."),
    ])

    faqs = [
        ("How do I get more Google reviews for my dealership?",
         "Ask satisfied customers at the right moment\u2014after delivery or a positive service experience. Use SMS follow-ups with direct review links, train staff to request reviews naturally, and make the process as simple as one click. Never offer incentives for reviews."),
        ("Should I respond to negative dealership reviews?",
         "Always respond professionally and promptly. Acknowledge the concern, apologize for their experience, and offer to resolve the issue offline. A thoughtful response shows prospective customers you care about making things right."),
        ("What star rating do car dealerships need to be competitive?",
         "Most shoppers expect at least 4.0 stars. Dealerships with 4.5+ stars see significantly higher click-through rates and trust. Focus on consistently earning 4-5 star reviews rather than worrying about occasional lower ratings."),
        ("How quickly should dealerships respond to online reviews?",
         "Respond within 24-48 hours for best results. Fast responses show you're actively engaged. For negative reviews, responding within a few hours can help de-escalate situations and demonstrates commitment to customer satisfaction."),
        ("Can I remove fake or unfair dealership reviews?",
         "You can flag reviews that violate platform guidelines (spam, fake, irrelevant). Google and other platforms may remove them after investigation. However, most negative reviews cannot be removed\u2014your best strategy is earning positive reviews to improve your overall rating."),
    ]

    _guide_page(
        "reputation-guide",
        "The Dealership Reputation Guide",
        "How to build, manage, and protect your dealership's online reputation.",
        "Practical Guide", "15 min read", "December 2025",
        body, faqs,
        "Need Help Building Your Dealership's Reputation?",
        "Our team can help you implement these strategies and build a reputation that drives results."
    )


# ===================================================================
# MAIN
# ===================================================================

def generate_all_resources():
    """Generate all 4 resource guide pages."""
    generate_seo_guide()
    generate_facebook_ads_playbook()
    generate_geo_guide()
    generate_reputation_guide()
    print("  Resources: 4 guide pages generated")
