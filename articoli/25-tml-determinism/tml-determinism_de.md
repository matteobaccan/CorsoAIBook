---
tags: ["Research", "Generative AI", "Training", "Startups"]
date: 2025-09-15
author: Dario Ferrero
---

# LLM: Gleiche Frage, andere Antwort? Vielleicht liegt es an den GPUs
![tml.jpg](tml.jpg)

*Stellen Sie sich vor, Sie haben einen Sternekoch, der Ihnen jedes Mal, wenn Sie nach seinem Carbonara-Rezept fragen, mit unterschiedlichen Nuancen antwortet. Heute fügt er zuerst den Guanciale hinzu, morgen die Eier, übermorgen ändert er die Reihenfolge der Nudeln. Das Endergebnis ist immer Carbonara, aber nie genau dasselbe. Genau das passiert mit Großen Sprachmodellen: gleicher Input, unterschiedliche Outputs. Immer.*

Es ist ein Phänomen, das jeder, der jemals mit ChatGPT gechattet hat, gut kennt, das aber bis heute als eine intrinsische Eigenschaft der künstlichen Intelligenz abgetan wurde. "Das ist normal", sagten die Experten, "das ist Teil des Sampling-Prozesses." Als ob es unvermeidlich wäre, dass ein deterministisches mathematisches System zufällige Ergebnisse liefert.

[Thinking Machines Lab](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/), das von KI-Veteranen geführte Startup, das kürzlich erhebliche Investitionen angezogen hat, beschloss, sich nicht mit dieser Erklärung zufrieden zu geben. Ihr neuestes Paper, das im September 2025 veröffentlicht wurde, identifiziert nicht nur das Problem: Es löst es. Und die Lösung ist ebenso elegant wie unerwartet.

## Wenn Zahlen anarchisch werden

Um den Kern des Problems zu verstehen, müssen wir einen Sprung in die Computermathematik machen. Wie in "Und täglich grüßt das Murmeltier", dem Film, in dem Bill Murray denselben Tag unendlich oft mit unmerklichen Variationen wiedererlebt, scheinen auch Computer dazu verdammt zu sein, dieselben Berechnungen zu wiederholen und leicht unterschiedliche Ergebnisse zu erhalten. Aber diesmal steckt keine existenzielle Lektion dahinter: Es ist die Physik der Prozessoren.

Der Hauptschuldige heißt "Nicht-Assoziativität von Gleitkommazahlen". In der Mathematik sollte (a+b)+c immer gleich a+(b+c) sein. Auf Computern springt diese Regel jedoch fröhlich aus dem Fenster. Es ist, als ob jedes Mal, wenn Sie eine Berechnung durchführen, die Reihenfolge, in der Sie die Zahlen addieren, das Endergebnis ändert.

Horace He, der leitende Forscher am Thinking Machines Lab, erklärt in dem Paper, dass [dieses Phänomen auf die Art und Weise zurückzuführen ist, wie Prozessoren sehr große und sehr kleine Zahlen zusammen verarbeiten](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/). Es ist ein bisschen so, als würde man versuchen, den Durchschnitt der Einwohnerzahl Roms und das Gewicht eines Sandkorns zu berechnen: Die begrenzte Präzision von Computern führt dazu, dass einige Details unweigerlich verloren gehen.

## Die Anatomie des Fehlers: Im Inneren der drei Säulen des Indeterminismus

Um den vollen Umfang der Lösung von Thinking Machines Lab zu verstehen, ist es notwendig, in das schlagende Herz eines Transformers einzutauchen. Wie ein Uhrmacher, der eine Patek Philippe zerlegt, um zu verstehen, warum sie ein paar Sekunden am Tag verliert, mussten die Forscher jede kritische Komponente des Modells sezieren, um zu identifizieren, wo der Indeterminismus entstand.

Die Architektur eines modernen Großen Sprachmodells stützt sich auf drei grundlegende Säulen, von denen jede auf unterschiedliche Weise zum Problem beiträgt. Es ist wie ein Kammerorchester, in dem jede Sektion ihre eigenen Besonderheiten hat: Die Geigen (RMSNorm) erzeugen subtile Dissonanzen, die Blechbläser (Matrixmultiplikationen) verstärken die Fehler, und die Holzbläser (Aufmerksamkeitsmechanismus) verwandeln kleine Variationen in dramatische Veränderungen der endgültigen Harmonie.

