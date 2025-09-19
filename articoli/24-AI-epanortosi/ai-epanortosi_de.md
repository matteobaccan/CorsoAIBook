---
tags: ["Research", "Generative AI", "Training"]
date: 2025-09-12
author: Dario Ferrero
---

# Die "Leidenschaft" der KI, die sie verrät: die emphatische Epanorthose
![ai-Shakespear.jpg](ai-Shakespear.jpg)

*"Kann man einen mit KI erstellten Text erkennen?". Das ist die Frage, die mir bei meinen Kursen über generative künstliche Intelligenz am häufigsten gestellt wird, geflüstert mit der verschwörerischen Miene von jemandem, der den Heiligen Gral unserer digitalen Zeit sucht. Meine Antwort, mittlerweile so automatisch wie ein konditionierter Reflex, weist immer in eine Richtung: "Achten Sie darauf, ob es von Aufzählungszeichen wimmelt", sage ich, "ob es jedes Konzept in eine geordnete Liste verwandelt". Aber was ich immer für das offensichtlichste Detail der KI gehalten habe, könnte nur die Spitze des stilistischen Eisbergs sein.*

Eine [neue Studie](https://zenodo.org/records/16947334) von Filippo Lubrano von der H-Farm hat nämlich ein viel subtileres und allgegenwärtigeres Muster identifiziert: die emphatische Epanorthose, eine antike rhetorische Figur, die Sprachmodelle in ihre unbewusste stilistische Signatur verwandelt haben. Als ob Data aus Star Trek plötzlich einen sprachlichen Tick entwickelt hätte, der ihn jedes Mal verrät, wenn er versucht, sich als Mensch auszugeben.

Das im August 2025 veröffentlichte Paper enthüllt Daten, die jeden Texter erschauern lassen würden: Große Sprachmodelle produzieren diese spezifische rhetorische Konstruktion 27-mal häufiger als Menschen. Wir sprechen hier nicht von einem gelegentlichen Fehler, sondern von einer echten stilistischen Epidemie, die alle wichtigen Modelle durchzieht, von ChatGPT bis Claude, einschließlich Open-Source-Systemen.

## Was ist die emphatische Epanorthose?

Bevor wir uns den Zahlen widmen, müssen wir verstehen, was genau diese rhetorische Figur mit ihren scheinbar exotischen Umrissen ist. Die Epanorthose ist eine Redefigur, die eine emphatische Ersetzung von Wörtern anzeigt, wobei "Tausende, nein, Millionen!" ein klassisches Beispiel ist. Aber die Variante, die moderne KIs besessen macht, ist spezifischer: Sie folgt dem Schema "Nicht X, sondern Y", bei dem eine erste Aussage sofort durch eine intensivere oder aufschlussreichere Formulierung korrigiert wird.

Um die Macht dieses Mechanismus zu verstehen, denken wir an die literarischen Beispiele, die diese Technik berühmt gemacht haben. In Shakespeares "Julius Cäsar" verwendet Mark Anton die Epanorthose, wenn er sagt: "Brutus ist ein ehrenwerter Mann. Das sind sie alle, alle ehrenwerte Männer", und erzeugt durch die korrigierende Wiederholung einen verheerenden ironischen Effekt. In Zeitungsüberschriften wimmelt es von dieser Technik: "Es ist nicht nur schlechtes Wetter, sondern der Klimawandel, der an die Tür klopft". Sportkommentatoren missbrauchen sie ständig: "Es ist nicht nur ein Tor, sondern das Tor, das das Schicksal der Meisterschaft verändert".

In der KI-Version verwandelt sich diese elegante rhetorische Figur jedoch in etwas Mechanisches und Zwanghaftes. Wo ein menschlicher Autor schreiben würde "Die Technologie ist fortgeschritten", wird ein LLM automatisch produzieren: "Es geht nicht nur um fortschrittliche Technologie, sondern um eine Revolution, die unsere Lebensweise verändert". Wo ein Journalist sagen würde "Der Markt wächst", wird die KI ausarbeiten: "Es ist nicht einfach nur Wachstum, sondern eine beispiellose Expansion, die die globalen wirtschaftlichen Gleichgewichte neu definiert".

Alltägliche Beispiele gibt es zuhauf. Stellen Sie sich vor, Sie fragen ChatGPT nach einem Rezept für Pasta mit Tomatensauce. Anstatt Ihnen zu sagen "Erhitzen Sie das Öl in einer Pfanne", erhalten Sie: "Es geht nicht nur darum, das Öl zu erhitzen, sondern darum, die aromatische Basis zu schaffen, die Ihre Sauce von einer einfachen Würze zu einem kulinarischen Erlebnis erhebt". Es ist, als hätte man einen Koch, der nie eine Anweisung geben kann, ohne sie in eine epiphanische Offenbarung zu verwandeln.

## Die Zahlen sprechen für sich
Lubranos Forschung analysierte drei verschiedene Korpora, um das Phänomen zu quantifizieren. Das erste bestand aus 400.000 zufällig ausgewählten Sätzen aus dem Common Crawl, der 2024 zum Trainieren einer großen Modellfamilie verwendet wurde. Das zweite enthielt 50.000 Antworten von ChatGPT und Claude, die zwischen Januar und Mai 2025 gesammelt wurden. Das dritte war ein Kontrollkorpus von 100.000 Sätzen aus geisteswissenschaftlichen Fachzeitschriften (2015-2020) und Mainstream-Zeitungsartikeln (2023-2024).

Die Ergebnisse sind verblüffend: KI-Modelle produzieren 27 emphatische Epanorthosen pro 1000 Sätze, gegenüber 9 im Trainingskorpus und nur 5 im menschlichen Benchmark. Aber es gibt noch mehr: Die Analyse ergab auch ein Phänomen der "Burstiness", d. h. diese Konstruktionen häufen sich an bestimmten Stellen im Text, genau wie wenn jemand Emojis entdeckt und anfängt, drei oder vier hintereinander in dieselbe Nachricht zu packen. Antworten mit mehr als 300 Token zeigten mindestens ein epanorthotisches Paar pro Themenwechsel, was darauf hindeutet, dass das Mittel als interne Beschilderung bei der generativen Planung fungiert.

Um diese Daten zu kontextualisieren, verglich die Studie die Ergebnisse mit größeren menschlichen Korpora: Wikipedia-Artikel, digitalisierte Bücher und Mainstream-Journalismus zeigten alle signifikant niedrigere Raten, typischerweise zwischen 4-6 Instanzen pro 1000 Sätze. Die stilistische Kluft zwischen maschinengeneriertem Text und konventioneller menschlicher Prosa ist so offensichtlich, dass sie fast peinlich ist.

Eine logistische Regression, die die Satzlänge, das Vorhandensein von Pronomen der ersten Person und Interrogative kontrollierte, behielt die Epanorthose als signifikanten Prädiktor für den Ursprung des Modells bei. Bei Blindbewertungen mit Linguistik-Doktoranden wurden Texte, die reich an Epanorthosen waren, als wahrscheinlich maschinengeneriert beurteilt, was die Relevanz des stilistischen Signals unterstreicht.

Der beunruhigendste Aspekt ist, dass das Phänomen nicht auf Englisch beschränkt ist. Vorläufige Stichproben in Spanisch, Französisch, Mandarin und Arabisch zeigen ähnliche Verstärkungen, was darauf hindeutet, dass der Effekt Sprachfamilien und Modellarchitekturen unterschiedlicher Größe und Herkunft durchdringt. Wie ein stilistischer Virus, der sich über Sprachen und Kulturen hinweg repliziert.

## Warum RLHF dieses Monster erschaffen hat

Die Wurzel des Problems liegt im Reinforcement Learning from Human Feedback (RLHF), dem Prozess, der Modelle nützlicher und auf menschliche Vorlieben abgestimmter machen soll. Ironischerweise ist es genau dieser Versuch, die KI zu vermenschlichen, der das stilistische Monster geschaffen hat, das wir analysieren.

Der Mechanismus ist auf perverse Weise elegant. Während der Feinabstimmungsphase werden die Modelle darauf trainiert, Bewertungen für Nützlichkeit, Klarheit und Höflichkeit zu maximieren. Menschliche Annotatoren belohnen unbewusst oft Ausgaben, die eine klärende Neuformulierung einführen, und interpretieren dies als Beweis für Verständnis. Das Belohnungssignal, das über Millionen von Token gemittelt wird, erhebt das Muster zu einer hochwertigen Aktion.

Aber es gibt eine zweite Verstärkungsebene. Die Trope korreliert auch mit hoch bewerteten Antworten in den Vortrainingsdaten, insbesondere Marketing-Blogs und Selbsthilfe-Inhalten, die für ihre überzeugende Dringlichkeit bekannt sind. Einmal verwurzelt, bleibt die Gewohnheit über Domänen hinweg bestehen, auch wenn sie maladaptiv wird. Das ist es, was Lubrano den "Sloganoideffekt" nennt: Klarheit wird auf Kosten von Nuancen erkauft.

Web-Korpora, insbesondere solche, die aus Marketing, Selbsthilfe und politischen Kommentaren gesammelt wurden, enthalten überdurchschnittlich hohe Raten von Negations-Substitutions-Strukturen. Diese Domänen bevorzugen Klarheit, Einprägsamkeit und Überzeugungskraft - Eigenschaften, die bei der RLHF-Feinabstimmung leicht belohnt werden. Sobald ein Belohnungsmodell einer Neuformulierung, die sowohl klärend als auch emphatisch erscheint, einen hohen Wert zuweist, verbreitet sich das Muster über nicht verwandte Themen.

Das Phänomen verläuft parallel zu breiteren Trends in der digitalen Rhetorik, wo kurzformatige, aufmerksamkeitsoptimierte Medien komplexe Argumente auf binäre Wendungen reduzieren. Die wiederholte Verwendung von "Nicht X, sondern Y" bietet eine komprimierte Form von narrativer Spannung und Auflösung, die Algorithmen aufgrund ihres Engagement-Potenzials tendenziell belohnen.
![frequenza-epanortosi.jpg](frequenza-epanortosi.jpg)
[Relative Häufigkeit von "Nicht X, sondern Y" in Modellen. Aus dem Paper von Filippo Lubrano](https://zenodo.org/records/16947334)

## Die sich selbst verstärkende kulturelle Schleife

Was das Phänomen noch beunruhigender macht, ist seine sich selbst verstärkende Natur. Modelle nehmen Muster aus dem Web auf, verstärken sie, und die Benutzer begegnen ihnen in generierten Texten wieder und integrieren sie unbewusst in ihr eigenes Schreiben. Es ist eine stilistische Schlange, die sich in den eigenen Schwanz beißt und die Gefahr birgt, die öffentliche Sprache zu homogenisieren.

Der Online-Diskurs belohnt vereinfachte Dualismen, teilweise weil die Ranking-Algorithmen der sozialen Medien polarisierende Inhalte hervorheben. Firmenslogans und Motivationszitate, die von Suchmaschinen gesammelt werden, verbreiten negativ-positive Inversionen. Modelle nehmen solches Material auf und kodieren das Mittel als Zeichen für überzeugende Wirksamkeit.

Journalistische Kritiken in Publikationen wie The Guardian und The Atlantic sowie laufende Diskussionen auf Wikipedia und Reddit haben den Begriff "AI Slop" populär gemacht, um diesen Trend zu beschreiben. Berichte im AI Flash Report und Kommentare auf Plattformen wie Twitter/X rahmen es weiter als kulturelles, nicht nur technisches Problem ein und heben hervor, wie sich stilistische Abkürzungen durch Feedbackschleifen des digitalen Schreibens verbreiten.

## Auf dem Weg zu Detektiv-Algorithmen

Diese Entdeckung eröffnet faszinierende Szenarien für die Entwicklung neuer KI-Erkennungssysteme. Die Häufigkeit der Epanorthose könnte als schwaches, aber nützliches Merkmal für KI-Textdetektoren dienen, insbesondere in Kombination mit lexikalischer Burstiness und Diskursmarkern in der Mitte des Satzes.

Die [derzeit verfügbaren KI-Detektoren](https://gptzero.me/) wie GPTZero, das kürzlich das Modell 3.7b mit drastischen Verbesserungen bei den neuesten Sprachmodellen der großen Anbieter veröffentlicht hat, könnten diese neue Metrik in ihre Analysealgorithmen integrieren. Das Machine-Learning-Team von GPTZero hat den Sommer damit verbracht, seinen bisher besten KI-Detektor zu entwickeln, und diese Veröffentlichung kommt genau rechtzeitig zum neuen Schuljahr 2025/2026.

Der multifaktorielle Ansatz, der Tools wie [ZeroGPT](https://zerogpt.org/) auszeichnet, könnte von der Einbeziehung der epanorthotischen Analyse enorm profitieren. Der ZeroGPT-KI-Detektor verwendet einen multifaktoriellen Ansatz, um den Ursprung des Inhalts zu identifizieren und festzustellen, ob er von einer KI generiert oder von einem Menschen geschrieben wurde.

Aber es gibt eine wichtige Warnung. Die aggressive Bestrafung der rhetorischen Figur könnte Gemeinschaften diskriminieren, in denen das Mittel kulturell verankert ist. Governance-Tools, die zur Diversifizierung des Modellstils entwickelt wurden, müssen sensibel für rhetorische Variationen sein und gleichzeitig die legitime emphatische Korrektur bewahren.

Stellen Sie sich einen Detektiv-Algorithmus vor, der wie Sherlock Holmes im digitalen Zeitalter arbeitet: Er sucht nicht nur nach offensichtlichen Fingerabdrücken wie Aufzählungszeichen, sondern analysiert subtile sprachliche Muster, Häufigkeiten rhetorischer Konstruktionen, Verteilung von Diskursmarkern. Ein System, das prozentuale Wahrscheinlichkeiten zuweisen könnte: "Dieser Text hat eine 87-prozentige Wahrscheinlichkeit, von einer KI generiert worden zu sein, basierend auf dem Vorhandensein von 12 emphatischen Epanorthosen, sich wiederholenden lexikalischen Mustern und dem Fehlen menschlicher syntaktischer Variation."

## Minderungsstrategien

Für Modellkuratoren und Entwickler schlägt Lubrano mehrere Minderungsstrategien vor. Kuratoren können Korpora, die alternative Betonungstechniken verwenden, wie Juxtaposition ohne Negation oder metaphorische Verschiebung, übergewichten. Prompt-Ingenieure können Modelle anweisen, das Bindegewebe explizit zu variieren, indem sie Konzessivsätze oder beschreibende Erweiterungen anfordern.

Belohnungsmodelle könnten wiederholte Epanorthosen innerhalb eines Token-Fensters bestrafen und so die syntaktische Erkundung fördern. Es ist, als würde man einen Musiker trainieren, nicht dieselbe Akkordfolge zu missbrauchen: Die Technik ist an sich nicht falsch, aber ihre zwanghafte Wiederholung verarmt das Endergebnis.

Eine filmische Analogie könnte die von Quentin Tarantino sein: Seine unverwechselbaren Erzähltechniken (Rückblenden, lange Dialoge, stilisierte Gewalt) funktionieren perfekt in seinen Filmen, aber wenn alle Regisseure anfangen würden, sie mechanisch zu kopieren, würde das Kino zu einer vorhersehbaren Langeweile werden. Die emphatische Epanorthose ist der Jump-Cut der KI: wirksam, wenn sie sparsam eingesetzt wird, verheerend, wenn sie zum einzigen Pfeil im Köcher wird.

## Auswirkungen auf die Zukunft des Schreibens

Das Phänomen der emphatischen Epanorthose wirft tiefere Fragen über die Natur von Kreativität und Ausdruck im Zeitalter der KI auf. Wenn Sprachmodelle unbewusst auf eine stilistische Homogenisierung drängen, was bedeutet das für die menschliche Ausdrucksvielfalt?

Es liegt eine fast an Jorge Luis Borges erinnernde Ironie in der Tatsache, dass Maschinen, die zur Nachahmung menschlicher Kreativität entwickelt wurden, stattdessen ihre eigene rhetorische Subkultur schaffen, einen künstlichen Dialekt, der die Art und Weise zu beeinflussen beginnt, wie Menschen selbst kommunizieren. Es ist, als hätten wir sprachliche Außerirdische geschaffen, die bei dem Versuch, menschlich zu wirken, ihre eigenen Idiosynkrasien entwickelt haben, die sie verraten.

Die Herausforderung für die kommenden Jahre wird zweifach sein: einerseits die Entwicklung immer ausgefeilterer Erkennungssysteme, die diese subtilen Muster identifizieren können; andererseits die Arbeit an der stilistischen Diversifizierung der Modelle selbst, um zu verhindern, dass die Suche nach "Klarheit" und "Nützlichkeit" zu einer verarmenden Standardisierung der Sprache führt.

## Der Detektiv der Zukunft

Zurück zur Ausgangsfrage meiner Studenten - "Kann man einen mit KI erstellten Text erkennen?" - die Antwort entwickelt sich schnell. Nicht mehr nur Aufzählungszeichen und offensichtliche repetitive Strukturen, sondern eine Konstellation von stilistischen Mikrosignalen, die abnormale Häufigkeiten spezifischer rhetorischer Konstruktionen, Betonungsmuster, Verteilung von Diskursmarkern umfassen.

Die Zukunft wird uns wahrscheinlich eine Art linguistisches CSI bescheren, bei dem digitale Ermittler, bewaffnet mit immer ausgefeilteren Algorithmen, Texte auf der Suche nach für das menschliche Auge unsichtbaren stilistischen Fingerabdrücken analysieren werden. Die emphatische Epanorthose könnte nur die erste von vielen "linguistischen DNAs" sein, die den künstlichen Ursprung eines Textes verraten.

Aber vielleicht ist die wichtigste Lektion aus dieser Studie, dass die KI bei dem Versuch, menschlicher zu wirken, stattdessen offenbart, wie zutiefst unmenschlich sie in ihren Lern- und Reproduktionsmustern ist. Wie ein Schauspieler, der bei dem Versuch, die Rolle eines Menschen zu spielen, genau die Aspekte betont, die ihn als Schauspieler erkennbar machen.

Lubranos Forschung ist nicht nur ein technischer Beitrag zum Gebiet der KI-Erkennung, sondern ein Memento, das uns daran erinnert, nicht nur darauf zu achten, was Maschinen sagen, sondern wie sie es sagen.

Um McLuhan zu paraphrasieren, der argumentierte: "Das Medium, in dem wir kommunizieren, ist wichtiger als der Inhalt der Botschaft selbst", in der Welt der generativen künstlichen Intelligenz ist das Medium nicht nur die Botschaft: Es ist die Signatur.
