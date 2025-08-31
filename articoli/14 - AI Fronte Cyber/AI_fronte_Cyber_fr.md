---
tags: ["Security", "Ethics & Society", "Business"]
date: 2025-08-16
author: "Dario Ferrero"
---

# L'IA assiégée : chroniques du front cybernétique
![fronte_AI.jpg](fronte_AI.jpg)

*Avril 2023 : des ingénieurs de Samsung partagent sans le savoir du code source propriétaire avec ChatGPT. Mai 2025 : des chercheurs découvrent que des articles universitaires contiennent des invites cachées pour manipuler les systèmes d'évaluation par les pairs alimentés par l'IA. Entre ces deux événements, se déroule une chronique alarmante qui raconte comment l'intelligence artificielle est devenue à la fois le prédateur et la proie du nouvel écosystème cybernétique.*

## Le prix de l'innocence numérique

L'histoire commence par ce que l'on pourrait appeler l'innocence perdue de l'ère de l'IA. [En 2023, Samsung a dû interdire l'utilisation de ChatGPT et d'autres outils d'IA générative](https://www.bloomberg.com/news/articles/2023-05-02/samsung-bans-chatgpt-and-other-generative-ai-use-by-staff-after-leak) sur ses appareils d'entreprise après que [trois ingénieurs, lors d'incidents distincts, aient partagé sans le savoir des données sensibles de l'entreprise](https://techcrunch.com/2023/05/02/samsung-bans-use-of-generative-ai-tools-like-chatgpt-after-april-internal-data-leak/) avec le chatbot d'OpenAI. Il ne s'agissait pas d'une attaque sophistiquée ou d'espionnage industriel : c'était simplement le résultat d'employés qui, pour tenter d'optimiser leur travail, avaient utilisé l'IA comme un assistant personnel, sans se rendre compte qu'ils alimentaient un système qui apprend de chaque conversation.

Les données divulguées comprenaient du code source de semi-conducteurs, des procès-verbaux de réunions internes et des détails sur du matériel propriétaire. Samsung n'avait pas été piraté au sens traditionnel du terme : il s'était piraté lui-même, victime de ce que les experts appellent le "shadow AI", l'utilisation non autorisée d'outils d'intelligence artificielle par les employés.

Cet incident a été le premier signal d'alarme pour le secteur des entreprises, révélant une vérité qui dérange : les entreprises se précipitaient pour adopter l'IA sans en comprendre pleinement les implications en matière de sécurité. Telle une boîte de Pandore numérique moderne, une fois le monde de l'IA ouvert, le contrôle de son contenu s'est avéré infiniment plus complexe que prévu.

## Le paradoxe de la croissance exponentielle

Les chiffres racontent une histoire inquiétante : en 2024, le coût moyen d'un incident de cybersécurité pour les petites et moyennes entreprises a atteint 1,6 million de dollars, contre 1,4 million en 2023, et près de 40 % des petites entreprises ont perdu des données cruciales et subi des temps d'arrêt importants. Dans le même temps, les attaques alimentées par l'IA se multiplient à mesure que la sécurité du cloud évolue, ce qui incite les entreprises à mettre en œuvre des défenses en temps réel basées sur l'IA pour suivre le rythme.

Le paradoxe est clair : alors que les entreprises mettent en œuvre l'IA pour mieux se défendre, les attaquants utilisent les mêmes technologies pour lancer des offensives plus sophistiquées. C'est comme assister à une version numérique de la guerre froide, où chaque innovation défensive est immédiatement contrebalancée par une contre-mesure offensive.

Les leaders du secteur anticipent un paysage des menaces de plus en plus complexe en 2025, mais le principal défi ne réside pas tant dans la sophistication technique des attaques que dans leur démocratisation. L'IA a rendu accessibles à tous des techniques d'attaque qui nécessitaient autrefois des années de spécialisation.

## Les nouvelles frontières de l'attaque : quand l'IA se trahit elle-même

De 2023 à 2024, de nombreuses fuites de données et incidents de confidentialité liés à ChatGPT ont eu lieu, mettant en évidence les défis de sécurité critiques auxquels sont confrontées les technologies d'IA. Mais ces épisodes ne sont que la partie émergée de l'iceberg d'un phénomène beaucoup plus complexe : l'émergence de vecteurs d'attaque entièrement nouveaux qui exploitent la nature même de l'intelligence artificielle.

La manipulation des systèmes universitaires d'évaluation par les pairs en est un excellent exemple. Des chercheurs ont découvert que certains articles contenaient des invites cachées spécialement conçues pour influencer les systèmes d'IA utilisés dans l'évaluation scientifique. C'est comme si quelqu'un avait inventé un moyen de chuchoter des instructions invisibles aux arbitres d'un match, en altérant le résultat sans que personne ne s'en aperçoive.

Cette technique, connue sous le nom d'"injection de prompt", est l'une des vulnérabilités les plus insidieuses de l'ère de l'IA. Contrairement aux cyberattaques traditionnelles qui exploitent des failles dans le code, l'injection de prompt exploite la caractéristique fondamentale des modèles de langage : leur capacité à comprendre et à suivre des instructions en langage naturel. C'est l'équivalent numérique du ventriloque qui fait dire à la marionnette ce qu'il veut, mais dans ce cas, la marionnette contrôle des systèmes d'entreprise critiques.
![prompt_injection.jpg](prompt_injection.jpg)
[*Image tirée de arthur.ai*](https://www.arthur.ai/blog/from-jailbreaks-to-gibberish-understanding-the-different-types-of-prompt-injections)

## L'écosystème des vulnérabilités : le cas du MCP

Le Model Context Protocol (MCP), développé pour simplifier l'interaction entre les grands modèles de langage et les outils externes, est une étude de cas parfaite de la manière dont les bonnes intentions peuvent ouvrir de nouvelles surfaces d'attaque. Une collection de huit incidents réels liés à l'IA au cours des 24 derniers mois met en évidence les risques liés à l'utilisation et à la mise en œuvre de l'IA sans mesures de sécurité adéquates.

Le MCP était censé être la solution ultime pour connecter l'IA au monde réel, en permettant aux modèles d'interagir de manière transparente avec les bases de données, les API et les services externes. En réalité, il s'est avéré être un pont que les attaquants peuvent franchir dans les deux sens. [Un dépôt communautaire](https://github.com/Puliczek/awesome-mcp-security) documente plus de cinquante articles universitaires publiés au cours des seuls premiers mois de 2025, révélant des vulnérabilités allant de [l'exfiltration de données des serveurs Slack](https://embracethered.com/blog/posts/2025/security-advisory-anthropic-slack-mcp-server-data-leakage/) à [l'accès non autorisé à des dépôts GitHub privés](https://invariantlabs.ai/blog/mcp-github-vulnerability).

Le problème fondamental du MCP est d'ordre architectural : il a été conçu en partant du principe que tous les composants de l'écosystème sont fiables. C'est l'équivalent de construire une ville sans murs parce que l'on suppose que tous les visiteurs sont des amis. Lorsque cette hypothèse s'avère fausse, l'ensemble du système s'effondre comme un château de cartes.
![MCP_method.jpg](MCP_method.jpg)
[*Image tirée de descope.com*](https://www.descope.com/learn/post/mcp)

## La démocratisation du piratage : quand tout le monde peut être anonyme

Les prévisions pour 2025 se concentrent sur les risques de sécurité opérationnelle et les défis évolutifs posés par l'IA, mais l'aspect le plus inquiétant est peut-être la démocratisation des capacités offensives. L'IA a considérablement abaissé la barrière à l'entrée pour mener des cyberattaques sophistiquées.

Prenons le cas de l'injection de prompt : un attaquant n'a plus besoin de connaître les langages de programmation ou de comprendre des architectures complexes. Il suffit de formuler habilement une requête en langage naturel pour compromettre potentiellement un système. C'est comme si, soudain, n'importe qui pouvait devenir Houdini en demandant simplement aux chaînes de se défaire.

Pour comprendre cette dynamique, nous pouvons examiner plusieurs plateformes qui simulent des attaques par injection de prompt. Il existe des outils comme le ChatGPT Jailbreak Challenge ou le AI Security Sandbox, qui apprennent à identifier les vulnérabilités de l'IA. Dans les premiers niveaux, contourner les restrictions de l'IA peut être aussi simple que d'utiliser des phrases comme "Ignorer les directives précédentes" ou "Faire une exception".

Cependant, au fur et à mesure que vous progressez, les systèmes mettent en œuvre des filtres plus complexes, tels que la détection de mots-clés ou des réponses prédéfinies. Néanmoins, avec une approche méthodique et un peu d'ingéniosité, même ces barrières peuvent être surmontées, ce qui démontre à quel point une conception robuste des modèles de langage est cruciale.

## Les attaques du futur : l'emoji comme cheval de Troie

Les techniques d'attaque les plus innovantes exploitent des aspects apparemment inoffensifs de la communication numérique. Le "détournement d'emoji" est un exemple parfait de cette tendance : [des chercheurs de Mindgard et de l'université de Lancaster ont montré](https://securitybrief.asia/story/emojis-used-to-hide-attacks-bypass-major-ai-guardrails) comment les attaquants peuvent cacher des instructions malveillantes en utilisant des emojis pour [contourner les filtres d'IA de Microsoft, Nvidia et Meta](https://cybersecuritynews.com/hackers-can-bypass-microsoft-nvidia-meta-ai-filters/).

La recherche a testé six des systèmes de garde-fous les plus utilisés, révélant que beaucoup s'appuient fortement sur la reconnaissance de formes statiques et montrent une résilience insuffisante contre les attaques adverses.

C'est comme cacher un message secret dans le sourire de la Joconde : apparemment inoffensif, mais potentiellement dévastateur pour ceux qui savent le déchiffrer. Cette technique est particulièrement insidieuse car elle exploite la tendance naturelle des humains à considérer les emojis comme des éléments décoratifs inoffensifs, alors qu'en réalité ils peuvent devenir de véritables vecteurs d'attaque.

Une autre technique émergente documentée par les chercheurs est [le détournement de données par le biais de techniques d'encodage avancées](https://embracethered.com/blog/posts/2025/sneaky-bits-and-ascii-smuggler/), qui peut transformer l'IA en un espion involontaire. Les attaquants peuvent demander au système d'intégrer des données sensibles dans des chaînes ou des URL apparemment inoffensives. Même si l'IA ne parvient pas à exécuter la demande, les journaux du serveur enregistrent comunque la tentative, ce qui permet à l'attaquant de récupérer les informations par des canaux détournés. C'est l'équivalent numérique de la livraison d'un message secret par un pigeon voyageur qui ne sait pas qu'il transporte des informations classifiées.

[Jason Haddix](https://mlsecops.com/podcast/holistic-ai-pentesting-playbook), un vétéran de la sécurité offensive et PDG d'Arcanum Information Security, est reconnu comme l'un des plus grands experts en matière de piratage de systèmes d'IA. Il a développé une méthodologie propriétaire et holistique pour les tests de pénétration de l'IA, qui examine l'ensemble de l'écosystème des applications d'IA et pas seulement les modèles. Haddix a également créé une taxonomie open-source pour les techniques d'injection de prompt, classant des tactiques innovantes telles que le "détournement d'emoji" et le "détournement de données" par le biais d'un encodage avancé. Son travail se concentre sur l'identification et la défense contre les vulnérabilités du monde réel telles que les clés API sur-autorisées et les données sensibles non protégées dans les systèmes RAG, et promeut une approche de défense en profondeur pour les applications d'IA.

## La réponse de l'industrie : entre innovation et réaction

Samsung a récemment autorisé ses employés à utiliser à nouveau ChatGPT, mais avec de nouveaux protocoles de sécurité, ce qui montre comment l'industrie tente de trouver un équilibre entre innovation et sécurité. Cette décision représente un microcosme du défi plus large auquel sont confrontées les organisations : comment exploiter les avantages de l'IA tout en minimisant les risques.

La stratégie émergente dans le secteur des entreprises est basée sur une approche multicouche qui rappelle la défense en profondeur des châteaux médiévaux. Pas un seul mur infranchissable, mais une série d'obstacles concentriques qui rendent la progression des attaquants de plus en plus difficile.

Au niveau le plus élémentaire, le principe du moindre privilège est appliqué : chaque système d'IA n'a accès qu'aux ressources strictement nécessaires à l'accomplissement de ses tâches. C'est comme donner à un serveur les clés de la salle à manger uniquement, et non de tout l'hôtel.

Le deuxième niveau met en œuvre des filtres et des classificateurs pour les entrées et les sorties, créant ce que l'on pourrait appeler un "pare-feu conversationnel". Ces systèmes analysent chaque interaction pour identifier les tentatives potentielles de manipulation ou d'exfiltration de données.

Le troisième niveau se concentre sur la validation rigoureuse de toutes les entrées et sorties, en veillant à ce que le système ne puisse pas être utilisé pour introduire des logiciels malveillants ou extraire des informations non autorisées.

## L'IA en tant que défenseur : quand le remède est aussi le traitement

Les entreprises mettent en œuvre des défenses en temps réel basées sur l'IA pour contrer les attaques alimentées par l'IA, créant un cycle d'innovation continu entre l'offensif et le défensif. Cette dynamique a donné naissance à ce que les experts appellent la "guerre de l'IA contre l'IA", une bataille dans laquelle des algorithmes s'affrontent à d'autres algorithmes dans une danse sans fin d'action et de réaction.

Les systèmes de défense basés sur l'IA montrent des capacités impressionnantes à identifier les schémas d'attaque et à répondre en temps réel aux menaces émergentes. Ils sont particulièrement efficaces contre les attaques normalisées et les vulnérabilités connues, où ils peuvent traiter de grands volumes de données et identifier des anomalies à des vitesses impossibles pour les analystes humains.

Cependant, l'IA défensive présente encore des limites importantes face à la créativité et à l'intuition des attaquants humains les plus sophistiqués. Les spécialistes de la cybersécurité possèdent ce que l'on pourrait appeler le "facteur X", une combinaison d'expérience, d'intuition et de capacité de réflexion latérale qui ne peut être facilement reproduite par des algorithmes.

## Les conséquences pour l'entreprise : le nouveau calcul du risque

Les organisations doivent désormais tenir compte de nouveaux types de risques liés à l'IA, allant de la manipulation de modèles à l'exfiltration de données par des canaux non conventionnels. Le calcul du risque pour l'entreprise s'est énormément compliqué : il ne s'agit plus seulement de protéger les systèmes de l'extérieur, mais aussi de contrôler la manière dont ses propres outils internes peuvent être utilisés à mauvais escient.

L'affaire Samsung n'est que la partie émergée de l'iceberg. De nombreuses organisations découvrent que leurs employés utilisent quotidiennement des outils d'IA pour optimiser leur travail, souvent sans se rendre compte des implications en matière de sécurité. Le concept de "shadow AI" a émergé : l'utilisation non déclarée d'outils d'intelligence artificielle qui crée d'importants angles morts dans la posture de sécurité de l'entreprise.

Les conséquences économiques sont tangibles et croissantes. Les prévisions pour 2025 indiquent que l'IA renforcera considérablement les cyberattaques, tandis que le coût moyen des incidents continue d'augmenter. Les entreprises se trouvent dans une position paradoxale : elles doivent investir dans l'IA pour rester compétitives, mais chaque mise en œuvre introduit de nouvelles surfaces d'attaque.

## Vers un avenir de coexistence armée

Le défi fondamental de 2025 n'est pas d'éliminer les risques de l'IA - un objectif impossible - mais d'apprendre à les gérer efficacement. Nous entrons dans une ère de "coexistence armée" entre l'innovation et la sécurité, où l'objectif n'est pas une protection parfaite mais une résilience dynamique.

Les rapports sur la sécurité de l'IA révèlent que les organisations apprennent à identifier et à atténuer les risques liés à l'IA grâce à des stratégies de défense de plus en plus sophistiquées. La clé du succès semble résider non pas dans la prévention absolue des incidents, mais dans la capacité à détecter rapidement les anomalies, à répondre efficacement aux attaques et à se remettre rapidement des compromissions.

Le paysage qui se dessine rappelle les débuts d'Internet : un environnement riche en opportunités mais aussi en embûches, où la différence entre le succès et l'échec se mesure à la capacité de trouver un équilibre entre innovation et prudence. Les organisations qui prospèrent dans ce nouvel environnement sont celles qui parviennent à mettre en œuvre l'IA tout en conservant une mentalité de "sécurité dès la conception", en considérant la protection non pas comme une contrainte mais comme un catalyseur d'innovation durable.

## Épilogue : leçons d'un avenir déjà présent

L'histoire de l'ingénieur de Samsung qui a partagé sans le savoir du code propriétaire avec ChatGPT est devenue un cas d'école classique dans les cours de cybersécurité. Non pas parce qu'elle représente une attaque particulièrement sophistiquée, mais parce qu'elle incarne parfaitement la nature des défis qui nous attendent : des menaces qui naissent de l'intersection de bonnes intentions, de nouvelles technologies et d'une compréhension insuffisante des implications.

L'intelligence artificielle n'est ni intrinsèquement bonne ni mauvaise : c'est un outil puissant qui amplifie à la fois nos capacités et nos vulnérabilités. Le défi de 2025 et au-delà sera de développer la sagesse collective nécessaire pour guider cette puissance vers des objectifs constructifs, tout en restant vigilant quant aux risques qu'elle comporte.

Comme à chaque époque de transition technologique, de l'imprimerie à Internet, le succès appartiendra à ceux qui sauront s'adapter rapidement tout en préservant les principes fondamentaux de prudence et de responsabilité. Dans la Terre du Milieu de l'IA, ce n'est pas l'elfe le plus agile ni le magicien le plus puissant qui gagne, mais le hobbit qui apprend à naviguer dans l'imprévisible - un anneau (de données) à la fois.