RMSNorm, ein Akronym für Root Mean Square Normalization, ist vielleicht die am einfachsten zu verstehende und paradoxerweise am einfachsten zu korrigierende Komponente. [Ihre Funktion ist es, die Eingangswerte zu normalisieren, um das Training zu stabilisieren](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/), ein bisschen wie ein Equalizer, der die Lautstärke unabhängig von der Intensität der Quelle konstant hält. Das Problem tritt auf, wenn die "Batch-Größe" (die Anzahl der gleichzeitig verarbeiteten Anfragen) zu klein ist.

Stellen Sie sich einen Dirigenten vor, der manchmal 100 Musiker, manchmal nur 10 dirigieren muss. Mit 100 Musikern kann er jeder Sektion eine spezifische Rolle zuweisen und eine präzise Kontrolle behalten. Mit nur 10 muss er einige bitten, ihre Instrumente zu verdoppeln, was unweigerlich die Dynamik der Aufführung verändert. RMSNorm verhält sich genauso: Wenn nur wenige Anfragen zu bearbeiten sind, ist es gezwungen, seine Parallelisierungsstrategie zu ändern, was zu Abweichungen bei den Berechnungen führt.

Die Lösung von Thinking Machines Lab ist so einfach wie radikal: Ignorieren Sie die problematischen Fälle. Wenn die Batch-Größe zu klein ist, um eine optimale Parallelisierung zu gewährleisten, akzeptiert das System einen Leistungsverlust, um die Konsistenz zu wahren. Es ist eine tiefgreifende philosophische Entscheidung: Es ist besser, immer konsistent zu sein als gelegentlich schnell.

Matrixmultiplikationen stellen eine Herausforderung von höherer Komplexität dar. Hier geht es nicht nur darum, eine Berechnung zu parallelisieren, sondern die "Tensor Cores", spezialisierte Recheneinheiten in modernen GPUs, die Tausende von gleichzeitigen Operationen ausführen können, optimal zu nutzen. Es ist, als würde man von einem traditionellen Klavier zu einer Kirchenorgel mit Hunderten von Registern wechseln: Die Leistung ist immens, aber die Komplexität der Steuerung wächst exponentiell.

Das Problem entsteht, wenn die Dimensionen der Matrizen zu klein sind, um diese spezialisierten Einheiten voll auszunutzen. In diesen Fällen greifen die GPU-Treiber auf alternative Strategien namens "Split-K" zurück, bei denen die Multiplikation entlang der Reduktionsdimension statt entlang der Ausgabedimensionen aufgeteilt wird. [Es ist eine brillante Technik zur Optimierung der Leistung, führt aber zu Variabilität in den Ergebnissen](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/), da sie die Reihenfolge der mathematischen Operationen ändert.

Die von Thinking Machines Lab gewählte Lösung ist scheinbar kontraintuitiv: Immer dieselbe Kernel-Konfiguration zu verwenden, unabhängig von der Größe der Matrizen. Es ist, als würde man beschließen, immer mit derselben Orchesterbesetzung zu spielen, auch wenn das Musikstück es nicht erfordert. Man verliert etwas an Effizienz, gewinnt aber an Vorhersagbarkeit.

Die dritte Säule, der Aufmerksamkeitsmechanismus, ist diejenige, die die größten Herausforderungen mit sich bringt. Es ist kein Zufall, dass die Aufmerksamkeit das Herzstück der Transformer-Architektur ist, die Komponente, die es dem Modell ermöglicht, auf verschiedene Teile des Inputs "aufzupassen", um jedes einzelne Wort zu erzeugen. Es ist wie ein Regisseur, der in jedem Moment der Szene entscheiden muss, auf welche Schauspieler er die Kamera richtet, basierend auf allem, was zuvor passiert ist.

Der Aufmerksamkeitsmechanismus führt zwei zusätzliche Komplexitätsebenen ein. Erstens muss er Reduktionen sowohl entlang der Merkmalsdimension als auch entlang der Sequenzdimension handhaben, was eine Verflechtung von Abhängigkeiten schafft, die es fast unmöglich macht, eine feste Berechnungsreihenfolge beizubehalten. Zweitens muss er mit allen modernen Inferenzoptimierungen interagieren: Chunked Prefill (wo lange Sequenzen in Stücken verarbeitet werden), Prefix Caching (wo gemeinsame Teile von Gesprächen wiederverwendet werden) und parallele Dekodierung.

