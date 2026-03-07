#!/usr/bin/env python3
"""
explain_paper.py - Genera una spiegazione dettagliata in italiano di un paper.

Uso:
    python explain_paper.py papers/2024-01-14/2401.07962.md   # spiega un paper specifico
    python explain_paper.py --latest                           # spiega il paper più recente
    python explain_paper.py --all                              # spiega tutti i paper
    python explain_paper.py --list                             # elenca i paper disponibili
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

PAPERS_DIR = Path(__file__).parent / "papers"

# ---------------------------------------------------------------------------
# Spiegazioni pre-scritte per i paper inclusi nell'archivio
# Formato: arxiv_id → testo Markdown della spiegazione (senza intestazione)
# ---------------------------------------------------------------------------

_EXPLANATIONS: dict[str, str] = {

    # ------------------------------------------------------------------
    "2401.09675": """\
## 🎯 Di cosa parla, in breve

Questo paper è una **review** (rassegna) sull'**olografia celestiale** — un programma di ricerca
che vuole riscrivere la fisica delle particelle in quattro dimensioni usando un linguaggio
bidimensionale, come se tutto ciò che succede nello spazio-tempo potesse essere "proiettato"
su una sfera lontanissima.

L'intuizione di fondo è semplice: quando due particelle si scontrano e poi si allontanano
all'infinito, le tracce di quell'evento le vediamo arrivare da una certa direzione nel cielo.
La **sfera celeste** è la sfera immaginaria che raccoglie tutte queste direzioni.
Le autrici mostrano che questa sfera ha la struttura matematica di una **CFT 2D** —
la stessa teoria usata per descrivere i materiali critici o le stringhe.

---

## 🔍 Il problema che questo paper vuole risolvere

La **S-matrix** — la matrice che codifica le probabilità di tutti i processi di scattering —
è l'oggetto centrale della fisica delle particelle. Ma la S-matrix è definita in quattro
dimensioni e dipende da dati (energia, momento) difficili da connettere a strutture geometriche semplici.

Il problema è: **esiste un modo più naturale di organizzare le ampiezze di scattering**,
uno che riveli simmetrie nascoste?

La risposta dell'olografia celestiale è sì: **cambia le variabili cinematiche** da
(energia, momento) a (peso conforme, direzione sulla sfera celeste). In queste variabili,
le ampiezze si trasformano come **operatori di una CFT 2D**.

---

## 🧠 L'idea principale: dal momento alla sfera celeste

