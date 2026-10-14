# Library catalog style

Applies to `catalog/index.html`, the local documentation preview.

- Layout: single reading column, maximum width 1120px; compact filter row and a semantic table. On narrow screens, allow the table to scroll horizontally.
- Background: `#f6f7f9`; surface: `#ffffff`; text: `#18212f`; secondary text: `#4c596a`; borders: `#d5dce5`.
- Accent and links: `#174c91`; focus outline: `#174c91`, 3px, offset 3px.
- Typography: system UI sans serif; normal body 16px, line height 1.5; heading 32px, weight 700; table text 14px. Code uses the system monospace font.
- Spacing: 8px base; page padding 24px; filters 12px gaps; table cells 12px.
- Corners: 6px for controls and the table container; borders 1px; no shadows, animation, gradients, icons, images, or external fonts.
- Interaction: search name, description and category; category filter; imported/legacy filter; visible result count and load errors. Build DOM nodes with `textContent`; skill descriptions must never render as HTML.
- Assets: none. All data and navigation stay local. No analytics or external requests.
