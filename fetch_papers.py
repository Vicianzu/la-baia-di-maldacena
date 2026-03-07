#!/usr/bin/env python3
"""
fetch_papers.py - Scarica i paper più recenti da arXiv su dS/CFT e olografia celestiale.

Usa l'API pubblica di arXiv (nessuna autenticazione necessaria).
Salva ogni paper come file Markdown in papers/YYYY-MM-DD/
e genera un riepilogo in papers/latest.md.

Uso:
    python fetch_papers.py              # scarica fino a 100 paper degli ultimi 7 giorni
    python fetch_papers.py --limit 5    # scarica solo i 5 paper più recenti
    python fetch_papers.py --days 14    # estende la finestra temporale a 14 giorni
"""

import argparse
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


def fetch_papers(query: str, max_results: int = 100, days_back: int = DAYS_BACK) -> list[dict]:
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

    cutoff = datetime.now(tz=timezone.utc) - timedelta(days=days_back)
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
    """Converte un paper in testo Markdown con guida alla lettura."""
    authors_str = ", ".join(paper["authors"]) if paper["authors"] else "N/A"
    categories_str = ", ".join(paper["categories"]) if paper["categories"] else "N/A"

    # Identifica i concetti chiave presenti nel titolo/abstract
    concepts = _detect_concepts(paper["title"] + " " + paper["summary"])
    concepts_section = _build_concepts_section(concepts)

    return f"""# {paper['title']}

**Autori:** {authors_str}

**Pubblicato:** {paper['published']}

**Categorie arXiv:** {categories_str}

**Link:** [{paper['link']}]({paper['link']})

## Abstract

{paper['summary']}

---

## 🧭 Guida alla lettura

### Come affrontare questo paper

1. **Abstract** — Già letto sopra. Identifica il problema che gli autori vogliono risolvere.
2. **Introduzione** — Spiega il contesto e riassume i risultati principali. Leggila prima del resto.
3. **Conclusioni** — Leggi subito dopo l'introduzione per capire dove si arriva.
4. **Sezioni tecniche** — Torna indietro solo per i dettagli che ti interessano.

> 💡 **Suggerimento Copilot:** Apri questo file in GitHub e avvia Copilot Chat con il prompt:
> *"Spiegami in italiano cosa dimostra questo paper e quali sono le sue implicazioni fisiche."*

### Concetti chiave rilevati in questo paper
{concepts_section}

### Domande guida per la comprensione

- Qual è il **problema aperto** che questo paper affronta?
- Quale **metodo o tecnica** usano gli autori?
- Quali sono i **risultati principali** (equazioni, teoremi, simulazioni)?
- Come si **collega** ad altri paper nell'archivio?
- Cosa rimane ancora **aperto o irrisolto**?
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


def save_latest_summary(papers: list[dict], days_back: int = DAYS_BACK) -> None:
    """Genera il file papers/latest.md con il riepilogo dell'ultimo run."""
    filepath = os.path.join(PAPERS_DIR, "latest.md")
    now_str = datetime.now(tz=timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    lines = [
        "# 📄 Ultimi paper arXiv — La Baia di Maldacena\n",
        f"**Aggiornato:** {now_str}\n",
        f"**Paper trovati negli ultimi {days_back} giorni:** {len(papers)}\n",
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


# ---------------------------------------------------------------------------
# Rilevamento concetti chiave
# ---------------------------------------------------------------------------

# Dizionario: pattern da cercare → descrizione breve in italiano
_CONCEPT_MAP: dict[str, str] = {
    r"dS/CFT|de Sitter": "**dS/CFT** — dualità tra gravità in spazio de Sitter e CFT sul bordo; analogo de Sitter dell'AdS/CFT.",
    r"AdS/CFT|Anti-de Sitter": "**AdS/CFT** — la corrispondenza di Maldacena: la gravità in AdS è equivalente a una CFT sul suo bordo.",
    r"celestial holograph|celestial CFT|CCFT": "**Olografia Celestiale / CCFT** — riformulazione della S-matrix 4D come una CFT 2D sulla sfera celeste.",
    r"BMS|Bondi-Metzner-Sachs": "**Simmetria BMS** — gruppo di simmetria asintotico dello spazio-tempo piatto; include supertraslazioni e superrotazioni.",
    r"flat.space holograph|flat holograph": "**Olografia in spazio piatto** — estensione dell'AdS/CFT al caso di spazio-tempo asintoticamente piatto.",
    r"soft theorem|soft graviton|soft photon": "**Soft theorems** — teoremi che descrivono l'emissione di particelle a bassa energia; collegati alle simmetrie asintotiche BMS.",
    r"entanglement entropy|von Neumann entropy": "**Entropia di entanglement** — misura della correlazione quantistica tra sottosistemi; centrale nell'olografia (formula RT).",
    r"black hole|event horizon|Hawking": "**Buchi neri** — oggetti con orizzonte degli eventi; al centro di molti problemi aperti (paradosso dell'informazione, radiazione di Hawking).",
    r"holograph": "**Olografia** — principio per cui la fisica in un volume D-dim è codificata sul suo bordo (D-1)-dim.",
    r"conformal field theory|CFT": "**CFT (Conformal Field Theory)** — teoria di campo invariante per trasformazioni conformi; il lato 'boundary' delle dualità olografiche.",
    r"string theory|superstring": "**Teoria delle stringhe** — framework che unifica gravità e meccanica quantistica sostituendo particelle puntuali con stringhe.",
    r"scattering amplitudes|S-matrix": "**Ampiezze di scattering / S-matrix** — quantità che descrivono le probabilità di interazione tra particelle.",
    r"Virasoro|Kac-Moody": "**Algebra di Virasoro / Kac-Moody** — algebre di simmetria infinite delle CFT 2D.",
    r"gravitational wave": "**Onde gravitazionali** — perturbazioni dello spazio-tempo che si propagano alla velocità della luce; collegate alle simmetrie BMS.",
    r"wormhole|ER=EPR": "**Wormhole / ER=EPR** — connessioni topologiche tra regioni di spazio-tempo; relate all'entanglement quantistico.",
}


def _detect_concepts(text: str) -> list[str]:
    """Restituisce le descrizioni dei concetti trovati nel testo."""
    found = []
    seen_keys = set()
    for pattern, description in _CONCEPT_MAP.items():
        key = pattern.split("|")[0]
        if key not in seen_keys and re.search(pattern, text, re.IGNORECASE):
            found.append(description)
            seen_keys.add(key)
    return found


def _build_concepts_section(concepts: list[str]) -> str:
    """Formatta la lista di concetti come elenco puntato Markdown."""
    if not concepts:
        return "_Nessun concetto chiave rilevato automaticamente. Consulta il [Glossario](../GLOSSARIO.md)._"
    items = "\n".join(f"- {c}" for c in concepts)
    return f"{items}\n\n> 📖 Per approfondire i termini vedi [`papers/GLOSSARIO.md`](../GLOSSARIO.md)"


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Scarica paper da arXiv su dS/CFT e olografia celestiale."
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        metavar="N",
        help="Limita il numero di paper scaricati (default: nessun limite).",
    )
    parser.add_argument(
        "--days",
        type=int,
        default=DAYS_BACK,
        metavar="D",
        help=f"Finestra temporale in giorni (default: {DAYS_BACK}).",
    )
    args = parser.parse_args()

    days_back = args.days

    print(f"🔍 Ricerca paper arXiv — ultimi {days_back} giorni")
    print(f"   Keyword: {', '.join(KEYWORDS)}\n")

    query = build_query()
    # Richiedi più risultati del necessario, poi taglia dopo deduplicazione
    max_api = (args.limit * 3) if args.limit else 100
    papers = fetch_papers(query, max_results=max_api, days_back=days_back)
    papers = deduplicate(papers)

    if args.limit:
        papers = papers[: args.limit]
        print(f"📥 Paper trovati (limitati a {args.limit}): {len(papers)}")
    else:
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
        save_latest_summary(papers, days_back=days_back)
        print(f"\n📝 Riepilogo salvato in papers/latest.md")

    print(f"\n✨ Completato — {new_count} nuovi paper salvati.")


if __name__ == "__main__":
    main()
