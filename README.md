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
├── fetch_papers.py                  # Script Python principale
├── requirements.txt                 # Dipendenze Python (requests, feedparser)
├── papers/                          # Cartella dove vengono salvati i paper
│   ├── latest.md                    # Riepilogo dell'ultimo aggiornamento
│   └── YYYY-MM-DD/                  # Sottocartelle per data
│       └── <arxiv-id>.md            # Un file per paper
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
   python fetch_papers.py
   ```

I paper verranno salvati nella cartella `papers/` suddivisi per data.

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
