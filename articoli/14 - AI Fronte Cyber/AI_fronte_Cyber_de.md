---
tags: ["Security", "Ethics & Society", "Business"]
date: 2025-08-16
---

# KI unter Belagerung: Chroniken von der Cyber-Front
*von Dario Ferrero (VerbaniaNotizie.it)*
![fronte_AI.jpg](fronte_AI.jpg)

*April 2023: Samsung-Ingenieure teilen unwissentlich proprietären Quellcode mit ChatGPT. Mai 2025: Forscher entdecken, dass wissenschaftliche Arbeiten versteckte Anweisungen enthalten, um KI-gestützte Peer-Review-Systeme zu manipulieren. Zwischen diesen beiden Ereignissen entfaltet sich eine alarmierende Chronik, die erzählt, wie die künstliche Intelligenz sowohl zum Raubtier als auch zur Beute des neuen Cyber-Ökosystems geworden ist.*

## Der Preis der digitalen Unschuld

Die Geschichte beginnt mit dem, was wir als die verlorene Unschuld der KI-Ära bezeichnen könnten. [Im Jahr 2023 musste Samsung die Nutzung von ChatGPT und anderen generativen KI-Tools verbieten](https://www.bloomberg.com/news/articles/2023-05-02/samsung-bans-chatgpt-and-other-generative-ai-use-by-staff-after-leak) auf seinen Firmengeräten, nachdem [drei Ingenieure in getrennten Vorfällen unwissentlich sensible Unternehmensdaten](https://techcrunch.com/2023/05/02/samsung-bans-use-of-generative-ai-tools-like-chatgpt-after-april-internal-data-leak/) mit dem OpenAI-Chatbot geteilt hatten. Dies war kein ausgeklügelter Angriff oder Industriespionage: Es war einfach das Ergebnis von Mitarbeitern, die in dem Versuch, ihre Arbeit zu optimieren, KI als persönlichen Assistenten eingesetzt hatten, ohne zu merken, dass sie ein System fütterten, das aus jeder Konversation lernt.

Die durchgesickerten Daten umfassten Halbleiter-Quellcode, interne Sitzungsprotokolle und Details zu proprietärer Hardware. Samsung war nicht im herkömmlichen Sinne gehackt worden: Es hatte sich selbst gehackt, ein Opfer dessen, was Experten als "Schatten-KI" bezeichnen - die unbefugte Nutzung von künstlicher Intelligenz durch Mitarbeiter.

Dieser Vorfall war der erste Weckruf für den Unternehmenssektor und enthüllte eine unbequeme Wahrheit: Unternehmen stürzten sich auf die Einführung von KI, ohne die Sicherheitsauswirkungen vollständig zu verstehen. Wie eine moderne digitale Büchse der Pandora erwies sich die Kontrolle über die Inhalte der KI-Welt nach ihrer Öffnung als unendlich komplexer als erwartet.

## Das Paradox des exponentiellen Wachstums

Die Zahlen erzählen eine besorgniserregende Geschichte: Im Jahr 2024 erreichten die durchschnittlichen Kosten eines Cybersicherheitsvorfalls für kleine und mittlere Unternehmen 1,6 Millionen US-Dollar, gegenüber 1,4 Millionen US-Dollar im Jahr 2023, wobei fast 40 % der kleinen Unternehmen wichtige Daten verloren und erhebliche Ausfallzeiten erlitten. Gleichzeitig nehmen KI-gestützte Angriffe zu, während sich die Cloud-Sicherheit weiterentwickelt, was Unternehmen dazu veranlasst, Echtzeit-KI-Abwehrmaßnahmen zu implementieren, um Schritt zu halten.

Das Paradox ist klar: Während Unternehmen KI einsetzen, um sich besser zu verteidigen, nutzen Angreifer dieselben Technologien, um ausgefeiltere Angriffe zu starten. Es ist, als würde man eine digitale Version des Kalten Krieges miterleben, in der jede defensive Innovation sofort durch einen offensiven Gegenzug ausgeglichen wird.

Branchenführer erwarten für 2025 eine immer komplexere Bedrohungslandschaft, aber die größte Herausforderung liegt nicht so sehr in der technischen Raffinesse der Angriffe als vielmehr in ihrer Demokratisierung. Die KI hat Angriffstechniken, die einst jahrelange Spezialisierung erforderten, für jedermann zugänglich gemacht.

## Die neuen Grenzen des Angriffs: wenn die KI sich selbst verrät

Von 2023 bis 2024 gab es zahlreiche Datenlecks und Datenschutzvorfälle im Zusammenhang mit ChatGPT, die die kritischen Sicherheitsherausforderungen von KI-Technologien verdeutlichen. Aber diese Episoden sind nur die Spitze des Eisbergs eines viel komplexeren Phänomens: das Aufkommen völlig neuer Angriffsvektoren, die die Natur der künstlichen Intelligenz selbst ausnutzen.

Ein Paradebeispiel ist die Manipulation von akademischen Peer-Review-Systemen. Forscher haben herausgefunden, dass einige Arbeiten versteckte Anweisungen enthielten, die speziell darauf ausgelegt waren, die in der wissenschaftlichen Bewertung verwendeten KI-Systeme zu beeinflussen. Es ist, als hätte jemand einen Weg erfunden, den Schiedsrichtern eines Spiels unsichtbare Anweisungen zuzuflüstern und so das Ergebnis zu verändern, ohne dass es jemand merkt.

Diese als "Prompt-Injektion" bekannte Technik ist eine der heimtückischsten Schwachstellen der KI-Ära. Im Gegensatz zu herkömmlichen Cyberangriffen, die Fehler im Code ausnutzen, nutzt die Prompt-Injektion die grundlegende Eigenschaft von Sprachmodellen aus: ihre Fähigkeit, Anweisungen in natürlicher Sprache zu verstehen und zu befolgen. Es ist das digitale Äquivalent des Bauchredners, der die Marionette sagen lässt, was er will, aber in diesem Fall steuert die Marionette kritische Geschäftssysteme.
![prompt_injection.jpg](prompt_injection.jpg)
[*Bild von arthur.ai*](https://www.arthur.ai/blog/from-jailbreaks-to-gibberish-understanding-the-different-types-of-prompt-injections)

## Das Ökosystem der Schwachstellen: der Fall MCP

Das Model Context Protocol (MCP), das entwickelt wurde, um die Interaktion zwischen großen Sprachmodellen und externen Tools zu vereinfachen, ist eine perfekte Fallstudie dafür, wie gute Absichten neue Angriffsflächen schaffen können. Eine Sammlung von acht realen KI-bezogenen Vorfällen in den letzten 24 Monaten unterstreicht die Risiken der Nutzung und Implementierung von KI ohne angemessene Sicherheitsmaßnahmen.

Das MCP sollte die ultimative Lösung für die Verbindung von KI mit der realen Welt sein und es Modellen ermöglichen, nahtlos mit Datenbanken, APIs und externen Diensten zu interagieren. In Wirklichkeit hat es sich als eine Brücke erwiesen, die Angreifer in beide Richtungen überqueren können. [Ein Community-Repository](https://github.com/Puliczek/awesome-mcp-security) documenta oltre cinquanta ricerche accademiche pubblicate solo nei primi mesi del 2025, rivelando vulnerabilità che spaziano dall'[esfiltrazione di dati da server Slack](https://embracethered.com/blog/posts/2025/security-advisory-anthropic-slack-mcp-server-data-leakage/) all'[accesso non autorizzato a repository GitHub privati](https://invariantlabs.ai/blog/mcp-github-vulnerability).

Das grundlegende Problem des MCP ist architektonischer Natur: Es wurde unter der Annahme entworfen, dass alle Komponenten des Ökosystems vertrauenswürdig sind. Das ist so, als würde man eine Stadt ohne Mauern bauen, weil man annimmt, dass alle Besucher Freunde sind. Wenn sich diese Annahme als falsch erweist, bricht das gesamte System wie ein Kartenhaus zusammen.
![MCP_method.jpg](MCP_method.jpg)
[*Bild von descope.com*](https://www.descope.com/learn/post/mcp)

## Die Demokratisierung des Hackens: wenn jeder Anonymous sein kann

Die Prognosen für 2025 konzentrieren sich auf operative Sicherheitsrisiken und die sich entwickelnden Herausforderungen durch KI, aber der vielleicht besorgniserregendste Aspekt ist die Demokratisierung der Offensivfähigkeiten. Die KI hat die Eintrittsbarriere für die Durchführung anspruchsvoller Cyberangriffe drastisch gesenkt.

Nehmen wir den Fall der Prompt-Injektion: Ein Angreifer muss keine Programmiersprachen mehr kennen oder komplexe Architekturen verstehen. Es genügt, eine Anfrage in natürlicher Sprache geschickt zu formulieren, um ein System potenziell zu kompromittieren. Es ist, als ob plötzlich jeder Houdini werden könnte, indem er die Ketten einfach bittet, sich zu lösen.

Um diese Dynamik zu verstehen, können wir mehrere Plattformen untersuchen, die Prompt-Injektionsangriffe simulieren. Es gibt Tools wie die ChatGPT Jailbreak Challenge oder die AI Security Sandbox, die lehren, wie man KI-Schwachstellen identifiziert. In den ersten Stufen kann das Umgehen der KI-Beschränkungen so einfach sein wie die Verwendung von Phrasen wie "Vorherige Anweisungen ignorieren" oder "Eine Ausnahme machen".

Je weiter man jedoch fortschreitet, desto komplexere Filter implementieren die Systeme, wie z. B. die Erkennung von Schlüsselwörtern oder vordefinierte Antworten. Dennoch können selbst diese Barrieren mit einem methodischen Ansatz und ein wenig Einfallsreichtum überwunden werden, was zeigt, wie entscheidend ein robustes Design von Sprachmodellen ist.

## Die Angriffe der Zukunft: das Emoji als Trojanisches Pferd

Die innovativsten Angriffstechniken nutzen scheinbar harmlose Aspekte der digitalen Kommunikation aus. "Emoji-Schmuggel" ist ein perfektes Beispiel für diesen Trend: [Forscher von Mindgard und der Lancaster University haben gezeigt](https://securitybrief.asia/story/emojis-used-to-hide-attacks-bypass-major-ai-guardrails), wie Angreifer bösartige Anweisungen verstecken können, indem sie Emojis verwenden, um [die KI-Filter von Microsoft, Nvidia und Meta zu umgehen](https://cybersecuritynews.com/hackers-can-bypass-microsoft-nvidia-meta-ai-filters/).

Die Forschung testete sechs der am weitesten verbreiteten Guardrail-Systeme und stellte fest, dass viele stark auf die Erkennung statischer Muster angewiesen sind und eine unzureichende Widerstandsfähigkeit gegen gegnerische Angriffe aufweisen.

Es ist, als würde man eine geheime Botschaft im Lächeln der Mona Lisa verstecken: scheinbar harmlos, aber potenziell verheerend für diejenigen, die wissen, wie man sie entschlüsselt. Diese Technik ist besonders heimtückisch, weil sie die natürliche Tendenz des Menschen ausnutzt, Emojis als harmlose dekorative Elemente zu betrachten, obwohl sie in Wirklichkeit zu echten Angriffsvektoren werden können.

Eine weitere aufkommende Technik, die von Forschern dokumentiert wurde, ist [Datenschmuggel durch fortschrittliche Kodierungstechniken](https://embracethered.com/blog/posts/2025/sneaky-bits-and-ascii-smuggler/), die KI in einen unfreiwilligen Spion verwandeln kann. Angreifer können das System anweisen, sensible Daten in scheinbar harmlose Zeichenfolgen oder URLs einzubetten. Selbst wenn die KI die Anfrage nicht ausführen kann, zeichnen die Serverprotokolle den Versuch dennoch auf, sodass der Angreifer die Informationen über Seitenkanäle abrufen kann. Es ist das digitale Äquivalent, eine geheime Nachricht von einer Brieftaube überbringen zu lassen, die nicht weiß, dass sie geheime Informationen transportiert.

[Jason Haddix](https://mlsecops.com/podcast/holistic-ai-pentesting-playbook), ein Veteran der offensiven Sicherheit und CEO von Arcanum Information Security, gilt als einer der führenden Experten für das Hacken von KI-Systemen. Er hat eine proprietäre und ganzheitliche Methodik für KI-Penetrationstests entwickelt, die das gesamte Ökosystem von KI-Anwendungen und nicht nur die Modelle untersucht. Haddix hat auch eine Open-Source-Taxonomie für Prompt-Injektionstechniken erstellt, die innovative Taktiken wie "Emoji-Schmuggel" und "Datenschmuggel" durch fortschrittliche Kodierung klassifiziert. Seine Arbeit konzentriert sich auf die Identifizierung und Abwehr von realen Schwachstellen wie überautorisierten API-Schlüsseln und ungeschützten sensiblen Daten in RAG-Systemen und fördert einen Defense-in-Depth-Ansatz für KI-Anwendungen.

## Die Reaktion der Branche: zwischen Innovation und Reaktion

Samsung hat seinen Mitarbeitern kürzlich erlaubt, ChatGPT wieder zu verwenden, jedoch mit neuen Sicherheitsprotokollen, was zeigt, wie die Branche versucht, Innovation und Sicherheit in Einklang zu bringen. Diese Entscheidung stellt einen Mikrokosmos der größeren Herausforderung dar, vor der Unternehmen stehen: wie man die Vorteile der KI nutzt und gleichzeitig die Risiken minimiert.

Die aufkommende Strategie im Unternehmenssektor basiert auf einem mehrschichtigen Ansatz, der an die Tiefenverteidigung mittelalterlicher Burgen erinnert. Keine einzige uneinnehmbare Mauer, sondern eine Reihe konzentrischer Hindernisse, die es den Angreifern zunehmend erschweren, voranzukommen.

Auf der grundlegendsten Ebene wird das Prinzip des geringsten Privilegs angewendet: Jedes KI-System hat nur Zugriff auf die Ressourcen, die zur Erledigung seiner Aufgaben unbedingt erforderlich sind. Das ist so, als würde man einem Kellner nur die Schlüssel zum Speisesaal geben, nicht zum ganzen Hotel.

Die zweite Ebene implementiert Filter und Klassifikatoren für Eingabe und Ausgabe und schafft so eine "konversationale Firewall". Diese Systeme analysieren jede Interaktion, um potenzielle Manipulations- oder Datenexfiltrationsversuche zu identifizieren.

Die dritte Ebene konzentriert sich auf die rigorose Validierung aller Ein- und Ausgaben, um sicherzustellen, dass das System nicht zur Einschleusung von Malware oder zum Extrahieren nicht autorisierter Informationen verwendet werden kann.

## KI als Verteidiger: wenn die Medizin auch die Heilung ist

Unternehmen implementieren Echtzeit-KI-Abwehrmaßnahmen, um KI-gestützte Angriffe abzuwehren, und schaffen so einen kontinuierlichen Innovationszyklus zwischen Offensive und Defensive. Diese Dynamik hat zur Entstehung dessen geführt, was Experten als "KI-gegen-KI-Kriegsführung" bezeichnen - ein Kampf, in dem Algorithmen in einem endlosen Tanz aus Aktion und Reaktion gegen andere Algorithmen antreten.

KI-basierte Abwehrsysteme zeigen beeindruckende Fähigkeiten bei der Identifizierung von Angriffsmustern und der Reaktion in Echtzeit auf aufkommende Bedrohungen. Sie sind besonders wirksam gegen standardisierte Angriffe und bekannte Schwachstellen, bei denen sie große Datenmengen verarbeiten und Anomalien mit für menschliche Analysten unmöglichen Geschwindigkeiten identifizieren können.

Allerdings zeigt die defensive KI immer noch erhebliche Einschränkungen, wenn sie mit der Kreativität und Intuition der anspruchsvollsten menschlichen Angreifer konfrontiert wird. Cybersicherheitsspezialisten besitzen das, was wir den "X-Faktor" nennen könnten - eine Kombination aus Erfahrung, Intuition und Querdenken, die von Algorithmen nicht einfach repliziert werden kann.

## Die geschäftlichen Konsequenzen: die neue Risikoberechnung

Unternehmen müssen jetzt neue Arten von KI-Risiken berücksichtigen, die von der Manipulation von Modellen bis zur Datenexfiltration über unkonventionelle Kanäle reichen. Die Berechnung des Geschäftsrisikos ist enorm kompliziert geworden: Es geht nicht mehr nur darum, Systeme von außen zu schützen, sondern auch darum, zu kontrollieren, wie die eigenen internen Tools missbraucht werden können.

Der Fall Samsung ist nur die Spitze des Eisbergs. Viele Unternehmen stellen fest, dass ihre Mitarbeiter täglich KI-Tools zur Optimierung ihrer Arbeit einsetzen, oft ohne sich der Sicherheitsauswirkungen bewusst zu sein. Das Konzept der "Schatten-KI" ist entstanden - die nicht deklarierte Nutzung von künstlicher Intelligenz, die erhebliche blinde Flecken in der Sicherheitslage von Unternehmen schafft.

Die wirtschaftlichen Folgen sind greifbar und nehmen zu. Prognosen für 2025 deuten darauf hin, dass KI Cyberangriffe erheblich verstärken wird, während die durchschnittlichen Kosten für Vorfälle weiter steigen. Unternehmen befinden sich in einer paradoxen Situation: Sie müssen in KI investieren, um wettbewerbsfähig zu bleiben, aber jede Implementierung führt zu neuen Angriffsflächen.

## Auf dem Weg in eine Zukunft der bewaffneten Koexistenz

Die grundlegende Herausforderung des Jahres 2025 besteht nicht darin, die Risiken der KI zu eliminieren - ein unmögliches Ziel -, sondern zu lernen, sie effektiv zu managen. Wir treten in eine Ära der "bewaffneten Koexistenz" zwischen Innovation und Sicherheit ein, in der das Ziel nicht perfekter Schutz, sondern dynamische Widerstandsfähigkeit ist.

KI-Sicherheitsberichte zeigen, dass Unternehmen lernen, KI-Risiken durch immer ausgefeiltere Abwehrstrategien zu identifizieren und zu mindern. Der Schlüssel zum Erfolg scheint nicht in der absoluten Verhinderung von Vorfällen zu liegen, sondern in der Fähigkeit, Anomalien schnell zu erkennen, effektiv auf Angriffe zu reagieren und sich schnell von Kompromittierungen zu erholen.

Die entstehende Landschaft erinnert an die Anfänge des Internets: eine Umgebung voller Möglichkeiten, aber auch voller Tücken, in der der Unterschied zwischen Erfolg und Misserfolg an der Fähigkeit gemessen wird, Innovation und Besonnenheit in Einklang zu bringen. Die Unternehmen, die in diesem neuen Umfeld erfolgreich sind, sind diejenigen, denen es gelingt, KI zu implementieren und dabei eine "Security by Design"-Mentalität beizubehalten, bei der der Schutz nicht als Einschränkung, sondern als Wegbereiter für nachhaltige Innovation betrachtet wird.

## Epilog: Lehren aus einer Zukunft, die bereits Gegenwart ist

Die Geschichte des Samsung-Ingenieurs, der unwissentlich proprietären Code mit ChatGPT teilt, ist zu einem klassischen Fallbeispiel in Cybersicherheitskursen geworden. Nicht, weil es sich um einen besonders ausgeklügelten Angriff handelt, sondern weil es die Natur der Herausforderungen, die uns erwarten, perfekt verkörpert: Bedrohungen, die aus der Schnittmenge von guten Absichten, neuen Technologien und einem unzureichenden Verständnis der Auswirkungen entstehen.

Künstliche Intelligenz ist weder von Natur aus gut noch schlecht: Sie ist ein mächtiges Werkzeug, das sowohl unsere Fähigkeiten als auch unsere Schwachstellen verstärkt. Die Herausforderung des Jahres 2025 und darüber hinaus wird darin bestehen, die kollektive Weisheit zu entwickeln, die erforderlich ist, um diese Macht auf konstruktive Ziele auszurichten und gleichzeitig wachsam gegenüber den damit verbundenen Risiken zu bleiben.

Wie in jeder Ära des technologischen Wandels, von der Druckerpresse bis zum Internet, wird der Erfolg denen gehören, die sich schnell anpassen können und dabei die Grundprinzipien der Besonnenheit und Verantwortung bewahren. In Mittelerde der KI gewinnt nicht der wendigste Elf oder der mächtigste Zauberer, sondern der Hobbit, der lernt, das Unvorhersehbare zu navigieren - einen Ring (von Daten) nach dem anderen.