Ogni particella nello stato iniziale o finale di uno scattering può essere descritta da:
- La sua **elicità** (spin nella direzione del moto)
- Un punto `z, z̄` sulla sfera di Riemann ℂ ∪ {∞} — la **sfera celeste**
- Il suo **peso conforme** `Δ` (legato all'energia tramite una trasformata di Mellin)

In queste variabili, le **ampiezze di scattering** si comportano come
**funzioni di correlazione di una CFT 2D** — soddisfano le stesse equazioni di invarianza
conforme che conosciamo dalla meccanica statistica bidimensionale.

---

## 🏛️ Il ruolo del gruppo BMS

Il **gruppo BMS** (Bondi-Metzner-Sachs) è il gruppo di simmetria dello spazio-tempo piatto
al futuro asintotico: le trasformazioni che lasciano invariata la struttura dello spazio-tempo
lontano da tutte le sorgenti. Include:

| Sottoinsieme | Cosa fa |
|---|---|
| Supertraslazioni | Traslazioni con parametro dipendente dalla direzione |
| Superrotazioni | Trasformazioni conformi sulla sfera celeste (infinite-dimensionali) |

Il risultato chiave del paper è che il **gruppo BMS agisce come gruppo di simmetria della CCFT
duale**. In altre parole: le simmetrie dello spazio-tempo a grande distanza si traducono
esattamente nelle simmetrie della CFT sulla sfera celeste. Questo è il cuore della dualità.

---

## 📐 Il collegamento con i soft theorems

Un **soft theorem** dice cosa succede a un'ampiezza di scattering quando aggiungo un gravitone
(o fotone) con energia che tende a zero. Il risultato classico di Weinberg (1965) è:

```
M(p₁,...,pₙ, q→0) = S⁽⁰⁾ · M(p₁,...,pₙ)
```

dove `S⁽⁰⁾` è un fattore universale che dipende solo dalle cariche delle particelle esterne.

Nell'olografia celestiale, questo soft theorem diventa una **identità di Ward** della CCFT:
l'operatore che inserisce un gravitone soft corrisponde a un **operatore corrente** nella CFT,
la cui conservazione è esattamente il soft theorem.

Questo trasforma una formula oscura di teoria di campo in un **principio di simmetria fondamentale**.

---

## 🧩 Il prodotto OPE celeste

Nella CCFT, due operatori vicini sulla sfera celeste si fondono in un terzo operatore
secondo l'**Operator Product Expansion (OPE)**. Per i gravitoni, questo OPE ha una struttura
singolare precisa che riflette la struttura della gravità.

Conoscere l'OPE celeste significa conoscere le regole di fusione della CCFT —
e quindi, in linea di principio, ricostruire tutta la S-matrix gravitazionale.

---

## 🌍 Perché è importante

1. **Nuova organizzazione della gravità perturbativa**: le simmetrie BMS danno vincoli infiniti
   sulle ampiezze gravitazionali.
2. **Connessione con la memoria gravitazionale**: ogni ramo del "triangolo BMS"
   (soft theorems, simmetrie asintotiche, memoria) diventa accessibile.
3. **Potenziale per un bootstrap celeste**: come nelle CFT 2D ordinarie,
   forse le sole simmetrie bastano a determinare tutte le ampiezze.
4. **Finestra sulla gravità quantistica**: se la S-matrix gravitazionale ha una descrizione CFT,
   questo suggerisce che la gravità in spazio piatto ha un **duale olografico** preciso.

---

## 📚 Connessioni con gli altri paper nell'archivio

| Paper | Collegamento |
|---|---|
| [2401.07962](../2024-01-14/2401.07962.md) — Strominger, BMS e soft theorems | Questo paper è la fonte delle idee che la review sintetizza; leggerlo prima aiuta molto |
| [2401.06543](../2024-01-14/2401.06543.md) — Flat space holography | Fornisce il contesto spaziale (infinito spaziale vs nullo) completando il quadro BMS |
| [2401.08441](../2024-01-15/2401.08441.md) — dS/CFT bootstrap | Approccio simile (bootstrap) ma in de Sitter invece di Minkowski |

---

## ❓ Domande per approfondire (con Copilot Chat)

Apri questo file in GitHub e prova questi prompt in Copilot Chat:

- *"Cos'è la trasformata di Mellin delle ampiezze di scattering e perché è utile?"*
- *"Spiega la differenza tra supertraslazioni e superrotazioni nel gruppo BMS."*
- *"Cos'è un operatore conforme primario e come appare nella CCFT?"*
- *"Perché lo stress tensor della CCFT è così difficile da costruire?"*
""",

    # ------------------------------------------------------------------
    "2401.08441": """\
## 🎯 Di cosa parla, in breve

Questo paper studia la **corrispondenza dS/CFT** — la versione de Sitter dell'AdS/CFT —
usando un approccio moderno chiamato **bootstrap cosmologico**.

Lo spazio de Sitter (dS) è lo spazio-tempo con costante cosmologica **positiva**:
è il tipo di spazio-tempo in cui viviamo, e descrive anche l'universo durante l'**inflazione**.
La grande sfida è capire cosa significhi "olografia" in questo contesto,
e se esista una teoria sul bordo che descriva la gravitazione in dS.

Il bootstrap cosmologico è un metodo per ricavare le funzioni di correlazione cosmologiche
usando solo i **principi di simmetria** (isometrie di de Sitter), senza calcolare i diagrammi
di Feynman uno per uno.

---

## 🔍 Il problema che questo paper vuole risolvere

In AdS/CFT, il dizionario olografico è ben stabilito: gli stati della gravità nel bulk
corrispondono a operatori nella CFT sul bordo. Ma in de Sitter:

- Il **bordo** è nel **futuro asintotico** ℐ⁺ (non spaziale come in AdS)
- L'osservatore ha un **orizzonte cosmologico** che oscura parte dell'universo
- Non è ovvio come definire **osservabili** gauge-invarianti

La domanda centrale del paper è: **la funzione d'onda di Hartle-Hawking di de Sitter
soddisfa equazioni di bootstrap simili a quelle di una CFT euclidea?**

---

## 🧠 L'idea principale: la funzione d'onda come partizione CFT

La **funzione d'onda di Hartle-Hawking** `Ψ[φ₀]` descrive lo stato quantistico dell'universo
su ℐ⁺, dove `φ₀` è il valore dei campi al bordo futuro.

L'intuizione fondamentale del paper è:

```
Ψ[φ₀] ≈ Z_CFT[φ₀]
```

cioè la funzione d'onda cosmologica si comporta come la **funzione di partizione di una CFT
euclidea** deformata da operatori rilevanti. Questo è l'analogo de Sitter del dizionario
AdS/CFT standard.

---

## 📐 Le isometrie di de Sitter come vincoli

Lo spazio de Sitter dS₄ ha gruppo di isometria **SO(1,4)**, lo stesso del gruppo conforme
in tre dimensioni euclidee. Questa non è una coincidenza: è il nucleo della dS/CFT.

Le isometrie di dS agiscono su ℐ⁺ come trasformazioni conformi. Quindi i **correlatori
cosmologici** (cioè le funzioni di correlazione dei campi su ℐ⁺) devono soddisfare
le stesse **identità di Ward conformi** di una CFT 3D.

Il paper usa queste identità come **equazioni di bootstrap** per determinare la struttura
analitica dei correlatori senza calcolare i Feynman diagram.

---

## 🔬 I risultati principali

1. **Bootstrap equations per la funzione d'onda**: le isometrie di dS determinano
   equazioni funzionali per i correlatori cosmologici che li vincolano fortemente.

2. **Struttura analitica**: i correlatori hanno poli e tagli in piani complessi specifici,
   con posizioni determinate dalla simmetria. Questo è analogo ai blocchi conformi nelle CFT.

3. **Versione precisa della congettura dS/CFT**: la wavefunction di Hartle-Hawking è duale
   a una CFT euclidea **deformata da operatori rilevanti** — il che spiega perché dS/CFT
   è più complicata di AdS/CFT (dove la deformazione è assente o marginale).

4. **Calcolo dei correlatori a 3 punti**: confermano i risultati della teoria perturbativa
   bulk, dando fiducia nel metodo.

---

## 🌍 Perché è importante

- **Cosmologia inflazionaria**: i correlatori cosmologici sono (in linea di principio)
  osservabili nei pattern del CMB (fondo cosmico a microonde) e nella distribuzione
  delle galassie. Un bootstrap potente potrebbe predirli da soli principi.

- **Paradosso dell'unitarietà in dS**: de Sitter ha un orizzonte termico a temperatura
  `T_dS = H/(2π)`. Un duale CFT ben definito aiuterebbe a capire se l'evoluzione è unitaria.

- **Inflazione eterna**: molti modelli inflazionari predicono un multiverso. La dS/CFT
  potrebbe dare un senso preciso a questo concetto.

---

## 📚 Connessioni con gli altri paper nell'archivio

| Paper | Collegamento |
|---|---|
| [2401.05128](../2024-01-13/2401.05128.md) — Isole in AdS₂ | Entrambi usano idee olografiche per problemi cosmologici; le isole potrebbero avere un analogo in dS |
| [2401.09675](../2024-01-15/2401.09675.md) — Celestial holography | Approccio bootstrap simile, ma per lo spazio piatto invece di dS |

---

## ❓ Domande per approfondire (con Copilot Chat)

- *"Cos'è la funzione d'onda di Hartle-Hawking e come si calcola?"*
- *"Perché lo spazio de Sitter ha un orizzonte termico? Qual è la temperatura associata?"*
- *"Cosa sono i 'conformal blocks' e come appaiono nel bootstrap?"*
- *"Qual è la differenza tra deformazione rilevante, marginale e irrilevante in una CFT?"*
""",

    # ------------------------------------------------------------------
    "2401.07962": """\
## 🎯 Di cosa parla, in breve

Questo paper è un articolo di Strominger che spiega uno dei risultati più eleganti
della fisica teorica moderna: il **teorema soft dei gravitoni** di Weinberg (1965)
è in realtà l'**identità di Ward della simmetria BMS di supertraslazione**.

In altre parole, una formula scoperta negli anni '60 per ragioni pratiche (calcolare
i processi con gravitoni a bassa energia) è in realtà il riflesso di una **profonda simmetria
dello spazio-tempo** che nessuno aveva capito prima.

