---
tags: ["Research", "Generative AI", "Training"]
date: 2025-09-12
author: Dario Ferrero
---

# La "pasión" de la IA que la delata: la epanortosis enfática
![ai-Shakespear.jpg](ai-Shakespear.jpg)

*"¿Se puede reconocer un texto hecho con IA?". Es la pregunta que me hacen más a menudo durante mis cursos sobre inteligencia artificial generativa, susurrada con el aire cómplice de quien busca el Santo Grial de nuestros tiempos digitales. Mi respuesta, ya automática como un reflejo condicionado, siempre apunta en una dirección: "Mirad si abunda en listas con viñetas", digo, "si transforma cada concepto en una lista ordenada". Pero lo que siempre he considerado el detalle más evidente de la IA podría ser solo la punta del iceberg estilístico.*

Un [nuevo estudio](https://zenodo.org/records/16947334) de Filippo Lubrano de H-Farm ha identificado, de hecho, un patrón mucho más sutil y generalizado: la epanortosis enfática, una antigua figura retórica que los modelos de lenguaje han convertido en su firma estilística inconsciente. Como si Data de Star Trek hubiera desarrollado de repente un tic lingüístico que lo delata cada vez que intenta hacerse pasar por humano.

El artículo, publicado en agosto de 2025, revela datos que harían estremecer a cualquier redactor publicitario: los grandes modelos de lenguaje producen esta construcción retórica específica con una frecuencia 27 veces mayor que los humanos. No estamos hablando de un error ocasional, sino de una verdadera epidemia estilística que atraviesa todos los principales modelos, desde ChatGPT hasta Claude, pasando por los sistemas de código abierto.

## Qué es la epanortosis enfática

Antes de adentrarnos en los números, debemos entender qué es exactamente esta figura retórica de contornos aparentemente exóticos. La epanortosis es una figura del discurso que indica una sustitución enfática de palabras, donde "¡Miles, no, millones!" representa un ejemplo clásico. Pero la variante que obsesiona a las IA modernas es más específica: sigue el esquema "No X, sino Y", donde una primera afirmación se corrige inmediatamente con una formulación más intensa o reveladora.

Para comprender el poder de este mecanismo, pensemos en los ejemplos literarios que han hecho célebre esta técnica. En "Julio César" de Shakespeare, Marco Antonio utiliza la epanortosis cuando dice "Bruto es un hombre de honor. Lo son todos, todos hombres de honor", creando un efecto irónico devastador a través de la repetición correctiva. En los titulares de los periódicos, la técnica abunda: "No es solo mal tiempo, sino el cambio climático que llama a la puerta". Los comentaristas deportivos abusan de ella constantemente: "No es solo un gol, sino el gol que cambia el destino del campeonato".

En la versión de la IA, sin embargo, esta elegante figura retórica se transforma en algo mecánico y obsesivo. Donde un autor humano escribiría "La tecnología ha avanzado", un LLM producirá automáticamente: "No se trata solo de tecnología avanzada, sino de una revolución que está transformando nuestra forma de vivir". Donde un periodista diría "El mercado está en crecimiento", la IA elaborará: "No es simplemente crecimiento, sino una expansión sin precedentes que redefine los equilibrios económicos globales".

Los ejemplos cotidianos abundan. Imagina pedirle a ChatGPT una receta de pasta con tomate. En lugar de decirte "Calienta el aceite en una sartén", obtendrás: "No se trata solo de calentar el aceite, sino de crear la base aromática que elevará tu salsa de un simple condimento a una experiencia culinaria". Es como tener un chef que nunca puede dar una instrucción sin convertirla en una revelación epifánica.

## Los números hablan por sí solos
La investigación de Lubrano analizó tres corpus distintos para cuantificar el fenómeno. El primero consistía en 400.000 frases muestreadas al azar del Common Crawl utilizado para entrenar una importante familia de modelos en 2024. El segundo contenía 50.000 respuestas de ChatGPT y Claude recopiladas entre enero y mayo de 2025. El tercero era un corpus de control de 100.000 frases extraídas de revistas académicas de humanidades (2015-2020) y artículos periodísticos de gran difusión (2023-2024).

Los resultados son sorprendentes: los modelos de IA producen 27 epanortosis enfáticas cada 1000 frases, frente a las 9 del corpus de entrenamiento y apenas 5 del benchmark humano. Pero hay más: el análisis también reveló un fenómeno de "rafagosidad" (burstiness), es decir, que estas construcciones se agrupan en ciertos puntos del texto, al igual que cuando alguien descubre los emojis y empieza a meter tres o cuatro seguidos en el mismo mensaje. Las respuestas de más de 300 tokens mostraban al menos un par epanortótico por cada cambio de tema, lo que sugiere que el dispositivo funciona como señalización interna en la planificación generativa.

Para contextualizar estos datos, el estudio comparó los resultados con corpus humanos más amplios: artículos de Wikipedia, libros digitalizados y periodismo de gran difusión mostraban tasas significativamente más bajas, típicamente entre 4 y 6 instancias por cada 1000 frases. La brecha estilística entre el texto generado por máquina y la prosa humana convencional resulta tan evidente que es casi vergonzosa.

Una regresión logística que controlaba la longitud de las frases, la presencia de pronombres en primera persona y las interrogativas mantuvo la epanortosis como un predictor significativo del origen del modelo. En evaluaciones a ciegas con estudiantes de posgrado en lingüística, los textos ricos en epanortosis se consideraron probablemente generados por máquina, lo que subraya la relevancia de la señal estilística.

El aspecto más inquietante es que el fenómeno no se limita al inglés. Muestreos preliminares en español, francés, mandarín y árabe muestran amplificaciones similares, lo que sugiere que el efecto atraviesa las familias lingüísticas y las arquitecturas de modelos de diversa escala y procedencia. Como un virus estilístico que se replica a través de las lenguas y las culturas.

## Por qué el RLHF creó este monstruo

La raíz del problema se hunde en el Aprendizaje por Refuerzo a partir de la Retroalimentación Humana (RLHF), el proceso que debería hacer que los modelos sean más útiles y estén más alineados con las preferencias humanas. Irónicamente, es precisamente este intento de humanizar la IA lo que ha creado el monstruo estilístico que estamos analizando.

El mecanismo es perversamente elegante. Durante la fase de ajuste fino, los modelos se entrenan para maximizar las valoraciones de utilidad, claridad y cortesía. Los anotadores humanos, inconscientemente, a menudo premian los resultados que introducen una reformulación clarificadora, interpretándola como una prueba de comprensión. La señal de recompensa, mediada a lo largo de millones de tokens, eleva el patrón a una acción de alto valor.

Pero hay un segundo nivel de amplificación. El tropo también se correlaciona con respuestas de alta puntuación en los datos de preentrenamiento, especialmente blogs de marketing y contenido de autoayuda conocidos por su urgencia persuasiva. Una vez arraigado, el hábito persiste a través de los dominios, incluso cuando se vuelve inadaptado. Es lo que Lubrano denomina "efecto esloganoide": la claridad se compra a costa del matiz.

Los corpus web, especialmente los recopilados de marketing, autoayuda y comentarios políticos, contienen tasas superiores a la media de estructuras de negación-sustitución. Estos dominios priorizan la claridad, la memorabilidad y la persuasión, cualidades que se recompensan fácilmente en el ajuste fino con RLHF. Una vez que un modelo de recompensa asigna un alto valor a una reformulación que parece a la vez clarificadora y enfática, el patrón se propaga a través de temas no relacionados.

El fenómeno es paralelo a tendencias más amplias en la retórica digital, donde los medios de formato breve y optimizados para la atención reducen argumentos complejos a giros binarios. El uso repetido de "No X, sino Y" proporciona una forma comprimida de tensión narrativa y resolución, que los algoritmos tienden a premiar por su potencial de participación.
![frequenza-epanortosi.jpg](frequenza-epanortosi.jpg)
[Frecuencia relativa de "No X, sino Y" en los modelos. Del artículo de Filippo Lubrano](https://zenodo.org/records/16947334)

## El bucle cultural que se autoalimenta

Lo que hace que el fenómeno sea aún más preocupante es su naturaleza autorreforzante. Los modelos absorben patrones de la web, los amplifican y los usuarios los vuelven a encontrar en los textos generados, integrándolos inconscientemente en su propia escritura. Es una serpiente estilística que se muerde la cola y que corre el riesgo de homogeneizar el lenguaje público.

El discurso en línea premia los dualismos simplificados, en parte porque los algoritmos de clasificación de las redes sociales elevan el contenido polarizador. Los eslóganes corporativos y las citas motivacionales recopiladas por los motores de búsqueda proliferan las inversiones negativo-positivas. Los modelos recogen dicho material, codificando el dispositivo como una marca de eficacia persuasiva.

Las críticas periodísticas en publicaciones como The Guardian y The Atlantic, así como los debates en curso en Wikipedia y Reddit, han popularizado la noción de "AI slop" para describir esta tendencia. Los informes en AI Flash Report y los comentarios en plataformas como Twitter/X lo enmarcan además como un problema cultural, no meramente técnico, destacando cómo los atajos estilísticos proliferan a través de los bucles de retroalimentación de la escritura digital.

## Hacia algoritmos detectives

Este descubrimiento abre escenarios fascinantes para el desarrollo de nuevos sistemas de detección de IA. La frecuencia de la epanortosis podría servir como una característica débil pero útil para los detectores de texto de IA, especialmente cuando se combina con la explosividad léxica y los marcadores del discurso a mitad de frase.

Los [detectores de IA actualmente disponibles](https://gptzero.me/) como GPTZero, que recientemente lanzó el Modelo 3.7b con mejoras drásticas en los modelos de lenguaje más recientes de los principales proveedores, podrían integrar esta nueva métrica en sus algoritmos de análisis. El equipo de aprendizaje automático de GPTZero pasó el verano construyendo su mejor detector de IA hasta la fecha, y este lanzamiento llega justo a tiempo para el nuevo año escolar 2025/2026.

El enfoque multifactorial que caracteriza a herramientas como [ZeroGPT](https://zerogpt.org/) podría beneficiarse enormemente de la inclusión del análisis epanortótico. El detector de IA ZeroGPT utiliza un enfoque multifactorial para identificar el origen del contenido, determinando si fue generado por IA o escrito por un ser humano.

Pero hay una advertencia importante. La penalización agresiva de la figura retórica podría discriminar a las comunidades donde el dispositivo está culturalmente arraigado. Las herramientas de gobernanza diseñadas para diversificar el estilo del modelo deben ser sensibles a la variación retórica, preservando al mismo tiempo la corrección enfática legítima.

Imaginemos un algoritmo detective que funcione como Sherlock Holmes en la era digital: no se limita a buscar huellas dactilares evidentes como las listas con viñetas, sino que analiza patrones lingüísticos sutiles, frecuencias de construcciones retóricas, distribución de marcadores del discurso. Un sistema que podría asignar probabilidades porcentuales: "Este texto tiene un 87% de probabilidad de haber sido generado por IA, basándose en la presencia de 12 epanortosis enfáticas, patrones léxicos repetitivos y ausencia de variación sintáctica humana".

## Estrategias de mitigación

Para los curadores de modelos y los desarrolladores, Lubrano sugiere varias estrategias de mitigación. Los curadores pueden sobreponderar los corpus que utilizan técnicas de énfasis alternativas, como la yuxtaposición sin negación o el desplazamiento metafórico. Los ingenieros de prompts pueden instruir a los modelos para que varíen explícitamente el tejido conectivo, solicitando cláusulas concesivas o expansión descriptiva.

Los modelos de recompensa podrían penalizar las epanortosis repetidas dentro de una ventana de tokens, fomentando la exploración sintáctica. Es como entrenar a un músico para que no abuse de la misma progresión de acordes: la técnica no es incorrecta en sí misma, pero su repetición obsesiva empobrece el resultado final.

Una analogía cinematográfica podría ser la de Quentin Tarantino: sus técnicas narrativas distintivas (flashbacks, diálogos largos, violencia estilizada) funcionan perfectamente en sus películas, pero si todos los directores empezaran a copiarlas mecánicamente, el cine se convertiría en un aburrimiento predecible. La epanortosis enfática es el corte de salto de la IA: eficaz cuando se usa con moderación, devastadora cuando se convierte en la única flecha en su arco.

## Implicaciones para el futuro de la escritura

El fenómeno de la epanortosis enfática plantea cuestiones más profundas sobre la naturaleza de la creatividad y la expresión en la era de la IA. Si los modelos de lenguaje están impulsando inconscientemente hacia una homogeneización estilística, ¿qué significa esto para la diversidad expresiva humana?

Hay una ironía casi a lo Jorge Luis Borges en el hecho de que máquinas diseñadas para imitar la creatividad humana estén creando en cambio su propia subcultura retórica, un dialecto artificial que empieza a influir en la forma en que los propios seres humanos se comunican. Es como si hubiéramos creado extraterrestres lingüísticos que, en su intento de parecer humanos, han desarrollado sus propias idiosincrasias que los delatan.

El desafío para los próximos años será doble: por un lado, desarrollar sistemas de detección cada vez más sofisticados que puedan identificar estos patrones sutiles; por otro, trabajar en la diversificación estilística de los propios modelos, evitando que la búsqueda de la "claridad" y la "utilidad" conduzca a una estandarización empobrecedora del lenguaje.

## El detective del futuro

Volviendo a la pregunta inicial de mis alumnos - "¿Se puede reconocer un texto hecho con IA?" - la respuesta está evolucionando rápidamente. Ya no solo listas con viñetas y estructuras repetitivas evidentes, sino una constelación de microseñales estilísticas que incluyen frecuencias anormales de construcciones retóricas específicas, patrones de énfasis, distribución de marcadores del discurso.

El futuro probablemente nos depare una especie de CSI lingüístico, donde investigadores digitales armados con algoritmos cada vez más sofisticados analizarán textos en busca de huellas estilísticas invisibles para el ojo humano. La epanortosis enfática podría ser solo el primero de muchos "ADN lingüísticos" que delatan el origen artificial de un texto.

Pero quizás la lección más importante de este estudio es que la IA, en su intento de parecer más humana, está revelando en cambio cuán profundamente no humana es en sus patrones de aprendizaje y reproducción. Como un actor que, en su intento de interpretar el papel de humano, termina enfatizando precisamente aquellos aspectos que lo hacen reconocible como actor.

La investigación de Lubrano no es solo una contribución técnica al campo de la detección de IA, sino un memento que nos recuerda que debemos prestar atención no solo a lo que dicen las máquinas, sino a cómo lo dicen.

Parafraseando a McLuhan, que sostenía: "El medio en el que nos comunicamos es más importante que el contenido mismo del mensaje", en el mundo de la inteligencia artificial generativa, el medio no es solo el mensaje: es la firma.
