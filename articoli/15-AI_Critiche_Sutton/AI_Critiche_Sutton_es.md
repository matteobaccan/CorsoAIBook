---
tags: ["Research", "Ethics & Society", "Business"]
date: 2025-08-20
author: "Dario Ferrero"
---

# El "Nobel" de informática: "Productores de IA, habéis perdido el rumbo"
![SuttonMoses.jpg](SuttonMoses.jpg)


*Imagina a un chef con estrella Michelin que, tras inventar la receta perfecta para el risotto, descubre que todos los restaurantes del mundo sólo sirven a los clientes arroz crudo con un poco de parmesano por encima. Esto es más o menos lo que debe de sentir Richard Sutton al observar el panorama actual de la inteligencia artificial. El [co-ganador del Premio Turing 2024](https://awards.acm.org/turing) -que en el mundo de la informática equivale al Premio Nobel- ha lanzado un j'accuse que suena a voz de alarma para una industria que, en su opinión, ha perdido por completo el rumbo hacia la verdadera inteligencia.*

## La anatomía de una revolución traicionada

Sutton, figura destacada del aprendizaje por refuerzo y ganador del Premio Turing, afirma que la industria de la IA ha perdido el rumbo, y no se trata de una crítica de un académico gruñón relegado a un rincón de la universidad. Estamos hablando de uno de los [padres fundadores del aprendizaje por refuerzo computacional](https://www.ualberta.ca/en/computing-science/news-and-events/news/2025/march/rich-sutton-receives-the-2024-acm-am-turing-award.html), el que junto con Andrew Barto sentó las bases conceptuales y algorítmicas de lo que hoy permite a los robots aprender a caminar y a los coches autónomos a navegar en el tráfico.

Pero, ¿a qué se refiere exactamente Sutton cuando dice que la industria "ha perdido el rumbo"? Su crítica no se dirige a los resultados comerciales -que son innegables-, sino al hecho de que el actual enfoque dominante en la IA está construyendo castillos de arena en lugar de cimientos sólidos para la inteligencia del futuro. [Como escribe en X](https://x.com/RichardSSutton/status/1957501548214513897), "A medida que la IA se ha convertido en una industria enorme, en cierta medida ha perdido el rumbo", argumentando que los avances recientes han ignorado los principios fundamentales necesarios para una verdadera inteligencia.

El quid de la cuestión es tanto filosófico como técnico. Los actuales Grandes Modelos Lingüísticos, esos gigantes que devoran terabytes de texto para darnos respuestas aparentemente inteligentes, según Sutton hacen exactamente lo contrario de lo que debería hacer una verdadera inteligencia artificial: tienen su conocimiento "programado" en el momento del diseño, en lugar de ser descubierto a través del aprendizaje experiencial.
![tweetsutton.jpg](tweetsutton.jpg)

## El gran malentendido: escalar frente a aprender

Para comprender la profundidad de la crítica de Sutton, hay que dar un paso atrás y considerar lo que él mismo llamó la ["Lección Amarga"](http://www.incompleteideas.net/IncIdeas/BitterLesson.html) en 2019, un ensayo que se ha convertido en una especie de manifiesto en la investigación de la IA. La lección amarga es la siguiente: a largo plazo, los métodos escalables y generales siempre ganan a los sistemas construidos incorporando conocimientos específicos del dominio. Es como la diferencia entre enseñar a alguien a pescar y darle un pescado cada día: el primer enfoque escala indefinidamente, el segundo te obliga a seguir pescando para él.

Y, sin embargo, si observamos la industria actual, parece que todo el mundo ha decidido pescar para sus IA en lugar de enseñarles a hacerlo. Los modelos lingüísticos contemporáneos se alimentan de cantidades astronómicas de texto humano, absorbiendo pasivamente patrones y correlaciones. Es un enfoque que funciona -y los resultados están a la vista de todos-, pero que, según Sutton, representa un callejón sin salida evolutivo.

La crítica se vuelve aún más mordaz si se tiene en cuenta que Sutton trabajó en Google DeepMind, una de las empresas que más ha contribuido al éxito de los modelos lingüísticos. Así que no se trata del clásico advenedizo que dispara contra el sistema, sino de alguien que conoce íntimamente los mecanismos internos de la industria y que ha decidido alzar la voz desde dentro.

## La arquitectura Oak: un manifiesto para el futuro

Sutton no se limita a diagnosticar el problema, sino que también propone una solución radical llamada arquitectura Oak (Opciones y Conocimiento). Es un marco que podría parecer sacado directamente de un episodio de Black Mirror, si Black Mirror estuviera escrito por ingenieros optimistas en lugar de por guionistas pesimistas.

Oak se basa en tres principios fundamentales: el agente debe ser de propósito general, partiendo sin conocimientos específicos de ningún mundo en particular; el aprendizaje se guía enteramente por la experiencia, adquiriendo el agente conocimientos exclusivamente a través de la interacción directa con su entorno; y se aplica la hipótesis de la recompensa, según la cual cualquier objetivo puede reducirse a la maximización de una simple señal de recompensa escalar.

El corazón de Oak es un bucle de autorrefuerzo que suena casi místico en su simplicidad: el agente crea abstracciones de nivel cada vez más alto a través de la retroalimentación, donde las características que ayudan en la planificación y la resolución de problemas se convierten en la base para la siguiente generación de conocimiento, aún más abstracto. Este proceso es abierto, limitado únicamente por la potencia de cálculo disponible, y según Sutton podría llegar a allanar el camino hacia la superinteligencia.

Suena a ciencia ficción, pero hay un problema muy terrenal que impide que esta visión se haga realidad: Oak depende de algoritmos que puedan aprender de forma continua y estable sin olvidar lo que ya han aprendido. Es el famoso problema del "olvido catastrófico": cuando una red neuronal aprende algo nuevo, tiende a "sobrescribir" lo que sabía antes, como un disco duro que sigue borrando archivos antiguos para hacer sitio a los nuevos.

## La paradoja del aprendizaje continuo

Aquí llegamos al meollo técnico de la cuestión, lo que separa los sueños de la realidad implementable. Sutton identifica el principal problema de los sistemas actuales en el hecho de que no pueden aprender de forma continua: luchan con el olvido catastrófico, donde la nueva información sobrescribe lo que ya han aprendido, perdiendo la capacidad de seguir aprendiendo con el tiempo.

Es un poco como si cada vez que aprendemos un nuevo idioma tuviéramos que olvidar todos los que sabíamos antes. En los humanos esto no ocurre -o al menos no de forma tan drástica- porque nuestros cerebros han desarrollado sofisticados mecanismos para integrar nuevos conocimientos sin borrar los anteriores. Pero nuestros algoritmos de aprendizaje profundo siguen siendo primitivos en este sentido: buenos para aprender de cero con enormes conjuntos de datos, pero incapaces de seguir aprendiendo sin perder la estabilidad.

No se trata de un mero detalle técnico, sino de la diferencia entre construir una inteligencia que crece y evoluciona continuamente y otra que permanece congelada en el momento de su última sesión de entrenamiento. Y es aquí donde la crítica de Sutton cobra más actualidad que nunca: la industria está invirtiendo billones en sistemas que, por muy impresionantes que sean, representan esencialmente instantáneas estáticas de conocimiento en lugar de inteligencias dinámicas y adaptativas.
![era_of_experience_graph.png](era_of_experience_graph.png)
[*Imagen de medium.com*](https://medium.com)

## La voz disidente en la era de la escalada

Sutton se une a otros destacados investigadores en la crítica a la fijación de la industria por la ampliación de los grandes modelos lingüísticos, pero su posición es especialmente interesante porque procede de alguien a quien no se puede acusar de estar fuera de juego. El [Premio Turing que recibió en 2024](https://www.nsf.gov/news/ai-pioneers-andrew-barto-richard-sutton-win-2024-turing) junto con Andrew Barto vino con un cheque de un millón de dólares patrocinado por Google, la empresa que más ha impulsado el enfoque basado en los grandes modelos lingüísticos.

Su crítica adquiere así los contornos de una verdadera disidencia intelectual desde dentro del sistema. Cuando uno de los ganadores del "Premio Nobel de informática" que ha trabajado para una de las empresas de Big Tech más influyentes del sector de la IA dice que la industria ha perdido el rumbo, quizá merezca la pena prestarle atención.

Pero Sutton no está solo en su escepticismo. Junto con David Silver, profesor del University College London, conocido entre otras cosas por haber dirigido el desarrollo de AlphaGo, el sistema que en 2016 derrotó al campeón mundial de Go Lee Sedol, ha [publicado recientemente un artículo](https://storage.googleapis.com/deepmind-media/Era-of-Experience%20/The%20Era%20of%20Experience%20Paper.pdf) en el que argumenta que la IA debería aprender haciendo, no sólo absorbiendo enormes cantidades de texto escrito por humanos. Es una postura que resuena con fuerza creciente en una parte de la comunidad investigadora que ve en los LLM una vía hacia el éxito comercial, pero no necesariamente hacia la inteligencia general.

## Las implicaciones de una revolución fallida

Si Sutton tiene razón -y su credibilidad científica sugiere que merece la pena tomarse en serio sus argumentos-, ¿qué significa esto para el futuro de la IA? En primer lugar, podríamos encontrarnos en lo que los biólogos llaman un "callejón sin salida evolutivo": un camino que conduce a éxitos localizados pero que no tiene salida a niveles superiores de complejidad.

Los sistemas de IA actuales, por muy impresionantes que sean en sus capacidades lingüísticas y de razonamiento, podrían representar una especie de meseta tecnológica: sistemas que destacan en tareas específicas pero que no pueden evolucionar hacia formas de inteligencia más generales y adaptativas. Es como si hubiéramos perfeccionado la máquina de escribir justo cuando estábamos a punto de inventar el ordenador.

En segundo lugar, hay una cuestión más profunda de sostenibilidad y eficiencia. Los enfoques actuales requieren cantidades crecientes de datos y potencia de cálculo, siguiendo una curva que puede no ser sostenible a largo plazo. El enfoque propuesto por Sutton, basado en agentes que aprenden a través de la interacción directa con el entorno, podría representar un camino más eficiente hacia la inteligencia artificial general.

## Hacia un futuro incierto pero fascinante

La visión de Sutton sobre el futuro de la IA no es meramente técnica, es casi filosófica en su alcance. Imagina sistemas que no sólo procesan información, sino que realmente "comprenden" el mundo a través de la experiencia directa, que construyen modelos de la realidad cada vez más sofisticados a través de la interacción y la retroalimentación continuas.

Es una visión que requiere una revolución no sólo en los algoritmos, sino también en la infraestructura. Como explica Sutton, "lo que necesitamos para volver al camino correcto hacia la verdadera inteligencia son agentes que aprendan continuamente, modelos del mundo y planificación, conocimiento de alto nivel y aprendible, y la metacapacidad de aprender a generalizar."

Por supuesto, existe el riesgo de que se trate del clásico "próximo gran acontecimiento" que siempre sigue siendo "próximo" sin llegar a ser nunca "actual". El aprendizaje continuo estable sigue siendo uno de los problemas más difíciles de la IA, y no está claro cuándo -o si- seremos capaces de resolverlo. Pero si hay una lección que nos ha enseñado la historia de la tecnología, es que las revoluciones suelen venir de los lugares más inesperados, propuestas por voces que al principio suenan a disidentes.

Richard Sutton, con su historial de innovaciones que han definido el campo y su posición única como conocedor crítico, podría ser exactamente el tipo de voz que la industria de la IA necesita oír. Incluso si -y quizás especialmente si- lo que dice pone en tela de juicio todo lo que hemos construido hasta ahora.

Mientras tanto, mientras la industria sigue superando los límites de lo que pueden hacer los grandes modelos lingüísticos, desde Alberta, un premio Turing que ha visto nacer y crecer a DeepMind desde dentro sigue soñando con agentes que aprenden como niños curiosos, explorando el mundo paso a paso. Es un poco como si Willy Wonka, después de inventar la fábrica de chocolate más avanzada del mundo, decidiera salir de ella para recordarnos que el mejor sabor no procede de las máquinas más sofisticadas, sino de la receta más sencilla: la de la experiencia directa.

Sutton observa hoy la industria que ayudó a forjar con los ojos de quien ha visto el futuro y sabe que vamos en la dirección equivocada. Su voz, amplificada por el peso de una carrera que ha definido a generaciones enteras de investigadores, resuena como una advertencia que no podemos permitirnos ignorar. Porque la experiencia nos enseña que los mayores cambios suelen empezar con alguien que tiene el valor de decir que el emperador está desnudo, incluso cuando ese emperador tiene billones de parámetros y sabe responder a cualquier pregunta.
