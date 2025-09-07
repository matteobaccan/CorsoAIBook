---
tags: ["Research", "Training", "Generative AI"]
date: 2025-09-07
author: Dario Ferrero
---

# Rivoluzione DeepConf: più precisione e meno risorse per gli LLM
![aideepconffire.jpg](aideepconffire.jpg)

*Immaginate di essere in un esame di matematica particolarmente difficile. Avete davanti un problema che vi fa sudare freddo, tipo quelli delle Olimpiadi della Matematica che fanno piangere anche i più bravi. La strategia classica? Provare e riprovare, scrivere decine di tentativi diversi sperando che uno sia giusto. Ma c'è un approccio più furbo: capire quando state andando nella direzione sbagliata e fermarvi prima di sprecare tempo ed energie.*

È proprio quello che ha fatto un giovane team di ricercatori di Meta AI, guidato da [Jiawei Zhao](https://jiaweizzhao.github.io/deepconf/), ricercatore presso Meta AI FAIR con una formazione al prestigioso Caltech, insieme ai colleghi [Yichao Fu e Xuewei Wang](https://ai.meta.com/research/publications/deep-think-with-confidence/).

Il loro lavoro, pubblicato su arXiv solo poche settimane fa con il titolo ["Deep Think with Confidence"](https://arxiv.org/abs/2508.15260), rappresenta una di quelle scoperte che sembrano semplici a posteriori ma che in realtà nascondono una complessità tecnica notevole. Come il gesto apparentemente banale di Archimede nella vasca da bagno, anche questa ricerca parte da un'osservazione elementare: se un'intelligenza artificiale sta ragionando male, perché non insegnarle a riconoscerlo da sola?

## Il Problema: Quando "Pensare di Più" Non Basta

Per capire la portata rivoluzionaria di questo approccio, facciamo un passo indietro. I modelli linguistici di grandi dimensioni, quelli che tutti chiamiamo LLM, hanno una caratteristica particolare quando affrontano problemi complessi: più tentativi fanno, migliori diventano le loro risposte. È come se fossero degli studenti particolarmente testardi che continuano a riprovare un esercizio fino a quando non lo azzeccano.

Questo approccio, chiamato tecnicamente "test-time scaling", funziona con una logica apparentemente semplice: se fai generare al modello cinquanta diverse soluzioni a un problema e poi scegli quella più frequente tra tutte, le probabilità di beccare quella giusta aumentano drasticamente. È il principio della "self-consistency with majority voting" (autocoerenza con voto di maggioranza), una strategia che ha funzionato egregiamente per anni.

Ma c'è un problema, anzi due. Il primo è economico: generare decine o centinaia di risposte costa una fortuna in termini di potenza computazionale. È come affittare cinquanta computer per fare lo stesso calcolo sperando che la maggioranza arrivi al risultato giusto. Il secondo problema è più sottile: dopo un certo punto, aggiungere più tentativi non migliora significativamente i risultati. È la classica "legge dei rendimenti decrescenti" che conoscono bene gli economisti, applicata al mondo dell'intelligenza artificiale.

## La Soluzione: Da "Più Forte" a "Più Furbo"

Ed è qui che entra in gioco l'intuizione geniale del team di Meta. Invece di continuare a martellare il problema con la forza bruta computazionale, perché non insegnare al modello a riconoscere quando sta per imboccare una strada sbagliata? È un po' come il radar di prossimità delle auto moderne: invece di aspettare l'impatto, ti avverte prima che tu stia per schiantarti contro un ostacolo.

[DeepConf, questo il nome del nuovo metodo](https://ai.meta.com/research/publications/deep-think-with-confidence/), sfrutta quello che i ricercatori chiamano "segnali di confidenza interni al modello". In parole semplici, ogni volta che un LLM genera una parola o un concetto, ha una sorta di "termometro interno" che indica quanto è sicuro di quella scelta. È come quando rispondete a una domanda a quiz: a volte siete sicuri al 100%, altre volte tentennate tra due opzioni.

La brillantezza di DeepConf sta nel trasformare questo "tentennare" interno in un filtro intelligente. Invece di generare ciecamente centinaia di tentativi e poi contarli uno per uno, il sistema monitora in tempo reale la confidenza del modello e scarta automaticamente i ragionamenti che mostrano segnali di incertezza troppo elevati. È come avere un assistente personale che vi sussurra all'orecchio "forse è meglio se riprovi con un altro approccio" quando vi vede incartarvi su una soluzione sbagliata.

## Come Funziona: I Segreti della Nuova Architettura

Dal punto di vista tecnico, DeepConf lavora su due livelli complementari. Il primo è quello che i ricercatori chiamano "filtering during generation", ovvero il filtraggio durante la generazione. Immaginate di essere Sherlock Holmes che, mentre sta ragionando ad alta voce, si accorge di star seguendo una pista sbagliata e cambia immediatamente direzione. Questo è esattamente quello che fa DeepConf: monitora le probabilità logaritmiche interne del modello token per token e, quando rileva pattern di incertezza, interrompe quella particolare linea di ragionamento e ne avvia una nuova.

Il secondo livello è il "filtering after generation", che funziona più come un editore esperto. Una volta che il modello ha generato diverse soluzioni complete, DeepConf analizza retrospettivamente i segnali di confidenza di ciascuna traccia di ragionamento e assegna loro un punteggio di affidabilità. È come avere un correttore di bozze che non si limita a contare gli errori, ma valuta la coerenza complessiva del ragionamento.

La vera magia, però, sta nella semplicità implementativa. Come sottolineano gli autori nel loro paper, [DeepConf non richiede alcun training aggiuntivo del modello né ottimizzazione di iperparametri](https://arxiv.org/abs/2508.15260). È un approccio "plug-and-play" che può essere integrato nei framework di serving esistenti come vLLM senza modifiche sostanziali all'architettura. È come installare un nuovo software sul vostro computer: non dovete cambiare l'hardware, funziona con quello che avete già.
![deepthinkconfidence.jpg](deepthinkconfidence.jpg)
[*Immagine tratta da jiaweizzhao.github.io/deepconf*](https://jiaweizzhao.github.io/deepconf/)

## I Numeri che Sbalordiscono

I risultati ottenuti dal team di Meta sono a dir poco impressionanti, con quel sapore di "troppo bello per essere vero" che caratterizza le scoperte davvero innovative. Su AIME 2025, uno dei benchmark più difficili per il ragionamento matematico (pensatelo come l'esame di maturità per le intelligenze artificiali), [DeepConf ha raggiunto un'accuratezza del 99.9% riducendo contemporaneamente l'uso di token dell'84.7%](https://venturebeat.com/ai/metas-deepconf-offers-a-dial-to-balance-llm-reasoning-cost-and-accuracy) rispetto ai metodi tradizionali.

Per capire la portata di questi numeri, facciamo un paragone cinematografico. È come se qualcuno avesse inventato un modo per girare film di qualità hollywoodiana usando un decimo del budget abituale, mantenendo la stessa qualità visiva e narrativa. Nel mondo dell'AI, dove ogni token generato ha un costo computazionale misurabile, una riduzione dell'85% significa letteralmente tagliare i costi operativi di un ordine di grandezza.

Ma non è solo una questione economica. L'aspetto più affascinante è che DeepConf riesce a migliorare le performance proprio eliminando il "rumore" computazionale. È controintuitivo: normalmente, in informatica, più risorse butti su un problema, migliori risultati ottieni. Qui invece succede l'opposto: togliendo i tentativi di bassa qualità, il segnale emerge più chiaramente dal rumore di fondo.

I test sono stati condotti sui modelli open-source più avanzati, inclusi Qwen 3 e la serie GPT-OSS, dimostrando che l'approccio funziona trasversalmente su architetture diverse. È come scoprire che un trucco funziona tanto su iPhone quanto su Android: significa che probabilmente avete trovato qualcosa di fondamentale.

## Due Modalità, Un Obiettivo

DeepConf opera in due modalità distinte, come un'auto sportiva che può funzionare sia in modalità eco che in modalità performance. La modalità "offline" analizza tutte le tracce di ragionamento generate e poi seleziona quelle con i migliori segnali di confidenza. È perfetta per applicazioni dove avete tempo di riflettere e volete la massima accuratezza possibile.

La modalità "online", invece, è pensata per applicazioni real-time dove la velocità è cruciale. In questo caso, DeepConf interrompe dinamicamente le tracce di ragionamento che mostrano segnali di scarsa confidenza e ne avvia di nuove al volo. È come avere un GPS intelligente che, invece di continuare a calcolare una strada che sa essere sbagliata, cambia immediatamente percorso verso una destinazione più promettente.

La flessibilità di questo approccio è uno dei suoi punti di forza. Gli sviluppatori possono calibrare il sistema in base alle proprie esigenze specifiche: più conservativo per applicazioni critiche dove l'errore non è tollerabile, più aggressivo per casi d'uso dove la velocità prevale sulla perfezione assoluta.

## Impatto Pratico: La Rivoluzione Economica

L'impatto economico di DeepConf potrebbe essere devastante per l'industria dell'AI, nel senso buono del termine. Pensate alle implicazioni: se potete ottenere le stesse performance di un sistema che costa 1000 dollari al giorno con uno che ne costa 150, all'improvviso servizi che prima erano economicamente insostenibili diventano accessibili a una platea molto più ampia di utenti e aziende.

Ma non è solo una questione di costi diretti. La riduzione dei token generati significa anche minori emissioni di CO2, meno stress sui data center e, in definitiva, un'AI più sostenibile dal punto di vista ambientale. È come passare da un SUV che consuma 15 litri per 100 chilometri a un'auto ibrida che ne consuma 4, mantenendo la stessa velocità e comfort.

Per le aziende che offrono servizi basati su LLM, DeepConf rappresenta un potenziale game-changer competitivo. Chi riuscirà a implementarlo per primo potrà offrire servizi di qualità superiore a prezzi inferiori, creando quel tipo di vantaggio competitivo che ridefinisce intere industrie. È la classica "disruption" di cui parla Clayton Christensen, applicata al mondo dell'intelligenza artificiale.

## Prospettive Future: Verso un'AI Autoconsapevole

Ma forse l'aspetto più affascinante di DeepConf non sono nemmeno i risultati immediati, bensì quello che rappresenta come direzione di ricerca. Per la prima volta, abbiamo un sistema che non si limita a generare risposte, ma sviluppa una forma primitiva di metacognizione: la capacità di riflettere sui propri processi di pensiero.

È un passo importante verso quello che i ricercatori chiamano "self-aware AI", sistemi che non solo risolvono problemi ma sono anche consapevoli di come li stanno risolvendo e, soprattutto, di quando stanno fallendo. Non stiamo parlando di coscienza nel senso fantascientifico del termine, ma di una forma di intelligenza procedurale che sa quando fidarsi di se stessa e quando essere scettica.

Il team di Meta ha dimostrato che questo tipo di "autodubbio costruttivo" può essere implementato senza stravolgere le architetture esistenti, aprendo la strada a una nuova generazione di modelli più efficienti ed economici. È come se avessimo trovato un modo per rendere le macchine non solo più intelligenti, ma anche più sagge nel senso di saper riconoscere i propri limiti.

Guardando al futuro, DeepConf potrebbe essere solo l'antipasto di una rivoluzione più ampia. Se le macchine possono imparare a dubitare delle proprie risposte in ambito matematico, cosa impedisce loro di applicare lo stesso principio alla scrittura creativa, alla risoluzione di problemi etici, o persino alla ricerca scientifica? La strada verso un'intelligenza artificiale davvero general-purpose potrebbe passare proprio da questa capacità di autocritica costruttiva.

Il lavoro di Zhao e dei suoi colleghi dimostra che a volte le rivoluzioni più importanti nascono dalle intuizioni più semplici. In un mondo dove tutti inseguono modelli sempre più grandi e potenti, loro hanno scelto di puntare sull'efficienza e l'autoconsapevolezza. Come direbbe il buon vecchio Einstein, "tutto dovrebbe essere reso il più semplice possibile, ma non più semplice". DeepConf sembra aver centrato perfettamente questo equilibrio, aprendo nuove frontiere per un'AI più smart, sostenibile e, paradossalmente, più umana nella sua capacità di mettere in dubbio se stessa.