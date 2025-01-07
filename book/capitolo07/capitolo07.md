## Capitolo 7: Valutazione delle AI

### 7.1 Introduzione

La valutazione delle Intelligenze Artificiali (AI) è un processo cruciale per garantire che i sistemi di AI siano efficaci, affidabili e sicuri. Con l'aumento dell'adozione dell'AI in settori critici come la medicina, la finanza e la sicurezza, è essenziale disporre di metodi robusti per valutare le prestazioni, l'usabilità, l'etica e l'interpretabilità dei modelli di AI. Questo capitolo esplora i principali approcci e strumenti utilizzati per valutare le AI, nonché le sfide e le considerazioni etiche associate a questo processo.

### 7.2 Test di Turing

#### 7.2.1 Cos'è il Test di Turing?

Il **Test di Turing** è stato proposto dal matematico britannico **Alan Turing** nel 1950 come criterio per determinare se una macchina può essere considerata "intelligente". Il test prevede una conversazione tra un giudice umano e due partecipanti, uno umano e uno macchina. Se il giudice non è in grado di distinguere tra i due, la macchina viene considerata intelligente.

#### 7.2.2 Applicazioni del Test di Turing

Il Test di Turing è stato utilizzato come punto di riferimento per valutare la capacità delle macchine di imitare il comportamento umano. Tuttavia, con l'evoluzione dell'AI, il test è stato criticato per la sua semplicità e per il fatto che non misura la vera intelligenza, ma solo la capacità di ingannare un essere umano.

#### 7.2.3 Limiti del Test di Turing

- **Superficialità**: Il test si concentra sull'imitazione del comportamento umano, ma non valuta la comprensione o la consapevolezza.
- **Soggettività**: Il risultato del test dipende dalla percezione del giudice, che può essere influenzata da pregiudizi o aspettative.
- **Mancanza di misurazione della creatività**: Il test non valuta la capacità della macchina di creare nuove idee o soluzioni.

### 7.3 Come valutiamo oggi le AI?

#### 7.3.1 Valutazione delle Prestazioni

La valutazione delle prestazioni è uno dei metodi più comuni per valutare l'AI. Questo approccio si concentra su metriche quantitative, come l'accuratezza, la precisione, il richiamo e l'F1-score, per misurare l'efficacia di un modello in un compito specifico.

**Metriche comuni**:
- **Accuratezza**: La percentuale di previsioni corrette rispetto al totale delle previsioni.
- **Precisione**: La percentuale di previsioni positive corrette rispetto al totale delle previsioni positive.
- **Richiamo**: La percentuale di casi positivi correttamente identificati rispetto al totale dei casi positivi.
- **F1-score**: La media armonica di precisione e richiamo, utile per bilanciare i due metrici.

#### 7.3.2 Valutazione dell'Usabilità

La valutazione dell'usabilità si concentra sulla facilità con cui gli utenti possono interagire con un sistema di AI. Questo include la progettazione dell'interfaccia utente, la chiarezza delle risposte e la capacità del sistema di adattarsi alle esigenze degli utenti.

**Metodi di valutazione**:
- **Test di usabilità**: Gli utenti interagiscono con il sistema mentre gli osservatori registrano problemi e difficoltà.
- **Questionari e sondaggi**: Gli utenti forniscono feedback sulla loro esperienza con il sistema.
- **Analisi delle sessioni**: I dati di interazione vengono analizzati per identificare pattern e aree di miglioramento.

#### 7.3.3 Valutazione dell'Etica

La valutazione dell'etica si concentra sull'impatto sociale e morale dell'AI. Questo include la valutazione del bias algoritmico, della privacy, della sicurezza e dell'impatto sul lavoro.

**Considerazioni etiche**:
- **Bias algoritmico**: Come discusso nel Capitolo 2, i modelli di AI possono perpetuare o amplificare pregiudizi presenti nei dati di addestramento, portando a decisioni discriminatorie.
- **Privacy**: L'AI spesso richiede grandi quantità di dati personali, sollevando preoccupazioni sulla protezione della privacy.
- **Sicurezza**: I sistemi di AI possono essere vulnerabili ad attacchi informatici, come l'avvelenamento dei dati o gli attacchi adversarial. ovvero immagina di mostrare ad un amico una foto di un gatto, ma con un filtro strano che lo fa sembrare un cane. Lui dice "cane", anche se è chiaramente un gatto..
- **Impatto sul lavoro**: L'automazione guidata dall'AI potrebbe portare alla perdita di posti di lavoro in alcuni settori, mentre ne creerà di nuovi in altri.

#### 7.3.4 Valutazione dell'Interpretabilità

