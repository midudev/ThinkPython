"""Header download button for the generated full-book PDF."""

PDF_FILENAME = "think-python-es.pdf"
PDF_TOOLTIP = "Descargar el libro completo en PDF"


def use_full_book_pdf_download(app, pagename, templatename, context, doctree):
    """Replace the page-download dropdown with the full-book PDF link."""
    header_buttons = context.get("header_buttons")
    if not isinstance(header_buttons, list):
        return

    pdf_button = {
        "type": "link",
        "url": context["pathto"](PDF_FILENAME, 1),
        "tooltip": PDF_TOOLTIP,
        "icon": "fas fa-file-pdf",
        "label": "download-book-pdf-button",
    }

    context["header_buttons"] = [
        pdf_button,
        *(
            button
            for button in header_buttons
            if button.get("label") != "download-buttons"
        ),
    ]


def setup(app):
    app.connect("html-page-context", use_full_book_pdf_download, priority=700)
    return {"parallel_read_safe": True, "parallel_write_safe": True}
