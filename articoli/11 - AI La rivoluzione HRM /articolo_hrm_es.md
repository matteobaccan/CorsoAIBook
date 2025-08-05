# "Cuando el tamaño no importa": La revolución del modelo HRM
*por Dario Ferrero (VerbaniaNotizie.it)*
![hrm_le_dimensioni_non_contano.jpg](hrm_le_dimensioni_non_contano.jpg)


*La mayor revolución en inteligencia artificial de los últimos años no proviene de los laboratorios de OpenAI o Google, sino de una pequeña startup de Singapur llamada [Sapient Intelligence](https://www.sapient.inc/).*

El protagonista de esta historia se llama [Hierarchical Reasoning Model](https://github.com/sapientinc/HRM) (HRM), un agente de IA que está sacudiendo los cimientos de todo el sector con una promesa aparentemente imposible: razonar mejor que los gigantes de la IA utilizando una fracción de sus recursos.

No se trata del habitual modelo de lenguaje ampliado hasta lo inverosímil, ni de otra variación sobre el tema de los transformadores. HRM está construido de forma diferente, inspirado directamente en el funcionamiento del cerebro humano, y los resultados que está obteniendo son, como mínimo, asombrosos. Este modelo de apenas 27 millones de parámetros, menos de una cuarta parte del primer GPT, está superando sistemáticamente a modelos cuatro veces más grandes en tareas de razonamiento complejo. Por si fuera poco, se entrena con solo mil ejemplos por problema, mientras que sus adversarios requieren montañas de datos y meses de procesamiento en los servidores más potentes del mundo.

Pero la verdadera magia de HRM no reside en su reducido tamaño ni en su eficiencia de entrenamiento. Su innovación radica en que no se limita a procesar información como todos los demás: razona de verdad, emulando los procesos cognitivos humanos de formas que parecían ciencia ficción hasta hace unos meses. Y los resultados hablan por sí solos: donde otros modelos fracasan por completo, HRM sobresale con una naturalidad que recuerda más a un cerebro pensante que a una máquina calculadora.

## Cuando la cadena de pensamiento se rompe

Para comprender la importancia de la revolución que trae consigo HRM, primero debemos entender cómo funcionan los modelos de inteligencia artificial actuales y por qué sus limitaciones son cada vez más evidentes. ChatGPT, Claude, Gemini y todos sus hermanos mayores se basan en una técnica llamada "Cadena de Pensamiento" o Chain of Thought, un enfoque que suena prometedor pero que esconde profundas fragilidades estructurales.

Imagina que tienes que resolver un problema matemático complejo escribiendo cada paso con un bolígrafo indeleble, sin poder volver atrás para comprobar o corregir lo que has escrito. Así es exactamente como funcionan los modelos actuales: se guían a sí mismos paso a paso a través de un problema, casi "hablando consigo mismos" en voz alta, pero si cometen un solo pequeño error en esta cadena, toda la respuesta puede desmoronarse como un castillo de naipes.

Como explican los investigadores de Sapient Intelligence en su [artículo científico](https://arxiv.org/abs/2506.21734), "la cadena de pensamiento para el razonamiento es una muleta, no una solución satisfactoria. Se basa en descomposiciones frágiles definidas por el hombre en las que un solo paso en falso o un desorden de los pasos puede hacer descarrilar por completo el proceso de razonamiento".

El problema es aún más profundo de lo que parece. Los modelos basados en transformadores, la arquitectura que domina la IA moderna, siempre realizan la misma cantidad de "pensamiento" independientemente de la dificultad de la pregunta. Es como si un detective tuviera que dedicar exactamente el mismo tiempo y los mismos recursos para resolver tanto un robo de bicicletas como un intrincado caso de asesinato. No pueden decir "Esto es difícil, necesito más tiempo para pensar" y no pueden revisar su razonamiento una vez que han empezado a generar la respuesta.

Esta rigidez tiene enormes consecuencias prácticas. Los modelos actuales se ven obligados a traducir cada proceso de razonamiento en un lenguaje explícito, produciendo respuestas largas, lentas y a menudo redundantes. Peor aún, esta dependencia del lenguaje los hace vulnerables a errores en cascada: si se equivocan en un paso intermedio, todo lo que sigue se ve comprometido, independientemente de lo correctas que puedan ser sus capacidades de razonamiento básicas.

## La arquitectura que imita al cerebro

HRM abandona por completo este paradigma, adoptando un enfoque radicalmente diferente que sus creadores describen como "inspirado en el cerebro". No se trata de una metáfora superficial o de marketing: la arquitectura de HRM toma prestada directamente la estrategia de decisión por capas del cerebro humano, aplicándola a la inteligencia artificial con resultados que están redefiniendo lo que es posible en el campo del aprendizaje automático.

En el corazón de HRM hay dos componentes que trabajan en tándem como un dúo perfectamente coordinado. El primero es un planificador de alto nivel, que podríamos imaginar como el "cerebro estratégico lento" que observa el panorama general, identifica el tipo de problema a resolver y traza un mapa general del enfoque a seguir. El segundo es un ejecutor de bajo nivel, el "procesador rápido" que recibe las órdenes del planificador y las ejecuta con precisión y rapidez.

La analogía más acertada es la de un maestro de ajedrez que colabora con un asistente increíblemente eficiente. El maestro estudia el tablero, planifica la estrategia general y decide qué movimiento hacer, mientras que el asistente ejecuta físicamente el movimiento con precisión milimétrica. Pero aquí la similitud se vuelve aún más interesante: los dos no se limitan a un único intercambio de información, sino que mantienen un diálogo continuo durante toda la duración del problema.

Este es el corazón de la innovación de HRM: el [bucle de razonamiento jerárquico](https://venturebeat.com/ai/new-ai-architecture-delivers-100x-faster-reasoning-than-llms-with-just-1000-training-examples/). El módulo de alto nivel elabora un plan estratégico y se lo pasa al módulo de bajo nivel, que lo ejecuta y devuelve los resultados. En este punto, el módulo de alto nivel analiza lo sucedido, actualiza su estrategia en función de los nuevos datos y proporciona al módulo de bajo nivel un nuevo subproblema refinado en el que trabajar. Este "toma y daca" continúa en ciclos iterativos hasta que el modelo converge en la solución óptima.

La belleza de este enfoque es que permite a HRM controlar y refinar internamente su propio razonamiento mientras aún está procesando el problema, una capacidad que la gran mayoría de los demás modelos simplemente no poseen. Es como si, mientras resuelves ese problema de matemáticas con el bolígrafo indeleble, alguien te permitiera de repente borrar, reescribir y repensar cada paso hasta que estés completamente seguro de la solución.

Pero hay más. La versión más avanzada de HRM utiliza el aprendizaje por refuerzo para decidir de forma autónoma cuántas iteraciones son necesarias para cada tipo de tarea, lo que lo asemeja aún más al pensamiento flexible humano. Al igual que nosotros dedicamos más tiempo y energía mental a los problemas complejos que a los sencillos, HRM aprende a modular sus ciclos de razonamiento en función de la dificultad intrínseca del problema al que se enfrenta.
![ragionamento_gerarchico_hrm.jpg](ragionamento_gerarchico_hrm.jpg)
*[Imagen extraída de Sapient.inc HRM](https://sapient.inc/)*

## David contra Goliat: los números que conmocionan

Los resultados obtenidos por HRM en los benchmarks de razonamiento más difíciles son el tipo de cifras que hacen arquear las cejas incluso a los expertos más escépticos del sector. Estamos hablando de un modelo con apenas 27 millones de parámetros que no solo compite con gigantes de miles de millones de parámetros, sino que los supera sistemáticamente en tareas que requieren un razonamiento profundo y abstracto.

En el [benchmark ARC-AGI](https://venturebeat.com/ai/openais-o3-shows-remarkable-progress-on-arc-agi-sparking-debate-on-ai-reasoning/), considerado una de las pruebas más fiables para medir las capacidades de razonamiento abstracto y generalización de la inteligencia artificial, HRM obtuvo una puntuación del 40,3%, superando a modelos mucho más grandes como o3-mini-high de OpenAI (34,5%) y Claude 3.7 Sonnet (21,2%). No se trata de pequeñas diferencias estadísticamente insignificantes: estamos hablando de brechas de rendimiento sustanciales que, en el mundo de la IA, equivalen a saltos generacionales.

Pero es en las tareas de razonamiento más extremas donde HRM demuestra realmente su superioridad arquitectónica. En las pruebas de Sudoku de nivel extremo y en los laberintos complejos, las diferencias se vuelven abismales. HRM resolvió el 55% de los Sudokus más difíciles, mientras que los modelos basados en la cadena de pensamiento obtuvieron un rotundo 0%. El mismo resultado para los laberintos de cuadrícula de 30x30: HRM encontró el camino óptimo en el 74,5% de los casos, mientras que sus competidores se quedaron en el punto de partida con un 0%.

Es la versión IA del adagio de Yoda: "El tamaño no importa. Mírame. ¿Me juzgas por mi tamaño?". Solo que en este caso, la Fuerza es la arquitectura jerárquica y Luke Skywalker son los modelos de miles de millones de parámetros que siguen estrellándose en el pantano.

No son solo números en una tabla: representan la diferencia entre una inteligencia artificial que puede enfrentarse a problemas complejos del mundo real y una que se atasca ante desafíos que requieren más que un razonamiento superficial. Es la diferencia entre un asistente que puede ayudarte a navegar por decisiones complejas y uno que, como mucho, puede ayudarte a escribir correos electrónicos más elocuentes.

Pero quizás el dato más impresionante de todos se refiere a la eficiencia del entrenamiento. Mientras que los modelos de lenguaje tradicionales requieren enormes conjuntos de datos extraídos de todo Internet y meses de procesamiento en los superordenadores más potentes del mundo, HRM se entrena con solo mil ejemplos por tarea. Como declaró Guan Wang, uno de los fundadores de Sapient Intelligence, "podrías entrenarlo en Sudoku a nivel profesional en dos horas de GPU", una eficiencia que define literalmente como "ridícula" en el mejor sentido de la palabra.
![benchmark_hrm.jpg](benchmark_hrm.jpg)
*[Imagen extraída de Sapient.inc HRM](https://sapient.inc/)*

## Más allá de los benchmarks: una revolución estructural

Los impresionantes resultados en las pruebas estandarizadas son solo la punta del iceberg. La verdadera revolución que aporta HRM reside en su capacidad para resolver problemas estructurales fundamentales que afectan a toda la generación actual de modelos basados en transformadores, problemas que hasta hace poco parecían una parte inevitable del panorama de la inteligencia artificial.

El primero y más significativo de estos problemas es la eficiencia de la memoria. Los transformadores tradicionales son notoriamente ávidos de recursos, ya que requieren enormes cantidades de memoria para funcionar y aún más para ser entrenados. HRM, en cambio, utiliza actualizaciones de gradiente más locales, que son más fáciles de calcular y "mucho más plausibles biológicamente", evitando la famosa "retropropagación profunda en el tiempo" que es intensiva en memoria y computacionalmente lenta.

Esta eficiencia de memoria no es una simple mejora incremental: es un cambio de paradigma que abre escenarios completamente nuevos. Menos memoria significa poder ejecutar más modelos simultáneamente en el mismo hardware, entrenar más rápido con menos recursos y, sobre todo, llevar la inteligencia artificial avanzada a dispositivos que hasta ayer eran impensables. Estamos hablando de ordenadores portátiles comunes, dispositivos de borde, robots e incluso coches, todos lugares donde la IA podría operar de forma autónoma sin depender de conexiones a Internet constantes o servidores remotos.

La empresa Sapient ya está probando HRM en aplicaciones del mundo real que demuestran esta versatilidad. En el sector sanitario, el modelo se utiliza para ayudar en el diagnóstico de enfermedades rares, esas patologías complejas que requieren exactamente el tipo de razonamiento profundo y matizado en el que HRM sobresale. En las previsiones climáticas estacionales, ha alcanzado tasas de precisión del 97%, un resultado que en el mundo de la meteorología equivale casi a la ciencia ficción.

Pero quizás el aspecto más alentador de HRM es el equipo que hay detrás. No se trata de investigadores desconocidos que trabajan en garajes: el grupo incluye a ex ingenieros de DeepMind, Anthropic, DeepSeek e incluso del grupo XAI de Elon Musk. Son personas que han trabajado en la vanguardia de la inteligencia artificial durante años y que ahora apuestan todo por el diseño inspirado en el cerebro de HRM. Cuando profesionales de este calibre abandonan las certezas de los grandes gigantes tecnológicos para perseguir una visión alternativa, merece la pena prestar atención.

Guan Wang, el CEO y fundador de Sapient Intelligence, no se anda con rodeos cuando habla del futuro de la inteligencia artificial. Su visión es que la AGI, la inteligencia artificial general, consiste en dar a las máquinas una inteligencia a nivel humano y superior. Y según Wang, la cadena de pensamiento es solo un "atajo", mientras que lo que han construido "puede pensar" en el verdadero sentido de la palabra.

## Código abierto y transparencia: un regalo a la comunidad

En una época en la que los grandes laboratorios de IA tienden a mantener secretos comerciales cada vez más estrictos sobre sus modelos más avanzados, la decisión de Sapient Intelligence de hacer que HRM sea completamente de código abierto representa un gesto de transparencia casi revolucionario. Todo el proyecto está [disponible en GitHub](https://github.com/sapientinc/HRM), lo que permite a cualquiera en el mundo verificarlo, entrenar su propia versión, modificarlo o construir sobre él. Este nivel de apertura es raro para una innovación tan prometedora y estratégicamente importante.

Por supuesto, HRM todavía tiene limitaciones que sus creadores reconocen abiertamente. Por ahora, el modelo tiene un enfoque más restringido que los grandes modelos de lenguaje generalistas: está construido para razonar, no para charlar amigablemente o escribir poesía romántica. Pero es precisamente esta especialización lo que lo hace tan potente en su dominio. Es una de las pruebas de concepto más sólidas que el sector ha visto para demostrar que el futuro de la IA podría no residir en modelos cada vez más grandes y generalistas, sino en arquitecturas más inteligentes y especializadas.

HRM no es el único experimento de este tipo en curso. El panorama de la investigación en IA está viviendo un momento de efervescencia creativa, con equipos de todo el mundo que exploran arquitecturas alternativas a los transformadores dominantes. Está Sakana con sus máquinas de pensamiento continuo, los modelos LLM de 1 bit que prometen una eficiencia extrema y los modelos de razonamiento basados en la difusión de Google. Pero hay una diferencia crucial: HRM "ya está funcionando" y superando a modelos mucho más grandes con una fracción de los datos de entrenamiento y sin necesidad de un preentrenamiento masivo.

Esto sugiere que estamos asistiendo a un cambio de paradigma fundamental. El próximo gran salto en la inteligencia artificial probablemente no será otro "clon de GPT escalado" a dimensiones aún más mastodónticas, sino algo similar a HRM: una nueva arquitectura que aporta un mejor razonamiento, un entrenamiento más rápido y una implementación más económica, todo ello sin la necesidad de centros de datos llenos de GPU que consumen la electricidad de ciudades enteras.

## El futuro que realmente piensa

De cara al futuro, la visión que se desprende del trabajo de HRM es la de un futuro en el que la inteligencia artificial ya no estará confinada en los centros de datos de las grandes corporaciones tecnológicas, sino que se convertirá en una presencia omnipresente y accesible en nuestra vida cotidiana. Imagina agentes de IA que viven en nuestros ordenadores portátiles, en los robots domésticos, en los coches, incluso en los dispositivos portátiles, todos capaces de un razonamiento sofisticado sin depender de conexiones a Internet constantes o de costosos servidores remotos.

Esta democratización de la inteligencia artificial avanzada podría tener profundas implicaciones en la forma en que trabajamos, aprendemos y resolvemos problemas. Un médico en una clínica rural podría tener acceso a las mismas herramientas de diagnóstico avanzado que un hospital metropolitano. Un ingeniero que trabaja en una obra de construcción remota podría obtener análisis estructurales complejos en tiempo real. Un investigador en un laboratorio con un presupuesto limitado podría explorar hipótesis científicas complejas sin tener que competir por el acceso a los superordenadores.

Pero quizás el aspecto más fascinante de todos es la idea de que estos agentes de IA ya no se limitarán a "hablar" con Internet o a regurgitar información procesada en otros lugares. Empezarán a "pensar de verdad", en el sentido más profundo del término, desarrollando soluciones originales, formulando hipótesis creativas y quizás incluso desarrollando intuiciones que los humanos nunca habríamos considerado.

Como toda revolución tecnológica, esta transformación traerá consigo nuevos desafíos y cuestiones éticas que deberemos afrontar. Pero si HRM y arquitecturas similares cumplen sus promesas, podríamos estar a las puertas de una era en la que la inteligencia artificial se convierta por fin en lo que su nombre promete: no solo un sofisticado sistema de procesamiento de información, sino un verdadero socio intelectual capaz de un razonamiento autónomo y creativo.

Como diría Tony Stark, a veces la mejor solución no es construir una armadura más grande, sino construirla más inteligente. Y HRM podría haber encontrado la manera de reemplazar la fuerza bruta computacional con algo mucho más elegante y eficiente.

El camino aún es largo y está lleno de incógnitas, pero una cosa es cierta: el pequeño modelo de 27 millones de parámetros creado en una startup de Singapur ya ha demostrado que en el mundo de la inteligencia artificial, como suele ocurrir en la ciencia, la calidad puede realmente superar a la cantidad. Y quizás, al igual que en las mejores historias de David contra Goliat, es precisamente el más pequeño el que nos muestra el camino hacia el futuro.
