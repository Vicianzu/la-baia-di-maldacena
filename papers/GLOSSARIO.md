# 📖 Glossario — La Baia di Maldacena

Questa guida spiega i concetti fisici e matematici che compaiono più spesso nei paper dell'archivio.
È pensata come **prima lettura** prima di affrontare un paper tecnico.

---

## Come usare questo glossario

1. Leggi l'**abstract** del paper che vuoi capire.
2. Cerca qui i termini che non conosci.
3. Usa **Copilot Chat** per domande più specifiche:
   > *"Spiegami in parole semplici cosa significa [termine] nel contesto di questo paper."*

---

## Concetti fondamentali

### AdS/CFT — La corrispondenza di Maldacena

La corrispondenza **Anti-de Sitter / Conformal Field Theory** è la pietra angolare dell'olografia moderna.
Formulata da Juan Maldacena nel 1997, afferma che:

> Una teoria di gravità (teoria delle stringhe) in uno spazio-tempo **AdS** di dimensione `D`
> è **equivalente** a una teoria di campo conforme (**CFT**) sul suo bordo di dimensione `D−1`.

**Perché è importante:** permette di studiare problemi di meccanica quantistica fortemente accoppiata
usando la gravità classica, e viceversa.

**Parole chiave correlate:** bulk/boundary, olographic dictionary, GKPW prescription.

---

### dS/CFT — L'estensione a de Sitter

Lo spazio **de Sitter (dS)** è lo spazio-tempo con costante cosmologica **positiva** — quello in cui
viviamo. La corrispondenza **dS/CFT** è la versione analoga dell'AdS/CFT per questo caso,
ma è molto meno compresa.

