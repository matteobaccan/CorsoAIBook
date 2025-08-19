---
tags: ["Startups", "Research", "Training"]
date: 2025-08-10
---

# "Quand la Taille n'a pas d'Importance" : La Révolution du Modèle HRM
*par Dario Ferrero (VerbaniaNotizie.it)*
![hrm_le_dimensioni_non_contano.jpg](hrm_le_dimensioni_non_contano.jpg)


*La plus grande révolution de l'intelligence artificielle de ces dernières années ne vient pas des laboratoires d'OpenAI ou de Google, mais d'une petite startup de Singapour appelée [Sapient Intelligence](https://www.sapient.inc/).*

Le protagoniste de cette histoire s'appelle le [Hierarchical Reasoning Model](https://github.com/sapientinc/HRM) (HRM), un agent IA qui fait trembler les fondations de tout le secteur avec une promesse apparemment impossible : raisonner mieux que les géants de l'IA en utilisant une fraction de leurs ressources.

Il ne s'agit pas du modèle linguistique habituel agrandi à l'extrême, ni d'une énième variation sur le thème des transformeurs. HRM est construit différemment, inspiré directement du fonctionnement du cerveau humain, et les résultats qu'il obtient sont pour le moins stupéfiants. Ce modèle d'à peine 27 millions de paramètres, moins d'un quart de la taille du premier GPT, surpasse systématiquement des modèles quatre fois plus grands dans des tâches de raisonnement complexe. Comme si cela ne suffisait pas, il est entraîné avec seulement mille exemples par problème, alors que ses adversaires nécessitent des montagnes de données et des mois de traitement sur les serveurs les plus puissants du monde.

Mais la vraie magie de HRM ne réside pas dans sa taille réduite ou son efficacité d'entraînement. Son innovation réside dans le fait qu'il ne se contente pas de traiter des informations comme tous les autres : il raisonne vraiment, émulant les processus cognitifs humains d'une manière qui semblait relever de la science-fiction il y a encore quelques mois. Et les résultats parlent d'eux-mêmes : là où d'autres modèles échouent complètement, HRM excelle avec une aisance qui rappelle plus un cerveau pensant qu'une machine à calculer.

## Quand la Chaîne de Pensée se Brise

Pour comprendre l'importance de la révolution apportée par HRM, nous devons d'abord comprendre comment fonctionnent les modèles d'intelligence artificielle actuels et pourquoi leurs limites deviennent de plus en plus évidentes. ChatGPT, Claude, Gemini et tous leurs grands frères reposent sur une technique appelée "Chaîne de Pensée" (Chain of Thought), une approche qui semble prometteuse mais qui cache de profondes fragilités structurelles.

Imaginez devoir résoudre un problème de mathématiques complexe en écrivant chaque étape avec un stylo indélébile, sans jamais pouvoir revenir en arrière pour vérifier ou corriger ce que vous avez écrit. C'est exactement ainsi que fonctionnent les modèles actuels : ils se guident pas à pas à travers un problème, presque en "se parlant à eux-mêmes" à voix haute, mais s'ils commettent ne serait-ce qu'une petite erreur dans cette chaîne, toute la réponse peut s'effondrer comme un château de cartes.

Comme l'expliquent les chercheurs de Sapient Intelligence dans leur [article scientifique](https://arxiv.org/abs/2506.21734), "la chaîne de pensée pour le raisonnement est une béquille, pas une solution satisfaisante. Elle repose sur des décompositions fragiles définies par l'homme où une seule fausse étape ou un désordre des étapes peut complètement faire dérailler le processus de raisonnement".

Le problème est encore plus profond qu'il n'y paraît. Les modèles basés sur les transformeurs, l'architecture qui domine l'IA moderne, effectuent toujours la même quantité de "pensée" quelle que soit la difficulté de la question. C'est comme si un détective devait consacrer exactement le même temps et les mêmes ressources pour résoudre à la fois un vol de vélo et une affaire de meurtre complexe. Ils ne peuvent pas dire "C'est difficile, j'ai besoin de plus de temps pour réfléchir" et ils ne peuvent pas revoir leur raisonnement une fois qu'ils ont commencé à générer la réponse.

Cette rigidité a d'énormes conséquences pratiques. Les modèles actuels sont contraints de traduire chaque processus de raisonnement en langage explicite, produisant des réponses longues, lentes et souvent redondantes. Pire encore, cette dépendance au langage les rend vulnérables aux erreurs en cascade : s'ils se trompent sur une étape intermédiaire, tout ce qui suit est compromis, indépendamment de la justesse de leurs capacités de raisonnement de base.

## L'Architecture qui Imite le Cerveau

