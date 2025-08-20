---
tags: ["Research", "Ethics & Society", "Business"]
date: 2025-08-20
---

# Le "Nobel" de l'informatique : "Producteurs d'IA, vous vous êtes égarés"
*par Dario Ferrero (VerbaniaNotizie.it)*
![SuttonMoses.jpg](SuttonMoses.jpg)


*Imaginez un chef étoilé qui, après avoir inventé la recette parfaite du risotto, découvre que tous les restaurants du monde ne servent aux clients que du riz cru saupoudré de parmesan. C'est à peu près ce que doit ressentir Richard Sutton en observant le paysage actuel de l'intelligence artificielle. Le [co-lauréat du prix Turing 2024](https://awards.acm.org/turing) - qui, dans le monde de l'informatique, équivaut au prix Nobel - a lancé un j'accuse qui sonne comme un signal d'alarme pour une industrie qui, selon lui, s'est complètement égarée sur la voie de la véritable intelligence.*

## L'anatomie d'une révolution trahie

Sutton, figure de proue de l'apprentissage par renforcement et lauréat du prix Turing, affirme que l'industrie de l'IA a perdu son chemin, et il ne s'agit pas d'une critique émanant d'un universitaire grincheux relégué dans un coin de l'université. Nous parlons de l'un des [pères fondateurs de l'apprentissage par renforcement computationnel](https://www.ualberta.ca/en/computing-science/news-and-events/news/2025/march/rich-sutton-receives-the-2024-acm-am-turing-award.html), celui qui, avec Andrew Barto, a jeté les bases conceptuelles et algorithmiques de ce qui permet aujourd'hui aux robots d'apprendre à marcher et aux voitures autonomes de naviguer dans la circulation.

Mais qu'entend exactement Sutton lorsqu'il dit que l'industrie "a perdu son chemin" ? Sa critique ne vise pas les résultats commerciaux - ils sont indéniables - mais le fait que l'approche dominante actuelle en matière d'IA consiste à construire des châteaux de sable plutôt que des fondations solides pour l'intelligence du futur. [Comme il l'écrit sur X](https://x.com/RichardSSutton/status/1957501548214513897), "À mesure que l'IA est devenue une industrie énorme, elle a, dans une certaine mesure, perdu son chemin", arguant que les progrès récents ont ignoré les principes fondamentaux nécessaires à une véritable intelligence.

Le cœur du problème est autant philosophique que technique. Les grands modèles de langage actuels, ces géants qui dévorent des téraoctets de texte pour nous donner des réponses apparemment intelligentes, font selon Sutton exactement le contraire de ce qu'une véritable intelligence artificielle devrait faire : ils ont leurs connaissances "programmées" au moment de la conception, plutôt que découvertes par l'apprentissage par l'expérience.
![tweetsutton.jpg](tweetsutton.jpg)

## Le grand malentendu : mise à l'échelle contre apprentissage

Pour comprendre la profondeur de la critique de Sutton, il faut prendre du recul et considérer ce qu'il a lui-même appelé la ["Leçon amère"](http://www.incompleteideas.net/IncIdeas/BitterLesson.html) en 2019 - un essai qui est devenu une sorte de manifeste dans la recherche sur l'IA. La leçon amère est la suivante : à long terme, les méthodes évolutives et générales l'emportent toujours sur les systèmes construits en incorporant des connaissances spécifiques à un domaine. C'est comme la différence entre apprendre à quelqu'un à pêcher et lui donner un poisson tous les jours : la première approche est évolutive à l'infini, la seconde vous oblige à continuer à pêcher pour lui.

Et pourtant, en regardant l'industrie aujourd'hui, il semble que tout le monde ait décidé de pêcher pour ses IA au lieu de leur apprendre à le faire. Les modèles de langage contemporains sont alimentés par des quantités astronomiques de textes humains, absorbant passivement des modèles et des corrélations. C'est une approche qui fonctionne - et les résultats sont là pour le prouver - mais qui, selon Sutton, représente une impasse évolutive.

La critique devient encore plus acerbe si l'on considère que Sutton a travaillé chez Google DeepMind, l'une des entreprises qui a le plus contribué au succès des modèles de langage. Il ne s'agit donc pas du classique outsider qui tire sur le système, mais de quelqu'un qui connaît intimement les mécanismes internes de l'industrie et qui a décidé d'élever la voix de l'intérieur.

## L'architecture Oak : un manifeste pour l'avenir

Sutton ne se contente pas de diagnostiquer le problème, il propose également une solution radicale appelée l'architecture Oak (Options and Knowledge). Il s'agit d'un cadre qui pourrait sembler tout droit sorti d'un épisode de Black Mirror, si Black Mirror était écrit par des ingénieurs optimistes plutôt que par des scénaristes pessimistes.

Oak repose sur trois principes fondamentaux : l'agent doit être polyvalent et ne disposer d'aucune connaissance spécifique d'un monde particulier ; l'apprentissage est entièrement guidé par l'expérience, l'agent n'acquérant des connaissances que par une interaction directe avec son environnement ; et l'hypothèse de la récompense est appliquée, selon laquelle tout objectif peut être réduit à la maximisation d'un simple signal de récompense scalaire.

Le cœur d'Oak est une boucle d'auto-renforcement qui semble presque mystique dans sa simplicité : l'agent crée des abstractions de plus en plus élevées grâce au retour d'information, où les caractéristiques qui aident à la planification et à la résolution de problèmes deviennent la base de la prochaine génération de connaissances, encore plus abstraites. Ce processus est ouvert, limité uniquement par la puissance de calcul disponible, et selon Sutton, il pourrait à terme ouvrir la voie à la superintelligence.

Cela ressemble à de la science-fiction, mais un problème bien terrestre empêche la réalisation de cette vision : Oak dépend d'algorithmes capables d'apprendre de manière continue et stable sans oublier ce qu'ils ont déjà appris. C'est le fameux problème de l'"oubli catastrophique" : lorsqu'un réseau neuronal apprend quelque chose de nouveau, il a tendance à "écraser" ce qu'il savait auparavant, comme un disque dur qui ne cesse d'effacer les anciens fichiers pour faire de la place aux nouveaux.

## Le paradoxe de l'apprentissage continu

Nous arrivons ici au cœur technique de la question, ce qui sépare les rêves de la réalité réalisable. Sutton identifie le principal problème des systèmes actuels dans le fait qu'ils ne peuvent pas apprendre en continu : ils luttent contre l'oubli catastrophique, où les nouvelles informations écrasent ce qu'ils ont déjà appris, perdant ainsi la capacité de continuer à apprendre au fil du temps.

C'est un peu comme si, chaque fois que nous apprenions une nouvelle langue, nous devions oublier toutes celles que nous connaissions auparavant. Chez l'homme, cela ne se produit pas - ou du moins pas de manière aussi radicale - parce que notre cerveau a développé des mécanismes sophistiqués pour intégrer de nouvelles connaissances sans effacer les précédentes. Mais nos algorithmes d'apprentissage profond sont encore primitifs en ce sens : ils sont bons pour apprendre à partir de zéro sur d'énormes ensembles de données, mais incapables de continuer à apprendre sans perdre leur stabilité.

Il ne s'agit pas d'un simple détail technique, mais de la différence entre la construction d'une intelligence qui croît et évolue en permanence et celle qui reste figée au moment de sa dernière session de formation. Et c'est ici que la critique de Sutton devient plus pertinente que jamais : l'industrie investit des milliards dans des systèmes qui, aussi impressionnants soient-ils, représentent essentiellement des instantanés statiques de connaissances plutôt que des intelligences dynamiques et adaptatives.
![era_of_experience_graph.png](era_of_experience_graph.png)
[*Image tirée de medium.com*](https://medium.com)

## La voix dissidente à l'ère de la mise à l'échelle

Sutton se joint à d'autres chercheurs de premier plan pour critiquer la fixation de l'industrie sur la mise à l'échelle des grands modèles de langage, mais sa position est particulièrement intéressante car elle émane de quelqu'un que l'on ne peut accuser d'être hors du coup. Le [prix Turing qu'il a reçu en 2024](https://www.nsf.gov/news/ai-pioneers-andrew-barto-richard-sutton-win-2024-turing) avec Andrew Barto était assorti d'un chèque d'un million de dollars sponsorisé par Google, l'entreprise qui a le plus encouragé l'approche basée sur les grands modèles de langage.

Sa critique prend ainsi les contours d'une véritable dissidence intellectuelle au sein du système. Lorsque l'un des lauréats du "prix Nobel d'informatique" qui a travaillé pour l'une des plus grandes entreprises de technologie du secteur de l'IA déclare que l'industrie s'est égarée, il convient peut-être d'y prêter attention.

Mais Sutton n'est pas le seul à être sceptique. Avec David Silver, professeur à l'University College London, connu entre autres pour avoir dirigé le développement d'AlphaGo, le système qui a battu en 2016 le champion du monde de Go Lee Sedol, il a récemment [publié un article](https://storage.googleapis.com/deepmind-media/Era-of-Experience%20/The%20Era%20of%20Experience%20Paper.pdf) qui soutient que l'IA devrait apprendre en faisant, et pas seulement en absorbant d'énormes quantités de textes écrits par des humains. C'est une position qui trouve un écho de plus en plus fort auprès d'une partie de la communauté des chercheurs qui voient dans les LLM une voie vers le succès commercial, mais pas nécessairement vers l'intelligence générale.

## Les implications d'une révolution manquée

Si Sutton a raison - et sa crédibilité scientifique suggère qu'il faut prendre ses arguments au sérieux - qu'est-ce que cela signifie pour l'avenir de l'IA ? Premièrement, nous pourrions nous trouver dans ce que les biologistes appellent une "impasse évolutive" : une voie qui mène à des succès localisés mais qui n'a pas d'issue vers des niveaux de complexité supérieurs.

Les systèmes d'IA actuels, aussi impressionnants soient-ils dans leurs capacités linguistiques et de raisonnement, pourraient représenter une sorte de plateau technologique - des systèmes qui excellent dans des tâches spécifiques mais qui ne peuvent pas évoluer vers des formes d'intelligence plus générales et adaptatives. C'est comme si nous avions perfectionné la machine à écrire au moment même où nous étions sur le point d'inventer l'ordinateur.

Deuxièmement, il y a une question plus profonde de durabilité et d'efficacité. Les approches actuelles nécessitent des quantités croissantes de données et de puissance de calcul, suivant une courbe qui pourrait ne pas être durable à long terme. L'approche proposée par Sutton, basée sur des agents qui apprennent par interaction directe avec l'environnement, pourrait représenter une voie plus efficace vers l'intelligence artificielle générale.

## Vers un avenir incertain mais fascinant

La vision de Sutton pour l'avenir de l'IA n'est pas seulement technique, elle est presque philosophique dans sa portée. Il imagine des systèmes qui non seulement traitent l'information, mais qui "comprennent" réellement le monde par l'expérience directe, qui construisent des modèles de réalité de plus en plus sophistiqués par une interaction et un retour d'information continus.

C'est une vision qui nécessite une révolution non seulement au niveau des algorithmes, mais aussi des infrastructures. Comme l'explique Sutton, "ce dont nous avons besoin pour nous remettre sur la bonne voie vers une véritable intelligence, ce sont des agents qui apprennent en permanence, des modèles du monde et de la planification, des connaissances de haut niveau et apprenables, et la méta-capacité d'apprendre à généraliser."

Bien sûr, il y a un risque que ce soit le classique "prochain grand truc" qui reste toujours "prochain" sans jamais devenir "actuel". L'apprentissage continu stable reste l'un des problèmes les plus difficiles en IA, et on ne sait pas quand - ni si - nous parviendrons à le résoudre. Mais s'il y a une leçon que l'histoire de la technologie nous a apprise, c'est que les révolutions viennent souvent des endroits les plus inattendus, proposées par des voix qui, au départ, sonnent comme des dissidents.

Richard Sutton, avec son palmarès d'innovations qui ont défini le domaine et sa position unique d'initié critique, pourrait être exactement le genre de voix que l'industrie de l'IA a besoin d'entendre. Même si - et peut-être surtout si - ce qu'il dit remet en question tout ce que nous avons construit jusqu'à présent.

Pendant ce temps, alors que l'industrie continue de repousser les limites de ce que les grands modèles de langage peuvent faire, depuis l'Alberta, un lauréat du prix Turing qui a vu naître et grandir DeepMind de l'intérieur continue de rêver d'agents qui apprennent comme des enfants curieux, explorant le monde pas à pas. C'est un peu comme si Willy Wonka, après avoir inventé l'usine de chocolat la plus avancée du monde, décidait d'en sortir pour nous rappeler que le meilleur goût ne vient pas des machines les plus sophistiquées, mais de la recette la plus simple : celle de l'expérience directe.

Sutton observe aujourd'hui l'industrie qu'il a contribué à façonner avec les yeux de quelqu'un qui a vu l'avenir et qui sait que nous allons dans la mauvaise direction. Sa voix, amplifiée par le poids d'une carrière qui a défini des générations entières de chercheurs, résonne comme un avertissement que nous ne pouvons pas nous permettre d'ignorer. Parce que l'expérience nous apprend que les plus grands changements commencent souvent par quelqu'un qui a le courage de dire que l'empereur est nu - même quand cet empereur a des milliards de paramètres et sait répondre à n'importe quelle question.
