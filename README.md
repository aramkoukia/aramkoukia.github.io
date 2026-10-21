# aramkoukia.github.io

Personal blog built with Jekyll and hosted on GitHub Pages.

## Write a new post
Create `_posts/YYYY-MM-DD-my-title.md`:

    ---
    layout: post
    title: "My title"
    date: 2026-10-19
    ---
    Content in Markdown.

## Preview locally (optional)
    bundle install
    bundle exec jekyll serve

## Edit the profile
The home page is the post list. Name, pronunciation, and headline for the About page live in
`_data/profile.yml`; the About bio is in `about.md`. Work history is on LinkedIn only. To use a photo instead of the
monogram, add it under `assets/img/` and set `avatar:` in `_config.yml`.
