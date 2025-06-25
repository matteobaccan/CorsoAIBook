## **Bewertung von KIs**

### **7.1 Einleitung**

Die Bewertung von Künstlichen Intelligenzen (KIs) ist ein grundlegender Prozess, um sicherzustellen, dass KI-Systeme effektiv, zuverlässig und sicher sind. Mit der zunehmenden Verbreitung von KI in kritischen Sektoren wie Medizin, Finanzen und Sicherheit ist es unerlässlich, über robuste Methoden zur Messung von Leistung, Benutzerfreundlichkeit, Ethik und Interpretierbarkeit von KI-Modellen zu verfügen. Dieses Kapitel untersucht die wichtigsten Ansätze und Werkzeuge zur Bewertung von KIs sowie die damit verbundenen Herausforderungen und ethischen Überlegungen.

### **7.2 Turing-Test**

#### **7.2.1 Was ist der Turing-Test?**

Der **Turing-Test**, 1950 von Alan Turing vorgeschlagen, war einer der ersten Versuche, ein Kriterium zur Bewertung der Intelligenz einer Maschine zu definieren. Der Test sieht ein Gespräch zwischen einem menschlichen Richter und zwei Teilnehmern vor, einem Menschen und einer Maschine. Wenn der Richter nicht in der Lage ist, zwischen den beiden zu unterscheiden, gilt die Maschine als "intelligent".

#### **7.2.2 Anwendungen und Grenzen des Turing-Tests**

Obwohl der Turing-Test ein historischer Meilenstein war, gilt er heute als eine begrenzte Methode zur Bewertung der Intelligenz von Maschinen. Der Test konzentriert sich hauptsächlich auf die Fähigkeit, menschliches Verhalten zu imitieren, bewertet jedoch Aspekte wie tiefes Verständnis, Kreativität oder die Fähigkeit zur Lösung komplexer Probleme nicht. Darüber hinaus ist der Test subjektiv und hängt von der Wahrnehmung des Richters ab, was ihn für objektive Bewertungen ungeeignet macht.

![Alan Mathison Turing gilt als einer der Väter der Informatik. Gemeinfreies Foto von Wikipedia](turing.jpg)

#### **7.2.3 Moderne Alternativen zum Turing-Test**

Mit der Entwicklung der KI wurden neue Bewertungsmethoden entwickelt, die über das einfache Kriterium der Nachahmung hinausgehen. Beispielsweise sind **Benchmarks** wie **FrontierMath** und **ARC** (AI2 Reasoning Challenge) darauf ausgelegt, die Fähigkeiten zum logischen Denken und zur Lösung komplexer Probleme zu testen und bieten ein objektiveres Maß für die Leistung von KIs.

### **7.3 Bewertungsmethoden für KIs**

#### **7.3.1 Leistungsbewertung**

Die Leistungsbewertung ist eine der häufigsten Methoden zur Messung der Effektivität eines KI-Modells. Dieser Ansatz basiert auf quantitativen Metriken wie Genauigkeit, Präzision, Recall und F1-Score, mit denen bewertet werden kann, wie gut ein Modell eine bestimmte Aufgabe erfüllt.

-   **Genauigkeit**: Der Prozentsatz der korrekten Vorhersagen im Verhältnis zur Gesamtzahl der Vorhersagen.
-   **Präzision**: Der Prozentsatz der korrekten positiven Vorhersagen im Verhältnis zur Gesamtzahl der positiven Vorhersagen.
-   **Recall**: Der Prozentsatz der korrekt identifizierten positiven Fälle im Verhältnis zur Gesamtzahl der positiven Fälle.
-   **F1-Score**: Das harmonische Mittel aus Präzision und Recall, nützlich, um die beiden Metriken auszugleichen.

#### **7.3.2 Bewertung der Benutzerfreundlichkeit**

Die Benutzerfreundlichkeit ist ein entscheidender Aspekt, um sicherzustellen, dass KI-Systeme für Endbenutzer zugänglich und einfach zu bedienen sind. Die Bewertung der Benutzerfreundlichkeit konzentriert sich auf Aspekte wie das Design der Benutzeroberfläche, die Klarheit der Antworten und die Fähigkeit des Systems, sich an die Bedürfnisse der Benutzer anzupassen.

-   **Benutzerfreundlichkeitstests**: Benutzer interagieren mit dem System, während Beobachter Probleme und Schwierigkeiten aufzeichnen.
-   **Fragebögen und Umfragen**: Benutzer geben Feedback zu ihrer Erfahrung mit dem System.
-   **Sitzungsanalyse**: Interaktionsdaten werden analysiert, um Muster und Verbesserungspotenziale zu identifizieren.

