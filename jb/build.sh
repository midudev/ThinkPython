#!/usr/bin/env bash
set -euo pipefail

# Build the Jupyter book version
cd "$(dirname "$0")"

# Link the translated notebooks into the Jupyter Book source directory.
for notebook in ../chapters/chap[01][0-9]*.ipynb; do
    target="$(basename "$notebook")"
    if [ -e "$target" ] && [ ! -L "$target" ]; then
        echo "Refusing to replace existing non-symlink: $target" >&2
        exit 1
    fi
    ln -sfn "$notebook" "$target"
done

if command -v jupyter-book >/dev/null 2>&1; then
    jupyter_book_cmd="jupyter-book"
else
    user_base="$(python3 -m site --user-base)"
    jupyter_book_cmd="$user_base/bin/jupyter-book"
fi

if [ ! -x "$(command -v "$jupyter_book_cmd" 2>/dev/null || printf '%s' "$jupyter_book_cmd")" ]; then
    echo "jupyter-book was not found. Install it with: python3 -m pip install --user 'jupyter-book<2'" >&2
    exit 1
fi

if ! python3 -c "import playwright" >/dev/null 2>&1; then
    echo "playwright was not found. Install PDF build dependencies with:" >&2
    echo "  python3 -m pip install --user playwright" >&2
    echo "  python3 -m playwright install chromium" >&2
    exit 1
fi

pdf_filename="think-python-es.pdf"
pdf_build_dir="_build/pdfhtml"
pdf_source="$pdf_build_dir/_build/pdf/book.pdf"
html_pdf="_build/html/$pdf_filename"
dist_dir="../dist"

"$jupyter_book_cmd" build .
"$jupyter_book_cmd" build . --builder pdfhtml --path-output "$pdf_build_dir"

if [ ! -f "$pdf_source" ]; then
    echo "Expected full-book PDF was not generated: $pdf_source" >&2
    exit 1
fi

cp "$pdf_source" "$html_pdf"
echo "Full-book PDF copied to $html_pdf"

rm -rf "$dist_dir"
mkdir -p "$dist_dir"
cp -R _build/html/. "$dist_dir/"
echo "Static site copied to $dist_dir"