[Das heimtückischste Problem tritt in der sogenannten "Dekodierungsphase" auf](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/), wenn das Modell ein Wort nach dem anderen erzeugt. In dieser Phase ist die Länge der Anfrage typischerweise sehr klein (oft nur ein Token), aber der Cache der Schlüssel und Werte kann riesig sein (Tausende von Token des vorherigen Kontexts). Es ist, als würde man einen Solosänger bitten, von einem Symphonieorchester begleitet aufzutreten: Das Kräfteverhältnis ist völlig unausgewogen.

Um eine akzeptable Leistung aufrechtzuerhalten, greifen Systeme auf Techniken wie "Split-KV" oder "FlashDecoding" zurück, die die Verarbeitung entlang der Cache-Dimension parallelisieren. Aber auch hier führt diese Parallelisierung zu Variabilität in der Reihenfolge der Berechnungen. Die Lösung von Thinking Machines Lab erfordert eine tiefgreifende Änderung dieser Algorithmen, indem eine Strategie mit "fester Aufteilungsgröße" anstelle einer Strategie mit "fester Anzahl von Aufteilungen" übernommen wird.

Es ist ein subtiler, aber grundlegender Unterschied. Anstatt zu sagen "immer in 8 Teile teilen", sagt das System "jeder Teil muss immer 256 Elemente haben". Auf diese Weise bleibt die Reihenfolge der Operationen unabhängig von der Gesamtlänge der Sequenz identisch. Es ist, als würde man entscheiden, dass jeder Musiker immer genau 4 Takte spielen muss, unabhängig von der Länge des Stücks.

Die Eleganz dieser Lösung liegt in ihrer Universalität: Sobald alle drei Säulen "batch-invariant" gemacht wurden, wird das gesamte System deterministisch. Es ist nicht notwendig, die Transformer-Architektur neu zu gestalten oder neue Algorithmen zu erfinden. Es genügt sicherzustellen, dass sich jede Komponente immer auf die gleiche Weise verhält, unabhängig vom Kontext, in dem sie ausgeführt wird.
![inference.jpg](inference.jpg)
[Von thinkingmachines.ai](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/)

## Batch-Invarianz: Der geheime Schlüssel

Aber hier ist der Paukenschlag, der eines Tech-Thrillers würdig ist: Das eigentliche Problem liegt nicht im Wettbewerb zwischen den GPU-Prozessoren, wie frühere Theorien behaupteten. Es ist etwas viel Subtileres und paradoxerweise leichter zu lösen.

Die Entdeckung von Thinking Machines Lab ist, dass sich das Verhalten von LLMs je nachdem ändert, wie viele Anfragen zusammen verarbeitet werden. Es ist, als würde unser Sternekoch sein Rezept ändern, je nachdem, wie viele Gedecke er gleichzeitig zubereiten muss. Gleiches Gericht, gleiche Zutaten, aber das Endergebnis hängt von der aktuellen Arbeitsbelastung ab.

Dieses Phänomen hat einen technischen Namen: Mangel an "Batch-Invarianz". Einfach ausgedrückt bedeutet dies, dass die Verarbeitung einer einzelnen Anfrage allein oder zusammen mit 100 anderen zu unterschiedlichen Antworten auf dieselbe Frage führen kann. [Die Forscher haben diesen Effekt mit überraschenden Experimenten nachgewiesen](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/): Indem sie einem Qwen-Modell 1000 Mal dieselbe Frage zu Richard Feynman stellten, erhielten sie 80 verschiedene Antworten, wobei die erste Abweichung genau beim 103. Token auftrat.

Die von Thinking Machines Lab vorgeschlagene Lösung ist elegant in ihrer Einfachheit: Ändern Sie die "Kernel" (die grundlegenden Rechenblöcke) so, dass sie immer die gleichen Ergebnisse liefern, unabhängig davon, wie viele andere Operationen parallel ausgeführt werden. Es ist, als würde man unserem Koch beibringen, immer dieselbe Abfolge von Schritten zu befolgen, egal ob er für eine oder für hundert Personen kocht.
![batch.jpg](batch.jpg)
[Von thinkingmachines.ai](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/)

## Der Preis der Konsistenz