---

## 🔍 Il problema che questo paper vuole risolvere

Nella fisica delle particelle, le **ampiezze di scattering** che coinvolgono gravitoni
a energia molto bassa (gravitoni "soft") hanno un comportamento universale:

```
M(p₁,...,pₙ, q) → [S⁽⁰⁾ + S⁽¹⁾ + ...] · M(p₁,...,pₙ)    quando q → 0
```

dove `S⁽⁰⁾` è il **fattore soft di Weinberg** — una somma di termini che dipendono solo
dalle masse e dai momenti delle particelle dure. Questo era noto da decenni ma sembrava
una proprietà tecnica delle ampiezze, senza un'interpretazione profonda.

Il paper risponde alla domanda: **perché esiste questo comportamento universale?**

---

## 🧠 L'idea principale: il triangolo infrarosso

Strominger identifica tre fenomeni che sembrano indipendenti ma sono in realtà equivalenti —
i tre vertici di un **triangolo**:

```
        Soft theorems
           /      \\
          /        \\
Simmetrie asintotiche — Effetti di memoria
```

| Vertice | Cosa descrive |
|---|---|
| **Soft theorem** | Comportamento delle ampiezze con particelle a energia → 0 |
| **Simmetria asintotica BMS** | Simmetrie dello spazio-tempo a grande distanza da tutte le sorgenti |
| **Effetto di memoria** | Spostamento permanente di rivelatori liberi dopo il passaggio di un'onda gravitazionale |