**Sfide principali:**
- Il bordo di dS è nel futuro asintotico (non spaziale come in AdS)
- Non è chiaro come definire gli osservabili olografici
- La termodinamica è più complicata (l'osservatore ha un orizzonte cosmologico)

**Paper tipici:** propongono nuove formulazioni della dualità, studiano correlatori,
o esplorano connessioni con la cosmologia inflazionaria.

---

### Olografia Celestiale (Celestial Holography / CCFT)

L'**olografia celestiale** è un approccio recente che reformula la fisica delle particelle 4D
(in spazio-tempo di Minkowski piatto) come una CFT 2D sulla **sfera celeste** — la sfera
immaginaria che circonda un osservatore a infinita distanza.

**Idea chiave:** le ampiezze di scattering di particelle ordinarie (fotoni, gravitoni, gluoni)
possono essere riscritte come funzioni di correlazione di una CFT 2D.

**Perché è interessante:** collega tre aree prima separate:
- Simmetrie BMS dello spazio-tempo piatto
- Soft theorems di Weinberg
- Memoria gravitazionale

---

### Simmetria BMS (Bondi-Metzner-Sachs)

Il gruppo **BMS** è il gruppo di simmetria dello spazio-tempo piatto di Minkowski
al futuro infinito nullo (`ℐ⁺`). Fu scoperto negli anni '60 da Bondi, van der Burg, Metzner e Sachs.

Contiene:
- **Supertraslazioni**: traslazioni spazio-temporali con parametro dipendente dalla direzione
- **Superrotazioni**: trasformazioni conformi sulla sfera celeste (scoperte più di recente)

**Il triangolo BMS:** Strominger ha mostrato che esiste una relazione triangolare tra
simmetrie BMS asintotiche, soft theorems e memoria gravitazionale.

---

### Soft Theorems

I **soft theorems** descrivono il comportamento delle ampiezze di scattering quando
un gravitone (o fotone) viene emesso con energia che tende a zero.

Il celebre **teorema di Weinberg** (1965) afferma che l'ampiezza con un gravitone soft
è universale e dipende solo dalla carica (o massa) delle particelle esterne.

**Connessione moderna:** i soft theorems sono le trasformate di Ward delle simmetrie BMS.
Questo ha trasformato un fatto oscuro della teoria di campo in un principio di simmetria profondo.

---

### Entropia di Entanglement e Formula di Ryu-Takayanagi

In AdS/CFT, l'**entropia di entanglement** di una regione `A` nella CFT sul bordo
è uguale all'area della superficie minimale `γ_A` nel bulk che ha `∂γ_A = ∂A`:

```
S(A) = Area(γ_A) / (4 G_N)
```

Questa è la **formula di Ryu-Takayanagi** (RT), un risultato fondamentale che collega
la geometria del bulk con l'informazione quantistica sul bordo.

**Generalizzazioni:** formula di Hubeny-Rangamani-Takayanagi (HRT) per il caso dipendente
dal tempo, e le correzioni quantistiche (formula di Engelhardt-Wall).

---

### Olografia in Spazio Piatto (Flat Space Holography)

Estensione dell'AdS/CFT al caso di spazio-tempo asintoticamente **piatto**.
La teoria duale vive su un bordo con struttura causale diversa da AdS.

È strettamente legata all'olografia celestiale e alle simmetrie BMS.
Un approccio è il limite `ℓ_AdS → ∞` della corrispondenza AdS/CFT.

---

### CFT — Conformal Field Theory

Una **CFT** è una teoria di campo quantistico invariante per trasformazioni conformi
(riscalamenti locali, inversioni, traslazioni, rotazioni).

Caratteristiche principali:
- Non ha scala di massa
- Gli operatori sono classificati dal loro **peso conforme** `Δ`
- Le funzioni a 2 e 3 punti sono completamente determinate dalla simmetria
- In 2D: simmetria infinito-dimensionale (algebra di Virasoro)

---

### Algebra di Virasoro e Kac-Moody

L'**algebra di Virasoro** è l'algebra di Lie dei generatori della simmetria conforme in 2D.
È caratterizzata dalla **carica centrale** `c`, che misura il "grado di libertà" della CFT.

Le algebre di **Kac-Moody** sono estensioni infinite di algebre di Lie ordinarie;
compaiono nelle CFT con simmetrie di gauge interne.

---

### Ampiezze di Scattering e S-matrix

La **S-matrix** codifica le probabilità di transizione tra stati asinptotici in entrata e in uscita.
Le **ampiezze di scattering** sono gli elementi di matrice della S-matrix.

Tecniche moderne:
- **Spinor helicity formalism**: rappresentazione efficiente degli stati di elicità
- **BCFW recursion**: calcolo ricorsivo senza diagrammi di Feynman
- **Amplituhedron**: struttura geometrica delle ampiezze in N=4 SYM

---

### Radiazione di Hawking e Paradosso dell'Informazione

**Radiazione di Hawking:** i buchi neri emettono radiazione termica a temperatura
`T_H = ℏ c³ / (8π G M k_B)`. Questo porta alla loro evaporazione.

**Paradosso dell'informazione:** se la radiazione è perfettamente termica, l'informazione
sullo stato iniziale che ha formato il buco nero sembrerebbe persa, violando l'unitarietà
della meccanica quantistica.

**Stato dell'arte:** il **Page curve** e le **isole** (islands) sono sviluppi recenti che
suggeriscono che l'informazione non è persa, attraverso effetti non-perturbativi della gravità.

---

## Guida rapida alle categorie arXiv

| Categoria | Significato |
|-----------|-------------|
| `hep-th`  | High Energy Physics – Theory (teoria delle stringhe, olografia, teoria di campo) |
| `gr-qc`   | General Relativity & Quantum Cosmology |
| `hep-ph`  | High Energy Physics – Phenomenology |
| `math-ph` | Mathematical Physics |
| `quant-ph`| Quantum Physics |
| `cond-mat`| Condensed Matter (spesso appare per connessioni con AdS/CFT) |

---

## Risorse per approfondire

- **TASI Lectures on AdS/CFT** — McGreevy (arXiv:0909.0518)
- **Lectures on the Infrared Structure of Gravity and Gauge Theory** — Strominger (arXiv:1703.05448)  
  *(La bibbia della simmetria BMS e dell'olografia celestiale)*
- **Celestial Holography** — Pasterski (arXiv:2111.11392)
- **Introduction to the AdS/CFT Correspondence** — AHARONY et al. (arXiv:hep-th/9905221)
- **An Introduction to Black Holes, Information and the String Theory Revolution** — Susskind & Lindesay

---

*Glossario generato automaticamente per **La Baia di Maldacena**. Contributi benvenuti.*
