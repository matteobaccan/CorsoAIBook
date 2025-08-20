---
tags: ["Research", "Ethics & Society", "Business"]
date: 2025-08-20
---

# Der "Nobelpreis" für Informatik: "KI-Hersteller, ihr habt den Weg verloren"
*von Dario Ferrero (VerbaniaNotizie.it)*
![SuttonMoses.jpg](SuttonMoses.jpg)


*Stellen Sie sich einen Sternekoch vor, der, nachdem er das perfekte Risotto-Rezept erfunden hat, feststellt, dass alle Restaurants der Welt den Kunden nur noch rohen Reis mit einer Prise Parmesan darüber servieren. So ähnlich muss es Richard Sutton gehen, wenn er die aktuelle Landschaft der künstlichen Intelligenz beobachtet. Der [Mitgewinner des Turing-Preises 2024](https://awards.acm.org/turing) - der in der Computerwelt dem Nobelpreis entspricht - hat ein J'accuse veröffentlicht, das wie eine Alarmglocke für eine Branche klingt, die seiner Meinung nach den Weg zur wahren Intelligenz völlig verloren hat.*

## Die Anatomie einer verratenen Revolution

Sutton, eine führende Persönlichkeit im Reinforcement Learning und Gewinner des Turing-Preises, sagt, die KI-Industrie habe den Weg verloren, und das ist keine Kritik von einem mürrischen Akademiker, der in eine Ecke der Universität verbannt wurde. Wir sprechen von einem der [Gründerväter des computergestützten Verstärkungslernens](https://www.ualberta.ca/en/computing-science/news-and-events/news/2025/march/rich-sutton-receives-the-2024-acm-am-turing-award.html), demjenigen, der zusammen mit Andrew Barto die konzeptionellen und algorithmischen Grundlagen dessen gelegt hat, was es Robotern heute ermöglicht, laufen zu lernen und autonomen Autos, im Verkehr zu navigieren.

Aber was genau meint Sutton, wenn er sagt, die Industrie habe "den Weg verloren"? Seine Kritik zielt nicht auf die kommerziellen Ergebnisse ab - die sind unbestreitbar - sondern auf die Tatsache, dass der derzeitige dominante Ansatz in der KI Sandburgen statt solider Fundamente für die Intelligenz der Zukunft baut. [Wie er auf X schreibt](https://x.com/RichardSSutton/status/1957501548214513897), "Da die KI zu einer riesigen Industrie geworden ist, hat sie gewissermaßen den Weg verloren", und argumentiert, dass die jüngsten Fortschritte die für eine wahre Intelligenz notwendigen Grundprinzipien ignoriert haben.

Der Kern der Sache ist ebenso philosophisch wie technisch. Die aktuellen großen Sprachmodelle, die riesigen, die Terabytes an Text verschlingen, um uns scheinbar intelligente Antworten zu geben, tun laut Sutton genau das Gegenteil von dem, was eine echte künstliche Intelligenz tun sollte: Sie haben ihr Wissen zum Zeitpunkt des Entwurfs "programmiert", anstatt es durch erfahrungsbasiertes Lernen zu entdecken.
![tweetsutton.jpg](tweetsutton.jpg)

## Das große Missverständnis: Skalierung vs. Lernen

Um die Tiefe von Suttons Kritik zu verstehen, muss man einen Schritt zurücktreten und betrachten, was er selbst 2019 die ["Bittere Lektion"](http://www.incompleteideas.net/IncIdeas/BitterLesson.html) nannte - ein Aufsatz, der zu einer Art Manifest in der KI-Forschung geworden ist. Die bittere Lektion lautet: Langfristig gewinnen skalierbare und allgemeine Methoden immer über Systeme, die durch die Einbeziehung von domänenspezifischem Wissen aufgebaut werden. Es ist wie der Unterschied zwischen dem Beibringen des Fischens und dem täglichen Geben eines Fisches: Der erste Ansatz skaliert unbegrenzt, der zweite zwingt einen, weiter für ihn zu fischen.

Und doch, wenn man sich die heutige Industrie ansieht, scheint es, als hätten alle beschlossen, für ihre KIs zu fischen, anstatt ihnen beizubringen, wie es geht. Heutige Sprachmodelle werden mit astronomischen Mengen an menschlichem Text gefüttert und absorbieren passiv Muster und Korrelationen. Es ist ein Ansatz, der funktioniert - und die Ergebnisse sind für alle sichtbar - aber der laut Sutton eine evolutionäre Sackgasse darstellt.

Die Kritik wird noch schärfer, wenn man bedenkt, dass Sutton bei Google DeepMind gearbeitet hat, einem der Unternehmen, das am meisten zum Erfolg von Sprachmodellen beigetragen hat. Es handelt sich also nicht um den klassischen Außenseiter, der auf das System schießt, sondern um jemanden, der die internen Mechanismen der Branche genau kennt und beschlossen hat, seine Stimme von innen heraus zu erheben.

## Die Oak-Architektur: Ein Manifest für die Zukunft

Sutton diagnostiziert nicht nur das Problem - er schlägt auch eine radikale Lösung namens Oak (Options and Knowledge) Architektur vor. Es ist ein Rahmen, der direkt aus einer Folge von Black Mirror stammen könnte, wenn Black Mirror von optimistischen Ingenieuren statt von pessimistischen Drehbuchautoren geschrieben worden wäre.

Oak basiert auf drei Grundprinzipien: Der Agent muss allzwecktauglich sein und ohne spezifisches Wissen über eine bestimmte Welt beginnen; das Lernen wird vollständig von der Erfahrung geleitet, wobei der Agent Wissen ausschließlich durch direkte Interaktion mit seiner Umgebung erwirbt; und die Belohnungshypothese wird angewendet, wonach jedes Ziel auf die Maximierung eines einfachen skalaren Belohnungssignals reduziert werden kann.

Das Herzstück von Oak ist eine sich selbst verstärkende Schleife, die in ihrer Einfachheit fast mystisch klingt: Der Agent schafft durch Feedback immer höhere Abstraktionsebenen, wobei die Merkmale, die bei der Planung und Problemlösung helfen, zur Grundlage für die nächste, noch abstraktere Wissensgeneration werden. Dieser Prozess ist offen, nur durch die verfügbare Rechenleistung begrenzt, und könnte laut Sutton schließlich den Weg zur Superintelligenz ebnen.

Es klingt nach Science-Fiction, aber es gibt ein sehr irdisches Problem, das die Verwirklichung dieser Vision verhindert: Oak ist auf Algorithmen angewiesen, die kontinuierlich und stabil lernen können, ohne zu vergessen, was sie bereits gelernt haben. Es ist das berühmte Problem des "katastrophalen Vergessens" - wenn ein neuronales Netz etwas Neues lernt, neigt es dazu, das, was es vorher wusste, zu "überschreiben", wie eine Festplatte, die ständig alte Dateien löscht, um Platz für neue zu schaffen.

## Das Paradox des kontinuierlichen Lernens

Hier kommen wir zum technischen Kern der Sache, der Träume von der umsetzbaren Realität trennt. Sutton identifiziert das Hauptproblem aktueller Systeme darin, dass sie nicht kontinuierlich lernen können: Sie kämpfen mit katastrophalem Vergessen, bei dem neue Informationen das bereits Gelernte überschreiben und die Fähigkeit verlieren, im Laufe der Zeit weiterzulernen.

Es ist ein bisschen so, als ob wir jedes Mal, wenn wir eine neue Sprache lernen, alle vergessen müssten, die wir vorher kannten. Bei Menschen passiert das nicht - oder zumindest nicht so drastisch - weil unser Gehirn ausgeklügelte Mechanismen entwickelt hat, um neues Wissen zu integrieren, ohne das vorherige zu löschen. Aber unsere Deep-Learning-Algorithmen sind in diesem Sinne noch primitiv: gut darin, von Grund auf mit riesigen Datensätzen zu lernen, aber unfähig, weiterzulernen, ohne an Stabilität zu verlieren.

Dies ist nicht nur ein technisches Detail - es ist der Unterschied zwischen dem Aufbau einer Intelligenz, die kontinuierlich wächst und sich entwickelt, und einer, die zum Zeitpunkt ihrer letzten Trainingseinheit eingefroren bleibt. Und hier wird Suttons Kritik relevanter denn je: Die Industrie investiert Billionen in Systeme, die, so beeindruckend sie auch sein mögen, im Wesentlichen statische Momentaufnahmen von Wissen darstellen und nicht dynamische und anpassungsfähige Intelligenzen.
![era_of_experience_graph.png](era_of_experience_graph.png)
[*Bild von medium.com*](https://medium.com)

## Die dissidente Stimme im Zeitalter der Skalierung

Sutton schließt sich anderen führenden Forschern an, die die Fixierung der Industrie auf die Skalierung großer Sprachmodelle kritisieren, aber seine Position ist besonders interessant, weil sie von jemandem kommt, dem man nicht vorwerfen kann, nicht auf dem Laufenden zu sein. Der [Turing-Preis, den er 2024](https://www.nsf.gov/news/ai-pioneers-andrew-barto-richard-sutton-win-2024-turing) zusammen mit Andrew Barto erhielt, war mit einem von Google gesponserten Scheck über eine Million Dollar dotiert, dem Unternehmen, das den auf großen Sprachmodellen basierenden Ansatz am stärksten vorangetrieben hat.

Seine Kritik nimmt damit die Konturen einer echten intellektuellen Dissidenz von innerhalb des Systems an. Wenn einer der Gewinner des "Nobelpreises für Informatik", der für eines der einflussreichsten Big-Tech-Unternehmen im KI-Sektor gearbeitet hat, sagt, dass die Branche den Weg verloren hat, lohnt es sich vielleicht, aufmerksam zu werden.

Aber Sutton ist mit seiner Skepsis nicht allein. Zusammen mit David Silver, einem Professor am University College London, der unter anderem für die Leitung der Entwicklung von AlphaGo bekannt ist, dem System, das 2016 den Go-Weltmeister Lee Sedol besiegte, hat er kürzlich [ein Papier veröffentlicht](https://storage.googleapis.com/deepmind-media/Era-of-Experience%20/The%20Era%20of%20Experience%20Paper.pdf), in dem er argumentiert, dass KI durch Handeln lernen sollte, nicht nur durch die Aufnahme riesiger Mengen an von Menschen geschriebenem Text. Es ist eine Position, die in einem Teil der Forschungsgemeinschaft, die LLMs als einen Weg zum kommerziellen Erfolg, aber nicht unbedingt zur allgemeinen Intelligenz ansieht, immer mehr Anklang findet.

## Die Auswirkungen einer gescheiterten Revolution

Wenn Sutton Recht hat - und seine wissenschaftliche Glaubwürdigkeit legt nahe, dass es sich lohnt, seine Argumente ernst zu nehmen - was bedeutet das für die Zukunft der KI? Erstens könnten wir uns in dem befinden, was Biologen eine "evolutionäre Sackgasse" nennen: ein Weg, der zu lokalisierten Erfolgen führt, aber keine Auswege zu höheren Komplexitätsebenen hat.

Heutige KI-Systeme, so beeindruckend sie auch in ihren sprachlichen und logischen Fähigkeiten sein mögen, könnten eine Art technologisches Plateau darstellen - Systeme, die bei bestimmten Aufgaben hervorragende Leistungen erbringen, sich aber nicht zu allgemeineren und anpassungsfähigeren Formen der Intelligenz entwickeln können. Es ist, als hätten wir die Schreibmaschine perfektioniert, gerade als wir im Begriff waren, den Computer zu erfinden.

Zweitens gibt es ein tieferes Problem der Nachhaltigkeit und Effizienz. Heutige Ansätze erfordern wachsende Mengen an Daten und Rechenleistung und folgen einer Kurve, die langfristig möglicherweise nicht nachhaltig ist. Der von Sutton vorgeschlagene Ansatz, der auf Agenten basiert, die durch direkte Interaktion mit der Umgebung lernen, könnte einen effizienteren Weg zur allgemeinen künstlichen Intelligenz darstellen.

## Auf dem Weg in eine ungewisse, aber faszinierende Zukunft

Suttons Vision für die Zukunft der KI ist nicht nur technisch - sie ist in ihrer Reichweite fast philosophisch. Er stellt sich Systeme vor, die nicht nur Informationen verarbeiten, sondern die Welt durch direkte Erfahrung wirklich "verstehen", die durch kontinuierliche Interaktion und Feedback immer ausgefeiltere Modelle der Realität erstellen.

Es ist eine Vision, die nicht nur eine Revolution bei den Algorithmen, sondern auch bei der Infrastruktur erfordert. Wie Sutton erklärt, "was wir brauchen, um wieder auf den richtigen Weg zur wahren Intelligenz zu kommen, sind Agenten, die kontinuierlich lernen, Modelle der Welt und Planung, hochrangiges und erlernbares Wissen und die Meta-Fähigkeit zu lernen, wie man verallgemeinert."

Natürlich besteht die Gefahr, dass dies das klassische "nächste große Ding" ist, das immer "nächstes" bleibt, ohne jemals "aktuell" zu werden. Stabiles kontinuierliches Lernen bleibt eines der schwierigsten Probleme in der KI, und es ist nicht klar, wann - oder ob - wir es lösen können. Aber wenn es eine Lektion gibt, die uns die Geschichte der Technologie gelehrt hat, dann ist es, dass Revolutionen oft von den unerwartetsten Orten kommen, vorgeschlagen von Stimmen, die anfangs wie Dissidenten klingen.

Richard Sutton, mit seiner Erfolgsbilanz von Innovationen, die das Feld definiert haben, und seiner einzigartigen Position als kritischer Insider, könnte genau die Art von Stimme sein, die die KI-Industrie hören muss. Auch wenn - und vielleicht gerade wenn - das, was er sagt, alles in Frage stellt, was wir bisher aufgebaut haben.

In der Zwischenzeit, während die Industrie weiterhin die Grenzen dessen auslotet, was große Sprachmodelle leisten können, träumt in Alberta ein Turing-Preisträger, der DeepMind von innen heraus entstehen und wachsen sah, weiterhin von Agenten, die wie neugierige Kinder lernen und die Welt Schritt für Schritt erkunden. Es ist ein bisschen so, als ob Willy Wonka, nachdem er die fortschrittlichste Schokoladenfabrik der Welt erfunden hat, beschließt, sie zu verlassen, um uns daran zu erinnern, dass der beste Geschmack nicht von den raffiniertesten Maschinen kommt, sondern vom einfachsten Rezept: dem der direkten Erfahrung.

Sutton beobachtet heute die Branche, die er mitgestaltet hat, mit den Augen von jemandem, der die Zukunft gesehen hat und weiß, dass wir in die falsche Richtung gehen. Seine Stimme, verstärkt durch das Gewicht einer Karriere, die ganze Generationen von Forschern geprägt hat, klingt wie eine Warnung, die wir uns nicht leisten können, zu ignorieren. Denn die Erfahrung lehrt uns, dass die größten Veränderungen oft mit jemandem beginnen, der den Mut hat zu sagen, dass der Kaiser nackt ist - auch wenn dieser Kaiser Billionen von Parametern hat und jede Frage beantworten kann.