HRM abandonne complètement ce paradigme, adoptant une approche radicalement différente que ses créateurs décrivent comme "inspirée du cerveau". Il ne s'agit pas d'une métaphore superficielle ou marketing : l'architecture de HRM emprunte directement la stratégie de décision en couches du cerveau humain, l'appliquant à l'intelligence artificielle avec des résultats qui redéfinissent ce qui est possible dans le domaine de l'apprentissage automatique.

Au cœur de HRM se trouvent deux composants qui travaillent en tandem comme un duo parfaitement coordonné. Le premier est un planificateur de haut niveau, que l'on pourrait imaginer comme le "cerveau stratégique lent" qui observe la situation dans son ensemble, identifie le type de problème à résoudre et trace une carte générale de l'approche à suivre. Le second est un exécuteur de bas niveau, le "processeur rapide" qui prend les ordres du planificateur et les exécute avec précision et rapidité.

L'analogie la plus pertinente est celle d'un maître d'échecs qui collabore avec un assistant incroyablement efficace. Le maître étudie l'échiquier, planifie la stratégie générale et décide du coup à jouer, tandis que l'assistant exécute physiquement le coup avec une précision millimétrique. Mais ici, la similitude devient encore plus intéressante : les deux ne se limitent pas à un seul échange d'informations, mais maintiennent un dialogue continu tout au long du problème.

