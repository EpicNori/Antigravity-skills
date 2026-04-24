---
name: pdf-ai
description: Use when PDFs, scanned documents, or document images must be converted into AI-ready Markdown, JSON, chunks, citations, or searchable text. Covers OCR, layout-aware extraction, table and formula preservation, classification of text-based vs scanned PDFs, and RAG ingestion.
---

# PDF AI Skill

## Start Here

- Decide whether the source is text-based, scanned, or mixed.
- If the source is a URL and remote extraction is available, prefer that first.
- If the document has a usable text layer, preserve structure with coordinate-aware extraction.
- If layout or OCR quality matters, render pages and inspect them before trusting plain text.

## Tool Choice

- `pdf-inspector`: classify PDFs and route text-based vs scanned files.
- `pdfplumber` or `pypdf`: text, tables, page metadata, and coordinates.
- `pypdfium2`: fast page rendering and page-image generation.
- `Marker`, `MinerU`, `PaddleOCR`: scanned, mixed, or complex-layout PDFs that need Markdown or JSON.
- `reportlab`: generate clean PDFs after extracting or normalizing content.

## Workflow

1. Classify the PDF.
2. Extract using the smallest tool that preserves the needed structure.
3. For scanned pages, render to images and OCR or VLM-extract from those images.
4. Preserve headings, tables, equations, footnotes, page numbers, and figure captions.
5. For RAG, chunk by section, keep page anchors, and store source metadata with each chunk.
6. Re-render the output and spot-check alignment, reading order, and table structure.

## Output Rules

- Prefer Markdown for narrative documents.
- Prefer JSON or schema-shaped output when downstream automation needs fields or citations.
- Keep image alt text and figure captions intact.
- Strip repeated headers and footers only after confirming they are boilerplate, not content.

## When to Escalate

- If text extraction looks clean but reading order is wrong, switch to page rendering and layout-aware extraction.
- If OCR misses formulas, tables, or multi-column text, use a document-intelligence extractor rather than plain OCR.
- If the document is a fillable form, use the main `pdf` skill's form workflow instead of converting it to text.

See [references/tool-selection.md](references/tool-selection.md) for the decision tree.
