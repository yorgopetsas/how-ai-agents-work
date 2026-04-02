from __future__ import annotations

# Pelican "publish" configuration (used by GitHub Pages/VM deployment).

import os

PLUGIN_PATHS: list[str] = []

# If you use this config on a different machine, you can override SITEURL via env.
SITEURL = os.environ.get("SITEURL", "https://howaiagentswork.com")

# For deployment, prefer absolute URLs.
RELATIVE_URLS = False

OUTPUT_PATH = "output"

# Keep the same theme and URL patterns from pelicanconf.py.

