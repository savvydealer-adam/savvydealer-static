"""Generate blog listing and individual blog post pages."""
import re
from pathlib import Path
from generate import (
    head, nav, footer, breadcrumb, cta_section, write_page,
    DOMAIN, CONTENT_DIR
)


def parse_frontmatter(text):
    """Parse YAML-ish frontmatter from markdown file."""
    if not text.startswith("---"):
        return {}, text
    end = text.find("---", 3)
    if end == -1:
        return {}, text
    fm_text = text[3:end].strip()
    body = text[end + 3:].strip()
    meta = {}
    for line in fm_text.split("\n"):
        if ":" not in line:
            continue
        key, _, val = line.partition(":")
        key = key.strip()
        val = val.strip().strip('"').strip("'")
        if val.startswith("[") and val.endswith("]"):
            val = [t.strip().strip('"').strip("'") for t in val[1:-1].split(",")]
        if val == "true":
            val = True
        elif val == "false":
            val = False
        meta[key] = val
    return meta, body


def md_to_html(md_text):
    """Simple markdown to HTML conversion."""
    lines = md_text.split("\n")
    html_lines = []
    in_list = False
    in_code = False
    in_blockquote = False

    for line in lines:
        stripped = line.strip()

        # Code blocks
        if stripped.startswith("```"):
            if in_code:
                html_lines.append("</code></pre>")
                in_code = False
            else:
                lang = stripped[3:].strip()
                html_lines.append(f'<pre class="bg-gray-100 rounded-lg p-4 overflow-x-auto"><code>')
                in_code = True
            continue
        if in_code:
            html_lines.append(line.replace("<", "&lt;").replace(">", "&gt;"))
            continue

        # Empty line
        if not stripped:
            if in_list:
                html_lines.append("</ul>")
                in_list = False
            if in_blockquote:
                html_lines.append("</blockquote>")
                in_blockquote = False
            continue

        # Headers
        if stripped.startswith("######"):
            html_lines.append(f'<h6 class="text-base font-semibold mt-6 mb-2">{stripped[6:].strip()}</h6>')
            continue
        if stripped.startswith("#####"):
            html_lines.append(f'<h5 class="text-base font-semibold mt-6 mb-2">{stripped[5:].strip()}</h5>')
            continue
        if stripped.startswith("####"):
            html_lines.append(f'<h4 class="text-lg font-semibold mt-6 mb-2">{stripped[4:].strip()}</h4>')
            continue
        if stripped.startswith("###"):
            html_lines.append(f'<h3 class="text-xl font-semibold mt-8 mb-3">{stripped[3:].strip()}</h3>')
            continue
        if stripped.startswith("##"):
            html_lines.append(f'<h2 class="text-2xl font-bold mt-10 mb-4">{stripped[2:].strip()}</h2>')
            continue
        if stripped.startswith("#"):
            html_lines.append(f'<h1 class="text-3xl font-bold mt-10 mb-4">{stripped[1:].strip()}</h1>')
            continue

        # Blockquote
        if stripped.startswith(">"):
            if not in_blockquote:
                html_lines.append('<blockquote class="border-l-4 border-blue-600 pl-4 italic text-gray-600 my-4">')
                in_blockquote = True
            html_lines.append(f"<p>{inline_md(stripped[1:].strip())}</p>")
            continue
        if in_blockquote:
            html_lines.append("</blockquote>")
            in_blockquote = False

        # Unordered list
        if stripped.startswith("- ") or stripped.startswith("* "):
            if not in_list:
                html_lines.append('<ul class="list-disc pl-6 space-y-1 my-4">')
                in_list = True
            html_lines.append(f"<li>{inline_md(stripped[2:])}</li>")
            continue
        if in_list:
            html_lines.append("</ul>")
            in_list = False

        # Horizontal rule
        if stripped in ("---", "***", "___"):
            html_lines.append('<hr class="my-8 border-gray-200">')
            continue

        # Paragraph
        html_lines.append(f'<p class="text-gray-700 leading-relaxed my-4">{inline_md(stripped)}</p>')

    if in_list:
        html_lines.append("</ul>")
    if in_code:
        html_lines.append("</code></pre>")
    if in_blockquote:
        html_lines.append("</blockquote>")

    return "\n".join(html_lines)


def inline_md(text):
    """Convert inline markdown (bold, italic, links, code)."""
    # Images
    text = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', r'<img src="\2" alt="\1" class="rounded-lg my-4 max-w-full" loading="lazy">', text)
    # Links
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2" class="text-blue-600 hover:underline">\1</a>', text)
    # Bold
    text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', text)
    # Italic
    text = re.sub(r'\*([^*]+)\*', r'<em>\1</em>', text)
    # Inline code
    text = re.sub(r'`([^`]+)`', r'<code class="bg-gray-100 px-1 rounded text-sm">\1</code>', text)
    return text