Questi tre vertici sono collegati da mappe precise. Capirne uno significa capire tutti e tre.

---

## 📐 La simmetria BMS spiegata

Il gruppo **BMS** (Bondi-Metzner-Sachs) è il gruppo di simmetria dello spazio-tempo piatto
nel limite in cui ci si allontana da tutte le sorgenti (infinito nullo `ℐ⁺`).

A differenza di quanto si potrebbe pensare (solo le isometrie di Poincaré), il gruppo BMS
è **infinito-dimensionale**: contiene

- Le 10 isometrie di Poincaré ordinarie (traslazioni + rotazioni + boost)
- Le **supertraslazioni**: traslazioni spazio-temporali con un parametro `f(z,z̄)` che dipende
  dalla direzione angolare. Ci sono ∞ supertraslazioni, una per ogni funzione sulla sfera.

Formalmente, la supertraslazione con parametro `f` agisce come:
```
u → u + f(z, z̄)
```
dove `u` è il tempo ritardato e `(z, z̄)` è la direzione angolare.

---

## 🔬 Il risultato centrale: Weinberg = Ward di BMS

Il paper dimostra che:

**Il teorema soft leading di Weinberg è l'identità di Ward della carica associata alla
supertraslazione BMS con parametro `f(z,z̄) = 1/(z-w̄)`.**

In formule:
```
⟨out| Q_f · S - S · Q_f |in⟩ = 0
```
dove `Q_f` è la carica BMS conservata e `S` è la S-matrix. Espandendo questa equazione
si ottiene esattamente il soft graviton theorem.

Questo trasforma il soft theorem da **curiosità tecnica** a **legge di conservazione**.

---

## ➡️ Estensioni: soft sub-leading e superrotazioni

Il paper estende l'analisi al termine **sub-leading** `S⁽¹⁾` (il "subleading soft graviton theorem"
di Cachazo-He e Low). Questo termine corrisponde all'identità di Ward delle **superrotazioni**
— trasformazioni conformi sulla sfera celeste che generalizzano le supertraslazioni.

Le superrotazioni sono generate da campi vettoriali conformi `Y^z ∂_z` sulla sfera e
includono la simmetria di Virasoro 2D come sottogruppo.

---

## 🌍 Perché è importante

1. **Nuova prospettiva sul paradosso dell'informazione**: se la S-matrix è vincolata da
   infinite simmetrie BMS, forse l'informazione non può davvero perdersi nei buchi neri.

2. **Unificazione di tre aree**: soft physics, simmetrie dello spazio-tempo e onde gravitazionali
   sembravano separate; il triangolo le unifica.

3. **Fondamento dell'olografia celestiale**: le simmetrie BMS di questo paper sono
   esattamente il gruppo di simmetria della CCFT del paper 2401.09675.

4. **Memoria gravitazionale misurabile**: gli interferometri come LIGO potrebbero in principio
   misurare l'effetto di memoria — e quindi "vedere" le simmetrie BMS.

---

## 📚 Connessioni con gli altri paper nell'archivio

| Paper | Collegamento |
|---|---|
| [2401.09675](../2024-01-15/2401.09675.md) — Celestial holography | Costruisce la CCFT usando le stesse simmetrie BMS di questo paper |
| [2401.06543](../2024-01-14/2401.06543.md) — Flat space holography | Studia le stesse simmetrie BMS ma all'infinito spaziale invece che nullo |

---

## ❓ Domande per approfondire (con Copilot Chat)

Apri questo file in GitHub e prova questi prompt:

- *"Spiega in parole semplici cos'è l'effetto di memoria gravitazionale e come si misurerebbe."*
- *"Cos'è un'identità di Ward? Come deriva dalla conservazione di una carica di Noether?"*
- *"Qual è la differenza tra il gruppo di Poincaré e il gruppo BMS?"*
- *"Perché le supertraslazioni formano un gruppo normale nel BMS?"*
""",

    # ------------------------------------------------------------------
    "2401.06543": """\
## 🎯 Di cosa parla, in breve

