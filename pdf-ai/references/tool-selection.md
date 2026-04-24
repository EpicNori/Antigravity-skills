# PDF AI Tool Selection

## 1. Classify the source

- Text-based PDF: use `pdf-inspector`, `pdfplumber`, or `pypdf`.
- Scanned or image-heavy PDF: use `Marker`, `MinerU`, or `PaddleOCR`.
- Mixed PDF: route per page; use text extraction where possible and OCR on scanned pages.
- Remote URL: prefer remote extraction if available before local processing.

## 2. Pick the primary path

- Quick plain text: `pypdf` or `pdfplumber`.
- Layout-aware extraction and coordinates: `pdfplumber`.
- Fast page rendering for inspection: `pypdfium2`.
- Markdown or JSON conversion: `Marker` or `MinerU`.
- Structured LLM-ready OCR in many languages: `PaddleOCR`.
- Page-type routing before extraction: `pdf-inspector`.

## 3. RAG and knowledge-base output

- Split on headings, subheadings, and page boundaries.
- Keep section titles, page numbers, and source file names in metadata.
- Store tables as tables, not flattened paragraphs.
- Keep a raw text fallback for every chunk.
- Preserve page images or figure references if the downstream system needs them.

## 4. Verification

- Render final pages to PNGs and inspect at least one sample page from each major layout type.
- Compare page count and heading sequence against the source.
- Spot-check a few tables, equations, and captions.
