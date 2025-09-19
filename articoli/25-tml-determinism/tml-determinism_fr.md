---
tags: ["Research", "Generative AI", "Training", "Startups"]
date: 2025-09-15
author: Dario Ferrero
---

# LLM : Même question, réponse différente ? C'est peut-être la faute des GPU
![tml.jpg](tml.jpg)

*Imaginez que vous ayez un chef étoilé qui, chaque fois que vous lui demandez la recette de la carbonara, vous répond avec des nuances différentes. Aujourd'hui, il ajoute le guanciale en premier, demain les œufs, après-demain il change l'ordre des pâtes. Le résultat final est toujours de la carbonara, mais jamais exactement la même. C'est exactement ce qui se passe avec les grands modèles de langage : même entrée, sorties différentes. Toujours.*

C'est un phénomène que quiconque a déjà discuté avec ChatGPT connaît bien, mais qui jusqu'à aujourd'hui était considéré comme une caractéristique intrinsèque de l'intelligence artificielle. "C'est normal", disaient les experts, "ça fait partie du processus d'échantillonnage". Comme s'il était inévitable qu'un système mathématique déterministe produise des résultats aléatoires.

[Thinking Machines Lab](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/), la startup dirigée par des vétérans de l'IA qui a récemment attiré d'importants investissements, a décidé de ne pas se contenter de cette explication. Leur dernier article, publié en septembre 2025, ne se contente pas d'identifier le problème : il le résout. Et la solution est aussi élégante qu'inattendue.

## Quand les chiffres deviennent anarchiques

Pour comprendre le cœur du problème, nous devons faire un saut dans les mathématiques informatiques. Comme dans "Un jour sans fin", le film où Bill Murray revit indéfiniment le même jour avec des variations imperceptibles, les ordinateurs semblent également condamnés à répéter les mêmes calculs en obtenant des résultats légèrement différents. Mais cette fois, il n'y a pas de leçon existentielle derrière : il y a la physique des processeurs.

Le principal coupable s'appelle la "non-associativité des nombres à virgule flottante". En mathématiques, (a+b)+c devrait toujours être égal à a+(b+c). Sur les ordinateurs, cependant, cette règle saute allègrement par la fenêtre. C'est comme si chaque fois que vous faites un calcul, l'ordre dans lequel vous additionnez les nombres changeait le résultat final.

Horace He, le chercheur principal de Thinking Machines Lab, explique dans l'article que [ce phénomène provient de la manière dont les processeurs gèrent ensemble des nombres très grands et très petits](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/). C'est un peu comme essayer de faire la moyenne entre le nombre d'habitants de Rome et le poids d'un grain de sable : la précision limitée des ordinateurs fait que certains détails se perdent inévitablement.

## L'anatomie de l'erreur : Au cœur des trois piliers de l'indéterminisme

Pour bien comprendre la portée de la solution de Thinking Machines Lab, il est nécessaire de pénétrer au cœur d'un transformeur. Tel un horloger qui démonte une Patek Philippe pour comprendre pourquoi elle perd quelques secondes par jour, les chercheurs ont dû disséquer chaque composant critique du modèle pour identifier l'origine de l'indéterminisme.

L'architecture d'un grand modèle de langage moderne repose sur trois piliers fondamentaux, qui contribuent chacun au problème de manière différente. C'est comme un orchestre de chambre où chaque section a ses particularités : les violons (RMSNorm) créent des dissonances subtiles, les cuivres (multiplications de matrices) amplifient les erreurs, et les bois (mécanisme d'attention) transforment de petites variations en changements dramatiques dans l'harmonie finale.

Le RMSNorm, acronyme de Root Mean Square Normalization, est peut-être le composant le plus simple à comprendre et paradoxalement le plus facile à corriger. [Sa fonction est de normaliser les valeurs d'entrée pour stabiliser l'entraînement](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/), un peu comme un égaliseur qui maintient le volume constant quelle que soit l'intensité de la source. Le problème se pose lorsque la "taille du lot" (le nombre de requêtes traitées simultanément) est trop petite.