Questo paper studia le **simmetrie asintotiche dello spazio-tempo piatto all'infinito spaziale** —
cioè cosa succede alla geometria quando ci si allontana da tutte le sorgenti non nel tempo
(come nel caso dell'infinito nullo `ℐ⁺`, dove arrivano le onde gravitazionali),
ma nello **spazio** (il limite `r → ∞` a `t` costante).

Il risultato principale è che il **gruppo BMS all'infinito spaziale** (chiamato `i⁰`) è
**isomorfo** al gruppo BMS all'infinito nullo. Questo stabilisce un ponte tra due
descrizioni complementari della fisica asintotica, rafforzando le basi dell'olografia
in spazio piatto.

---

## 🔍 Il problema che questo paper vuole risolvere

In spazio piatto, ci sono diversi "bordi" dell'universo:

| Regione | Simbolo | Descrive |
|---|---|---|
| Infinito nullo futuro | `ℐ⁺` | Dove arrivano fotoni/gravitoni |
| Infinito nullo passato | `ℐ⁻` | Da dove partono fotoni/gravitoni |
| Infinito spaziale | `i⁰` | Limite a grandi distanze spaziali |
| Infinito temporale futuro/passato | `i±` | Fine/inizio del tempo |

L'infinito nullo `ℐ⁺` è ben studiato: il gruppo BMS che agisce su `ℐ⁺` è alla base
dei soft theorems e dell'olografia celestiale. Ma cosa succede a `i⁰`?

Il problema è tecnico ma importante: i campi gravitazionali all'infinito spaziale hanno
**struttura conica** (singolari lungo le direzioni a `ℐ`). Gestire queste singolarità
correttamente è il cuore del paper.

---

## 🧠 L'idea principale: collimare ℐ con i⁰

I lavori precedenti di Ashtekar e Romano avevano definito una versione "smussata"
dell'infinito spaziale che evita le singolarità. I due autori (Geiller e Zwikel)
costruiscono su questo fondamento e:

1. **Definiscono il gruppo BMS a `i⁰`** con una procedura sistematica
2. **Calcolano le cariche BMS** (le quantità conservate associate alle simmetrie)
3. **Dimostrano l'isomorfismo** tra il gruppo BMS a `i⁰` e quello a `ℐ⁺`

L'isomorfismo significa che le **stesse simmetrie** governano sia il comportamento
spaziale asintotico che quello nullo — sono due facce della stessa medaglia.

---

## 📐 Cariche e flussi BMS

Per ogni simmetria continua c'è una **carica conservata** (teorema di Noether).
Per il BMS, le cariche sono:

```
Q_f = ∫_{S²} f · m  dΩ     (carica di supertraslazione)
```

dove `f(z,z̄)` è il parametro della supertraslazione e `m` è la **massa di Bondi** —
una funzione sulla sfera che misura la distribuzione angolare della massa-energia.

I **flussi** misurano come queste cariche cambiano nel tempo quando passano onde
gravitazionali. L'equazione di bilancio carica-flusso è:

```
Q_f(ℐ⁺) - Q_f(ℐ⁻) = Flusso attraverso ℐ
```

Il paper calcola le versioni di queste quantità all'infinito spaziale e verifica
che coincidono con quelle all'infinito nullo.

---

## 🔬 La struttura simplettica

Un risultato tecnico importante: la **struttura simplettica** (la "geometria dello spazio
delle fasi" del campo gravitazionale) è **ben definita** all'infinito spaziale, senza
divergenze o ambiguità.

Questo è un prerequisito necessario per poter definire:
- Una teoria quantistica dell'olografia in spazio piatto
- Un calcolo coerente delle cariche e delle loro algebre di Poisson

---

## 🌍 Perché è importante

1. **Completezza del programma olografico in spazio piatto**: per avere un duale olografico
   completo, servono tutte le regioni asintotiche — questo paper riempie il pezzo `i⁰`.

2. **Matching con la S-matrix**: le cariche a `i⁰` devono coincidere con quelle a `ℐ±`
   per garantire la conservazione globale — questo paper lo verifica.

3. **Fondamento per la quantizzazione**: senza una struttura simplettica ben definita,
   non si può quantizzare il sistema e definire la CCFT duale.

---

## 📚 Connessioni con gli altri paper nell'archivio

| Paper | Collegamento |
|---|---|
| [2401.07962](./2401.07962.md) — BMS e soft theorems | Le stesse cariche BMS di questo paper danno i soft theorems |
| [2401.09675](../2024-01-15/2401.09675.md) — Celestial holography | Usa le simmetrie BMS come gruppo di simmetria della CCFT |

---

## ❓ Domande per approfondire (con Copilot Chat)

- *"Cos'è la massa di Bondi e come si misura? È diversa dalla massa ADM?"*
- *"Spiega il diagramma di Penrose dello spazio di Minkowski e indica dove sono ℐ⁺, i⁰, i±."*
- *"Cos'è una struttura simplettica e perché è importante per la meccanica hamiltoniana?"*
- *"Perché ci sono problemi con le singolarità all'infinito spaziale che non ci sono a ℐ?"*
""",

    # ------------------------------------------------------------------
    "2401.05128": """\
## 🎯 Di cosa parla, in breve

Questo paper risolve il **paradosso dell'informazione dei buchi neri** in un modello
semplificato: un buco nero in AdS₂ (AdS bidimensionale) accoppiato a un bagno esterno.

Il risultato principale è che l'**entropia di entanglement** della radiazione di Hawking
segue la **curva di Page** — cioè cresce, raggiunge un massimo a metà dell'evaporazione,
poi scende — risolvendo il paradosso. Il meccanismo chiave sono le **isole**:
regioni spaziali nel buco nero che contribuiscono all'entropia del sistema esterno.

---

## 🔍 Il problema che questo paper vuole risolvere

Quando un buco nero evapora emettendo radiazione di Hawking:

- Se la radiazione è **puramente termica** (come suggerisce il calcolo semiclassico),
  l'entropia aumenta indefinitamente. Alla fine dell'evaporazione si ha più entropia
  di quanta ce ne fosse all'inizio — violando il **secondo principio** e l'**unitarietà**.

- Se invece l'evoluzione è unitaria (come richiede la meccanica quantistica),
  l'entropia della radiazione deve prima crescere e poi **decrescere**, seguendo la curva di Page.

Il **paradosso** è che il calcolo semiclassico standard dà sempre la risposta sbagliata
(l'entropia cresce senza sosta). Dove sbaglia?

---

## 🧠 L'idea principale: le isole

La risposta del paper è che il calcolo semiclassico standard usa la formula sbagliata
per l'entropia. La formula corretta è la **formula delle isole**:

```
S_rad = min_X [ (Area(X))/(4Gₙ) + S_QFT(Rad ∪ Island(X)) ]
```

dove:
- `X` è la superficie di estremizzazione quantistica (quantum extremal surface)
- `Island(X)` è la regione tra `X` e il centro del buco nero — **l'isola**
- `S_QFT` è l'entropia della QFT nei campi di materia

L'isola è una regione nel **buco nero** che, paradossalmente, deve essere inclusa
nel calcolo dell'entropia del **sistema esterno**. È questa inclusione che "corregge"
l'errore semiclassico.

---

## 📐 Il modello: Jackiw-Teitelboim + bagno

Il modello è costruito in due strati:

**Gravità**: il modello di **Jackiw-Teitelboim (JT)** in 1+1 dimensioni:
```
S = [1/(16πGₙ)] ∫ φ(R + 2) √g d²x + topologico
```
dove `φ` è il dilatone (un campo scalare che gioca il ruolo del "raggio effettivo").
Questo è esattamente il modello della gola di un buco nero in AdS₂.

**Bagno**: il sistema di gravità è accoppiato a una teoria di campo conforme (CFT) in
1+1 dimensioni che non ha gravità — il "bagno" che raccoglie la radiazione di Hawking.

In questo setup si può calcolare esattamente l'entropia della radiazione nel bagno.

---

## 🔬 I risultati: la curva di Page

Calcolando l'entropia con la formula delle isole:

- **Prima della scrambling time**: non esiste un'isola che minimizza la formula.
  L'entropia cresce come la formula semiclassica (legge di Hawking).

- **Dopo la scrambling time**: appare un'isola che minimizza l'entropia. L'entropia
  della radiazione smette di crescere e rimane sotto il limite di unitarietà (entropia di Bekenstein-Hawking).

- **Al termine dell'evaporazione**: l'entropia della radiazione ritorna a zero — il buco nero
  si è evaporato completamente e tutta l'informazione è nella radiazione.

Questo è esattamente la **curva di Page**: il paradosso è risolto.

---

## ⚛️ Il metodo: repliche gravitazionali

Il paper calcola l'entropia usando il **replica trick** gravitazionale:

```
S = -∂ₙ Tr[ρⁿ]|_{n=1}
```

Invece di calcolare l'entropia direttamente, si calcola `Tr[ρⁿ]` per `n` intero
(facendo n copie del sistema) e poi si fa la continuazione analitica a `n → 1`.

La novità: in presenza di gravità, le **geometrie del buco nero** si possono "connettere"
in modi non-perturbativi tra le copie. Queste geometrie a forma di sella si chiamano
**wormholes di replica** e danno il contributo dominante all'entropia nell'era tardiva.

---

## 🌍 Perché è importante

1. **Risoluzione del paradosso dell'informazione**: per la prima volta, si vede
   esplicitamente (in un modello risolvibile) che l'informazione non si perde.

2. **Gravità non-perturbativa**: i wormholes di replica sono effetti non-perturbativi
   in `Gₙ`. Questo suggerisce che la gravità quantistica ha sorprese fondamentali
   nei processi di evaporazione.

3. **Nascita del programma delle "isole"**: dopo questo paper, si sono trovate
   isole in buchi neri in AdS₄, in buchi neri eterni, in modelli FRW.
   Il programma è molto attivo.

4. **Connessione ER=EPR**: le isole suggeriscono che l'entanglement tra buco nero
   e radiazione è sostenuto da wormholes geometrici — consistente con la congettura ER=EPR
   di Maldacena e Susskind.

---

## 📚 Connessioni con gli altri paper nell'archivio

| Paper | Collegamento |
|---|---|
| [2401.08441](../2024-01-15/2401.08441.md) — dS/CFT bootstrap | Entrambi usano l'olografia per affrontare il problema dell'unitarietà cosmologica |
| [2401.07962](./2401.07962.md) — BMS e soft theorems | Le simmetrie BMS potrebbero vincolare la S-matrix del buco nero evaporante |

---

## ❓ Domande per approfondire (con Copilot Chat)

- *"Cos'è la curva di Page? Quando fu proposta e cosa implica per l'unitarietà?"*
- *"Spiega il replica trick per il calcolo dell'entropia di entanglement."*
- *"Cos'è il modello Jackiw-Teitelboim e perché è un buon modello di buco nero?"*
- *"Come si collega la formula delle isole alla formula di Ryu-Takayanagi?"*
- *"Cos'è uno wormhole di replica? È fisicamente reale?"*
""",
}

# ---------------------------------------------------------------------------
# Parsing del file Markdown del paper
# ---------------------------------------------------------------------------


def parse_paper_md(filepath: Path) -> dict:
    """Estrae i metadati da un file paper Markdown generato da fetch_papers.py."""
    text = filepath.read_text(encoding="utf-8")
    lines = text.splitlines()

    title = ""
    authors = ""
    published = ""
    categories = ""
    link = ""
    abstract = ""

    # Titolo: prima riga H1
    for line in lines:
        if line.startswith("# "):
            title = line[2:].strip()
            break

    # Campi bold
    for line in lines:
        if line.startswith("**Autori:**"):
            authors = line.replace("**Autori:**", "").strip()
        elif line.startswith("**Pubblicato:**"):
            published = line.replace("**Pubblicato:**", "").strip()
        elif line.startswith("**Categorie arXiv:**"):
            categories = line.replace("**Categorie arXiv:**", "").strip()
        elif line.startswith("**Link:**"):
            m = re.search(r"https://arxiv\.org/abs/[\w./\-]+", line)
            link = m.group(0) if m else ""

    # Abstract: testo tra "## Abstract" e "---" o prossimo heading
    in_abstract = False
    abstract_lines = []
    for line in lines:
        if line.strip() == "## Abstract":
            in_abstract = True
            continue
        if in_abstract:
            if line.startswith("---") or line.startswith("## "):
                break
            abstract_lines.append(line)
    abstract = " ".join(l.strip() for l in abstract_lines if l.strip())

    # arXiv ID dal link
    arxiv_id = ""
    if link:
        m = re.search(r"abs/([\w./\-]+)$", link)
        arxiv_id = m.group(1) if m else ""

    return {
        "title": title,
        "authors": authors,
        "published": published,
        "categories": categories,
        "link": link,
        "arxiv_id": arxiv_id,
        "abstract": abstract,
    }


# ---------------------------------------------------------------------------
# Generazione della spiegazione
# ---------------------------------------------------------------------------

_TEMPLATE_EXPLANATION = """\
## 🎯 Di cosa parla, in breve

> *Spiegazione automatica basata sull'abstract. Per una spiegazione personalizzata,
> apri questo file in GitHub e usa Copilot Chat con il prompt:*
> *"Spiegami in italiano, passo per passo, cosa dimostra questo paper e perché è importante."*

---

## 📄 Abstract analizzato

{abstract}

---

## 🔍 Punti chiave estratti dall'abstract

{bullet_points}

---

## 🧠 Come approcciare questo paper

1. Leggi l'**introduzione** completa del paper su arXiv — di solito è la parte più accessibile
   e riassume tutto ciò che segue.
2. Vai alle **conclusioni** subito dopo: capisci dove si arriva prima di immergerti nei dettagli.
3. Torna alle **sezioni tecniche** solo per i punti che ti interessano davvero.

---

## ❓ Domande da usare con Copilot Chat

Apri questo file in GitHub e prova:

- *"Qual è il problema principale affrontato da questo paper?"*
- *"Spiega i risultati principali di questo paper in termini semplici."*
- *"Quali tecniche matematiche usano gli autori? Sono alla mia portata?"*
- *"Come si collega questo paper agli altri nell'archivio?"*
"""


def _abstract_to_bullets(abstract: str) -> str:
    """Genera un elenco puntato elementare dividendo l'abstract in frasi."""
    sentences = re.split(r"(?<=[.!?])\s+", abstract.strip())
    bullets = []
    for s in sentences[:6]:  # max 6 punti
        s = s.strip()
        if len(s) > 20:
            bullets.append(f"- {s}")
    return "\n".join(bullets) if bullets else "- (vedi abstract sopra)"


def generate_explanation(meta: dict) -> str:
    """Genera il testo Markdown completo della spiegazione."""
    arxiv_id = meta["arxiv_id"]
    title = meta["title"]
    authors = meta["authors"]
    published = meta["published"]
    link = meta["link"]

    # Intestazione comune
    header = f"""# 📖 Spiegazione: {title}

**Autori:** {authors}  
**Pubblicato:** {published}  
**Link arXiv:** [{link}]({link})

---

"""

    # Corpo: pre-baked se disponibile, altrimenti template
    if arxiv_id in _EXPLANATIONS:
        body = _EXPLANATIONS[arxiv_id]
    else:
        body = _TEMPLATE_EXPLANATION.format(
            abstract=meta["abstract"],
            bullet_points=_abstract_to_bullets(meta["abstract"]),
        )

    return header + body


def write_explanation(paper_path: Path) -> Path:
    """Legge un paper .md e scrive il file *_SPIEGAZIONE.md accanto."""
    meta = parse_paper_md(paper_path)
    content = generate_explanation(meta)

    out_path = paper_path.with_name(paper_path.stem + "_SPIEGAZIONE.md")
    out_path.write_text(content, encoding="utf-8")
    return out_path


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def _collect_all_papers() -> list[Path]:
    """Raccoglie tutti i file paper .md (esclude GLOSSARIO, latest, *_SPIEGAZIONE)."""
    papers = []
    for child in sorted(PAPERS_DIR.iterdir()):
        if child.is_dir() and re.match(r"\d{4}-\d{2}-\d{2}", child.name):
            for md in sorted(child.glob("*.md")):
                if "_SPIEGAZIONE" not in md.name:
                    papers.append(md)
    return papers


def _find_latest_paper() -> Path | None:
    """Restituisce il paper più recente (data directory più alta, file più recente)."""
    papers = _collect_all_papers()
    return papers[-1] if papers else None


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Genera una spiegazione in italiano di un paper arXiv."
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "paper",
        nargs="?",
        metavar="PAPER.md",
        help="Percorso del file Markdown del paper da spiegare.",
    )
    group.add_argument(
        "--latest",
        action="store_true",
        help="Spiega il paper più recente nell'archivio.",
    )
    group.add_argument(
        "--all",
        action="store_true",
        help="Spiega tutti i paper nell'archivio.",
    )
    group.add_argument(
        "--list",
        action="store_true",
        help="Elenca i paper disponibili nell'archivio.",
    )
    args = parser.parse_args()

    if args.list:
        papers = _collect_all_papers()
        if not papers:
            print("Nessun paper trovato in papers/. Esegui prima fetch_papers.py.")
            sys.exit(0)
        print(f"📚 {len(papers)} paper nell'archivio:\n")
        for p in papers:
            has_spiegazione = p.with_name(p.stem + "_SPIEGAZIONE.md").exists()
            tag = " ✅ spiegazione disponibile" if has_spiegazione else ""
            print(f"  {p.relative_to(Path.cwd()) if Path.cwd() in p.parents else p}{tag}")
        return

    if args.all:
        papers = _collect_all_papers()
        if not papers:
            print("Nessun paper trovato. Esegui prima fetch_papers.py.")
            sys.exit(1)
        for p in papers:
            out = write_explanation(p)
            print(f"✅ Spiegazione generata: {out}")
        return

    if args.latest:
        paper_path = _find_latest_paper()
        if paper_path is None:
            print("Nessun paper trovato. Esegui prima fetch_papers.py.")
            sys.exit(1)
    elif args.paper:
        paper_path = Path(args.paper)
        if not paper_path.exists():
            print(f"❌ File non trovato: {args.paper}")
            sys.exit(1)
    else:
        # Comportamento di default: spiega il paper più recente
        paper_path = _find_latest_paper()
        if paper_path is None:
            print("Nessun paper trovato. Esegui prima fetch_papers.py.")
            sys.exit(1)
        print(f"ℹ️  Nessun paper specificato. Uso il più recente: {paper_path.name}\n")

    out = write_explanation(paper_path)
    print(f"✅ Spiegazione generata: {out}")
    print(f"\n💡 Apri il file in GitHub e usa Copilot Chat per approfondire ulteriormente.")


if __name__ == "__main__":
    main()
