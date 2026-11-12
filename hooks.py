"""Build hooks for conventionalbranch.org.

The site is MkDocs NG with the Sumi theme. These hooks do what is particular to it:

* Publish static/ at the site root: spec.json and its frozen copies, the JSON Schema,
  llms.txt, the badge, robots.txt and CNAME. Those files are served byte for byte,
  and tests/conformance.py reads them where they are.
* Lay out each page: a specification page is a hero, then the specification beside
  its outline, then (on the English homepage) the checker and the sections under it.
  Enforce and About are a hero, the page, and their own sections. The layout is Sumi's
  landing page, filled in from data here so that no content file has to repeat it.
* Render the registries in data/ where a page asks for them, with `{{< agents >}}`
  and `{{< tooling compact >}}` (the Hugo shortcodes the pages already used).
* Keep what the Hugo site published: the FAQ as FAQPage structured data, a sitemap
  index with one sitemap per language, and the /en/ and /v<current>/ forwards.
"""

from __future__ import annotations

import html
import json
import os
import re
import shutil
from pathlib import Path
from typing import Any

import yaml
from mkdocs import languages
from mkdocs.structure.files import File, Files

ROOT = Path(__file__).resolve().parent
STATIC = ROOT / "static"
DATA = ROOT / "data"
STRINGS = ROOT / "i18n" / "en.yaml"
REPO = "https://github.com/conventional-branch/conventional-branch"
# Files in static/ that document the folder and are not published.
NOT_PUBLISHED = {"README.md", ".gitkeep"}


def _yaml(path: Path) -> Any:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def _lang(config) -> str:
    lang = languages.current(config)
    return lang.code if lang else "en"


def _is_default(config) -> bool:
    lang = languages.current(config)
    return lang is None or lang.default


def _pick(by_lang: dict[str, str], lang: str) -> str:
    return by_lang.get(lang) or by_lang.get("en", "")


# -- configuration -------------------------------------------------------------------


def on_config(config):
    spec = json.loads((STATIC / "spec.json").read_text(encoding="utf-8"))
    strings = _yaml(STRINGS)
    agents = _yaml(DATA / "agents.yaml")
    home_data = _yaml(DATA / "home.yaml")
    versions = config.theme.get("versions") or []
    current = versions[0]["title"] if versions else spec["version"]
    if current != spec["version"]:
        raise SystemExit(
            f"mkdocs.yml: theme.versions starts with {current}, static/spec.json is "
            f"{spec['version']}. The first entry is the current version."
        )

    # Each type, with what a person and a pipeline make of it (for the checker).
    types = []
    for t in spec["types"]:
        if t.get("category") == "ai-source":
            name = strings["checker_person_generic_agent"]
            for a in agents["agents"]:
                if a["prefix"] == t["type"] and not a.get("generic"):
                    name = a["name"]
            person = strings["checker_person_agent"].replace("{Name}", name)
            pipeline = strings["pipeline_agent"]
        else:
            person = strings[f"checker_person_{t['type']}"]
            pipeline = strings[f"pipeline_{t['type']}"]
        types.append({
            "type": t["type"], "aliases": t.get("aliases") or [], "category": t["category"],
            "person": person, "pipeline": pipeline,
        })

    # "Specification" in the navigation is the specification section of this
    # language's homepage, which a nav entry can only name by its address.
    lang = languages.current(config)
    home = "/" if lang is None or lang.default else f"/{lang.path}/"
    for item in config.nav or []:
        if isinstance(item, dict):
            for key, value in item.items():
                if value == "#spec":
                    item[key] = f"{home}#spec"

    config.extra["cb"] = {
        "spec": spec,
        "s": strings,
        "home": home_data,
        "history": _yaml(DATA / "history.yaml"),
        "types": types,
        "type_names": [n for t in types for n in [t["type"], *t["aliases"]]],
        "languages": len(config.get("languages") or []) or 1,
        "repo": REPO,
    }
    return config


# -- files -----------------------------------------------------------------------------


def on_files(files: Files, config):
    if not _is_default(config):
        return files
    for path in sorted(STATIC.rglob("*")):
        if path.is_file() and path.name not in NOT_PUBLISHED:
            rel = path.relative_to(STATIC).as_posix()
            files.append(File(rel, str(STATIC), config.site_dir, False))
    return files


# -- page layout ---------------------------------------------------------------------

_SHORTCODE = re.compile(r"^\{\{<\s*(agents|tooling)(?:\s+(\w+))?\s*>\}\}\s*$", re.M)