Imaginez un chef d'orchestre qui doit diriger parfois 100 musiciens, parfois seulement 10. Avec 100 musiciens, il peut assigner un rôle spécifique à chaque section et maintenir un contrôle précis. Avec seulement 10, il doit demander à certains de doubler leurs instruments, ce qui modifie inévitablement la dynamique de l'exécution. Le RMSNorm se comporte de la même manière : lorsqu'il y a peu de requêtes à traiter, il est contraint de changer de stratégie de parallélisation, ce qui entraîne des variations dans les calculs.

La solution de Thinking Machines Lab est aussi simple que radicale : ignorer les cas problématiques. Lorsque la taille du lot est trop petite pour garantir une parallélisation optimale, le système accepte une perte de performance pour maintenir la cohérence. C'est un choix philosophique profond : il vaut mieux être toujours cohérent que parfois rapide.

Les multiplications de matrices représentent un défi d'une complexité supérieure. Il ne s'agit pas seulement de paralléliser un calcul, mais d'exploiter au mieux les "tensor cores", des unités de calcul spécialisées présentes dans les GPU modernes qui peuvent effectuer des milliers d'opérations simultanées. C'est comme passer de l'utilisation d'un piano traditionnel à un orgue d'église avec des centaines de registres : la puissance est immense, mais la complexité du contrôle augmente de façon exponentielle.

