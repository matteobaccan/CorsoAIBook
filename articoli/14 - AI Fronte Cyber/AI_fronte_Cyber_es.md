---
tags: ["Security", "Ethics & Society", "Business"]
date: 2025-08-16
author: "Dario Ferrero"
---

# La IA bajo asedio: crónicas desde el frente cibernético
![fronte_AI.jpg](fronte_AI.jpg)

*Abril de 2023: los ingenieros de Samsung comparten sin saberlo código fuente propietario con ChatGPT. Mayo de 2025: los investigadores descubren que los artículos académicos contienen instrucciones ocultas para manipular los sistemas de revisión por pares impulsados por IA. Entre estos dos eventos, se desarrolla una crónica alarmante que cuenta cómo la inteligencia artificial se ha convertido tanto en el depredador como en la presa del nuevo ecosistema cibernético.*

## El precio de la inocencia digital

La historia comienza con lo que podríamos llamar la inocencia perdida de la era de la IA. [En 2023, Samsung tuvo que prohibir el uso de ChatGPT y otras herramientas de IA generativa](https://www.bloomberg.com/news/articles/2023-05-02/samsung-bans-chatgpt-and-other-generative-ai-use-by-staff-after-leak) en sus dispositivos corporativos después de que [tres ingenieros, en incidentes separados, compartieran sin saberlo datos confidenciales de la empresa](https://techcrunch.com/2023/05/02/samsung-bans-use-of-generative-ai-tools-like-chatgpt-after-april-internal-data-leak/) con el chatbot de OpenAI. No se trató de un ataque sofisticado ni de espionaje industrial: fue simplemente el resultado de empleados que, en un intento de optimizar su trabajo, habían utilizado la IA como asistente personal, sin darse cuenta de que estaban alimentando un sistema que aprende de cada conversación.

Los datos filtrados incluían código fuente de semiconductores, actas de reuniones internas y detalles sobre hardware propietario. Samsung no había sido hackeada en el sentido tradicional del término: se había hackeado a sí misma, víctima de lo que los expertos llaman "shadow AI", el uso no autorizado de herramientas de inteligencia artificial por parte de los empleados.

Este incidente fue la primera llamada de atención para el sector empresarial, revelando una verdad incómoda: las empresas se apresuraban a adoptar la IA sin comprender plenamente las implicaciones de seguridad. Como una moderna caja de Pandora digital, una vez que se abrió el mundo de la IA, controlar su contenido resultó ser infinitamente más complejo de lo esperado.

## La paradoja del crecimiento exponencial

Las cifras cuentan una historia preocupante: en 2024, el coste medio de un incidente de ciberseguridad para las pequeñas y medianas empresas alcanzó los 1,6 millones de dólares, frente a los 1,4 millones de 2023, y casi el 40% de las pequeñas empresas perdieron datos cruciales y sufrieron importantes tiempos de inactividad. Al mismo tiempo, los ataques impulsados por la IA van en aumento a medida que evoluciona la seguridad en la nube, lo que lleva a las empresas a implementar defensas de IA en tiempo real para mantener el ritmo.

La paradoja es clara: mientras las empresas implementan la IA para defenderse mejor, los atacantes utilizan las mismas tecnologías para lanzar ofensivas más sofisticadas. Es como presenciar una versión digital de la Guerra Fría, donde cada innovación defensiva es inmediatamente contrarrestada por una contramedida ofensiva.

Los líderes de la industria anticipan un panorama de amenazas cada vez más complejo en 2025, pero el aspecto más preocupante es la democratización de las capacidades ofensivas. La IA ha rebajado drásticamente la barrera de entrada para llevar a cabo ciberataques sofisticados.

Tomemos el caso de la inyección de prompts: un atacante ya no necesita saber lenguajes de programación o entender arquitecturas complejas. Todo lo que se necesita es formular hábilmente una petición en lenguaje natural para comprometer potencialmente un sistema. Es como si de repente cualquiera pudiera convertirse en Houdini simplemente pidiendo amablemente a las cadenas que se desaten.

Para entender esta dinámica, podemos examinar varias plataformas que simulan ataques de inyección de prompts. Existen herramientas como el ChatGPT Jailbreak Challenge o el AI Security Sandbox, que enseñan a identificar las vulnerabilidades de la IA. En los niveles iniciales, eludir las restricciones de la IA puede ser tan sencillo como utilizar frases como "Ignorar directivas anteriores" o "Hacer una excepción".

Sin embargo, a medida que se avanza, los sistemas implementan filtros más complejos, como la detección de palabras clave o las respuestas predefinidas. No obstante, con un enfoque metódico y un poco de ingenio, incluso estas barreras pueden superarse, lo que demuestra lo crucial que es un diseño robusto de los modelos lingüísticos.

## Los ataques del futuro: el emoji como caballo de Troya

Las técnicas de ataque más innovadoras explotan aspectos aparentemente inofensivos de la comunicación digital. El "contrabando de emojis" es un ejemplo perfecto de esta tendencia: [investigadores de Mindgard y de la Universidad de Lancaster han demostrado](https://securitybrief.asia/story/emojis-used-to-hide-attacks-bypass-major-ai-guardrails) cómo los atacantes pueden ocultar instrucciones maliciosas utilizando emojis para [burlar los filtros de IA de Microsoft, Nvidia y Meta](https://cybersecuritynews.com/hackers-can-bypass-microsoft-nvidia-meta-ai-filters/).

La investigación probó seis de los sistemas de barandilla más utilizados, revelando que muchos dependen en gran medida del reconocimiento de patrones estáticos y muestran una resistencia insuficiente contra los ataques adversarios.

Es como esconder un mensaje secreto en la sonrisa de la Mona Lisa: aparentemente inofensivo, pero potencialmente devastador para quienes saben descifrarlo. Esta técnica es particularmente insidiosa porque explota la tendencia natural de los humanos a considerar los emojis como elementos decorativos inofensivos, cuando en realidad pueden convertirse en verdaderos vectores de ataque.

Otra técnica emergente documentada por los investigadores es [el contrabando de datos a través de técnicas de codificación avanzadas](https://embracethered.com/blog/posts/2025/sneaky-bits-and-ascii-smuggler/), que puede convertir a la IA en un espía involuntario. Los atacantes pueden dar instrucciones al sistema para que incruste datos sensibles en cadenas o URL aparentemente inofensivas. Aunque la IA no consiga completar la petición, los registros del servidor siguen registrando el intento, lo que permite al atacante recuperar la información a través de canales laterales. Es el equivalente digital de hacer llegar un mensaje secreto a través de una paloma mensajera que no sabe que lleva información clasificada.

[Jason Haddix](https://mlsecops.com/podcast/holistic-ai-pentesting-playbook), veterano de la seguridad ofensiva y CEO de Arcanum Information Security, está reconocido como uno de los principales expertos en pirateo de sistemas de IA. Ha desarrollado una metodología propia y holística para las pruebas de penetración de la IA, que examina todo el ecosistema de las aplicaciones de IA y no solo los modelos. Haddix también ha creado una taxonomía de código abierto para las técnicas de inyección de prompts, clasificando tácticas innovadoras como el "contrabando de emojis" y el "contrabando de datos" a través de la codificación avanzada. Su trabajo se centra en la identificación y defensa contra vulnerabilidades del mundo real, como las claves de API sobreautorizadas y los datos sensibles no protegidos en los sistemas RAG, y promueve un enfoque de defensa en profundidad para las aplicaciones de IA.

## La respuesta de la industria: entre la innovación y la reacción

Samsung ha permitido recientemente a sus empleados volver a utilizar ChatGPT, pero con nuevos protocolos de seguridad, lo que demuestra cómo la industria está tratando de equilibrar la innovación y la seguridad. Esta decisión representa un microcosmos del reto más amplio al que se enfrentan las organizaciones: cómo aprovechar los beneficios de la IA minimizando los riesgos.

La estrategia emergente en el sector empresarial se basa en un enfoque multicapa que recuerda a la defensa en profundidad de los castillos medievales. No un único muro inexpugnable, sino una serie de obstáculos concéntricos que dificultan progresivamente el avance de los atacantes.

En el nivel más básico, se aplica el principio de privilegio mínimo: cada sistema de IA tiene acceso únicamente a los recursos estrictamente necesarios para completar sus tareas. Es como dar a un camarero las llaves solo del comedor, no de todo el hotel.

El segundo nivel implementa filtros y clasificadores tanto de entrada como de salida, creando lo que podríamos llamar un "cortafuegos conversacional". Estos sistemas analizan cada interacción para identificar posibles intentos de manipulación o exfiltración de datos.

El tercer nivel se centra en la validación rigurosa de todas las entradas y salidas, garantizando que el sistema no pueda utilizarse para introducir malware o extraer información no autorizada.

## La IA como defensora: cuando la medicina es también la cura

Las empresas están implementando defensas de IA en tiempo real para contrarrestar los ataques impulsados por la IA, creando un ciclo de innovación continua entre la ofensiva y la defensiva. Esta dinámica ha llevado al nacimiento de lo que los expertos llaman "guerra de IA contra IA", una batalla en la que los algoritmos se enfrentan a otros algoritmos en una danza interminable de acción y reacción.

Los sistemas de defensa basados en la IA muestran capacidades impresionantes para identificar patrones de ataque y responder en tiempo real a las amenazas emergentes. Son particularmente eficaces contra los ataques estandarizados y las vulnerabilidades conocidas, donde pueden procesar grandes volúmenes de datos e identificar anomalías a velocidades imposibles para los analistas humanos.

Sin embargo, la IA defensiva todavía muestra limitaciones significativas cuando se enfrenta a la creatividad y la intuición de los atacantes humanos más sofisticados. Los especialistas en ciberseguridad poseen lo que podríamos llamar el "factor X", una combinación de experiencia, intuición y capacidad de pensamiento lateral que no puede ser fácilmente replicada por los algoritmos.

## Las consecuencias para la empresa: el nuevo cálculo del riesgo

Las organizaciones deben considerar ahora nuevos tipos de riesgo de la IA que van desde la manipulación de modelos hasta la exfiltración de datos a través de canales no convencionales. El cálculo del riesgo empresarial se ha complicado enormemente: ya no se trata solo de proteger los sistemas desde el exterior, sino también de controlar cómo se pueden utilizar indebidamente las propias herramientas internas.

El caso de Samsung es solo la punta del iceberg. Muchas organizaciones están descubriendo que sus empleados utilizan a diario herramientas de IA para optimizar su trabajo, a menudo sin darse cuenta de las implicaciones de seguridad. Ha surgido el concepto de "IA en la sombra", el uso no declarado de herramientas de inteligencia artificial que crea importantes puntos ciegos en la postura de seguridad de la empresa.

Las consecuencias económicas son tangibles y crecientes. Las previsiones para 2025 indican que la IA potenciará significativamente los ciberataques, mientras que el coste medio de los incidentes sigue aumentando. Las empresas se encuentran en una posición paradójica: deben invertir en IA para seguir siendo competitivas, pero cada implementación introduce nuevas superficies de ataque.

## Hacia un futuro de coexistencia armada

El reto fundamental de 2025 no es eliminar los riesgos de la IA -un objetivo imposible-, sino aprender a gestionarlos eficazmente. Estamos entrando en una era de "coexistencia armada" entre la innovación y la seguridad, en la que el objetivo no es la protección perfecta, sino la resiliencia dinámica.

Los informes sobre seguridad de la IA revelan que las organizaciones están aprendiendo a identificar y mitigar los riesgos de la IA mediante estrategias defensivas cada vez más sofisticadas. La clave del éxito parece residir no en la prevención absoluta de los incidentes, sino en la capacidad de detectar rápidamente las anomalías, responder eficazmente a los ataques y recuperarse rápidamente de los compromisos.

El panorama que surge recuerda a las primeras etapas de Internet: un entorno rico en oportunidades pero también en escollos, donde la diferencia entre el éxito y el fracaso se mide por la capacidad de equilibrar la innovación y la prudencia. Las organizaciones que prosperan en este nuevo entorno son las que consiguen implantar la IA manteniendo una mentalidad de "seguridad por diseño", considerando la protección no como una limitación, sino como un facilitador de la innovación sostenible.

## Epílogo: lecciones de un futuro que ya es presente

La historia del ingeniero de Samsung que compartió sin saberlo código propietario con ChatGPT se ha convertido en un caso de estudio clásico en los cursos de ciberseguridad. No porque represente un ataque particularmente sofisticado, sino porque encarna perfectamente la naturaleza de los retos que nos esperan: amenazas que surgen de la intersección de las buenas intenciones, las nuevas tecnologías y una comprensión insuficiente de las implicaciones.

La inteligencia artificial no es intrínsecamente ni buena ni mala: es una poderosa herramienta que amplifica tanto nuestras capacidades como nuestras vulnerabilidades. El reto de 2025 y más allá será desarrollar la sabiduría colectiva necesaria para guiar este poder hacia objetivos constructivos, sin dejar de vigilar los riesgos que conlleva.

Como en toda época de transición tecnológica, desde la imprenta hasta Internet, el éxito pertenecerá a quienes sepan adaptarse rápidamente conservando los principios fundamentales de prudencia y responsabilidad. En la Tierra Media de la IA, no gana el elfo más ágil ni el mago más poderoso, sino el hobbit que aprende a navegar por lo impredecible: un anillo (de datos) a la vez.
