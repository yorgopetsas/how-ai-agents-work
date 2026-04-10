# Content workflow (no database)

This site is fully file-based. Add one Markdown file per post.

## Folder layout

- `content/posts/en/` -> all English News, Blog, and Tutorial posts
- `content/pages/en/news.md` -> News section page
- `content/pages/en/blog.md` -> Blog section page
- `content/pages/en/tutorials.md` -> Tutorials section page

## Required frontmatter for every new post

```yaml
---
lang: en
title: Your post title
slug: your-post-slug
date: 2026-04-10
section: news   # news | blog | tutorial
category: Self-hosted   # For blog: Self-hosted | Cloud | Hybrid
tags: [Open-Source, API, Cloude, OpenAI, ChatGPT]
summary: One-line summary
status: published
---
```

## Tutorial-specific metadata

Use one difficulty lane:

- `difficulty: beginner`
- `difficulty: it-ops`
- `difficulty: dev-no-ai`

This keeps audiences separated in the Tutorials section.

