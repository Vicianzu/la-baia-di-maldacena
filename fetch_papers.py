#!/usr/bin/env python3
"""
fetch_papers.py - Scarica i paper più recenti da arXiv su dS/CFT e olografia celestiale.

Usa l'API pubblica di arXiv (nessuna autenticazione necessaria).
Salva ogni paper come file Markdown in papers/YYYY-MM-DD/
e genera un riepilogo in papers/latest.md.
"""

import os
import re
from datetime import datetime, timedelta, timezone

import feedparser
import requests

# Keyword di ricerca
KEYWORDS = [
    "dS/CFT",
    "celestial holography",
    "celestial CFT",
    "BMS symmetry",
    "flat space holography",
    "AdS/CFT",
    "Maldacena",
]

ARXIV_API_URL = "https://export.arxiv.org/api/query"
PAPERS_DIR = os.path.join(os.path.dirname(__file__), "papers")
DAYS_BACK = 7


def build_query() -> str:
    """Costruisce la query per l'API di arXiv con le keyword configurate."""
    terms = [f'all:"{kw}"' for kw in KEYWORDS]
    return " OR ".join(terms)


def fetch_papers(query: str, max_results: int = 100) -> list[dict]:
    """
    Interroga l'API di arXiv e restituisce una lista di paper.

    Ogni paper è un dizionario con: id, title, authors, summary, link, categories, published.
    """
    params = {
        "search_query": query,
        "start": 0,
        "max_results": max_results,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    }

    try:
        response = requests.get(ARXIV_API_URL, params=params, timeout=30)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Errore durante la richiesta all'API di arXiv: {e}")
        return []

    feed = feedparser.parse(response.text)

    cutoff = datetime.now(tz=timezone.utc) - timedelta(days=DAYS_BACK)
    papers = []

    for entry in feed.entries:
        # Parsing della data di pubblicazione
        published_struct = entry.get("published_parsed")
        if published_struct is None:
            continue
        published_dt = datetime(*published_struct[:6], tzinfo=timezone.utc)

        if published_dt < cutoff:
            continue

        # Estrazione dell'ID arXiv: supporta sia il formato moderno (YYMM.NNNNN)
        # che il formato legacy (categoria/NNNNNNN, es. hep-th/9711200)
        raw_id = entry.get("id", "")
        arxiv_id_match = re.search(r"(\d{4}\.\d{4,5}|[a-z\-]+/\d{7})(v\d+)?$", raw_id)
        arxiv_id = arxiv_id_match.group(1) if arxiv_id_match else raw_id

        authors = [a.get("name", "") for a in entry.get("authors", [])]
        categories = [t.get("term", "") for t in entry.get("tags", [])]

        papers.append(
            {
                "id": arxiv_id,
                "title": entry.get("title", "").replace("\n", " ").strip(),
                "authors": authors,
                "summary": entry.get("summary", "").replace("\n", " ").strip(),
                "link": f"https://arxiv.org/abs/{arxiv_id}",
                "categories": categories,
                "published": published_dt.strftime("%Y-%m-%d"),
            }
        )

    return papers


def paper_to_markdown(paper: dict) -> str:
    """Converte un paper in testo Markdown."""
    authors_str = ", ".join(paper["authors"]) if paper["authors"] else "N/A"
    categories_str = ", ".join(paper["categories"]) if paper["categories"] else "N/A"

    return f"""# {paper['title']}

**Autori:** {authors_str}

**Pubblicato:** {paper['published']}

**Categorie arXiv:** {categories_str}

**Link:** [{paper['link']}]({paper['link']})

## Abstract

{paper['summary']}
"""


def save_paper(paper: dict) -> bool:
    """
    Salva un paper come file Markdown in papers/YYYY-MM-DD/.

    Restituisce True se il file è stato creato, False se esisteva già.
    """
    date_dir = os.path.join(PAPERS_DIR, paper["published"])
    os.makedirs(date_dir, exist_ok=True)

    # Nome file sicuro basato sull'ID arXiv
    safe_id = re.sub(r"[^\w.\-]", "_", paper["id"])
    filepath = os.path.join(date_dir, f"{safe_id}.md")

    if os.path.exists(filepath):
        return False  # Già scaricato

    content = paper_to_markdown(paper)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    return True


def save_latest_summary(papers: list[dict]) -> None:
    """Genera il file papers/latest.md con il riepilogo dell'ultimo run."""
    filepath = os.path.join(PAPERS_DIR, "latest.md")
    now_str = datetime.now(tz=timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    lines = [
        "# 📄 Ultimi paper arXiv — La Baia di Maldacena\n",
        f"**Aggiornato:** {now_str}\n",
        f"**Paper trovati negli ultimi {DAYS_BACK} giorni:** {len(papers)}\n",
        "\n---\n",
    ]

    for paper in papers:
        authors_str = ", ".join(paper["authors"][:3])
        if len(paper["authors"]) > 3:
            authors_str += " et al."
        lines.append(
            f"\n## [{paper['title']}]({paper['link']})\n"
            f"\n**Autori:** {authors_str}  \n"
            f"**Pubblicato:** {paper['published']}  \n"
            f"**Categorie:** {', '.join(paper['categories'])}\n"
            f"\n> {paper['summary'][:400]}{'...' if len(paper['summary']) > 400 else ''}\n"
        )

    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def deduplicate(papers: list[dict]) -> list[dict]:
    """Rimuove duplicati basandosi sull'ID arXiv."""
    seen = set()
    unique = []
    for paper in papers:
        if paper["id"] not in seen:
            seen.add(paper["id"])
            unique.append(paper)
    return unique


def main() -> None:
    print(f"🔍 Ricerca paper arXiv — ultimi {DAYS_BACK} giorni")
    print(f"   Keyword: {', '.join(KEYWORDS)}\n")

    query = build_query()
    papers = fetch_papers(query)
    papers = deduplicate(papers)

    print(f"📥 Paper trovati: {len(papers)}")

    new_count = 0
    for paper in papers:
        created = save_paper(paper)
        if created:
            new_count += 1
            print(f"   ✅ Salvato: [{paper['published']}] {paper['title'][:70]}")
        else:
            print(f"   ⏭️  Già presente: {paper['id']}")

    if papers:
        save_latest_summary(papers)
        print(f"\n📝 Riepilogo salvato in papers/latest.md")

    print(f"\n✨ Completato — {new_count} nuovi paper salvati.")


if __name__ == "__main__":
    main()
