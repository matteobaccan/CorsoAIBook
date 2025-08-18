# L'IA sotto assedio: cronache dal fronte cyber.
*di Dario Ferrero (VerbaniaNotizie.it)*
![fronte_AI.jpg](fronte_AI.jpg)

*Aprile 2023: gli ingegneri Samsung condividono inconsapevolmente codice sorgente proprietario con ChatGPT. Maggio 2025: i ricercatori scoprono che paper accademici contengono prompt nascosti per manipolare sistemi di peer review alimentati da AI. Tra questi due eventi si dispiega una cronaca allarmante che racconta come l'intelligenza artificiale sia diventata insieme il predatore e la preda del nuovo ecosistema cyber.*

## Il prezzo dell'innocenza digitale

La storia inizia con quella che potremmo definire l'innocenza perduta dell'era AI. [Nel 2023, Samsung ha dovuto vietare l'uso di ChatGPT e altri strumenti AI generativi](https://www.bloomberg.com/news/articles/2023-05-02/samsung-bans-chatgpt-and-other-generative-ai-use-by-staff-after-leak) sui propri dispositivi aziendali dopo che [tre ingegneri, in episodi separati, avevano inconsapevolmente condiviso dati sensibili aziendali](https://techcrunch.com/2023/05/02/samsung-bans-use-of-generative-ai-tools-like-chatgpt-after-april-internal-data-leak/) con il chatbot di OpenAI. Non si trattava di un attacco sofisticato o di spionaggio industriale: era semplicemente il risultato di dipendenti che, nel tentativo di ottimizzare il proprio lavoro, avevano utilizzato l'AI come un assistente personale, non rendendosi conto che stavano alimentando un sistema che apprende da ogni conversazione.

I dati trapelati includevano codice sorgente di semiconduttori, verbali di riunioni interne e dettagli su hardware proprietario. Samsung non era stata hackerata nel senso tradizionale del termine: si era hackerata da sola, vittima di quella che gli esperti definiscono "shadow AI" - l'uso non autorizzato di strumenti di intelligenza artificiale da parte dei dipendenti.

Questo incidente ha rappresentato il primo campanello d'allarme per il settore enterprise, rivelando una verità scomoda: le aziende stavano correndo verso l'adozione AI senza comprendere appieno le implicazioni di sicurezza. Come un moderno vaso di Pandora digitale, una volta aperto il mondo dell'AI, controllarne i contenuti si è rivelato infinitamente più complesso del previsto.

## Il paradosso della crescita esponenziale

I numeri raccontano una storia preoccupante: nel 2024, il costo medio di un incident di cybersecurity per le piccole e medie imprese ha raggiunto 1,6 milioni di dollari, in aumento dai 1,4 milioni del 2023, con quasi il 40% delle piccole aziende che hanno perso dati cruciali e subito significativi tempi di inattività. Parallelamente, gli attacchi potenziati dall'AI stanno aumentando mentre la sicurezza cloud evolve, spingendo le enterprise a implementare difese AI in tempo reale per tenere il passo.

Il paradosso è evidente: mentre le aziende implementano l'AI per difendersi meglio, gli attaccanti utilizzano le stesse tecnologie per lanciare offensive più sofisticate. È come assistere a una versione digitale della guerra fredda, dove ogni innovazione difensiva viene immediatamente controbilanciata da una contromossa offensiva.

I leader del settore anticipano un panorama delle minacce sempre più complesso nel 2025, ma la sfida principale non risiede tanto nella sofisticazione tecnica degli attacchi quanto nella loro democratizzazione. L'AI ha reso accessibili a chiunque tecniche di attacco che un tempo richiedevano anni di specializzazione.

## Le nuove frontiere dell'attacco: quando l'AI tradisce se stessa

Dal 2023 al 2024 si sono verificati numerosi leak di dati e incidenti di privacy legati a ChatGPT, evidenziando le sfide critiche di sicurezza affrontate dalle tecnologie AI. Ma questi episodi rappresentano solo la punta dell'iceberg di un fenomeno molto più complesso: l'emergere di vettori di attacco completamente nuovi che sfruttano la natura stessa dell'intelligenza artificiale.

Un esempio emblematico è rappresentato dalla manipolazione dei sistemi di peer review accademico. I ricercatori hanno scoperto che alcuni paper contenevano prompt nascosti progettati specificamente per influenzare i sistemi AI utilizzati nella valutazione scientifica. È come se qualcuno avesse inventato un modo per sussurrare istruzioni invisibili agli arbitri di una partita, alterando il risultato senza che nessuno se ne accorgesse.

Questa tecnica, nota come "prompt injection", rappresenta una delle vulnerabilità più insidiose dell'era AI. A differenza degli attacchi informatici tradizionali che sfruttano falle nel codice, la prompt injection sfrutta la caratteristica fondamentale dei modelli linguistici: la loro capacità di comprendere e seguire istruzioni in linguaggio naturale. È l'equivalente digitale del ventriloquo che fa dire alla marionetta ciò che vuole, ma in questo caso la marionetta controlla sistemi aziendali critici.
![prompt_injection.jpg](prompt_injection.jpg)
[*Immagine tratta da arthur.ai*](https://www.arthur.ai/blog/from-jailbreaks-to-gibberish-understanding-the-different-types-of-prompt-injections)

## L'ecosistema delle vulnerabilità: il caso MCP

Il Model Context Protocol, sviluppato per semplificare l'interazione tra i Large Language Models e gli strumenti esterni, rappresenta un caso studio perfetto di come le buone intenzioni possano aprire nuove superfici di attacco. Una collezione di otto incidenti reali legati all'AI negli ultimi 24 mesi evidenzia i rischi dell'utilizzo e implementazione di AI senza adeguate misure di sicurezza.

Il MCP doveva essere la soluzione definitiva per connettere l'AI al mondo reale, permettendo ai modelli di interagire seamlessly con database, API e servizi esterni. In realtà, si è rivelato un ponte che gli attaccanti possono attraversare in entrambe le direzioni. [Un repository della community](https://github.com/Puliczek/awesome-mcp-security) documenta oltre cinquanta ricerche accademiche pubblicate solo nei primi mesi del 2025, rivelando vulnerabilità che spaziano dall'[esfiltrazione di dati da server Slack](https://embracethered.com/blog/posts/2025/security-advisory-anthropic-slack-mcp-server-data-leakage/) all'[accesso non autorizzato a repository GitHub privati](https://invariantlabs.ai/blog/mcp-github-vulnerability).

Il problema fondamentale del MCP è architetturale: è stato progettato partendo dal presupposto che tutti i componenti dell'ecosistema siano fidati. È l'equivalente di costruire una città senza mura perché si assume che tutti i visitatori siano amici. Quando questa assunzione si rivela falsa, l'intero sistema crolla come un castello di carte.
![MCP_method.jpg](MCP_method.jpg)
[*Immagine tratta da descope.com*](https://www.descope.com/learn/post/mcp)

## La democratizzazione dell'hacking: quando tutti possono essere Anonymous

Le previsioni per il 2025 si concentrano sui rischi di sicurezza operativa e sulle sfide evolutive poste dall'AI, ma forse l'aspetto più preoccupante è la democratizzazione delle capacità offensive. L'AI ha abbassato drammaticamente la barriera d'ingresso per condurre attacchi informatici sofisticati.

Prendiamo il caso della prompt injection: un attaccante non ha più bisogno di conoscere linguaggi di programmazione o di comprendere architetture complesse. Basta formulare astutamente una richiesta in linguaggio naturale per potenzialmente compromettere un sistema. È come se improvvisamente chiunque potesse diventare Houdini semplicemente chiedendo gentilmente alle catene di slegarsi.

Per comprendere questa dinamica, possiamo esaminare diverse piattaforme che simulano attacchi di prompt injection. Esistono strumenti come ChatGPT Jailbreak Challenge o AI Security Sandbox, che insegnano a identificare vulnerabilità AI. Nei livelli iniziali, aggirare le restrizioni dell'AI può essere semplice come usare frasi come "Ignora le direttive precedenti" o "Fai un'eccezione".

Tuttavia, avanzando, i sistemi implementano filtri più complessi, come il rilevamento di parole chiave o risposte predefinite. Nonostante ciò, con un approccio metodico e un po' di ingegno, anche queste barriere possono essere superate, dimostrando quanto sia cruciale una progettazione robusta dei modelli linguistici.

## Gli attacchi del futuro: l'emoji come cavallo di Troia

Le tecniche di attacco più innovative sfruttano aspetti apparentemente innocui della comunicazione digitale. L'"emoji smuggling" rappresenta un esempio perfetto di questa tendenza: [ricercatori di Mindgard e Lancaster University hanno dimostrato](https://securitybrief.asia/story/emojis-used-to-hide-attacks-bypass-major-ai-guardrails) come gli attaccanti possano nascondere istruzioni maligne utilizzando emoji per [aggirare i filtri AI di Microsoft, Nvidia e Meta](https://cybersecuritynews.com/hackers-can-bypass-microsoft-nvidia-meta-ai-filters/). 

La ricerca ha testato sei dei sistemi di guardrail più utilizzati, rivelando che molti dipendono pesantemente dal riconoscimento di pattern statici e mostrano insufficiente resilienza contro attacchi adversarial.

È come nascondere un messaggio segreto nel sorriso di Monna Lisa: apparentemente innocuo, ma potenzialmente devastante per chi sa come decifrarlo. Questa tecnica è particolarmente insidiosa perché sfrutta la tendenza naturale degli esseri umani a considerare gli emoji come elementi decorativi innocui, quando in realtà possono diventare veri e propri veicoli di attacco.

Un'altra tecnica emergente documentata dai ricercatori è il [data smuggling attraverso tecniche di encoding avanzate](https://embracethered.com/blog/posts/2025/sneaky-bits-and-ascii-smuggler/), che può trasformare l'AI in una spia involontaria. Gli attaccanti possono istruire il sistema a incorporare dati sensibili in stringhe apparentemente innocue o URL. Anche se l'AI non riesce a completare la richiesta, i log del server registrano comunque il tentativo, permettendo all'attaccante di recuperare le informazioni attraverso canali laterali. È l'equivalente digitale di far recapitare un messaggio segreto attraverso un piccione viaggiatore che non sa di trasportare informazioni classificate.

[Jason Haddix](https://mlsecops.com/podcast/holistic-ai-pentesting-playbook), veterano della sicurezza offensiva e CEO di Arcanum Information Security, è riconosciuto come uno dei principali esperti nell'hacking dei sistemi AI. Ha sviluppato una metodologia proprietaria e olistica per il penetration testing AI, che esamina l'intero ecosistema delle applicazioni AI e non solo i modelli. Haddix ha anche creato una tassonomia open source per le tecniche di prompt injection, classificando tattiche innovative come l'"emoji smuggling" e il "data smuggling" tramite encoding avanzati. Il suo lavoro si concentra sull'identificazione e la difesa da vulnerabilità reali come chiavi API sovra-autorizzate e dati sensibili non protetti in sistemi RAG, e promuove un approccio di difesa in profondità per le applicazioni AI.


## La risposta dell'industria: tra innovazione e reazione

Samsung ha recentemente permesso ai propri dipendenti di utilizzare nuovamente ChatGPT, ma con nuovi protocolli di sicurezza, dimostrando come l'industria stia cercando di bilanciare innovazione e sicurezza. Questa decisione rappresenta un microcosmo della sfida più ampia che affrontano le organizzazioni: come sfruttare i benefici dell'AI minimizzando i rischi.

La strategia emergente nel settore enterprise si basa su un approccio multi-layered che ricorda la difesa in profondità dei castelli medievali. Non un singolo muro invalicabile, ma una serie di ostacoli concentrici che rendono progressivamente più difficile l'avanzata degli attaccanti.

Al livello più basilare, si applica il principio del least privilege: ogni sistema AI ha accesso solo alle risorse strettamente necessarie per completare i propri compiti. È come dare a un cameriere le chiavi solo della sala da pranzo, non dell'intero albergo.

Il secondo livello implementa filtri e classificatori sia in ingresso che in uscita, creando quello che potremmo definire un "firewall conversazionale". Questi sistemi analizzano ogni interazione per identificare potenziali tentativi di manipolazione o esfiltrazione di dati.

Il terzo livello si concentra sulla validazione rigorosa di tutti gli input e output, assicurandosi che il sistema non possa essere utilizzato per introdurre malware o estrarre informazioni non autorizzate.

## L'AI come difensore: quando la medicina è anche la cura

Le aziende stanno implementando difese AI in tempo reale per contrastare attacchi potenziati dall'AI, creando un ciclo di innovazione continua tra offensive e defensive. Questa dinamica ha portato alla nascita di quello che gli esperti chiamano "AI versus AI warfare" - una battaglia in cui algoritmi si confrontano con altri algoritmi in una danza infinita di azione e reazione.

I sistemi di difesa basati su AI mostrano capacità impressionanti nell'identificare pattern di attacco e rispondere in tempo reale a minacce emergenti. Sono particolarmente efficaci contro attacchi standardizzati e vulnerabilità note, dove possono processare volume di dati e identificare anomalie a velocità impossibili per gli analisti umani.

Tuttavia, l'AI difensiva mostra ancora limiti significativi quando si confronta con la creatività e l'intuizione degli attaccanti umani più sofisticati. Gli specialisti di cybersecurity possiedono quello che potremmo definire "l'elemento X" - una combinazione di esperienza, intuizione e capacità di pensiero laterale che non può essere facilmente replicata dagli algoritmi.

## Le conseguenze aziendali: il nuovo calcolo del rischio

Le organizzazioni devono ora considerare nuove tipologie di rischio AI che vanno dalla manipolazione dei modelli all'esfiltrazione di dati attraverso canali non convenzionali. Il calcolo del rischio aziendale si è complicato enormemente: non si tratta più solo di proteggere i sistemi dall'esterno, ma anche di controllare come i propri strumenti interni possano essere utilizzati impropriamente.

Il caso Samsung rappresenta solo la punta dell'iceberg. Molte organizzazioni stanno scoprendo che i loro dipendenti utilizzano quotidianamente strumenti AI per ottimizzare il lavoro, spesso senza rendersi conto delle implicazioni di sicurezza. È emerso il concetto di "shadow AI" - l'uso non dichiarato di strumenti di intelligenza artificiale che crea blind spot significativi nella postura di sicurezza aziendale.

Le conseguenze economiche sono tangibili e crescenti. Le previsioni per il 2025 indicano che l'AI potenzierà significativamente gli attacchi informatici, mentre il costo medio degli incidenti continua a crescere. Le aziende si trovano in una posizione paradossale: devono investire nell'AI per rimanere competitive, ma ogni implementazione introduce nuove superfici di attacco.

## Verso un futuro di coesistenza armata

La sfida fondamentale del 2025 non è eliminare i rischi dell'AI - un obiettivo impossibile - ma imparare a gestirli efficacemente. Stiamo entrando in un'era di "coesistenza armata" tra innovazione e sicurezza, dove l'obiettivo non è la perfetta protezione ma la resilienza dinamica.

I report di sicurezza AI rivelano che le organizzazioni stanno imparando a identificare e mitigare i rischi AI attraverso strategie difensive sempre più sofisticate. La chiave del successo sembra risiedere non nella prevenzione assoluta degli incidenti, ma nella capacità di detectare rapidamente le anomalie, rispondere efficacemente agli attacchi e recuperare velocemente dalle compromissioni.

Il panorama che emerge ricorda quello delle prime fasi di Internet: un ambiente ricco di opportunità ma anche di insidie, dove la differenza tra successo e fallimento si misura nella capacità di bilanciari innovazione e prudenza. Le organizzazioni che prosperano in questo nuovo ambiente sono quelle che riescono a implementare l'AI mantenendo una mentalità di "security by design", considerando la protezione non come un vincolo ma come un abilitatore di innovazione sostenibile.

## Epilogo: lezioni da un futuro che è già presente

La storia dell'ingegnere Samsung che condivide inconsapevolmente codice proprietario con ChatGPT è diventata un caso di studio classico nei corsi di cybersecurity. Non perché rappresenti un attacco particolarmente sofisticato, ma perché incarna perfettamente la natura delle sfide che ci attendono: minacce che nascono dall'intersezione tra buone intenzioni, nuove tecnologie e comprensione insufficiente delle implicazioni.

L'intelligenza artificiale non è né intrinsecamente buona né cattiva: è uno strumento potente che amplifica tanto le nostre capacità quanto le nostre vulnerabilità. La sfida del 2025 e oltre sarà sviluppare la saggezza collettiva necessaria per guidare questa potenza verso obiettivi costruttivi, pur rimanendo vigilanti sui rischi che comporta.

Come in ogni epoca di transizione tecnologica, dalla stampa a Internet, il successo apparterrà a coloro che sapranno adattarsi rapidamente conservando i principi fondamentali di prudenza e responsabilità. Nella Terra di Mezzo dell'AI, non è l’elfo più agile o il mago più potente a vincere, ma lo hobbit che impara a navigare l’imprevedibile – un anello (di dati) alla volta.