def _agents_table(config, lang: str) -> str:
    data = _yaml(DATA / "agents.yaml")
    labels = data["labels"]
    head = [_pick(labels[k], lang) for k in ("prefix", "agent", "vendor", "since")]
    rows = [f"| {' | '.join(head)} |", "| --- | --- | --- | --- |"]
    for a in data["agents"]:
        name = _pick(labels["generic"], lang) if a.get("generic") else a["name"]
        if a.get("homepage"):
            name = f"[{name}]({a['homepage']})"
        rows.append(f"| `{a['prefix']}/` | {name} | {a['vendor']} | v{a['since']} |")
    return "\n".join(rows)


def _tooling(config, lang: str, mode: str) -> str:
    data = _yaml(DATA / "tooling.yaml")
    intro = data["intro"].get(mode) or data["intro"]["full"]
    out = [_pick(intro, lang), ""]
    for item in data["items"]:
        text = item["summary"] if mode == "compact" else item["description"]
        out.append(f"- [{item['name']}]({item['url']}): {_pick(text, lang)}")
    install = data.get("install")
    if install:
        out += ["", _pick(install["label"], lang), "", "```bash {data-snippet=\"agent_skill\"}", install["command"], "```"]
    return "\n".join(out)


def _spec_version(page) -> str | None:
    """The version a specification page is: "current", "v1.0.0", or None if it isn't one."""
    if page.file.src_uri.split(".")[0] == "index":
        return "current"
    m = re.match(r"(v\d+\.\d+\.\d+)/index\.", page.file.src_uri)
    return m.group(1) if m else None


_LIST_ITEM = re.compile(r"^(?:[-*+]|\d+\.)\s")
_FENCE = re.compile(r"^\s*(```|~~~)")


def _lists_after_paragraphs(markdown: str) -> str:
    """Start a list that follows a paragraph line on a new block.

    The pages were written for Hugo's Markdown, where a list may follow a paragraph
    directly; Python-Markdown needs a blank line between them, and would otherwise
    run the list into the paragraph.
    """
    out: list[str] = []
    fence = None
    for line in markdown.split("\n"):
        m = _FENCE.match(line)
        if m:
            fence = None if fence == m.group(1) else (fence or m.group(1))
        elif fence is None and out and _LIST_ITEM.match(line):
            prev = out[-1]
            if prev.strip() and not prev[0].isspace() and not _LIST_ITEM.match(prev) \
                    and not prev.startswith(("#", "|", ">", "<")):
                out.append("")
        out.append(line)
    return "\n".join(out)


def on_page_markdown(markdown: str, page, config, files):
    lang = _lang(config)
    markdown = _SHORTCODE.sub(
        lambda m: "\n" + (_agents_table(config, lang) if m.group(1) == "agents"
                          else _tooling(config, lang, m.group(2) or "full")) + "\n",
        markdown,
    )
    markdown = _lists_after_paragraphs(markdown)

    meta = page.meta
    if meta.get("seoDescription"):
        meta.setdefault("description", meta["seoDescription"])
    version = _spec_version(page)
    if version:
        meta.setdefault("template", "landing.html")
        hero = {"title": config.site_name, "text": config.site_description, "image": "/img/logo.svg"}
        if version == "current":
            hero["actions"] = [
                {**a, "primary": i == 0} for i, a in enumerate(config.extra.get("actions") or [])
            ]
        meta.setdefault("hero", hero)
        sections = [{"type": "content", "toc": True, "id": "spec", "aside": "partials/spec-tools.html"}]
        if version == "current" and config.extra.get("landing"):
            sections += [
                {"type": "include", "template": "partials/checker.html", "class": "cb-checker-section"},
                {"type": "include", "template": "partials/adopters.html", "class": "cb-adopters-section"},
                {"type": "include", "template": "partials/why.html"},
                {"type": "include", "template": "partials/adopt.html", "tone": "soft"},
            ]
        meta.setdefault("sections", sections)
        meta["cb_spec"] = True
        meta["cb_version"] = version
    elif meta.get("heroTitle"):
        slug = page.file.src_uri.split("/")[0]
        meta.setdefault("template", "landing.html")
        meta.setdefault("hero", {"title": meta["heroTitle"], "text": meta.get("heroLead", "")})
        sections = [{"type": "content", "toc": True}]
        if slug == "enforce":
            sections.insert(0, {"type": "include", "template": "partials/enforce-layers.html", "tone": "soft"})
        if slug == "about":
            sections += [
                {"type": "include", "template": "partials/about-history.html"},
                {"type": "include", "template": "partials/about-people.html", "class": "cb-people-section"},
            ]
        meta.setdefault("sections", sections)
    return markdown