C'est le cœur de l'innovation de HRM : la [boucle de raisonnement hiérarchique](https://venturebeat.com/ai/new-ai-architecture-delivers-100x-faster-reasoning-than-llms-with-just-1000-training-examples/). Le module de haut niveau élabore un plan stratégique et le transmet au module de bas niveau, qui l'exécute et renvoie les résultats. À ce stade, le module de haut niveau analyse ce qui s'est passé, met à jour sa stratégie en fonction des nouvelles données et fournit au module de bas niveau un nouveau sous-problème affiné sur lequel travailler. Cet "échange" se poursuit en cycles itératifs jusqu'à ce que le modèle converge vers la solution optimale.

La beauté de cette approche est qu'elle permet à HRM de contrôler et d'affiner son propre raisonnement en interne pendant qu'il traite encore le problème, une capacité que la grande majorité des autres modèles ne possèdent tout simplement pas. C'est comme si, en résolvant ce problème de mathématiques avec un stylo indélébile, quelqu'un vous permettait soudainement d'effacer, de réécrire et de repenser chaque étape jusqu'à ce que vous soyez complètement sûr de la solution.

Mais ce n'est pas tout. La version la plus avancée de HRM utilise l'apprentissage par renforcement pour décider de manière autonome du nombre d'itérations nécessaires pour chaque type de tâche, ce qui le rend encore plus semblable à la pensée flexible humaine. Tout comme nous consacrons plus de temps et d'énergie mentale aux problèmes complexes qu'aux problèmes simples, HRM apprend à moduler ses cycles de raisonnement en fonction de la difficulté intrinsèque du problème auquel il est confronté.
![ragionamento_gerarchico_hrm.jpg](ragionamento_gerarchico_hrm.jpg)
*[Image tirée de Sapient.inc HRM](https://sapient.inc/)*

## David Contre Goliath : Les Chiffres qui Bouleversent

Les résultats obtenus par HRM sur les benchmarks de raisonnement les plus difficiles sont le genre de chiffres qui font hausser les sourcils même aux experts les plus sceptiques du secteur. Nous parlons d'un modèle avec à peine 27 millions de paramètres qui non seulement rivalise avec des géants de milliards de paramètres, mais les surpasse systématiquement dans des tâches qui nécessitent un raisonnement profond et abstrait.

Sur le [benchmark ARC-AGI](https://venturebeat.com/ai/openais-o3-shows-remarkable-progress-on-arc-agi-sparking-debate-on-ai-reasoning/), considéré comme l'un des tests les plus fiables pour mesurer les capacités de raisonnement abstrait et de généralisation de l'intelligence artificielle, HRM a obtenu un score de 40,3 %, dépassant des modèles beaucoup plus grands comme o3-mini-high d'OpenAI (34,5 %) et Claude 3.7 Sonnet (21,2 %). Il ne s'agit pas de petites différences statistiquement insignifiantes : nous parlons d'écarts de performance substantiels qui, dans le monde de l'IA, équivalent à des sauts générationnels.

Mais c'est sur les tâches de raisonnement les plus extrêmes que HRM démontre vraiment sa supériorité architecturale. Dans les tests de Sudoku de niveau extrême et dans les labyrinthes complexes, les différences deviennent abyssales. HRM a résolu 55 % des Sudokus les plus difficiles, tandis que les modèles basés sur la chaîne de pensée ont obtenu un score de 0 %. Même résultat pour les labyrinthes en grille 30x30 : HRM a trouvé le chemin optimal dans 74,5 % des cas, tandis que ses concurrents sont restés bloqués à 0 %.

C'est la version IA de l'adage de Yoda : "La taille n'a pas d'importance. Regarde-moi. Me juges-tu par ma taille ?" Sauf qu'ici, la Force est l'architecture hiérarchique et Luke Skywalker, ce sont les modèles de milliards de paramètres qui continuent de s'écraser dans le marais.

Ce ne sont pas de simples chiffres sur un tableau : ils représentent la différence entre une intelligence artificielle capable de s'attaquer à des problèmes complexes du monde réel et une autre qui se bloque face à des défis nécessitant plus qu'un raisonnement superficiel. C'est la différence entre un assistant qui peut vous aider à naviguer dans des décisions complexes et un autre qui peut tout au plus vous aider à rédiger des e-mails plus éloquents.

Mais le chiffre peut-être le plus impressionnant de tous concerne l'efficacité de l'entraînement. Alors que les modèles linguistiques traditionnels nécessitent d'énormes ensembles de données extraits de tout Internet et des mois de traitement sur les superordinateurs les plus puissants du monde, HRM est entraîné avec seulement mille exemples par tâche. Comme l'a déclaré Guan Wang, l'un des fondateurs de Sapient Intelligence, "vous pourriez l'entraîner au Sudoku à un niveau professionnel en deux heures de GPU" – une efficacité qu'il qualifie littéralement de "ridicule" dans le bon sens du terme.
![benchmark_hrm.jpg](benchmark_hrm.jpg)
*[Image tirée de Sapient.inc HRM](https://sapient.inc/)*

## Au-delà des Benchmarks : Une Révolution Structurelle

Les résultats impressionnants sur les tests standardisés ne sont que la partie visible de l'iceberg. La véritable révolution apportée par HRM réside dans sa capacité à résoudre des problèmes structurels fondamentaux qui affectent toute la génération actuelle de modèles basés sur les transformeurs, des problèmes qui, jusqu'à récemment, semblaient faire partie intégrante du paysage de l'intelligence artificielle.

Le premier et le plus significatif de ces problèmes est l'efficacité de la mémoire. Les transformeurs traditionnels sont notoirement gourmands en ressources, nécessitant d'énormes quantités de mémoire pour fonctionner et encore plus pour être entraînés. HRM, en revanche, utilise des mises à jour de gradient plus locales, qui sont plus faciles à calculer et "beaucoup plus biologiquement plausibles", évitant la fameuse "rétropropagation profonde dans le temps" qui est intensive en termes de mémoire et lente en calcul.

Cette efficacité de la mémoire n'est pas une simple amélioration incrémentielle : c'est un changement de paradigme qui ouvre des scénarios entièrement nouveaux. Moins de mémoire signifie pouvoir exécuter plus de modèles simultanément sur le même matériel, entraîner plus rapidement avec moins de ressources, et surtout, amener l'intelligence artificielle avancée sur des appareils qui, jusqu'à hier, étaient impensables. Nous parlons d'ordinateurs portables courants, d'appareils en périphérie de réseau (edge), de robots, et même de voitures – tous des endroits où l'IA pourrait fonctionner de manière autonome sans dépendre de connexions Internet constantes ou de serveurs distants.

L'entreprise Sapient teste déjà HRM dans des applications du monde réel qui démontrent cette polyvalence. Dans le secteur de la santé, le modèle est utilisé pour aider au diagnostic de maladies rares, ces pathologies complexes qui nécessitent exactement le type de raisonnement profond et nuancé dans lequel HRM excelle. Dans les prévisions climatiques saisonnières, il a atteint des taux de précision de 97 %, un résultat qui, dans le monde de la météorologie, équivaut presque à de la science-fiction.

Mais l'aspect peut-être le plus encourageant de HRM est l'équipe qui se cache derrière. Il ne s'agit pas de chercheurs inconnus travaillant dans un garage : le groupe comprend d'anciens ingénieurs de DeepMind, Anthropic, DeepSeek et même du groupe XAI d'Elon Musk. Ce sont des personnes qui ont travaillé à la pointe de l'intelligence artificielle pendant des années et qui parient maintenant tout sur la conception inspirée du cerveau de HRM. Lorsque des professionnels de ce calibre quittent les certitudes des grands géants de la technologie pour poursuivre une vision alternative, cela vaut la peine d'y prêter attention.

Guan Wang, le PDG et fondateur de Sapient Intelligence, ne mâche pas ses mots lorsqu'il parle de l'avenir de l'intelligence artificielle. Sa vision est que l'AGI, l'intelligence artificielle générale, consiste à donner aux machines une intelligence de niveau humain et au-delà. Et selon Wang, la chaîne de pensée n'est qu'un "raccourci", alors que ce qu'ils ont construit "peut penser" au vrai sens du terme.

## Open Source et Transparence : Un Cadeau à la Communauté

À une époque où les grands laboratoires d'IA ont tendance à garder leurs modèles les plus avancés sous le sceau du secret commercial, la décision de Sapient Intelligence de rendre HRM entièrement open source représente un geste de transparence quasi révolutionnaire. L'ensemble du projet est [disponible sur GitHub](https://github.com/sapientinc/HRM), permettant à quiconque dans le monde de le vérifier, d'entraîner sa propre version, de le modifier ou de construire par-dessus. Ce niveau d'ouverture est rare pour une innovation aussi prometteuse et stratégiquement importante.

Bien sûr, HRM a encore des limites que ses créateurs reconnaissent ouvertement. Pour l'instant, le modèle a une portée plus restreinte que les grands modèles linguistiques généralistes : il est conçu pour raisonner, pas pour discuter amicalement ou écrire de la poésie romantique. Mais c'est précisément cette spécialisation qui le rend si puissant dans son domaine. C'est l'une des preuves de concept les plus solides que le secteur ait jamais vues pour démontrer que l'avenir de l'IA pourrait ne pas résider dans des modèles toujours plus grands et généralistes, mais dans des architectures plus intelligentes et spécialisées.

HRM n'est pas la seule expérience de ce type en cours. Le paysage de la recherche en IA connaît un moment d'effervescence créative, avec des équipes du monde entier explorant des architectures alternatives aux transformeurs dominants. Il y a Sakana avec leurs machines à pensée continue, les modèles LLM à un bit qui promettent une efficacité extrême, et les modèles de raisonnement basés sur la diffusion de Google. Mais il y a une différence cruciale : HRM "fonctionne déjà" et surpasse des modèles beaucoup plus grands avec une fraction des données d'entraînement et sans avoir besoin d'un pré-entraînement massif.

Cela suggère que nous assistons à un changement de paradigme fondamental. Le prochain grand bond en avant dans l'intelligence artificielle ne sera probablement pas un autre "clone de GPT mis à l'échelle" à des dimensions encore plus gigantesques, mais quelque chose de similaire à HRM : une nouvelle architecture qui apporte un meilleur raisonnement, un entraînement plus rapide et une mise en œuvre plus économique, le tout sans avoir besoin de centres de données remplis de GPU consommant l'électricité de villes entières.

## L'Avenir qui Pense Vraiment

En regardant vers l'avenir, la vision qui émerge du travail de HRM est celle d'un futur où l'intelligence artificielle ne sera plus confinée dans les centres de données des grandes entreprises technologiques, mais deviendra une présence omniprésente et accessible dans notre vie quotidienne. Imaginez des agents IA vivant dans nos ordinateurs portables, nos robots domestiques, nos voitures, et même nos appareils portables, tous capables d'un raisonnement sophistiqué sans dépendre de connexions Internet constantes ou de serveurs distants coûteux.

Cette démocratisation de l'intelligence artificielle avancée pourrait avoir des implications profondes sur notre façon de travailler, d'apprendre et de résoudre les problèmes. Un médecin dans une clinique rurale pourrait avoir accès aux mêmes outils de diagnostic avancé qu'un hôpital métropolitain. Un ingénieur travaillant sur un chantier de construction isolé pourrait obtenir des analyses structurelles complexes en temps réel. Un chercheur dans un laboratoire au budget limité pourrait explorer des hypothèses scientifiques complexes sans avoir à se battre pour l'accès aux superordinateurs.

Mais l'aspect peut-être le plus fascinant de tous est l'idée que ces agents IA ne se contenteront plus de "parler" avec Internet ou de régurgiter des informations traitées ailleurs. Ils commenceront à "penser réellement", au sens le plus profond du terme, en élaborant des solutions originales, en formulant des hypothèses créatives, et peut-être même en développant des intuitions que nous, les humains, n'aurions jamais envisagées.

Comme toute révolution technologique, cette transformation apportera son lot de nouveaux défis et de questions éthiques que nous devrons affronter. Mais si HRM et les architectures similaires tiennent leurs promesses, nous pourrions être à l'aube d'une ère où l'intelligence artificielle devient enfin ce que son nom promet : non seulement un système sophistiqué de traitement de l'information, mais un véritable partenaire intellectuel capable de raisonnement autonome et créatif.

Comme le dirait Tony Stark, parfois la meilleure solution n'est pas de construire une armure plus grande, mais de la construire plus intelligemment. Et HRM pourrait avoir trouvé le moyen de remplacer la force brute computationnelle par quelque chose de beaucoup plus élégant et efficace.

La route est encore longue et semée d'inconnues, mais une chose est sûre : le petit modèle de 27 millions de paramètres créé par une start-up singapourienne a déjà démontré que dans le monde de l'intelligence artificielle, comme c'est souvent le cas en science, la qualité peut véritablement surpasser la quantité. Et peut-être, comme dans les meilleures histoires de David contre Goliath, c'est le plus petit qui nous montre la voie de l'avenir.
