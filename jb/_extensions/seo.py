"""SEO metadata for the public book site."""

SITE_URL = "https://libropython.es"
SITE_NAME = "Libro Python"
BOOK_TITLE = "Think Python en español"
AUTHOR = "Allen B. Downey"
TRANSLATOR = "midudev"
TWITTER_SITE = "@midudev"
THEME_COLOR = "#2d3748"
LOCALE = "es_ES"

DEFAULT_DESCRIPTION = (
    "Think Python en español: introducción gratuita a Python de Allen B. Downey. "
    "3.ª edición traducida con capítulos online, notebooks en Colab y PDF descargable."
)

PAGE_DESCRIPTIONS = {
    "index": DEFAULT_DESCRIPTION,
}


def _page_url(app, pagename: str) -> str:
    base = SITE_URL.rstrip("/")
    if pagename in {app.config.root_doc, "index"}:
        return f"{base}/"
    return f"{base}/{pagename}.html"


def _page_title(app, pagename: str, title: str) -> str:
    if pagename in {app.config.root_doc, "index"}:
        return BOOK_TITLE
    return f"{title} — {BOOK_TITLE}"


def update_seo_context(app, pagename, templatename, context, doctree):
    description = PAGE_DESCRIPTIONS.get(pagename, DEFAULT_DESCRIPTION)
    is_home = pagename in {app.config.root_doc, "index"}
    page_title = _page_title(app, pagename, context.get("title", BOOK_TITLE))
    page_url = _page_url(app, pagename)
    image_url = f"{SITE_URL.rstrip('/')}/og-image.jpg"

    if is_home:
        context["title"] = BOOK_TITLE
        context["titlesuffix"] = ""
        context["pageurl"] = page_url

    context["seo"] = {
        "site_url": SITE_URL,
        "site_name": SITE_NAME,
        "book_title": BOOK_TITLE,
        "description": description,
        "page_title": page_title,
        "page_url": page_url,
        "image_url": image_url,
        "author": AUTHOR,
        "translator": TRANSLATOR,
        "twitter_site": TWITTER_SITE,
        "theme_color": THEME_COLOR,
        "locale": LOCALE,
        "is_home": is_home,
    }


def setup(app):
    app.connect("html-page-context", update_seo_context, priority=800)
    return {"parallel_read_safe": True, "parallel_write_safe": True}
