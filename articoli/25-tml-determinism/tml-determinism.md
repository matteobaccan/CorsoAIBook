---
tags: ["Research", "Generative AI", "Training", "Startups"]
date: 2025-09-15
author: Dario Ferrero
---

# LLM: Domanda uguale, risposta diversa? Forse colpa delle GPU
![tml.jpg](tml.jpg)

*Immaginate di avere un cuoco stellato che, ogni volta che gli chiedete la ricetta della carbonara, vi risponde con sfumature diverse. Oggi aggiunge il guanciale per primo, domani le uova, dopodomani cambia l'ordine della pasta. Il risultato finale è sempre carbonara, ma mai esattamente la stessa. Questo è esattamente ciò che accade con i Large Language Model: stesso input, output diversi. Sempre.*

È un fenomeno che chiunque abbia mai chattato con ChatGPT conosce bene, ma che fino ad oggi veniva liquidato come una caratteristica intrinseca dell'intelligenza artificiale. "È normale", dicevano gli esperti, "fa parte del processo di sampling". Come se fosse inevitabile che un sistema matematico deterministico producesse risultati casuali.

[Thinking Machines Lab](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/), la startup guidata da veterani dell'IA che ha recentemente attirato investimenti significativi, ha deciso di non accontentarsi di questa spiegazione. Il loro ultimo paper, pubblicato a settembre 2025, non si limita a identificare il problema: lo risolve. E la soluzione è tanto elegante quanto inaspettata.

## Quando i Numeri Diventano Anarchici

Per capire il cuore del problema, dobbiamo fare un salto nella matematica dei computer. Come in "Ricomincio da capo", il film dove Bill Murray rivive infinite volte lo stesso giorno con variazioni impercettibili, anche i computer sembrano condannati a ripetere gli stessi calcoli ottenendo risultati leggermente diversi. Ma stavolta non c'è una lezione esistenziale dietro: c'è la fisica dei processori.

Il colpevole principale si chiama "non-associatività dei numeri in virgola mobile". In matematica, (a+b)+c dovrebbe sempre essere uguale a a+(b+c). Sui computer, invece, questa regola salta allegramente fuori dalla finestra. È come se ogni volta che fate un conto, l'ordine in cui sommate i numeri cambiasse il risultato finale. 

Horace He, il ricercatore principale di Thinking Machines Lab, spiega nel paper che [questo fenomeno deriva dal modo in cui i processori gestiscono numeri molto grandi e molto piccoli insieme](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/). È un po' come cercare di fare una media tra il numero di abitanti di Roma e il peso di un granello di sabbia: la precisione limitata dei computer fa sì che alcuni dettagli vadano inevitabilmente persi.

## L'Anatomia dell'Errore: Dentro i Tre Pilastri dell'Indeterminismo

Per comprendere appieno la portata della soluzione di Thinking Machines Lab, è necessario entrare nel cuore pulsante di un transformer. Come un orologiaio che smonta un Patek Philippe per capire perché perde qualche secondo al giorno, i ricercatori hanno dovuto sezionare ogni componente critico del modello per identificare dove nasceva l'indeterminismo.

L'architettura di un Large Language Model moderno poggia su tre pilastri fondamentali, ognuno dei quali contribuisce al problema in modo diverso. È come un'orchestra da camera dove ogni sezione ha le sue peculiarità: i violini (RMSNorm) creano dissonanze sottili, gli ottoni (moltiplicazioni matriciali) amplificano gli errori, e i fiati (attention mechanism) trasformano piccole variazioni in cambiamenti drammatici nell'armonia finale.

