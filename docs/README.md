# Domain 1 Docs

This folder is published via GitHub Pages. Structure mirrors domain_2:

- index.html — cards grid, built from markdown files in assets/md
- initial-theory.html, practice.html, reflective-questions.html, new-theory.html — templates that load markdown by filename
- assets/css — shared styles
- assets/md — content in simple markdown
- assets/images — images used on cards and pages

How to add a new card/content:
1. Add assets/md/<your_file>.md with first line as title and second line as short description.
2. Update the `cards` array in `docs/index.html` to include `{ file: '<your_file>', images: ['1.jpg','1.jpg','1.jpg'], page: '<target>.html[?content=<your_file>]' }`.
3. Optionally link to the content via `?content=<your_file>` on any page template.
