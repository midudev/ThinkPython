"""Site links for the public book build."""

PDF_FILENAME = "think-python-es.pdf"
PDF_TOOLTIP = "Descargar el libro completo en PDF"
SITE_HOME_URL = "https://libropython.es"


def update_site_links(app, pagename, templatename, context, doctree):
    """Point site-level home/download links to their public targets."""
    context["theme_logo_link"] = SITE_HOME_URL
    context["theme_site_home_url"] = SITE_HOME_URL

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
    app.connect("html-page-context", update_site_links, priority=700)
    return {"parallel_read_safe": True, "parallel_write_safe": True}