Il RMSNorm, acronimo di Root Mean Square Normalization, è forse il componente più semplice da comprendere e paradossalmente il più facile da correggere. [La sua funzione è normalizzare i valori di input per stabilizzare l'addestramento](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/), un po' come un equalizzatore che mantiene il volume costante indipendentemente dall'intensità della fonte. Il problema sorge quando il "batch size" (il numero di richieste elaborate contemporaneamente) è troppo piccolo.

Immaginate un direttore d'orchestra che deve dirigere a volte 100 musicisti, a volte solo 10. Con 100 musicisti, può assegnare un ruolo specifico a ogni sezione e mantenere un controllo preciso. Con solo 10, deve chiedere ad alcuni di raddoppiare gli strumenti, cambiando inevitabilmente la dinamica dell'esecuzione. Il RMSNorm si comporta allo stesso modo: quando ci sono poche richieste da elaborare, è costretto a cambiare strategia di parallelizzazione, introducendo variazioni nei calcoli.

La soluzione di Thinking Machines Lab è tanto semplice quanto radicale: ignorare i casi problematici. Quando il batch size è troppo piccolo per garantire parallelizzazione ottimale, il sistema accetta una perdita di performance pur di mantenere la consistenza. È una scelta filosofica profonda: meglio essere sempre coerenti che occasionalmente veloci.

Le moltiplicazioni matriciali rappresentano una sfida di complessità superiore. Qui non si tratta solo di parallelizzare un calcolo, ma di sfruttare al meglio le "tensor core", unità di calcolo specializzate presenti nelle GPU moderne che possono eseguire migliaia di operazioni simultanee. È come passare dall'uso di un pianoforte tradizionale a un organo da chiesa con centinaia di registri: la potenza è immensa, ma la complessità di controllo cresce esponenzialmente.

Il problema nasce quando le dimensioni delle matrici sono troppo piccole per sfruttare appieno queste unità specializzate. In questi casi, i driver GPU ricorrono a strategie alternative chiamate "Split-K", dove la moltiplicazione viene spezzettata lungo la dimensione di riduzione invece che lungo le dimensioni di output. [È una tecnica brillante per ottimizzare le performance, ma introduce variabilità nei risultati](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/) perché cambia l'ordine delle operazioni matematiche.

La soluzione adottata da Thinking Machines Lab è apparentemente contro-intuitiva: utilizzare sempre la stessa configurazione kernel, indipendentemente dalle dimensioni delle matrici. È come decidere di suonare sempre con la stessa formazione orchestrale, anche quando il pezzo musicale non lo richiede. Si perde qualcosa in efficienza, ma si guadagna in predicibilità.

Il terzo pilastro, l'attention mechanism, è quello che presenta le sfide maggiori. Non a caso, l'attention è il cuore dell'architettura transformer, il componente che permette al modello di "prestare attenzione" a parti diverse dell'input per generare ogni singola parola. È come un regista che deve decidere su quali attori puntare la camera in ogni momento della scena, basandosi su tutto quello che è successo prima.

Il meccanismo di attention introduce due livelli aggiuntivi di complessità. Prima di tutto, deve gestire riduzioni sia lungo la dimensione delle feature che lungo la dimensione della sequenza, creando un intreccio di dipendenze che rende quasi impossibile mantenere un ordine di calcolo fisso. Secondo, deve interfacciarsi con tutte le ottimizzazioni moderne dell'inferenza: chunked prefill (dove le sequenze lunghe vengono elaborate a pezzi), prefix caching (dove parti comuni delle conversazioni vengono riutilizzate), e decoding parallelo.

[Il problema più insidioso emerge nel cosiddetto "decode stage"](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/), quando il modello genera una parola alla volta. In questa fase, la lunghezza della query è tipicamente molto piccola (spesso solo un token), ma la cache delle chiavi e valori può essere enorme (migliaia di token di contesto precedente). È come chiedere a un cantante solista di esibirsi accompagnato da un'orchestra sinfonica: il rapporto di forze è completamente sbilanciato.

Per mantenere performance accettabili, i sistemi ricorrono a tecniche chiamate "Split-KV" o "FlashDecoding", che parallelizzano l'elaborazione lungo la dimensione della cache. Ma ancora una volta, questa parallelizzazione introduce variabilità nell'ordine dei calcoli. La soluzione di Thinking Machines Lab richiede una modifica profonda di questi algoritmi, adottando una strategia a "dimensione di split fissa" invece che a "numero di split fisso".

È una distinzione sottile ma fondamentale. Invece di dire "dividi sempre in 8 parti", il sistema dice "ogni parte deve essere sempre di 256 elementi". In questo modo, l'ordine delle operazioni rimane identico indipendentemente dalla lunghezza totale della sequenza. È come decidere che ogni musicista deve suonare sempre per esattamente 4 battute, indipendentemente dalla lunghezza del brano.

L'eleganza di questa soluzione sta nella sua universalità: una volta che tutti e tre i pilastri sono stati resi "batch-invariant", l'intero sistema diventa deterministico. Non serve riprogettare l'architettura dei transformer o inventare nuovi algoritmi. Basta garantire che ogni componente si comporti sempre allo stesso modo, indipendentemente dal contesto in cui viene eseguito.
![inference.jpg](inference.jpg)
[Tratto da thinkingmachines.ai](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/)

## L'Invarianza dei Batch: La Chiave Segreta

Ma ecco il colpo di scena degno di un thriller tecnologico: il vero problema non sta nella concorrenza tra processori GPU, come sostenevano le teorie precedenti. È qualcosa di molto più sottile e, paradossalmente, più facile da risolvere.

La scoperta di Thinking Machines Lab è che il comportamento degli LLM cambia a seconda di quante richieste vengono elaborate insieme. È come se il nostro cuoco stellato cambiasse ricetta a seconda di quanti coperti deve preparare contemporaneamente. Stesso piatto, stessi ingredienti, ma il risultato finale dipende dal carico di lavoro del momento.

Questo fenomeno ha un nome tecnico: mancanza di "batch invariance". In parole semplici, significa che elaborare una richiesta da sola o insieme ad altre 100 può produrre risposte diverse per la stessa domanda. [I ricercatori hanno dimostrato questo effetto con esperimenti sorprendenti](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/): chiedendo 1000 volte la stessa domanda su Richard Feynman a un modello Qwen, hanno ottenuto 80 risposte diverse, con la prima divergenza che si manifestava esattamente al 103° token.

La soluzione proposta da Thinking Machines Lab è elegante nella sua semplicità: modificare i "kernel" (i blocchi di calcolo fondamentali) in modo che producano sempre gli stessi risultati, indipendentemente da quante altre operazioni vengono eseguite in parallelo. È come insegnare al nostro cuoco a seguire sempre la stessa sequenza di passaggi, che stia cucinando per uno o per cento.
![batch.jpg](batch.jpg)
[Tratto da thinkingmachines.ai](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/)

## Il Prezzo della Coerenza

Come in ogni storia di innovazione tecnologica, la soluzione comporta dei compromessi. I kernel "batch-invariant" sviluppati dal team sono più lenti di quelli standard. Non di molto, per fortuna: nei test condotti su un server con GPU singola utilizzando il modello Qwen-3-8B, il rallentamento si è attestato intorno al 60% rispetto alla versione ottimizzata, scendendo al 30% con alcune migliorie all'implementazione dell'attention.

Potrebbe sembrare un prezzo alto da pagare, ma considerate le implicazioni. [L'indeterminismo degli LLM non è solo un fastidio estetico](https://dataconomy.com/2025/09/11/tml-defeating-nondeterminism-in-llm-inference/): compromette la riproducibilità scientifica, rende impossibile il debugging accurato e, soprattutto, trasforma quello che dovrebbe essere reinforcement learning "on-policy" in qualcosa di completamente diverso.

È un po' come cercare di addestrare un pilota di Formula 1 su un simulatore che cambia le leggi della fisica ogni volta che si accende. Il pilota impara ad adattarsi alle variazioni, ma non impara davvero a guidare quella macchina specifica.

## La Rivoluzione Silenziosa dell'RL

Qui entra in gioco uno degli aspetti più interessanti della ricerca di Thinking Machines Lab. Il reinforcement learning, la tecnica che sta dietro ai modelli più avanzati come ChatGPT, si basa sull'idea che l'IA impari dalle proprie esperienze. Ma se ogni volta che l'IA "prova" la stessa azione ottiene un risultato leggermente diverso, sta davvero imparando dalla stessa esperienza?

I ricercatori hanno dimostrato che [l'indeterminismo trasforma subdolamente l'apprendimento "on-policy" in "off-policy"](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/), creando una discrepanza tra quello che il modello fa durante l'addestramento e quello che fa quando viene utilizzato. È come se un musicista si esercitasse su un pianoforte scordato per poi suonare su uno accordato: la differenza è sottile ma fondamentale.

Con i kernel deterministici di Thinking Machines Lab, questo problema scompare. Nei loro esperimenti su una configurazione di RL applicata al dataset Bigmath, il team ha ottenuto una divergenza KL perfettamente piatta a zero, indicando una corrispondenza perfetta tra addestramento e inferenza. È il Santo Graal del machine learning: un sistema che si comporta esattamente come è stato addestrato a fare.

## Il Panorama Industriale: Chi Vincerà la Guerra della Riproducibilità

Nel mondo dell'intelligenza artificiale, dove i giganti tecnologici si sfidano a colpi di modelli sempre più grandi e performanti, Thinking Machines Lab ha scelto di combattere una battaglia diversa. Mentre OpenAI, Google e Anthropic si concentrano sulla potenza bruta dei loro sistemi, questo team relativamente piccolo ha deciso di puntare sulla precisione. È la classica storia di Davide contro Golia, ma stavolta la fionda di Davide è la matematica pura.

La startup, fondata da ex-ricercatori di alcune delle aziende più prestigiose del settore, rappresenta un approccio completamente diverso alla ricerca sull'IA. [Non si tratta di creare il modello più grande o più veloce, ma di comprendere fino in fondo come questi sistemi funzionano davvero](https://americanbazaaronline.com/2025/09/11/inside-thinking-machines-lab-muratis-12-billion-ai-startup-tackles-reproducibility-467536/). È un po' come la differenza tra costruire un'auto da corsa sempre più potente e capire perché a volte l'auto va a sinistra quando dovrebbe andare dritto.

Il timing di questa ricerca non è casuale. L'industria dell'IA si trova a un punto di svolta cruciale, dove la corsa alle performance pure sta cedendo il passo a considerazioni più mature su affidabilità, sicurezza e predicibilità. È il momento in cui un settore adolescente inizia a comportarsi da adulto, e la riproducibilità è uno dei primi segnali di questa maturazione.

I settori più critici stanno già alzando la voce. Nel mondo della sanità, dove gli algoritmi di IA vengono sempre più utilizzati per diagnosi e piani di trattamento, l'idea che lo stesso sintomo possa produrre valutazioni diverse è semplicemente inaccettabile. È come avere un termometro che dà temperature diverse ogni volta che lo usate: magari la febbre c'è sempre, ma non sapere se è 38 o 39 gradi fa la differenza tra una tachipirina e una corsa in ospedale.

Il settore finanziario non è da meno. Gli algoritmi di trading automatico e i sistemi di valutazione del rischio devono operare in un mondo dove la reproducibilità non è una preferenza, ma un requisito normativo. [Le autorità di vigilanza stanno iniziando a richiedere che i modelli di IA usati per decisioni creditizie o investimenti producano risultati tracciabili e verificabili](https://dataconomy.com/2025/09/11/tml-defeating-nondeterminism-in-llm-inference/). È impossibile spiegare a un giudice perché lo stesso algoritmo ha dato pareri diversi su due richieste di mutuo identiche.

Anche il mondo della ricerca scientifica sta prendendo coscienza del problema. Quando un paper scientifico afferma di aver ottenuto certi risultati usando un modello di IA, altri ricercatori devono poter replicare esattamente quegli esperimenti. È il fondamento stesso del metodo scientifico, messo in discussione dall'indeterminismo degli LLM. Come se ogni volta che replicate un esperimento di fisica, la gravità fosse leggermente diversa.

Ma le implicazioni vanno ben oltre questi settori ovviamente critici. Pensate all'impatto sull'debugging e lo sviluppo di software. Attualmente, quando un'applicazione basata su IA si comporta in modo inaspettato, gli sviluppatori si trovano in una situazione kafkiana: il bug potrebbe essere nel loro codice, oppure potrebbe essere semplicemente l'ennesima manifestazione dell'indeterminismo del modello. È come cercare di aggiustare un orologio che ogni tanto decide autonomamente di andare più veloce o più lento.

La soluzione di Thinking Machines Lab promette di trasformare questa caccia al fantasma in un processo di debugging normale. Se il modello produce sempre gli stessi output per gli stessi input, ogni comportamento anomalo è necessariamente dovuto a un errore reale, non a una fluttuazione casuale. È la differenza tra essere un detective in un mondo dove le prove cambiano spontaneamente e essere un detective in un mondo dove le prove rimangono coerenti.

L'aspetto più interessante di questa dinamica è che nessuno dei grandi player del settore sembra aver dato priorità a questo problema. OpenAI, Google, Meta e gli altri giganti sono tutti ossessionati dalla corsa alle performance, mentre la questione della riproducibilità è rimasta in secondo piano. È una di quelle situazioni rare nel mondo tech dove una startup può effettivamente battere sul tempo aziende con risorse cento volte superiori, semplicemente perché ha identificato il problema giusto al momento giusto.

Naturalmente, convincere l'industria ad adottare una soluzione che comporta un rallentamento del 30-60% non sarà facile. Nel mondo dell'IA, dove i millisecondi di latenza possono fare la differenza tra il successo e il fallimento di un prodotto, ogni compromesso sulle performance viene visto con sospetto. Ma i segnali di cambiamento ci sono già.

Alcune aziende pioniere stanno iniziando a sperimentare con versioni "deterministiche" dei loro sistemi per applicazioni specifiche. Non sorprende che i primi adottatori siano proprio quelli che operano in settori altamente regolamentati, dove il costo dell'indeterminismo supera largamente il beneficio di qualche millisecondo in meno di latenza.

## Verso un Futuro Deterministico

La vera partita si giocherà quando i kernel batch-invariant di Thinking Machines Lab saranno ottimizzati al punto da ridurre significativamente il gap di performance. A quel punto, la domanda non sarà più "possiamo permetterci di essere deterministici?" ma "possiamo permetterci di non esserlo?".

La soluzione proposta da Thinking Machines Lab non è ancora pronta per la produzione su larga scala. Il codice è disponibile su GitHub come dimostrazione di fattibilità, ma richiede modifiche significative alle pipeline di inferenza esistenti. Tuttavia, le implicazioni sono enormi.

Pensate a un mondo in cui gli LLM producono sempre la stessa risposta alla stessa domanda. Non stiamo parlando di IA meno creative o più rigide, ma di sistemi più affidabili e predicibili. Un assistente virtuale che vi dà sempre lo stesso consiglio medico per lo stesso sintomo. Un sistema di traduzione che non cambia versione del testo ogni volta che lo riavviate. Un modello di analisi finanziaria che produce sempre la stessa valutazione per gli stessi dati.

È interessante notare come questa ricerca si inserisca in un trend più ampio verso quella che potremmo chiamare "IA responsabile". Dopo anni di corsa sfrenata verso modelli sempre più grandi e potenti, l'industria sta iniziando a porsi domande più mature: non solo "cosa possiamo fare?" ma anche "cosa dovremmo fare?" e "come possiamo farlo meglio?".

In questo contesto, Thinking Machines Lab potrebbe trovarsi nella posizione invidiabile di essere arrivata prima degli altri a una consapevolezza che diventerà inevitabile. Come spesso accade nella tecnologia, quello che oggi sembra un requisito di nicchia domani potrebbe diventare lo standard industriale. E chi avrà investito per primo in questa direzione si troverà con un vantaggio competitivo significativo.

L'aspetto più affascinante di questa storia è che la soluzione non richiede rivoluzioni tecnologiche o breakthrough scientifici. È un problema di ingegneria pura, risolto con rigore matematico e attenzione ai dettagli. In un'epoca in cui l'IA sembra sempre più magica e incomprensibile, Thinking Machines Lab ci ricorda che dietro ogni algoritmo intelligente c'è sempre matematica solida e implementazioni precise.

Forse il vero insegnamento di questa ricerca non riguarda tanto gli LLM quanto la maturità di un intero settore. Siamo arrivati al punto in cui non basta più che l'intelligenza artificiale funzioni: deve funzionare in modo prevedibile, tracciabile e riproducibile. È il passaggio dall'arte alla scienza, dall'alchimia alla chimica.

In fondo, chi avrebbe mai pensato che il vero salto evolutivo dell'IA non sarebbe arrivato da modelli più grandi o algoritmi più sofisticati, ma dalla semplice capacità di fare sempre la stessa cosa allo stesso modo? Come nei migliori colpi di scena cinematografici, la risposta era nascosta in bella vista. Bastava avere il coraggio di cercarla.