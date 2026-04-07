from __future__ import annotations

# Basic Pelican configuration for a lightweight, SEO-friendly static site.
#
# Note: bilingual URLs follow the requirement "English lives in /en/ and Spanish in /es/".

AUTHOR = "EdelConnect"
SITENAME = "How AI Agents Work"
SITEURL = ""

PATH = "content"
TIMEZONE = "Europe/Madrid"

DEFAULT_LANG = "en"

# GA4 Measurement ID
GA4_MEASUREMENT_ID = "G-ZPPPDS52YR"

THEME = "simple"

# Override only templates using our Tailwind-based design.
EXTRA_TEMPLATES_PATHS = ["themes/aiagents_theme/templates"]

# URL patterns include language prefix.
ARTICLE_URL = "{lang}/{slug}/"

# Pages (home pages for EN/ES) should land at /en/ and /es/.
PAGE_URL = "{lang}/"

# Ensure language-prefixed output paths are created.
ARTICLE_SAVE_AS = "{lang}/{slug}/index.html"
PAGE_SAVE_AS = "{lang}/index.html"

# Copy Spanish placeholder from ./es to the output (so it appears at /es/).
STATIC_PATHS = ["es"]

# Restrict Pelican content discovery (so static HTML isn't treated as a page/article).
ARTICLE_PATHS = ["posts"]
PAGE_PATHS = ["pages"]

# Keep URLs relative for local builds.
RELATIVE_URLS = True

# Markdown is built-in; keep defaults.

# Simple defaults for content metadata.
DEFAULT_METADATA = {
    "lang": DEFAULT_LANG,
}

