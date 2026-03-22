# La Baia di Maldacena 🌊

[![Daily arXiv Paper Fetch](https://github.com/Vicianzu/la-baia-di-maldacena/actions/workflows/fetch-papers.yml/badge.svg)](https://github.com/Vicianzu/la-baia-di-maldacena/actions/workflows/fetch-papers.yml)

Sistema automatico per raccogliere ogni giorno i paper più recenti da arXiv su **dS/CFT**, **olografia celestiale** e argomenti correlati alla fisica teorica delle stringhe e della gravità quantistica.

---

## 📚 Descrizione

**La Baia di Maldacena** è un archivio automatizzato che interroga l'API pubblica di arXiv ogni mattina alle 08:00 UTC e scarica i paper pubblicati negli ultimi 7 giorni sui seguenti argomenti:

- `dS/CFT`
- `celestial holography` (olografia celestiale)
- `celestial CFT`
- `BMS symmetry`
- `flat space holography`
- `AdS/CFT`
- `Maldacena`

Ogni paper viene salvato come file Markdown leggibile nella cartella `papers/`.

---

## 🗂️ Struttura del repository

```
la-baia-di-maldacena/
├── README.md                        # Questo file
├── fetch_papers.py                  # Scarica paper da arXiv
├── explain_paper.py                 # Genera spiegazioni in italiano dei paper
├── requirements.txt                 # Dipendenze Python (requests, feedparser)
├── papers/                          # Cartella dove vengono salvati i paper
│   ├── GLOSSARIO.md                 # Glossario dei concetti fisici chiave
│   ├── latest.md                    # Riepilogo dell'ultimo aggiornamento
│   └── YYYY-MM-DD/                  # Sottocartelle per data
│       ├── <arxiv-id>.md            # Paper (abstract + guida alla lettura)
│       └── <arxiv-id>_SPIEGAZIONE.md  # Spiegazione dettagliata in italiano
└── .github/
    └── workflows/
        └── fetch-papers.yml         # GitHub Action schedulata
```

---

## 🚀 Eseguire lo script manualmente

1. Clona il repository:
   ```bash
   git clone https://github.com/Vicianzu/la-baia-di-maldacena.git
   cd la-baia-di-maldacena
   ```

2. Installa le dipendenze:
   ```bash
   pip install -r requirements.txt
   ```

3. Esegui lo script:
   ```bash
   python fetch_papers.py              # tutti i paper degli ultimi 7 giorni
   python fetch_papers.py --limit 5    # solo i 5 paper più recenti
   python fetch_papers.py --days 14    # amplia la finestra a 14 giorni
   ```

I paper verranno salvati nella cartella `papers/` suddivisi per data,
ciascuno con una **sezione "Guida alla lettura"** che spiega i concetti chiave rilevati.

Consulta [`papers/GLOSSARIO.md`](papers/GLOSSARIO.md) per una spiegazione
dei termini fisici più comuni (AdS/CFT, BMS, olografia celestiale…).

---

## 💡 Farsi spiegare un paper

Dopo aver scaricato i paper, usa `explain_paper.py` per generare una spiegazione
dettagliata in italiano — con contesto storico, idea principale, risultati chiave
e domande guida per approfondire:

```bash
python explain_paper.py                              # spiega il paper più recente
python explain_paper.py papers/2024-01-14/2401.07962.md  # spiega un paper specifico
python explain_paper.py --all                        # spiega tutti i paper
python explain_paper.py --list                       # elenca i paper (con stato spiegazione)
```

Le spiegazioni vengono salvate come `<arxiv-id>_SPIEGAZIONE.md` accanto al paper originale,
con sezioni di:

- 🎯 **Sommario** — di cosa parla il paper in parole semplici
- 🔍 **Il problema** — cosa cercano di risolvere gli autori
- 🧠 **L'idea principale** — il metodo o la tecnica centrale
- 📐 **La matematica** — le formule chiave spiegate
- 🌍 **Perché è importante** — le implicazioni fisiche
- 📚 **Connessioni** — link agli altri paper dell'archivio
- ❓ **Domande per Copilot Chat** — prompt pronti da usare

---

## 🤖 Usare Copilot Chat per leggere i paper

Puoi usare **GitHub Copilot Chat** direttamente nel repository per farti spiegare i paper scaricati. Alcuni esempi di prompt utili:

- *"Spiegami in italiano cosa tratta questo paper e quali sono i risultati principali."*
- *"Quali sono le implicazioni fisiche di questo risultato per la dualità AdS/CFT?"*
- *"Confronta questo paper con i precedenti sulla simmetria BMS."*
- *"Spiega la notazione matematica usata nell'abstract."*

Basta aprire un file Markdown nella cartella `papers/` e avviare una conversazione con Copilot Chat nel pannello laterale.

---

## ⚙️ Come funziona la GitHub Action

Il workflow `.github/workflows/fetch-papers.yml`:

- **Si attiva** ogni giorno alle 08:00 UTC (o manualmente dalla tab Actions)
- **Installa** Python 3.11 e le dipendenze
- **Esegue** `fetch_papers.py`
- **Fa commit e push** dei nuovi file Markdown con messaggio `📄 Daily arXiv update - YYYY-MM-DD`
- **Non fa commit** se non ci sono nuovi paper
