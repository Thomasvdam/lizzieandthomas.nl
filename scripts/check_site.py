"""Check local references and basic structure on this static site."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parents[1]


class SiteParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.errors = []
        self.has_title = False
        self.has_viewport = False
        self.has_main = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "title":
            self.has_title = True
        if tag == "main":
            self.has_main = True
        if tag == "meta" and attrs.get("name") == "viewport":
            self.has_viewport = True
        if "id" in attrs:
            if attrs["id"] in self.ids:
                self.errors.append(f"duplicate id: {attrs['id']}")
            self.ids.add(attrs["id"])
        if tag == "img" and not attrs.get("alt"):
            self.errors.append("image is missing alt text")
        for key in ("src", "href"):
            value = attrs.get(key, "")
            if not value or value.startswith(("#", "data:", "mailto:", "tel:")):
                continue
            parsed = urlsplit(value)
            if parsed.scheme or parsed.netloc:
                continue
            path = (ROOT / parsed.path.lstrip("/")).resolve()
            if not path.is_relative_to(ROOT) or not path.is_file():
                self.errors.append(f"missing local asset: {value}")


parser = SiteParser()
parser.feed((ROOT / "index.html").read_text(encoding="utf-8"))
for present, name in (
    (parser.has_title, "title"),
    (parser.has_viewport, "viewport meta tag"),
    (parser.has_main, "main element"),
):
    if not present:
        parser.errors.append(f"missing {name}")

if parser.errors:
    raise SystemExit("\n".join(parser.errors))
print("Static site checks passed")