Le problème se pose lorsque les dimensions des matrices sont trop petites pour exploiter pleinement ces unités spécialisées. Dans ces cas, les pilotes GPU ont recours à des stratégies alternatives appelées "Split-K", où la multiplication est décomposée le long de la dimension de réduction plutôt que le long des dimensions de sortie. [C'est une technique brillante pour optimiser les performances, mais elle introduit de la variabilité dans les résultats](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/) car elle modifie l'ordre des opérations mathématiques.

La solution adoptée par Thinking Machines Lab est apparemment contre-intuitive : utiliser toujours la même configuration de noyau, quelles que soient les dimensions des matrices. C'est comme décider de jouer toujours avec la même formation orchestrale, même lorsque la pièce musicale ne l'exige pas. On perd en efficacité, mais on gagne en prévisibilité.

Le troisième pilier, le mécanisme d'attention, est celui qui présente les plus grands défis. Ce n'est pas un hasard si l'attention est au cœur de l'architecture du transformeur, le composant qui permet au modèle de "prêter attention" à différentes parties de l'entrée pour générer chaque mot. C'est comme un réalisateur qui doit décider sur quels acteurs pointer la caméra à chaque instant de la scène, en se basant sur tout ce qui s'est passé avant.

Le mécanisme d'attention introduit deux niveaux de complexité supplémentaires. Tout d'abord, il doit gérer des réductions à la fois le long de la dimension des caractéristiques et le long de la dimension de la séquence, créant un enchevêtrement de dépendances qui rend presque impossible le maintien d'un ordre de calcul fixe. Deuxièmement, il doit s'interfacer avec toutes les optimisations modernes de l'inférence : le pré-remplissage par blocs (où les longues séquences sont traitées par morceaux), la mise en cache des préfixes (où les parties communes des conversations sont réutilisées) et le décodage parallèle.

[Le problème le plus insidieux apparaît au stade dit du "décodage"](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/), lorsque le modèle génère un mot à la fois. Dans cette phase, la longueur de la requête est généralement très petite (souvent un seul jeton), mais le cache des clés et des valeurs peut être énorme (des milliers de jetons de contexte précédent). C'est comme demander à un chanteur soliste de se produire accompagné d'un orchestre symphonique : le rapport de forces est complètement déséquilibré.

Pour maintenir des performances acceptables, les systèmes ont recours à des techniques appelées "Split-KV" ou "FlashDecoding", qui parallélisent le traitement le long de la dimension du cache. Mais une fois de plus, cette parallélisation introduit de la variabilité dans l'ordre des calculs. La solution de Thinking Machines Lab nécessite une modification profonde de ces algorithmes, en adoptant une stratégie de "taille de division fixe" plutôt qu'une stratégie de "nombre de divisions fixe".

C'est une distinction subtile mais fondamentale. Au lieu de dire "divise toujours en 8 parties", le système dit "chaque partie doit toujours faire 256 éléments". De cette manière, l'ordre des opérations reste identique quelle que soit la longueur totale de la séquence. C'est comme décider que chaque musicien doit toujours jouer exactement 4 mesures, quelle que soit la longueur du morceau.

L'élégance de cette solution réside dans son universalité : une fois que les trois piliers ont été rendus "invariants au lot", l'ensemble du système devient déterministe. Il n'est pas nécessaire de redessiner l'architecture des transformeurs ou d'inventer de nouveaux algorithmes. Il suffit de garantir que chaque composant se comporte toujours de la même manière, quel que soit le contexte dans lequel il est exécuté.
![inference.jpg](inference.jpg)
[De thinkingmachines.ai](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/)

## L'invariance des lots : la clé secrète

Mais voici le rebondissement digne d'un thriller technologique : le vrai problème ne réside pas dans la concurrence entre les processeurs GPU, comme le soutenaient les théories précédentes. C'est quelque chose de beaucoup plus subtil et, paradoxalement, plus facile à résoudre.

La découverte de Thinking Machines Lab est que le comportement des LLM change en fonction du nombre de requêtes traitées simultanément. C'est comme si notre chef étoilé changeait de recette en fonction du nombre de couverts qu'il doit préparer en même temps. Même plat, mêmes ingrédients, mais le résultat final dépend de la charge de travail du moment.

Ce phénomène a un nom technique : le manque d'"invariance de lot". En termes simples, cela signifie que le traitement d'une seule requête ou de 100 requêtes en même temps peut produire des réponses différentes pour la même question. [Les chercheurs ont démontré cet effet avec des expériences surprenantes](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/) : en posant 1000 fois la même question sur Richard Feynman à un modèle Qwen, ils ont obtenu 80 réponses différentes, la première divergence se manifestant exactement au 103e jeton.

La solution proposée par Thinking Machines Lab est d'une simplicité élégante : modifier les "noyaux" (les blocs de calcul fondamentaux) pour qu'ils produisent toujours les mêmes résultats, quel que soit le nombre d'autres opérations effectuées en parallèle. C'est comme apprendre à notre chef à suivre toujours la même séquence d'étapes, qu'il cuisine pour une ou pour cent personnes.
![batch.jpg](batch.jpg)
[De thinkingmachines.ai](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/)

## Le prix de la cohérence

Comme dans toute histoire d'innovation technologique, la solution comporte des compromis. Les noyaux "invariants au lot" développés par l'équipe sont plus lents que les noyaux standard. Pas de beaucoup, heureusement : lors des tests effectués sur un serveur à GPU unique utilisant le modèle Qwen-3-8B, le ralentissement s'est établi à environ 60 % par rapport à la version optimisée, tombant à 30 % avec quelques améliorations de l'implémentation de l'attention.

Cela peut sembler un prix élevé à payer, mais considérez les implications. [L'indéterminisme des LLM n'est pas seulement une nuisance esthétique](https://dataconomy.com/2025/09/11/tml-defeating-nondeterminism-in-llm-inference/) : il compromet la reproductibilité scientifique, rend impossible un débogage précis et, surtout, transforme ce qui devrait être un apprentissage par renforcement "on-policy" en quelque chose de complètement différent.

C'est un peu comme essayer d'entraîner un pilote de Formule 1 sur un simulateur qui change les lois de la physique à chaque fois qu'on l'allume. Le pilote apprend à s'adapter aux variations, mais il n'apprend pas vraiment à conduire cette voiture spécifique.

## La révolution silencieuse du RL

C'est là qu'intervient l'un des aspects les plus intéressants de la recherche de Thinking Machines Lab. L'apprentissage par renforcement, la technique qui sous-tend les modèles les plus avancés comme ChatGPT, repose sur l'idée que l'IA apprend de ses propres expériences. Mais si chaque fois que l'IA "essaie" la même action, elle obtient un résultat légèrement différent, apprend-elle vraiment de la même expérience ?

Les chercheurs ont montré que [l'indéterminisme transforme subrepticement l'apprentissage "on-policy" en apprentissage "off-policy"](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/), créant un décalage entre ce que le modèle fait pendant l'entraînement et ce qu'il fait lorsqu'il est utilisé. C'est comme si un musicien s'entraînait sur un piano désaccordé pour ensuite jouer sur un piano accordé : la différence est subtile mais fondamentale.

Avec les noyaux déterministes de Thinking Machines Lab, ce problème disparaît. Dans leurs expériences sur une configuration de RL appliquée à l'ensemble de données Bigmath, l'équipe a obtenu une divergence KL parfaitement plate à zéro, ce qui indique une correspondance parfaite entre l'entraînement et l'inférence. C'est le Saint Graal de l'apprentissage automatique : un système qui se comporte exactement comme il a été entraîné à le faire.

## Le paysage industriel : qui gagnera la guerre de la reproductibilité ?

Dans le monde de l'intelligence artificielle, où les géants de la technologie s'affrontent avec des modèles toujours plus grands et plus performants, Thinking Machines Lab a choisi de mener une bataille différente. Alors qu'OpenAI, Google et Anthropic se concentrent sur la puissance brute de leurs systèmes, cette équipe relativement petite a décidé de miser sur la précision. C'est l'histoire classique de David contre Goliath, mais cette fois, la fronde de David est la mathématique pure.

La startup, fondée par d'anciens chercheurs de certaines des entreprises les plus prestigieuses du secteur, représente une approche complètement différente de la recherche en IA. [Il ne s'agit pas de créer le modèle le plus grand ou le plus rapide, mais de comprendre en profondeur comment ces systèmes fonctionnent réellement](https://americanbazaaronline.com/2025/09/11/inside-thinking-machines-lab-muratis-12-billion-ai-startup-tackles-reproducibility-467536/). C'est un peu comme la différence entre construire une voiture de course de plus en plus puissante et comprendre pourquoi la voiture va parfois à gauche alors qu'elle devrait aller tout droit.

Le moment de cette recherche n'est pas un hasard. L'industrie de l'IA se trouve à un tournant crucial, où la course à la performance pure cède la place à des considérations plus mûres sur la fiabilité, la sécurité et la prévisibilité. C'est le moment où un secteur adolescent commence à se comporter en adulte, et la reproductibilité est l'un des premiers signes de cette maturation.

Les secteurs les plus critiques se font déjà entendre. Dans le monde de la santé, où les algorithmes d'IA sont de plus en plus utilisés pour les diagnostics et les plans de traitement, l'idée que le même symptôme puisse produire des évaluations différentes est tout simplement inacceptable. C'est comme avoir un thermomètre qui donne des températures différentes à chaque fois qu'on l'utilise : peut-être que la fièvre est toujours là, mais ne pas savoir si elle est de 38 ou 39 degrés fait la différence entre un paracétamol et une course à l'hôpital.

Le secteur financier n'est pas en reste. Les algorithmes de trading automatique et les systèmes d'évaluation des risques doivent fonctionner dans un monde où la reproductibilité n'est pas une préférence, mais une exigence réglementaire. [Les autorités de surveillance commencent à exiger que les modèles d'IA utilisés pour les décisions de crédit ou d'investissement produisent des résultats traçables et vérifiables](https://dataconomy.com/2025/09/11/tml-defeating-nondeterminism-in-llm-inference/). Il est impossible d'expliquer à un juge pourquoi le même algorithme a donné des avis différents sur deux demandes de prêt identiques.

Le monde de la recherche scientifique prend également conscience du problème. Lorsqu'un article scientifique affirme avoir obtenu certains résultats à l'aide d'un modèle d'IA, d'autres chercheurs doivent pouvoir reproduire exactement ces expériences. C'est le fondement même de la méthode scientifique, remis en question par l'indéterminisme des LLM. Comme si chaque fois que vous reproduisiez une expérience de physique, la gravité était légèrement différente.

Mais les implications vont bien au-delà de ces secteurs évidemment critiques. Pensez à l'impact sur le débogage et le développement de logiciels. Actuellement, lorsqu'une application basée sur l'IA se comporte de manière inattendue, les développeurs se retrouvent dans une situation kafkaïenne : le bogue pourrait se trouver dans leur code, ou il pourrait simplement s'agir d'une autre manifestation de l'indéterminisme du modèle. C'sest comme essayer de réparer une montre qui décide parfois d'elle-même d'aller plus vite ou plus lentement.

La solution de Thinking Machines Lab promet de transformer cette chasse au fantôme en un processus de débogage normal. Si le modèle produit toujours les mêmes sorties pour les mêmes entrées, tout comportement anormal est nécessairement dû à une erreur réelle, et non à une fluctuation aléatoire. C'est la différence entre être un détective dans un monde où les preuves changent spontanément et être un détective dans un monde où les preuves restent cohérentes.

L'aspect le plus intéressant de cette dynamique est qu'aucun des grands acteurs du secteur ne semble avoir donné la priorité à ce problème. OpenAI, Google, Meta et les autres géants sont tous obsédés par la course à la performance, tandis que la question de la reproductibilité est restée au second plan. C'est l'une de ces rares situations dans le monde de la technologie où une startup peut réellement devancer des entreprises disposant de cent fois plus de ressources, simplement parce qu'elle a identifié le bon problème au bon moment.

Bien sûr, convaincre l'industrie d'adopter une solution qui entraîne un ralentissement de 30 à 60 % ne sera pas facile. Dans le monde de l'IA, où les millisecondes de latence peuvent faire la différence entre le succès et l'échec d'un produit, tout compromis sur les performances est vu avec méfiance. Mais les signes de changement sont déjà là.

Certaines entreprises pionnières commencent à expérimenter des versions "déterministes" de leurs systèmes pour des applications spécifiques. Il n'est pas surprenant que les premiers à les adopter soient précisément ceux qui opèrent dans des secteurs hautement réglementés, où le coût de l'indéterminisme dépasse de loin l'avantage de quelques millisecondes de latence en moins.

## Vers un avenir déterministe

La vraie partie se jouera lorsque les noyaux invariants au lot de Thinking Machines Lab seront optimisés au point de réduire considérablement l'écart de performance. À ce moment-là, la question ne sera plus "pouvons-nous nous permettre d'être déterministes ?" mais "pouvons-nous nous permettre de ne pas l'être ?".

La solution proposée par Thinking Machines Lab n'est pas encore prête pour la production à grande échelle. Le code est disponible sur GitHub à titre de preuve de concept, mais il nécessite des modifications importantes des pipelines d'inférence existants. Cependant, les implications sont énormes.

Pensez à un monde où les LLM produisent toujours la même réponse à la même question. Nous ne parlons pas d'IA moins créatives ou plus rigides, mais de systèmes plus fiables et prévisibles. Un assistant virtuel qui vous donne toujours le même conseil médical pour le même symptôme. Un système de traduction qui ne change pas de version du texte à chaque redémarrage. Un modèle d'analyse financière qui produit toujours la même évaluation pour les mêmes données.

Il est intéressant de noter comment cette recherche s'inscrit dans une tendance plus large vers ce que l'on pourrait appeler une "IA responsable". Après des années de course effrénée vers des modèles toujours plus grands et plus puissants, l'industrie commence à se poser des questions plus mûres : non seulement "que pouvons-nous faire ?" mais aussi "que devrions-nous faire ?" et "comment pouvons-nous le faire mieux ?".

Dans ce contexte, Thinking Machines Lab pourrait se trouver dans la position enviable d'être arrivé avant les autres à une prise de conscience qui deviendra inévitable. Comme c'est souvent le cas en technologie, ce qui semble aujourd'hui une exigence de niche pourrait devenir demain la norme de l'industrie. Et celui qui aura investi le premier dans cette direction se retrouvera avec un avantage concurrentiel significatif.

L'aspect le plus fascinant de cette histoire est que la solution ne nécessite pas de révolutions technologiques ou de percées scientifiques. C'est un problème d'ingénierie pure, résolu avec une rigueur mathématique et une attention aux détails. À une époque où l'IA semble de plus en plus magique et incompréhensible, Thinking Machines Lab nous rappelle que derrière chaque algorithme intelligent, il y a toujours des mathématiques solides et des implémentations précises.

Peut-être que la vraie leçon de cette recherche ne concerne pas tant les LLM que la maturité de tout un secteur. Nous sommes arrivés au point où il ne suffit plus que l'intelligence artificielle fonctionne : elle doit fonctionner de manière prévisible, traçable et reproductible. C'est le passage de l'art à la science, de l'alchimie à la chimie.

Après tout, qui aurait cru que le véritable saut évolutif de l'IA ne viendrait pas de modèles plus grands ou d'algorithmes plus sophistiqués, mais de la simple capacité à faire toujours la même chose de la même manière ? Comme dans les meilleurs rebondissements de films, la réponse était cachée à la vue de tous. Il suffisait d'avoir le courage de la chercher.
