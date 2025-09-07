---
tags: ["Research", "Training", "Generative AI"]
date: 2025-09-07
author: Dario Ferrero
---

# Revolución DeepConf: más precisión y menos recursos para los LLM
![aideepconffire.jpg](aideepconffire.jpg)

*Imagina que estás en un examen de matemáticas particularmente difícil. Tienes delante un problema que te hace sudar frío, de esos de las Olimpiadas de Matemáticas que hacen llorar hasta a los más listos. ¿La estrategia clásica? Probar y volver a probar, escribir decenas de intentos diferentes con la esperanza de que uno sea el correcto. Pero hay un enfoque más inteligente: darte cuenta de cuándo vas en la dirección equivocada y detenerte antes de malgastar tiempo y energía.*

Eso es exactamente lo que ha hecho un joven equipo de investigadores de Meta AI, liderado por [Jiawei Zhao](https://jiaweizzhao.github.io/deepconf/), investigador en Meta AI FAIR con formación en el prestigioso Caltech, junto a sus colegas [Yichao Fu y Xuewei Wang](https://ai.meta.com/research/publications/deep-think-with-confidence/).

Su trabajo, publicado en arXiv hace solo unas semanas con el título ["Deep Think with Confidence"](https://arxiv.org/abs/2508.15260), representa uno de esos descubrimientos que parecen sencillos a posteriori pero que en realidad esconden una notable complejidad técnica. Como el gesto aparentemente trivial de Arquímedes en la bañera, esta investigación también parte de una observación elemental: si una inteligencia artificial está razonando mal, ¿por qué no enseñarle a reconocerlo por sí misma?

## El Problema: Cuando "Pensar Más" No Es Suficiente

Para entender el alcance revolucionario de este enfoque, demos un paso atrás. Los modelos de lenguaje grandes, los que todos llamamos LLM, tienen una característica particular cuando se enfrentan a problemas complejos: cuantos más intentos hacen, mejores son sus respuestas. Es como si fueran estudiantes particularmente tercos que siguen reintentando un ejercicio hasta que lo aciertan.

Este enfoque, llamado técnicamente "test-time scaling", funciona con una lógica aparentemente simple: si haces que el modelo genere cincuenta soluciones diferentes a un problema y luego eliges la más frecuente entre todas, las probabilidades de acertar aumentan drásticamente. Es el principio de la "self-consistency with majority voting" (autoconsistencia con voto por mayoría), una estrategia que ha funcionado muy bien durante años.

Pero hay un problema, en realidad dos. El primero es económico: generar decenas o cientos de respuestas cuesta una fortuna en términos de potencia computacional. Es como alquilar cincuenta ordenadores para hacer el mismo cálculo esperando que la mayoría llegue al resultado correcto. El segundo problema es más sutil: después de cierto punto, añadir más intentos no mejora significativamente los resultados. Es la clásica "ley de rendimientos decrecientes" que conocen bien los economistas, aplicada al mundo de la inteligencia artificial.

## La Solución: De "Más Fuerte" a "Más Inteligente"

Y aquí es donde entra en juego la genial intuición del equipo de Meta. En lugar de seguir martilleando el problema con la fuerza bruta computacional, ¿por qué no enseñar al modelo a reconocer cuándo está a punto de tomar un camino equivocado? Es un poco como el radar de proximidad de los coches modernos: en lugar de esperar el impacto, te avisa antes de que estés a punto de chocar contra un obstáculo.

[DeepConf, este es el nombre del nuevo método](https://ai.meta.com/research/publications/deep-think-with-confidence/), aprovecha lo que los investigadores llaman "señales de confianza internas del modelo". En palabras sencillas, cada vez que un LLM genera una palabra o un concepto, tiene una especie de "termómetro interno" que indica cuán seguro está de esa elección. Es como cuando respondes a una pregunta de un concurso: a veces estás 100% seguro, otras veces dudas entre dos opciones.

La brillantez de DeepConf reside en transformar este "dudar" interno en un filtro inteligente. En lugar de generar ciegamente cientos de intentos y luego contarlos uno por uno, el sistema monitoriza en tiempo real la confianza del modelo y descarta automáticamente los razonamientos que muestran señales de incertidumbre demasiado elevadas. Es como tener un asistente personal que te susurra al oído "quizás sea mejor que pruebes con otro enfoque" cuando te ve enredarte en una solución equivocada.

## Cómo Funciona: Los Secretos de la Nueva Arquitectura

Desde el punto de vista técnico, DeepConf trabaja en dos niveles complementarios. El primero es lo que los investigadores llaman "filtering during generation", es decir, el filtrado durante la generación. Imagina ser Sherlock Holmes que, mientras razona en voz alta, se da cuenta de que está siguiendo una pista equivocada y cambia de dirección inmediatamente. Esto es exactamente lo que hace DeepConf: monitoriza las probabilidades logarítmicas internas del modelo token por token y, cuando detecta patrones de incertidumbre, interrumpe esa línea de razonamiento particular y comienza una nueva.

El segundo nivel es el "filtering after generation", que funciona más como un editor experto. Una vez que el modelo ha generado varias soluciones completas, DeepConf analiza retrospectivamente las señales de confianza de cada traza de razonamiento y les asigna una puntuación de fiabilidad. Es como tener un corrector de pruebas que no se limita a contar los errores, sino que evalúa la coherencia general del razonamiento.

La verdadera magia, sin embargo, reside en la simplicidad de su implementación. Como señalan los autores en su artículo, [DeepConf no requiere ningún entrenamiento adicional del modelo ni optimización de hiperparámetros](https://arxiv.org/abs/2508.15260). Es un enfoque "plug-and-play" que puede integrarse en los frameworks de servicio existentes como vLLM sin modificaciones sustanciales en la arquitectura. Es como instalar un nuevo software en tu ordenador: no tienes que cambiar el hardware, funciona con lo que ya tienes.
![deepthinkconfidence.jpg](deepthinkconfidence.jpg)
[*Imagen de jiaweizzhao.github.io/deepconf*](https://jiaweizzhao.github.io/deepconf/)

## Los Números que Asombran

Los resultados obtenidos por el equipo de Meta son, como mínimo, impresionantes, con ese sabor a "demasiado bueno para ser verdad" que caracteriza a los descubrimientos realmente innovadores. En AIME 2025, uno de los benchmarks más difíciles para el razonamiento matemático (piénsalo como el examen de selectividad para las inteligencias artificiales), [DeepConf alcanzó una precisión del 99.9% reduciendo simultáneamente el uso de tokens en un 84.7%](https://venturebeat.com/ai/metas-deepconf-offers-a-dial-to-balance-llm-reasoning-cost-and-accuracy) en comparación con los métodos tradicionales.

Para entender el alcance de estas cifras, hagamos una comparación cinematográfica. Es como si alguien hubiera inventado una forma de rodar películas de calidad de Hollywood usando una décima parte del presupuesto habitual, manteniendo la misma calidad visual y narrativa. En el mundo de la IA, donde cada token generado tiene un coste computacional medible, una reducción del 85% significa literalmente recortar los costes operativos en un orden de magnitud.

Pero no es solo una cuestión económica. El aspecto más fascinante es que DeepConf consigue mejorar el rendimiento precisamente eliminando el "ruido" computacional. Es contraintuitivo: normalmente, en informática, cuantos más recursos dedicas a un problema, mejores resultados obtienes. Aquí, en cambio, ocurre lo contrario: al eliminar los intentos de baja calidad, la señal emerge más claramente del ruido de fondo.

Las pruebas se realizaron en los modelos de código abierto más avanzados, incluidos Qwen 3 y la serie GPT-OSS, lo que demuestra que el enfoque funciona de forma transversal en diferentes arquitecturas. Es como descubrir que un truco funciona tanto en iPhone como en Android: significa que probablemente has encontrado algo fundamental.

## Dos Modos, Un Objetivo

DeepConf opera en dos modos distintos, como un coche deportivo que puede funcionar tanto en modo eco como en modo performance. El modo "offline" analiza todas las trazas de razonamiento generadas y luego selecciona aquellas con las mejores señales de confianza. Es perfecto para aplicaciones en las que tienes tiempo para reflexionar y quieres la máxima precisión posible.

El modo "online", en cambio, está pensado para aplicaciones en tiempo real donde la velocidad es crucial. En este caso, DeepConf interrumpe dinámicamente las trazas de razonamiento que muestran señales de baja confianza y comienza otras nuevas sobre la marcha. Es como tener un GPS inteligente que, en lugar de seguir calculando una ruta que sabe que es incorrecta, cambia inmediatamente de rumbo hacia un destino más prometedor.

La flexibilidad de este enfoque es uno de sus puntos fuertes. Los desarrolladores pueden calibrar el sistema según sus necesidades específicas: más conservador para aplicaciones críticas donde el error no es tolerable, más agresivo para casos de uso donde la velocidad prevalece sobre la perfección absoluta.

## Impacto Práctico: La Revolución Económica

El impacto económico de DeepConf podría ser devastador para la industria de la IA, en el buen sentido del término. Piensa en las implicaciones: si puedes obtener el mismo rendimiento de un sistema que cuesta 1000 dólares al día con uno que cuesta 150, de repente servicios que antes eran económicamente insostenibles se vuelven accesibles a un público mucho más amplio de usuarios y empresas.

Pero no es solo una cuestión de costes directos. La reducción de los tokens generados también significa menores emisiones de CO2, menos estrés en los centros de datos y, en definitiva, una IA más sostenible desde el punto de vista medioambiental. Es como pasar de un SUV que consume 15 litros cada 100 kilómetros a un coche híbrido que consume 4, manteniendo la misma velocidad y comodidad.

Para las empresas que ofrecen servicios basados en LLM, DeepConf representa un potencial cambio de juego competitivo. Quien consiga implementarlo primero podrá ofrecer servicios de mayor calidad a precios más bajos, creando ese tipo de ventaja competitiva que redefine industrias enteras. Es la clásica "disrupción" de la que habla Clayton Christensen, aplicada al mundo de la inteligencia artificial.

## Perspectivas Futuras: Hacia una IA Autoconsciente

Pero quizás el aspecto más fascinante de DeepConf no son ni siquiera los resultados inmediatos, sino lo que representa como dirección de investigación. Por primera vez, tenemos un sistema que no se limita a generar respuestas, sino que desarrolla una forma primitiva de metacognición: la capacidad de reflexionar sobre sus propios procesos de pensamiento.

Es un paso importante hacia lo que los investigadores llaman "IA autoconsciente", sistemas que no solo resuelven problemas, sino que también son conscientes de cómo los están resolviendo y, sobre todo, de cuándo están fallando. No estamos hablando de conciencia en el sentido de ciencia ficción del término, sino de una forma de inteligencia procedimental que sabe cuándo confiar en sí misma y cuándo ser escéptica.

El equipo de Meta ha demostrado que este tipo de "autoduda constructiva" se puede implementar sin revolucionar las arquitecturas existentes, abriendo el camino a una nueva generación de modelos más eficientes y económicos. Es como si hubiéramos encontrado una forma de hacer que las máquinas no solo sean más inteligentes, sino también más sabias en el sentido de saber reconocer sus propios límites.

Mirando al futuro, DeepConf podría ser solo el aperitivo de una revolución más amplia. Si las máquinas pueden aprender a dudar de sus propias respuestas en el ámbito matemático, ¿qué les impide aplicar el mismo principio a la escritura creativa, a la resolución de problemas éticos o incluso a la investigación científica? El camino hacia una inteligencia artificial verdaderamente de propósito general podría pasar precisamente por esta capacidad de autocrítica constructiva.

El trabajo de Zhao y sus colegas demuestra que a veces las revoluciones más importantes nacen de las intuiciones más simples. En un mundo donde todos persiguen modelos cada vez más grandes y potentes, ellos han optado por centrarse en la eficiencia y la autoconciencia. Como diría el buen viejo Einstein, "todo debería hacerse tan simple como sea posible, pero no más simple". DeepConf parece haber encontrado perfectamente este equilibrio, abriendo nuevas fronteras para una IA más inteligente, sostenible y, paradójicamente, más humana en su capacidad de cuestionarse a sí misma.