def generate_blog():
    """Generate blog listing and individual post pages."""
    print("Generating blog...")

    # Read all blog posts
    posts = []
    for md_file in sorted(CONTENT_DIR.glob("*.md")):
        text = md_file.read_text(encoding="utf-8")
        meta, body = parse_frontmatter(text)
        if not meta.get("title"):
            continue
        # Normalize fields
        slug = meta.get("slug", md_file.stem)
        published = meta.get("publishedAt", meta.get("date", ""))
        if isinstance(published, str) and "T" in published:
            published = published.split("T")[0]
        reading_time = meta.get("readingTime", meta.get("readTime", "5"))
        if isinstance(reading_time, str):
            reading_time = reading_time.replace(" min read", "").strip()
        image = meta.get("featuredImage", meta.get("image", ""))
        # Fix image path for static site
        if image.startswith("/attached_assets/"):
            image = "/images/" + image.split("/")[-1]

        posts.append({
            "title": meta["title"],
            "slug": slug,
            "excerpt": meta.get("excerpt", ""),
            "category": meta.get("category", ""),
            "author": meta.get("author", "Savvy Dealer Team"),
            "author_role": meta.get("authorRole", ""),
            "image": image,
            "published": published,
            "reading_time": reading_time,
            "tags": meta.get("tags", []),
            "body_html": md_to_html(body),
        })

    # Sort by date descending
    posts.sort(key=lambda p: p["published"], reverse=True)

    # Generate listing page
    cards_html = ""
    for p in posts:
        tags_html = ""
        if isinstance(p["tags"], list):
            for t in p["tags"][:3]:
                tags_html += f'<span class="bg-gray-100 text-gray-600 text-xs px-2 py-0.5 rounded-full">{t}</span>'
        img_html = f'<img src="{p["image"]}" alt="{p["title"]}" class="w-full h-48 object-cover rounded-t-xl" loading="lazy">' if p["image"] else '<div class="w-full h-48 bg-gray-200 rounded-t-xl"></div>'
        cards_html += f'''      <a href="/blog/{p["slug"]}" class="bg-white rounded-xl shadow-sm border border-gray-100 hover:shadow-md transition block">
        {img_html}
        <div class="p-5">
          <div class="flex items-center gap-2 mb-2 flex-wrap">
            <span class="bg-blue-100 text-blue-700 text-xs px-2 py-0.5 rounded-full">{p["category"]}</span>
            <span class="text-xs text-gray-500">{p["published"]}</span>
            <span class="text-xs text-gray-500">{p["reading_time"]} min read</span>
          </div>
          <h3 class="text-lg font-semibold text-gray-900 mb-2 line-clamp-2">{p["title"]}</h3>
          <p class="text-gray-600 text-sm line-clamp-3">{p["excerpt"]}</p>
          <div class="flex gap-2 mt-3">{tags_html}</div>
        </div>
      </a>\n'''

    listing = f'''{head("The Savvy Blog - Automotive Digital Marketing Insights", "Expert insights on automotive digital marketing, dealer websites, SEO, PPC, and industry trends.", "blog")}
{nav()}
  <main class="flex-1">
{breadcrumb([("Home", "/"), ("Blog", None)])}
    <section class="hero-bg text-white py-16 px-4 text-center">
      <div class="max-w-4xl mx-auto">
        <h1 class="text-4xl md:text-5xl font-extrabold mb-4">The Savvy Blog</h1>
        <p class="text-lg text-blue-200">Expert insights on automotive digital marketing, dealer websites, SEO, PPC, and industry trends.</p>
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
    write_page("blog/index.html", listing)

    # Generate individual posts
    for p in posts:
        schema = '{' + f'"@context":"https://schema.org","@type":"BlogPosting","headline":"{p["title"]}","author":{{"@type":"Person","name":"{p["author"]}"}},"datePublished":"{p["published"]}","publisher":{{"@type":"Organization","name":"Savvy Dealer","url":"{DOMAIN}"}}' + '}'

        post_html = f'''{head(f'{p["title"]} | Savvy Dealer Blog', p["excerpt"], f'blog/{p["slug"]}', og_type="article")}
{nav()}
  <main class="flex-1">
{breadcrumb([("Home", "/"), ("Blog", "/blog"), (p["title"][:50] + "..." if len(p["title"]) > 50 else p["title"], None)])}
    <article class="py-12 px-4">
      <div class="max-w-3xl mx-auto">
        <div class="mb-8">
          <div class="flex items-center gap-3 mb-4 flex-wrap">
            <span class="bg-blue-100 text-blue-700 text-xs px-2 py-0.5 rounded-full">{p["category"]}</span>
            <span class="text-sm text-gray-500">{p["published"]}</span>
            <span class="text-sm text-gray-500">{p["reading_time"]} min read</span>
          </div>
          <h1 class="text-3xl md:text-4xl font-extrabold text-gray-900 mb-4">{p["title"]}</h1>
          <p class="text-lg text-gray-600 mb-4">{p["excerpt"]}</p>
          <p class="text-sm text-gray-500">By {p["author"]}</p>
        </div>
        {f'<img src="{p["image"]}" alt="{p["title"]}" class="w-full rounded-xl mb-8" loading="lazy">' if p["image"] else ""}
        <div class="prose prose-lg max-w-none">
          {p["body_html"]}
        </div>
      </div>
    </article>
    <script type="application/ld+json">{schema}</script>
{cta_section("Ready to Dominate Your Market?", "See how Savvy Dealer can help your dealership drive measurable results.")}
  </main>
{footer()}'''
        write_page(f'blog/{p["slug"]}.html', post_html)

    print(f"  Blog: {len(posts)} posts generated")