La valutazione dell'interpretabilità si concentra sulla capacità di un sistema di AI di spiegare le sue decisioni e il suo funzionamento interno. Questo è particolarmente importante in contesti critici, come la medicina e la finanza, dove è essenziale comprendere come vengono prese le decisioni.

**Metodi di interpretabilità**:
- **Modelli interpretabili**: Utilizzo di modelli semplici e trasparenti, come gli alberi di decisione, che sono più facili da interpretare.
- **Tecniche di spiegazione**: Utilizzo di strumenti come **LIME** (Local Interpretable Model-agnostic Explanations) immagina di avere un modello che classifica immagini: Input: Una foto di un gatto. LIME: Ti mostra che il modello ha guardato le orecchie e il naso per decidere "gatto", e **SHAP** (SHapley Additive exPlanations) per spiegare le previsioni di modelli complessi. Immagina un modello che approva prestiti: Input: Una persona di 30 anni, reddito medio. SHAP: Ti dice che l’età ha contribuito +10%, il reddito -5% al rifiuto).
- **Visualizzazione**: Utilizzo di grafici e diagrammi per rappresentare il funzionamento interno del modello e le sue decisioni.

### 7.4 Nuovi Test e Benchmark

#### 7.4.1 FrontierMath

**FrontierMath** è un benchmark (un punto di riferimento, ovvero uno standard, per misurare le prestazioni di un sistema, modello o tecnologia) sviluppato per testare le capacità di ragionamento matematico dei modelli di AI. Questo benchmark include problemi matematici complessi e originali, progettati per essere particolarmente impegnativi anche per esperti umani. FrontierMath utilizza sistemi di verifica automatizzati per valutare le prestazioni dei modelli in modo efficiente e riproducibile.

**Caratteristiche di FrontierMath**:
- **Difficoltà**: I problemi sono progettati per essere estremamente difficili, richiedendo ore o giorni di lavoro per essere risolti.
- **Originalità**: Tutti i problemi sono nuovi e non pubblicati, eliminando il rischio di contaminazione dei dati.
- **Valutazione Automatizzata**: Utilizza sistemi di verifica automatizzati per valutare le prestazioni dei modelli in modo efficiente.

#### 7.4.2 ARC Benchmark

L'**ARC Benchmark** (AI2 Reasoning Challenge) è stato sviluppato per testare le capacità di ragionamento dei modelli di linguaggio di grandi dimensioni (LLM). Questo benchmark include domande complesse a scelta multipla, progettate per valutare la comprensione profonda del linguaggio e il ragionamento.

**Caratteristiche dell'ARC Benchmark**:
- **Domande Complesse**: Include 7.787 domande a scelta multipla, suddivise in "Easy Set" e "Challenge Set".
- **Integrazione delle Informazioni**: Valuta come i modelli integrano informazioni sparse per rispondere a domande complesse.
- **Scoring**: Ogni risposta corretta guadagna un punto, con punteggi distribuiti equamente in caso di pareggio.

### 7.5 Sfide nella Valutazione delle AI

#### 7.5.1 Bias nei Dati di Addestramento

I modelli di AI possono essere influenzati da bias presenti nei dati di addestramento, portando a decisioni discriminatorie o ingiuste. È essenziale garantire che i dati siano rappresentativi e privi di pregiudizi.

#### 7.5.2 Complessità Computazionale

La valutazione di modelli di AI complessi, come le reti neurali profonde, richiede grandi quantità di risorse computazionali e tempo. Questo può rendere difficile la valutazione su larga scala o in contesti con risorse limitate.

#### 7.5.3 Interpretabilità

I modelli di AI, in particolare quelli basati su deep learning, sono spesso considerati "scatole nere" perché è difficile comprendere come prendono decisioni. Questo solleva preoccupazioni sulla trasparenza e l'affidabilità, specialmente in contesti critici.

#### 7.5.4 Etica e Responsabilità

La valutazione delle AI deve considerare le implicazioni etiche e sociali dell'uso di questa tecnologia. È essenziale garantire che i sistemi di AI siano utilizzati in modo responsabile e che le decisioni siano giustificabili e trasparenti.

### 7.6 Conclusione

La valutazione delle AI è un processo complesso e multidisciplinare che richiede l'integrazione di metodi quantitativi, qualitativi ed etici. Con l'aumento dell'adozione dell'AI in settori critici, è essenziale disporre di strumenti e approcci robusti per garantire che i sistemi di AI siano efficaci, affidabili e sicuri. Mentre continuiamo a sviluppare e implementare nuove tecnologie di AI, è importante bilanciare l'innovazione con la consapevolezza delle implicazioni etiche e sociali, garantendo che questa tecnologia sia utilizzata in modo responsabile e benefico per tutti.