#### **7.3.3 Ethische Bewertung**

Ethik ist ein immer wichtigerer Aspekt bei der Bewertung von KIs, insbesondere in Kontexten, in denen algorithmische Entscheidungen erhebliche Auswirkungen auf das Leben von Menschen haben können. Die ethische Bewertung konzentriert sich auf Themen wie algorithmische Verzerrungen, Datenschutz, Sicherheit und Auswirkungen auf die Arbeit.

-   **Algorithmische Verzerrung**: KI-Modelle können durch in den Trainingsdaten vorhandene Vorurteile beeinflusst werden, was zu diskriminierenden oder unfairen Entscheidungen führt.
-   **Datenschutz**: KI benötigt oft große Mengen personenbezogener Daten, was Bedenken hinsichtlich des Schutzes der Privatsphäre aufwirft.
-   **Sicherheit**: KI-Systeme können anfällig für Cyberangriffe sein, wie z. B. Datenvergiftung oder gegnerische Angriffe.
-   **Auswirkungen auf die Arbeit**: Die KI-gesteuerte Automatisierung könnte in einigen Sektoren zum Verlust von Arbeitsplätzen führen, während sie in anderen neue schafft.

#### **7.3.4 Bewertung der Interpretierbarkeit**

Interpretierbarkeit ist die Fähigkeit eines KI-Systems, seine Entscheidungen für Menschen verständlich zu erklären. Dies ist besonders wichtig in kritischen Kontexten wie Medizin und Finanzen, wo es unerlässlich ist zu verstehen, wie Entscheidungen getroffen werden.

-   **Interpretierbare Modelle**: Verwendung einfacher und transparenter Modelle wie Entscheidungsbäume, die leichter zu interpretieren sind.
-   **Erklärungstechniken**: Verwendung von Werkzeugen wie **LIME** (Local Interpretable Model-agnostic Explanations) und **SHAP** (SHapley Additive exPlanations) zur Erklärung der Vorhersagen komplexer Modelle.
-   **Visualisierung**: Verwendung von Grafiken und Diagrammen zur Darstellung der internen Funktionsweise des Modells und seiner Entscheidungen.

### **7.4 Neue Tests und Benchmarks**

#### **7.4.1 FrontierMath**

**FrontierMath** ist ein Benchmark, der entwickelt wurde, um die mathematischen Denkfähigkeiten von KI-Modellen zu testen. Dieser Benchmark umfasst komplexe und originelle mathematische Probleme, die selbst für menschliche Experten besonders herausfordernd sein sollen. FrontierMath verwendet automatisierte Verifizierungssysteme, um die Leistung von Modellen effizient und reproduzierbar zu bewerten.

#### **7.4.2 ARC Benchmark**

Der **ARC Benchmark** (AI2 Reasoning Challenge) wurde entwickelt, um die Denkfähigkeiten großer Sprachmodelle (LLMs) zu testen. Dieser Benchmark umfasst komplexe Multiple-Choice-Fragen, die darauf ausgelegt sind, das tiefe Sprachverständnis und logisches Denken zu bewerten.
![Ein Benchmark ist ein Referenzstandard. Grafik erstellt mit Claude](benchmark.jpg)

### **7.5 Herausforderungen bei der Bewertung von KIs**

#### **7.5.1 Verzerrungen in den Trainingsdaten**

KI-Modelle können durch in den Trainingsdaten vorhandene Verzerrungen beeinflusst werden, was zu diskriminierenden oder unfairen Entscheidungen führt. Es ist unerlässlich sicherzustellen, dass die Daten repräsentativ und frei von Vorurteilen sind. Verzerrungen, oder besser gesagt kognitive Verzerrungen, sind Verzerrungen, die Menschen bei der Bewertung von Fakten und Ereignissen anwenden. Solche Verzerrungen veranlassen uns, unsere eigene subjektive Sichtweise neu zu erschaffen, die nicht originalgetreu der Realität entspricht. Im Fall von KI bezieht sich Verzerrung (oder Vorurteil) auf systematische Fehler in den Ergebnissen eines KI-Modells, die durch fehlerhafte oder unvollständige Annahmen in den Trainingsdaten oder im Entwicklungsprozess des Modells verursacht werden.

#### **7.5.2 Rechenkomplexität**

Die Bewertung komplexer KI-Modelle wie tiefer neuronaler Netze erfordert große Mengen an Rechenressourcen und Zeit. Dies kann die Bewertung im großen Maßstab oder in Kontexten mit begrenzten Ressourcen erschweren.

