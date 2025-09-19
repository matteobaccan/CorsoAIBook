---
tags: ["Copyright", "Business", "Ethics & Society"]
date: 2025-09-17
author: Dario Ferrero
---

# RSL, das neue Protokoll, das KI für Webinhalte bezahlen lassen will
![rls-money.jpg](rls-money.jpg)

*Wenn künstliche Intelligenz der Pac-Man des digitalen Zeitalters wäre, wäre das Internet sein endloses Labyrinth voller Punkte zum Verschlingen. Nur dass diesmal die Punkte unsere Artikel, unsere Fotos, unsere Videos sind und Pac-Man noch nie in die Tasche gegriffen hat. In diesem digitalen Wildwest-Szenario entsteht [Really Simple Licensing (RSL)](https://rslstandard.org/), ein neuer Standard, der verspricht, etwas Ordnung in das Chaos des wilden Daten-Scrapings für das KI-Training zu bringen.*

## Die Rückkehr des Vaters von RSS

Wie in jeder guten Geschichte über ein technologisches Comeback, die etwas auf sich hält, hat auch diese ihren Ursprung in einer Web-Legende. [Dave Winer](https://techcrunch.com/2025/09/10/rss-co-creator-launches-new-protocol-for-ai-data-licensing/), Miterfinder von RSS in den 90er Jahren, kehrt nicht aus Nostalgie auf die Bühne zurück, sondern mit einer klaren Mission: den Inhaltserstellern die Werkzeuge an die Hand zu geben, um zu entscheiden, wie ihr geistiges Eigentum im Zeitalter der künstlichen Intelligenz genutzt wird.

Neben Winer sind die Hauptakteure des RSL-Projekts [Eckart Walther](https://www.theregister.com/2025/09/11/rsl_content_grabbing_ai_digital_licensing/) - Mitbegründer und CEO des Startups, das den Standard entwickelt - und [Doug Leeds](https://searchengineland.com/really-simple-licensing-461834), ehemaliger Manager bei Yahoo und IAB Tech Lab. Ein Triumvirat, das technische Erfahrung, unternehmerische Vision und tiefes Wissen über den digitalen Markt vereint.

Die Entstehung des Projekts wurzelt in einer Frustration, die viele Verleger teilen: zu sehen, wie ihre Inhalte zum Trainieren von KI-Modellen verwendet werden, ohne ausdrückliche Zustimmung oder Vergütung. "RSL ist ein offener Standard, der es Verlagen ermöglicht, maschinenlesbare Lizenzbedingungen für ihre Inhalte zu definieren, einschließlich Namensnennung, Bezahlung pro Crawl und Bezahlung pro Inferenzkompensation", erklärt die offizielle Website des Projekts.

## Eine GEMA für das digitale Zeitalter

Wenn wir eine Analogie in der realen Welt finden müssten, funktioniert RSL wie eine Hightech-Version der GEMA für Musikrechte, aber angewendet auf die Welt der Webinhalte. Das Protokoll ermöglicht es Verlagen, die Nutzungsbedingungen ihrer Inhalte für KI-Trainingszwecke standardisiert und maschinenlesbar zu definieren.

Technisch basiert RSL auf einem XML-Format, das direkt in Webseiten integriert oder als separater Feed bereitgestellt werden kann. Das System sieht verschiedene Arten von Lizenzen vor: von der einfachen Namensnennung bis hin zu "Pay-per-Crawl"- oder "Pay-per-Inference"-Modellen, bei denen die Vergütung auf der Grundlage der tatsächlichen Nutzung des Inhalts in KI-Modellen berechnet wird.

Die Implementierung ist überraschend elegant in ihrer Einfachheit. Ein Verlag kann festlegen, dass seine Inhalte eine benutzerdefinierte Lizenz für das KI-Training erfordern, oder sie unter Creative Commons mit einfacher Namensnennung zur Verfügung stellen. Es ist, als hätte man ein digitales Schild mit der Aufschrift "Zum Passieren Maut bezahlen", aber in einer Sprache geschrieben, die selbst die ausgeklügeltsten Bots verstehen können.

## Die Web-Giganten mobilisieren sich

Der Start von RSL erfolgte nicht im luftleeren Raum. [Einige der größten Namen im Web](https://www.theverge.com/news/775072/rsl-standard-licensing-ai-publishing-reddit-yahoo-medium) haben beschlossen, die Initiative von Anfang an zu unterstützen: Reddit, Yahoo, Automattic (das Unternehmen hinter WordPress.com), Quora und Medium sind alle als Early Adopters beigetreten.

Die Entscheidung dieser Giganten ist kein Zufall. Insbesondere Reddit hat bereits mit der Monetarisierung seiner Daten für die KI durch direkte Vereinbarungen mit Google und OpenAI experimentiert. [Die Einführung von RSL stellt eine natürliche Weiterentwicklung](https://indianexpress.com/article/artificial-intelligence/reddit-quora-yahoo-rsl-really-simple-licensing-ai-data-scraping-10243214/) dieser Strategie dar, die es ermöglicht, den Lizenzierungsprozess zu automatisieren und zu standardisieren.

Yahoo wiederum bringt einen reichen Schatz an Inhalten mit, der über Jahrzehnte hinweg angesammelt wurde, während Medium und Quora zwei der wichtigsten Plattformen für nutzergenerierte Inhalte darstellen. Ihre Teilnahme signalisiert, dass RSL nicht nur eine Angelegenheit großer Medienunternehmen ist, sondern das gesamte Ökosystem der digitalen Inhaltserstellung betrifft.

## Die Technologie unter der Haube

Aus technischer Sicht stellt sich RSL als natürliche Weiterentwicklung bereits bestehender Schutzmechanismen dar. War robots.txt das digitale Äquivalent eines "Betreten verboten"-Schildes, so ist RSL eher mit einem ausgeklügelten automatischen Ticketsystem zu vergleichen.

Das Protokoll unterstützt verschiedene Zahlungs- und Lizenzierungsmodalitäten. Ein Verlag kann sich dafür entscheiden, ein Abonnement für den Zugriff auf seine Inhalte für KI-Trainingszwecke zu verlangen oder sich für ein Pay-per-Use-Modell zu entscheiden. Die Flexibilität des Systems ermöglicht es auch, unterschiedliche Lizenzen für unterschiedliche Inhaltstypen auf derselben Plattform zu definieren.

Die Integration in bestehende Systeme wurde so konzipiert, dass sie so wenig invasiv wie möglich ist. RSL kann mit robots.txt und anderen Standards koexistieren und fügt eine Granularitätsebene bei der Rechteverwaltung hinzu, die es bisher einfach nicht gab. Es ist, als würde man von einem Ein-/Ausschalter zu einem Dimmer mit unendlichen Abstufungen wechseln.

![diritti.jpg](diritti.jpg)
![diritti2.jpg](diritti2.jpg)
[Beispiele von rslstandard.org](https://rslstandard.org/)

## Die Herausforderungen der Durchsetzung

Natürlich ist im Garten von RSL nicht alles eitel Sonnenschein. Die größte Herausforderung bleibt die der Durchsetzung: Wie kann sichergestellt werden, dass KI-Crawler die angegebenen Lizenzen tatsächlich respektieren? Hier offenbart das Projekt seine noch experimentelle Natur und seine potenziellen Schwächen.

Im Gegensatz zu robots.txt, das von "zivilen" Crawlern fast universell respektiert wurde, betritt RSL ein rechtlich und wirtschaftlich weitaus komplexeres Terrain. Wenn ein KI-Modell die RSL-Lizenzen ignoriert und die Inhalte trotzdem verwendet, was sind die praktischen Konsequenzen? Und vor allem, wie kann ein kleiner Verlag seine Rechte gegenüber Tech-Giganten mit Heerscharen von Anwälten durchsetzen?

Die Antwort befindet sich im Moment noch in der Entwicklung. Das Projekt setzt darauf, dass die großen KI-Unternehmen ein Interesse daran haben, transparente und legale Beziehungen zu den Inhaltsanbietern zu pflegen, insbesondere in einer Zeit, in der die Regulierung des Sektors immer strenger wird.

## Der Datenmarkt entwickelt sich weiter

RSL kommt zu einem besonders interessanten Zeitpunkt für die Datenökonomie. Der 60-Millionen-Dollar-Deal zwischen Reddit und Google für die Nutzung der Inhalte der Plattform für das KI-Training hat Schule gemacht und gezeigt, dass es einen realen und substanziellen Markt für diese Art von Inhalten gibt.

Der neue Standard könnte diesen Markt demokratisieren und es auch kleineren Verlagen ermöglichen, ihre Inhalte zu monetarisieren, anstatt sie einfach von KI-Crawlern "requirieren" zu lassen. Es ist ein bisschen so, als ob nach Jahren, in denen jeder in Ihren Laden kommen und die Ware kostenlos mitnehmen konnte, endlich ein System eingeführt wird, um die Rechnung zu bezahlen.

Die Herausforderung wird darin bestehen, ein Ökosystem zu schaffen, in dem der Wert von Inhalten anerkannt wird, ohne übermäßige Hürden für die Innovation in der KI zu schaffen. Es ist ein empfindliches Gleichgewicht, ähnlich dem, das die Musikindustrie mit dem Aufkommen des Streamings finden musste.

## Wenn Indies auf Majors treffen: Das neue Inhaltsökosystem

Wenn die großen Player wie Reddit und Yahoo die "Major Labels" des digitalen Inhalts darstellen, könnte RSL endlich auch den "Indie-Künstlern" des Webs eine Stimme geben: unabhängigen Bloggern, Kreativen auf Nischenplattformen, kleinen Nachrichtenagenturen. Hier zeigt der neue Standard sein revolutionärstes Potenzial.

Ein Blogger, der von zu Hause aus über vegane Küche schreibt, könnte feststellen, dass seine Inhalte zum Trainieren von kulinarischen Chatbots verwendet werden, ohne jemals einen Cent zu sehen. Mit RSL könnte derselbe Blogger angeben, dass seine Inhalte eine kommerzielle Lizenz für die KI-Nutzung erfordern, und so seine Leidenschaft in eine passive Einnahmequelle verwandeln.

Die Situation erinnert an die der Musiker vor dem Aufkommen von Spotify und Streaming-Plattformen: Nur die großen Plattenfirmen hatten die Verhandlungsmacht für vorteilhafte Verträge, während unabhängige Künstler am Rande blieben. RSL verspricht, diese Dynamik in der Welt der digitalen Inhalte zu ändern.

Zwischenplattformen spielen bei dieser Transformation eine entscheidende Rolle. WordPress.com, das Millionen von Blogs hostet, könnte RSL als native Funktion implementieren, die es seinen Nutzern ermöglicht, ihre Inhalte automatisch für die KI-Nutzung zu monetarisieren. Substack könnte dasselbe für seine Newsletter-Autoren tun und so eine neue Einnahmequelle für unabhängige Kreative schaffen.

Aber im Land der Pixel ist nicht alles Gold, was glänzt. Die Einführung von RSL durch kleine Kreative stellt einzigartige Herausforderungen dar. Die technische Komplexität der Implementierung, die Notwendigkeit, die verschiedenen Lizenzmodelle zu verstehen, und vor allem die Fähigkeit, die eigenen Rechte durchzusetzen, sind allesamt erhebliche Hindernisse für diejenigen, die kein Rechtsteam im Rücken haben.

Hier kommt die Bedeutung technologischer Vermittler ins Spiel. Plattformen wie Medium, das sich dem RSL-Projekt angeschlossen hat, könnten als "Rechte-Aggregatoren" fungieren, die Tarifverträge für ihre Kreativen aushandeln und die Erlöse verteilen. Es ist ein Modell, das an das der musikalischen Verwertungsgesellschaften erinnert, aber auf die digitale Welt angewendet wird.

Der wahre Härtetest für RSL wird darin bestehen, zu beweisen, dass es auch für die kleinsten Kreativen einen Mehrwert schaffen kann, nicht nur für die Web-Giganten. Wenn ein Food-Blogger mit RSL genug verdienen kann, um hochwertigere Zutaten für seine Rezepte zu kaufen, dann wird das System die Wirtschaft der digitalen Inhalte wirklich demokratisiert haben.

## KI, die sich gut benimmt: Compliance, Gesetzgebung und die Zukunft der digitalen Rechte

Wäre RSL eine Figur aus Star Wars, wäre es C-3PO: besessen von Protokollen, Regeln und der korrekten Auslegung intergalaktischer Gesetze. Und wie der goldene Droide könnte sich RSL als wertvoller erweisen, als es zunächst scheint, insbesondere in einem regulatorischen Universum, das immer komplexer wird.

Das Timing des RSL-Starts ist kein Zufall. Europa hat bereits das KI-Gesetz verabschiedet, die umfassendste Gesetzgebung zur künstlichen Intelligenz der Welt, die 2025 vollständig in Kraft treten wird. Die Vereinigten Staaten arbeiten an ähnlichen regulatorischen Rahmenbedingungen, während China bereits mehrere spezifische Vorschriften für die KI umgesetzt hat. In diesem Zusammenhang wird ein Standard, der die Einhaltung erleichtert, nicht nur nützlich, sondern unerlässlich.

Das europäische KI-Gesetz führt insbesondere das Konzept der "Transparenz" bei der Nutzung von Daten für das Training von KI-Modellen ein. Unternehmen müssen die Herkunft der verwendeten Daten dokumentieren und nachweisen, dass sie die erforderlichen Rechte für ihre Nutzung besitzen. RSL passt perfekt in diesen Rahmen und bietet einen standardisierten Mechanismus zur Dokumentation und Verwaltung dieser Rechte.

Die Parallele zur DSGVO ist aufschlussreich. Als die europäische Datenschutzverordnung 2018 in Kraft trat, schrien viele Katastrophe und sagten das Ende des freien Webs voraus. Stattdessen schuf die DSGVO einen neuen globalen Standard und drängte sogar außereuropäische Unternehmen dazu, datenschutzfreundlichere Praktiken einzuführen. RSL könnte einen ähnlichen Weg einschlagen: als Reaktion auf spezifische regulatorische Bedürfnisse beginnen und zu einem de-facto-globalen Standard werden.

Die Strafen für die Verletzung von Inhaltsrechten werden immer härter. Im Jahr 2023 haben mehrere Verlage rechtliche Schritte gegen KI-Unternehmen wegen der unbefugten Nutzung ihrer Inhalte eingeleitet. Die New York Times verklagte OpenAI und Microsoft, während andere Verlage ähnliche Maßnahmen erwägen. In diesem Szenario könnte RSL als "sicherer Hafen" fungieren: Wer sich daran hält, hat einen größeren rechtlichen Schutz als diejenigen, die die Inhaltslizenzen vollständig ignorieren.

Die Regulierungsbehörden schenken diesen Entwicklungen immer mehr Aufmerksamkeit. Die US-amerikanische Federal Trade Commission hat bereits mehrere Untersuchungen zu den Datenerfassungspraktiken von KI-Unternehmen eingeleitet, während die italienische Wettbewerbsbehörde ähnliche Verfahren eingeleitet hat. Ein anerkannter Standard wie RSL könnte den Dialog zwischen Unternehmen und Regulierungsbehörden erleichtern und einen gemeinsamen Diskussionsrahmen schaffen.

Die globale Perspektive ist besonders interessant. Während Europa zu einer strengen Regulierung tendiert und die Vereinigten Staaten einen eher marktorientierten Ansatz bevorzugen, bietet Asien ein vielfältiges Bild. Länder wie Singapur und Südkorea experimentieren mit "regulatorischen Sandkästen" für die KI, in denen Standards wie RSL in kontrollierten Umgebungen getestet werden könnten, bevor sie breiter eingeführt werden.

Aber der vielleicht faszinierendste Aspekt ist, wie sich RSL über seine ursprünglichen Zwecke hinaus entwickeln könnte. Wenn das System seine Wirksamkeit bei der Verwaltung von Inhaltsrechten für die KI unter Beweis stellt, könnte es auf andere Bereiche ausgeweitet werden: von der Verwaltung der Rechte für Multimedia-Inhalte bis hin zur Definition von Standards für die ethische Nutzung personenbezogener Daten. Es ist ein bisschen so, als würden wir der Geburt eines neuen "Betriebssystems" für digitale Rechte beiwohnen.

## Ausblick und abschließende Überlegungen

RSL stellt sicherlich einen Schritt nach vorne in Richtung eines faireren Webs aus Sicht der Verteilung des durch digitale Inhalte geschaffenen Werts dar. Sein Erfolg wird jedoch von der Fähigkeit abhängen, ein Ökosystem zu schaffen, in dem alle Hauptakteure - Verlage, KI-Unternehmen und technologische Vermittler - es für vorteilhaft halten, teilzunehmen.

Die Geschichte der Technologie ist voll von vielversprechenden Standards, die es nicht geschafft haben, die kritische Masse zu erreichen, um wirklich allgegenwärtig zu werden. RSS selbst ist trotz seiner Nützlichkeit nie so Mainstream geworden, wie seine Schöpfer gehofft hatten. RSL wird dieses Schicksal vermeiden müssen, und das kann es nur, indem es für alle Beteiligten einen konkreten Mehrwert nachweist.

In einer Zeit, in der die künstliche Intelligenz verspricht, jeden Aspekt unseres digitalen Lebens zu revolutionieren, ist es nicht nur wünschenswert, sondern unerlässlich, über Werkzeuge zu verfügen, die es den Inhaltserstellern ermöglichen, die Kontrolle über ihr geistiges Eigentum zu behalten. RSL könnte genau das richtige Werkzeug zur richtigen Zeit sein, aber wie immer in der Welt der Technologie wird nur der Markt das letzte Wort haben.

Die Zukunft wird zeigen, ob dieser neue Standard es schaffen wird, den digitalen Daten-Wildwest in eine zivilisiertere Grenze zu verwandeln, in der alle gedeihen können. In der Zwischenzeit täten Verlage und KI-Unternehmen gut daran, diese Entwicklung im Auge zu behalten: Sie könnte die Spielregeln für die kommenden Jahrzehnte definieren.