Wie in jeder Geschichte technologischer Innovationen bringt die Lösung Kompromisse mit sich. Die vom Team entwickelten "batch-invarianten" Kernel sind langsamer als die Standard-Kernel. Glücklicherweise nicht viel: Bei Tests auf einem Server mit einer einzelnen GPU unter Verwendung des Qwen-3-8B-Modells lag die Verlangsamung bei etwa 60 % im Vergleich zur optimierten Version und sank mit einigen Verbesserungen an der Attention-Implementierung auf 30 %.

Das mag wie ein hoher Preis erscheinen, aber bedenken Sie die Auswirkungen. [Der Indeterminismus von LLMs ist nicht nur ein ästhetisches Ärgernis](https://dataconomy.com/2025/09/11/tml-defeating-nondeterminism-in-llm-inference/): Er beeinträchtigt die wissenschaftliche Reproduzierbarkeit, macht ein genaues Debugging unmöglich und verwandelt vor allem das, was ein "On-Policy"-Verstärkungslernen sein sollte, in etwas völlig anderes.

Es ist ein bisschen so, als würde man versuchen, einen Formel-1-Fahrer auf einem Simulator zu trainieren, der bei jedem Einschalten die Gesetze der Physik ändert. Der Fahrer lernt, sich an die Variationen anzupassen, aber er lernt nicht wirklich, dieses spezielle Auto zu fahren.

## Die stille Revolution des RL

Hier kommt einer der interessantesten Aspekte der Forschung von Thinking Machines Lab ins Spiel. Das Verstärkungslernen, die Technik hinter den fortschrittlichsten Modellen wie ChatGPT, basiert auf der Idee, dass die KI aus ihren eigenen Erfahrungen lernt. Aber wenn die KI jedes Mal, wenn sie dieselbe Aktion "versucht", ein leicht unterschiedliches Ergebnis erhält, lernt sie dann wirklich aus derselben Erfahrung?

Die Forscher haben gezeigt, dass [der Indeterminismus das "On-Policy"-Lernen subtil in "Off-Policy"-Lernen verwandelt](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/) und eine Diskrepanz zwischen dem, was das Modell während des Trainings tut, und dem, was es bei der Verwendung tut, schafft. Es ist, als würde ein Musiker auf einem verstimmten Klavier üben und dann auf einem gestimmten spielen: Der Unterschied ist subtil, aber grundlegend.

Mit den deterministischen Kerneln von Thinking Machines Lab verschwindet dieses Problem. In ihren Experimenten mit einer RL-Konfiguration, die auf den Bigmath-Datensatz angewendet wurde, erzielte das Team eine perfekt flache KL-Divergenz bei Null, was eine perfekte Übereinstimmung zwischen Training und Inferenz anzeigt. Es ist der Heilige Gral des maschinellen Lernens: ein System, das sich genau so verhält, wie es trainiert wurde.

## Die industrielle Landschaft: Wer gewinnt den Krieg der Reproduzierbarkeit?

In der Welt der künstlichen Intelligenz, in der sich die Tech-Giganten mit immer größeren und leistungsfähigeren Modellen messen, hat Thinking Machines Lab beschlossen, einen anderen Kampf zu führen. Während sich OpenAI, Google und Anthropic auf die rohe Kraft ihrer Systeme konzentrieren, hat sich dieses relativ kleine Team entschieden, auf Präzision zu setzen. Es ist die klassische Geschichte von David gegen Goliath, aber diesmal ist Davids Schleuder die reine Mathematik.

Das Startup, das von ehemaligen Forschern einiger der renommiertesten Unternehmen der Branche gegründet wurde, repräsentiert einen völlig anderen Ansatz für die KI-Forschung. [Es geht nicht darum, das größte oder schnellste Modell zu erstellen, sondern darum, tiefgreifend zu verstehen, wie diese Systeme wirklich funktionieren](https://americanbazaaronline.com/2025/09/11/inside-thinking-machines-lab-muratis-12-billion-ai-startup-tackles-reproducibility-467536/). Es ist ein bisschen wie der Unterschied zwischen dem Bau eines immer leistungsfähigeren Rennwagens und dem Verständnis, warum das Auto manchmal nach links fährt, wenn es geradeaus fahren sollte.

Das Timing dieser Forschung ist kein Zufall. Die KI-Industrie befindet sich an einem entscheidenden Wendepunkt, an dem der Wettlauf um reine Leistung reiferen Überlegungen zu Zuverlässigkeit, Sicherheit und Vorhersagbarkeit weicht. Es ist der Moment, in dem ein jugendlicher Sektor beginnt, sich wie ein Erwachsener zu verhalten, und die Reproduzierbarkeit ist eines der ersten Anzeichen dieser Reifung.

Die kritischsten Sektoren erheben bereits ihre Stimme. In der Gesundheitsbranche, wo KI-Algorithmen zunehmend für Diagnosen und Behandlungspläne eingesetzt werden, ist die Vorstellung, dass dasselbe Symptom zu unterschiedlichen Bewertungen führen kann, einfach inakzeptabel. Es ist, als hätte man ein Thermometer, das jedes Mal, wenn man es benutzt, unterschiedliche Temperaturen anzeigt: Vielleicht ist das Fieber immer da, aber nicht zu wissen, ob es 38 oder 39 Grad sind, macht den Unterschied zwischen einem Paracetamol und einem Krankenhausaufenthalt aus.

Der Finanzsektor ist nicht anders. Automatisierte Handelsalgorithmen und Risikobewertungssysteme müssen in einer Welt operieren, in der die Reproduzierbarkeit keine Präferenz, sondern eine regulatorische Anforderung ist. [Aufsichtsbehörden beginnen zu fordern, dass KI-Modelle, die für Kredit- oder Investitionsentscheidungen verwendet werden, nachvollziehbare und überprüfbare Ergebnisse liefern](https://dataconomy.com/2025/09/11/tml-defeating-nondeterminism-in-llm-inference/). Es ist unmöglich, einem Richter zu erklären, warum derselbe Algorithmus bei zwei identischen Hypothekenanträgen unterschiedliche Meinungen abgegeben hat.

Auch die wissenschaftliche Forschung wird sich des Problems bewusst. Wenn ein wissenschaftliches Paper behauptet, bestimmte Ergebnisse mit einem KI-Modell erzielt zu haben, müssen andere Forscher in der Lage sein, diese Experimente exakt zu replizieren. Es ist die Grundlage der wissenschaftlichen Methode, die durch den Indeterminismus der LLMs in Frage gestellt wird. Als ob jedes Mal, wenn Sie ein Physikexperiment replizieren, die Schwerkraft etwas anders wäre.

Aber die Auswirkungen gehen weit über diese offensichtlich kritischen Sektoren hinaus. Denken Sie an die Auswirkungen auf das Debugging und die Softwareentwicklung. Wenn sich eine KI-basierte Anwendung derzeit unerwartet verhält, befinden sich die Entwickler in einer kafkaesken Situation: Der Fehler könnte in ihrem Code liegen, oder es könnte sich einfach um eine weitere Manifestation des Indeterminismus des Modells handeln. Es ist, als würde man versuchen, eine Uhr zu reparieren, die manchmal von selbst beschließt, schneller oder langsamer zu gehen.

Die Lösung von Thinking Machines Lab verspricht, diese Geisterjagd in einen normalen Debugging-Prozess zu verwandeln. Wenn das Modell immer die gleichen Ausgaben für die gleichen Eingaben erzeugt, ist jedes anomale Verhalten notwendigerweise auf einen echten Fehler zurückzuführen, nicht auf eine zufällige Schwankung. Es ist der Unterschied zwischen einem Detektiv in einer Welt, in der sich die Beweise spontan ändern, und einem Detektiv in einer Welt, in der die Beweise konsistent bleiben.

Der interessanteste Aspekt dieser Dynamik ist, dass keiner der großen Akteure der Branche diesem Problem Priorität eingeräumt zu haben scheint. OpenAI, Google, Meta und die anderen Giganten sind alle von der Jagd nach Leistung besessen, während die Frage der Reproduzierbarkeit im Hintergrund geblieben ist. Es ist eine dieser seltenen Situationen in der Tech-Welt, in der ein Startup Unternehmen mit hundertmal mehr Ressourcen tatsächlich zuvorkommen kann, einfach weil es das richtige Problem zur richtigen Zeit identifiziert hat.

Natürlich wird es nicht einfach sein, die Industrie davon zu überzeugen, eine Lösung zu übernehmen, die eine Verlangsamung von 30-60 % mit sich bringt. In der Welt der KI, in der Millisekunden Latenz über den Erfolg oder Misserfolg eines Produkts entscheiden können, wird jeder Kompromiss bei der Leistung mit Misstrauen betrachtet. Aber die Anzeichen für einen Wandel sind bereits da.

Einige wegweisende Unternehmen beginnen, mit "deterministischen" Versionen ihrer Systeme für spezifische Anwendungen zu experimentieren. Es überrascht nicht, dass die ersten Anwender genau diejenigen sind, die in stark regulierten Sektoren tätig sind, in denen die Kosten des Indeterminismus den Nutzen einiger Millisekunden weniger Latenz bei weitem übersteigen.

## Auf dem Weg in eine deterministische Zukunft

Das eigentliche Spiel wird gespielt, wenn die batch-invarianten Kernel von Thinking Machines Lab so optimiert sind, dass sie den Leistungsunterschied erheblich verringern. An diesem Punkt wird die Frage nicht mehr lauten: "Können wir es uns leisten, deterministisch zu sein?", sondern "Können wir es uns leisten, es nicht zu sein?".

Die von Thinking Machines Lab vorgeschlagene Lösung ist noch nicht für die Massenproduktion bereit. Der Code ist auf GitHub als Machbarkeitsnachweis verfügbar, erfordert aber erhebliche Änderungen an bestehenden Inferenz-Pipelines. Die Auswirkungen sind jedoch enorm.

Stellen Sie sich eine Welt vor, in der LLMs immer die gleiche Antwort auf die gleiche Frage geben. Wir sprechen nicht von weniger kreativen oder starreren KIs, sondern von zuverlässigeren und vorhersagbareren Systemen. Ein virtueller Assistent, der Ihnen immer den gleichen medizinischen Rat für das gleiche Symptom gibt. Ein Übersetzungssystem, das nicht bei jedem Neustart die Version des Textes ändert. Ein Finanzanalysemodell, das immer die gleiche Bewertung für die gleichen Daten liefert.

Es ist interessant festzustellen, wie sich diese Forschung in einen breiteren Trend zu dem einfügt, was wir als "verantwortungsvolle KI" bezeichnen könnten. Nach Jahren eines ungezügelten Wettlaufs um immer größere und leistungsfähigere Modelle beginnt die Industrie, sich reifere Fragen zu stellen: nicht nur "Was können wir tun?", sondern auch "Was sollten wir tun?" und "Wie können wir es besser machen?".

In diesem Zusammenhang könnte sich Thinking Machines Lab in der beneidenswerten Lage befinden, vor anderen zu einer Erkenntnis gelangt zu sein, die unvermeidlich werden wird. Wie es in der Technologie oft der Fall ist, könnte das, was heute wie eine Nischenanforderung erscheint, morgen zum Industriestandard werden. Und wer als Erster in diese Richtung investiert hat, wird einen erheblichen Wettbewerbsvorteil haben.

Der faszinierendste Aspekt dieser Geschichte ist, dass die Lösung keine technologischen Revolutionen oder wissenschaftlichen Durchbrüche erfordert. Es ist ein reines Ingenieurproblem, das mit mathematischer Strenge und Liebe zum Detail gelöst wurde. In einer Zeit, in der die KI immer magischer und unverständlicher erscheint, erinnert uns Thinking Machines Lab daran, dass hinter jedem intelligenten Algorithmus immer solide Mathematik und präzise Implementierungen stehen.

Vielleicht betrifft die wahre Lehre aus dieser Forschung nicht so sehr die LLMs, sondern die Reife eines ganzen Sektors. Wir sind an dem Punkt angelangt, an dem es nicht mehr ausreicht, dass künstliche Intelligenz funktioniert: Sie muss auf vorhersehbare, nachvollziehbare und reproduzierbare Weise funktionieren. Es ist der Übergang von der Kunst zur Wissenschaft, von der Alchemie zur Chemie.

Wer hätte schließlich gedacht, dass der wahre evolutionäre Sprung in der KI nicht von größeren Modellen oder ausgefeilteren Algorithmen kommen würde, sondern von der einfachen Fähigkeit, immer dasselbe auf dieselbe Weise zu tun? Wie in den besten Film-Twists war die Antwort die ganze Zeit über in Sichtweite versteckt. Man musste nur den Mut haben, danach zu suchen.