def on_page_content(html_text: str, page, config, files):
    if not page.meta.get("cb_spec"):
        return html_text
    # The page has one h1, the hero's, so the specification's own title is demoted to
    # head its section. Its id is kept, so links to it still land.
    html_text = re.sub(r"<h1([^>]*)>(.*?)</h1>", r'<h2 class="cb-spec-title"\1>\2</h2>', html_text, count=1, flags=re.S)
    if page.meta.get("cb_version") == "current":
        page.meta["cb_faq"] = _faq(html_text)
    # The examples table marks each name ✅ or ❌; the script draws those as icons and
    # highlights what breaks a rule, knowing the types from here.
    types = " ".join(config.extra["cb"]["type_names"])
    return f'<div class="cb-spec" data-spec-types="{types}">\n{html_text}\n</div>'


def on_page_context(context, page, config, nav):
    if page.meta.get("cb_spec") and page.toc:
        # Every language's specification ends with its FAQ, whose questions are too long
        # to list in the outline: the last section keeps its own entry only.
        items = page.toc.items
        if len(items) == 1 and items[0].level == 1:
            items = items[0].children
        if items:
            items[-1].children = []
    if page.meta.get("seoTitle"):
        context["cb_title"] = page.meta["seoTitle"]
    elif page.meta.get("cb_version", "current") != "current":
        # Every language's copy of an old version names it, so it can't be mistaken
        # for the current one in a search result.
        context["cb_title"] = f"{config.site_name} {page.meta['cb_version'].lstrip('v')}"
    return context


# -- FAQ structured data -------------------------------------------------------------

_TAG = re.compile(r"<[^>]+>")


def _plain(fragment: str) -> str:
    fragment = re.sub(r'<a class="headerlink"[^>]*>.*?</a>', "", fragment, flags=re.S)
    fragment = re.sub(r"<li>", "- ", fragment)
    fragment = re.sub(r"</(p|li|ul|ol|pre)>", "\n", fragment)
    text = html.unescape(_TAG.sub("", fragment))
    text = re.sub(r"[ \t]+", " ", text)
    return re.sub(r" *\n[\n ]*", "\n", text).strip(" \n")


def _faq(html_text: str) -> str | None:
    """The FAQ, the last h2 section, as FAQPage JSON-LD: each h3 is a question."""
    last = html_text.split("<h2")[-1]
    parts = last.split("<h3")[1:]
    questions = []
    for part in parts:
        title, _, answer = part.partition("</h3>")
        title = _plain(title.split(">", 1)[1])
        questions.append({
            "@type": "Question",
            "name": title,
            "acceptedAnswer": {"@type": "Answer", "text": _plain(answer)},
        })
    if not questions:
        return None
    data = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": questions}
    return json.dumps(data, ensure_ascii=False).replace("</", "<\\/")


# -- after the build ----------------------------------------------------------------

_FORWARD = """<!DOCTYPE html>
<html lang="en">
  <head>
    <title>{url}</title>
    <link rel="canonical" href="{url}">
    <meta charset="utf-8">
    <meta http-equiv="refresh" content="0; url=/">
  </head>
</html>
"""


def on_post_build(config):
    if not _is_default(config):
        return
    site = Path(config.site_dir)
    root_url = config.site_url
    # /en/ was the English homepage's alias, and /v<current>/ is where every archived
    # version lives, so people try it for the current one too. Both forward to /.
    current = (config.theme.get("versions") or [{}])[0].get("title")
    for folder in ("en", f"v{current}" if current else None):
        if folder and not (site / folder / "index.html").exists():
            (site / folder).mkdir(parents=True, exist_ok=True)
            (site / folder / "index.html").write_text(_FORWARD.format(url=root_url), encoding="utf-8")

    # One sitemap per language, listed by an index at /sitemap.xml, as the Hugo site
    # published them: search consoles already know these addresses.
    langs = config.get("languages") or []
    if langs and (site / "sitemap.xml").exists():
        (site / "en").mkdir(exist_ok=True)
        shutil.move(site / "sitemap.xml", site / "en" / "sitemap.xml")
        gz = site / "sitemap.xml.gz"
        if gz.exists():
            gz.unlink()
        entries = "".join(
            f"  <sitemap>\n    <loc>{root_url}{'en' if lang.default else lang.path}/sitemap.xml</loc>\n  </sitemap>\n"
            for lang in sorted(langs, key=lambda lang: "en" if lang.default else lang.path)
        )
        (site / "sitemap.xml").write_text(
            '<?xml version="1.0" encoding="utf-8" standalone="yes"?>\n'
            '<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            f"{entries}</sitemapindex>\n",
            encoding="utf-8",
        )
