# CollateMD

CollateMD is a Python script that recursively searches a directory for files of specified extensions, skips designated folders, and compiles all matching files into a single Markdown document. Each file's content is wrapped in a language-specific code fence for syntax highlighting.

## Features

- **Recursive Search**: Walks through the specified path and its subdirectories.
- **Selective Extensions**: Includes only files with certain extensions (e.g., `.py`, `.html`).
- **Skippable Folders**: Bypass folders like `node_modules`, `.git`, or any you specify.
- **Unified Output**: Gathers all content into one Markdown file, with each file’s relative path as a heading.
- **Syntax Highlighting**: Automatically detects common extensions (`py`, `html`, `js`, `css`, `sql`, `ejs`) and applies the corresponding language in code fences.

## Getting Started

### Prerequisites

- **Python 3** or later (no extra libraries required—only the standard library).