#### **7.5.3 Interpretierbarkeit**

KI-Modelle, insbesondere solche, die auf Deep Learning basieren, werden oft als "Black Boxes" betrachtet, da es schwierig ist zu verstehen, wie sie Entscheidungen treffen. Dies wirft Bedenken hinsichtlich Transparenz und Zuverlässigkeit auf, insbesondere in kritischen Kontexten.

#### **7.5.4 Ethik und Verantwortung**

Die Bewertung von KIs muss die ethischen und sozialen Auswirkungen des Einsatzes dieser Technologie berücksichtigen. Es ist unerlässlich sicherzustellen, dass KI-Systeme verantwortungsvoll eingesetzt werden und dass Entscheidungen nachvollziehbar und transparent sind.

#### **7.5.5 Ethik oder Moral? Die Kultur und Nationalität der Entwickler**

Menschliches Feedback in der künstlichen Intelligenz ist ein Prozess, bei dem Menschen Bewertungen, Korrekturen und Anleitungen für Modelle des maschinellen Lernens bereitstellen und ihnen so helfen, ihre Leistung zu verbessern und sich zu verfeinern. Dieser Mechanismus ermöglicht es, die KI an ethische Werte anzupassen, Verzerrungen zu reduzieren, die Genauigkeit der Antworten zu verbessern und sicherzustellen, dass die künstliche Intelligenz kohärenter und angemessener auf menschliche Erwartungen reagiert.

Die Ausrichtung oder das menschliche Feedback der künstlichen Intelligenz ist jedoch nicht nur eine technische Frage, sondern ein sensibler Prozess, der die Werte, die Ethik und die Kultur ihrer Entwickler tiefgreifend widerspiegelt. Jedes System der künstlichen Intelligenz wird durch riesige Datensätze "erzogen", die niemals neutral sind, sondern immer von den Werten, Vorurteilen und Perspektiven der Personen und Institutionen durchdrungen sind, die sie auswählen und kuratieren. Das Herkunftsland einer KI wird somit zu einem entscheidenden Faktor: Ethische Normen, gesetzliche Beschränkungen, kulturelle Befindlichkeiten und sogar Zensursysteme beeinflussen unweigerlich die Art und Weise, wie künstliche Intelligenz Informationen verarbeitet und Antworten formuliert. Eine in einer Nation mit einer starken Tradition der Meinungsfreiheit entwickelte KI wird wahrscheinlich offenere und vielfältigere Antworten geben als eine künstliche Intelligenz, die in einem restriktiveren Kontext geschaffen wurde, in dem Kontroll- und Denkbeschränkungsmechanismen weiter verbreitet sind. Dieses "menschliche Feedback" ist daher keine einfache technische Anpassung, sondern ein echter Prozess der moralischen und kulturellen "Erziehung" der künstlichen Intelligenz, der sie zu einem Spiegel der Gesellschaften macht, die sie hervorbringen.

Für den Durchschnittsnutzer wird es daher unerlässlich, ein kritisches Bewusstsein zu entwickeln: Die Herkunft einer künstlichen Intelligenz zu kennen bedeutet, ihre Antworten mit einem bewussten Filter interpretieren zu können. So wie man eine journalistische Quelle oder die Meinung eines Experten bewertet, muss dies auch bei der KI geschehen. Sich zu fragen, woher sie kommt, wer sie entwickelt hat, welche kulturellen und ethischen Werte sie beeinflussen, wird zu einer grundlegenden Übung des kritischen Denkens. Die zurückgegebenen Informationen sollten nicht als absolute Wahrheiten akzeptiert werden, sondern als Perspektiven, die kritisch analysiert, verglichen und geprüft werden müssen, im Bewusstsein, dass sich hinter jeder Antwort Entscheidungen, Filter und Perspektiven verbergen, die über die reine Information hinausgehen.

### **7.6 Schlussfolgerung**

Die Bewertung von KIs ist ein komplexer und multidisziplinärer Prozess, der die Integration quantitativer, qualitativer und ethischer Methoden erfordert. Mit der zunehmenden Verbreitung von KI in kritischen Sektoren ist es unerlässlich, über robuste Werkzeuge und Ansätze zu verfügen, um sicherzustellen, dass KI-Systeme effektiv, zuverlässig und sicher sind. Während wir weiterhin neue KI-Technologien entwickeln und implementieren, ist es wichtig, Innovation mit dem Bewusstsein für ethische und soziale Auswirkungen in Einklang zu bringen und sicherzustellen, dass diese Technologie verantwortungsvoll und zum Wohle aller eingesetzt wird.
