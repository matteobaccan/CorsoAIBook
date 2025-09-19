---
tags: ["Research", "Generative AI", "Training"]
date: 2025-09-12
author: Dario Ferrero
---

# La "passion" de l'IA qui la trahit : l'épanorthose emphatique
![ai-Shakespear.jpg](ai-Shakespear.jpg)

*"Peut-on reconnaître un texte rédigé par une IA ?". C'est la question que l'on me pose le plus souvent lors de mes cours sur l'intelligence artificielle générative, murmurée avec l'air complice de celui qui cherche le Saint Graal de notre époque numérique. Ma réponse, désormais aussi automatique qu'un réflexe conditionné, pointe toujours dans une direction : "Regardez s'il y a une abondance de listes à puces", dis-je, "s'il transforme chaque concept en une liste ordonnée". Mais ce que j'ai toujours considéré comme le détail le plus évident de l'IA pourrait n'être que la partie émergée de l'iceberg stylistique.*

Une [nouvelle étude](https://zenodo.org/records/16947334) de Filippo Lubrano de H-Farm a en effet identifié un schéma beaucoup plus subtil et omniprésent : l'épanorthose emphatique, une figure de rhétorique ancienne que les modèles de langage ont transformée en leur signature stylistique involontaire. C'est comme si Data de Star Trek avait soudainement développé un tic linguistique qui le trahit chaque fois qu'il essaie de se faire passer pour un humain.

L'article, publié en août 2025, révèle des données qui feraient frémir n'importe quel concepteur-rédacteur : les grands modèles de langage produisent cette construction rhétorique spécifique à une fréquence 27 fois supérieure à celle des humains. Il ne s'agit pas d'une erreur occasionnelle, mais d'une véritable épidémie stylistique qui touche tous les principaux modèles, de ChatGPT à Claude, en passant par les systèmes open-source.

## Qu'est-ce que l'épanorthose emphatique

Avant de nous plonger dans les chiffres, nous devons comprendre ce qu'est exactement cette figure de rhétorique aux contours apparemment exotiques. L'épanorthose est une figure de style qui indique une substitution de mots emphatique, où "Des milliers, non, des millions !" en est un exemple classique. Mais la variante qui obsède les IA modernes est plus spécifique : elle suit le schéma "Non pas X, mais Y", où une première affirmation est immédiatement corrigée par une formulation plus intense ou révélatrice.

Pour comprendre la puissance de ce mécanisme, pensons aux exemples littéraires qui ont rendu cette technique célèbre. Dans "Jules César" de Shakespeare, Marc Antoine utilise l'épanorthose lorsqu'il dit "Brutus est un homme d'honneur. Ils le sont tous, tous des hommes d'honneur", créant un effet ironique dévastateur par la répétition corrective. Dans les titres de journaux, la technique abonde : "Ce n'est pas seulement le mauvais temps, mais le changement climatique qui frappe à la porte". Les commentateurs sportifs en abusent constamment : "Ce n'est pas seulement un but, mais le but qui change le destin du championnat".

Dans la version IA, cependant, cette élégante figure de rhétorique se transforme en quelque chose de mécanique et d'obsessionnel. Là où un auteur humain écrirait "La technologie est avancée", un LLM produira automatiquement : "Il ne s'agit pas seulement de technologie avancée, mais d'une révolution qui transforme notre façon de vivre". Là où un journaliste dirait "Le marché est en croissance", l'IA élaborera : "Ce n'est pas simplement de la croissance, mais une expansion sans précédent qui redéfinit les équilibres économiques mondiaux".

Les exemples quotidiens abondent. Imaginez que vous demandiez à ChatGPT une recette de pâtes à la tomate. Au lieu de vous dire "Faites chauffer l'huile dans une poêle", vous obtiendrez : "Il ne s'agit pas seulement de faire chauffer l'huile, mais de créer la base aromatique qui élèvera votre sauce d'un simple condiment à une expérience culinaire". C'est comme avoir un chef qui ne peut jamais donner une instruction sans la transformer en une révélation épiphanique.

## Les chiffres parlent d'eux-mêmes
La recherche de Lubrano a analysé trois corpus distincts pour quantifier le phénomène. Le premier était composé de 400 000 phrases échantillonnées au hasard à partir du Common Crawl utilisé pour entraîner une importante famille de modèles en 2024. Le deuxième contenait 50 000 réponses de ChatGPT et Claude recueillies entre janvier et mai 2025. Le troisième était un corpus de contrôle de 100 000 phrases tirées de revues universitaires en sciences humaines (2015-2020) et d'articles de presse grand public (2023-2024).

Les résultats sont frappants : les modèles d'IA produisent 27 épanorthoses emphatiques pour 1000 phrases, contre 9 dans le corpus d'entraînement et à peine 5 dans le benchmark humain. Mais ce n'est pas tout : l'analyse a également révélé un phénomène de "rafale" (burstiness), c'est-à-dire que ces constructions se regroupent à certains endroits du texte, tout comme lorsque quelqu'un découvre les émojis et commence à en mettre trois ou quatre d'affilée dans le même message. Les réponses de plus de 300 jetons présentaient au moins une paire épanorthotique pour chaque changement de sujet, ce qui suggère que le dispositif fonctionne comme une signalisation interne dans la planification générative.

Pour contextualiser ces données, l'étude a comparé les résultats avec des corpus humains plus vastes : les articles de Wikipédia, les livres numérisés et le journalisme grand public présentaient tous des taux significativement plus bas, généralement entre 4 et 6 occurrences pour 1000 phrases. L'écart stylistique entre le texte généré par la machine et la prose humaine conventionnelle est si évident qu'il en est presque embarrassant.

Une régression logistique contrôlant la longueur des phrases, la présence de pronoms à la première personne et les interrogatives a maintenu l'épanorthose comme un prédicteur significatif de l'origine du modèle. Lors d'évaluations à l'aveugle avec des étudiants diplômés en linguistique, les textes riches en épanorthoses étaient jugés susceptibles d'être générés par une machine, ce qui souligne la pertinence du signal stylistique.

L'aspect le plus inquiétant est que le phénomène ne se limite pas à l'anglais. Des échantillonnages préliminaires en espagnol, français, mandarin et arabe montrent des amplifications similaires, ce qui suggère que l'effet traverse les familles linguistiques et les architectures de modèles de différentes échelles et origines. Comme un virus stylistique qui se réplique à travers les langues et les cultures.

## Pourquoi le RLHF a créé ce monstre

La racine du problème se trouve dans l'apprentissage par renforcement à partir de la rétroaction humaine (RLHF), le processus qui est censé rendre les modèles plus utiles et alignés sur les préférences humaines. Ironiquement, c'est précisément cette tentative d'humaniser l'IA qui a créé le monstre stylistique que nous analysons.

Le mécanisme est d'une élégance perverse. Pendant la phase de mise au point, les modèles sont entraînés à maximiser les évaluations sur l'utilité, la clarté et la politesse. Les annotateurs humains, inconsciemment, récompensent souvent les sorties qui introduisent une reformulation clarifiante, l'interprétant comme une preuve de compréhension. Le signal de récompense, moyenné sur des millions de jetons, élève le schéma au rang d'action de grande valeur.

Mais il y a un deuxième niveau d'amplification. Le trope est également corrélé avec des réponses très bien notées dans les données de pré-entraînement, en particulier les blogs marketing et le contenu de développement personnel connus pour leur urgence persuasive. Une fois enracinée, l'habitude persiste dans tous les domaines, même lorsqu'elle devient inadaptée. C'est ce que Lubrano appelle "l'effet sloganique" : la clarté s'achète au prix de la nuance.

Les corpus web, en particulier ceux collectés à partir du marketing, du développement personnel et des commentaires politiques, contiennent des taux supérieurs à la moyenne de structures de négation-substitution. Ces domaines privilégient la clarté, la mémorisation et la persuasion - des qualités facilement récompensées lors de la mise au point par RLHF. Une fois qu'un modèle de récompense attribue une grande valeur à une reformulation qui semble à la fois clarifiante et emphatique, le schéma se propage à des sujets non liés.

Le phénomène est parallèle à des tendances plus larges de la rhétorique numérique, où les médias de format court et optimisés pour l'attention réduisent les arguments complexes à des tournures binaires. L'utilisation répétée de "Non pas X, mais Y" fournit une forme compressée de tension narrative et de résolution, que les algorithmes ont tendance à récompenser pour son potentiel d'engagement.
![frequenza-epanortosi.jpg](frequenza-epanortosi.jpg)
[Fréquence relative de "Non pas X, mais Y" dans les modèles. Tiré de l'article de Filippo Lubrano](https://zenodo.org/records/16947334)

## La boucle culturelle qui s'auto-alimente

Ce qui rend le phénomène encore plus préoccupant, c'est sa nature auto-renforçante. Les modèles absorbent des schémas du web, les amplifient, et les utilisateurs les rencontrent à nouveau dans les textes générés, les intégrant inconsciemment dans leur propre écriture. C'est un serpent stylistique qui se mord la queue et qui risque d'homogénéiser le langage public.

Le discours en ligne récompense les dualismes simplifiés, en partie parce que les algorithmes de classement des médias sociaux élèvent le contenu polarisant. Les slogans d'entreprise et les citations de motivation recueillis par les moteurs de recherche prolifèrent les inversions négatif-positif. Les modèles collectent ce matériel, codant le dispositif comme une marque d'efficacité persuasive.

Les critiques journalistiques dans des publications comme The Guardian et The Atlantic, ainsi que les discussions en cours sur Wikipédia et Reddit, ont popularisé la notion de "AI slop" pour décrire cette tendance. Les rapports dans AI Flash Report et les commentaires sur des plateformes comme Twitter/X le présentent en outre comme un problème culturel, et non simplement technique, soulignant comment les raccourcis stylistiques prolifèrent à travers les boucles de rétroaction de l'écriture numérique.

## Vers des algorithmes détectives

Cette découverte ouvre des scénarios fascinants pour le développement de nouveaux systèmes de détection de l'IA. La fréquence de l'épanorthose pourrait servir de caractéristique faible mais utile pour les détecteurs de texte d'IA, en particulier lorsqu'elle est combinée à la "rafale" lexicale et aux marqueurs de discours en milieu de phrase.

Les [détecteurs d'IA actuellement disponibles](https://gptzero.me/) comme GPTZero, qui a récemment publié le modèle 3.7b avec des améliorations drastiques sur les derniers modèles de langage des principaux fournisseurs, pourraient intégrer cette nouvelle métrique dans leurs algorithmes d'analyse. L'équipe d'apprentissage automatique de GPTZero a passé l'été à construire son meilleur détecteur d'IA à ce jour, cette version arrivant juste à temps pour la nouvelle année scolaire 2025/2026.

L'approche multi-facteurs qui caractérise des outils comme [ZeroGPT](https://zerogpt.org/) pourrait bénéficier énormément de l'inclusion de l'analyse épanorthotique. Le détecteur d'IA ZeroGPT utilise une approche multi-facteurs pour identifier l'origine du contenu, en déterminant s'il a été généré par l'IA ou écrit par un être humain.

Mais il y a un avertissement important. La pénalisation agressive de la figure de rhétorique pourrait discriminer les communautés où le dispositif est culturellement intégré. Les outils de gouvernance conçus pour diversifier le style du modèle doivent être sensibles à la variation rhétorique tout en préservant la correction emphatique légitime.

Imaginons un algorithme détective qui fonctionne comme Sherlock Holmes à l'ère numérique : il ne se contente pas de chercher des empreintes digitales évidentes comme les listes à puces, mais il analyse des schémas linguistiques subtils, des fréquences de constructions rhétoriques, la distribution de marqueurs de discours. Un système qui pourrait attribuer des probabilités en pourcentage : "Ce texte a 87 % de chances d'avoir été généré par une IA, sur la base de la présence de 12 épanorthoses emphatiques, de schémas lexicaux répétitifs et de l'absence de variation syntaxique humaine."

## Stratégies d'atténuation

Pour les conservateurs de modèles et les développeurs, Lubrano suggère plusieurs stratégies d'atténuation. Les conservateurs peuvent surpondérer les corpus qui utilisent des techniques d'emphase alternatives, comme la juxtaposition sans négation ou le déplacement métaphorique. Les ingénieurs de prompt peuvent demander aux modèles de varier explicitement le tissu conjonctif, en demandant des clauses concessives ou une expansion descriptive.

Les modèles de récompense pourraient pénaliser les épanorthoses répétées dans une fenêtre de jetons, encourageant l'exploration syntaxique. C'est comme entraîner un musicien à ne pas abuser de la même progression d'accords : la technique n'est pas mauvaise en soi, mais sa répétition obsessionnelle appauvrit le résultat final.

Une analogie cinématographique pourrait être celle de Quentin Tarantino : ses techniques narratives distinctives (flashbacks, longs dialogues, violence stylisée) fonctionnent parfaitement dans ses films, mais si tous les réalisateurs commençaient à les copier mécaniquement, le cinéma deviendrait d'un ennui prévisible. L'épanorthose emphatique est le jump cut de l'IA : efficace lorsqu'elle est utilisée avec parcimonie, dévastatrice lorsqu'elle devient la seule flèche à son arc.

## Implications pour l'avenir de l'écriture

Le phénomène de l'épanorthose emphatique soulève des questions plus profondes sur la nature de la créativité et de l'expression à l'ère de l'IA. Si les modèles de langage poussent inconsciemment à une homogénéisation stylistique, qu'est-ce que cela signifie pour la diversité expressive humaine ?

Il y a une ironie presque à la Jorge Luis Borges dans le fait que des machines conçues pour imiter la créativité humaine créent au contraire leur propre sous-culture rhétorique, un dialecte artificiel qui commence à influencer la façon dont les humains eux-mêmes communiquent. C'est comme si nous avions créé des extraterrestres linguistiques qui, en essayant de paraître humains, ont développé leurs propres idiosyncrasies qui les trahissent.

Le défi pour les années à venir sera double : d'une part, développer des systèmes de détection de plus en plus sophistiqués capables d'identifier ces schémas subtils ; d'autre part, travailler à la diversification stylistique des modèles eux-mêmes, en évitant que la recherche de la "clarté" et de l'"utilité" ne conduise à une standardisation appauvrissante du langage.

## Le détective du futur

Pour en revenir à la question initiale de mes étudiants - "Peut-on reconnaître un texte rédigé par une IA ?" - la réponse évolue rapidement. Plus seulement des listes à puces et des structures répétitives évidentes, mais une constellation de micro-signaux stylistiques qui incluent des fréquences anormales de constructions rhétoriques spécifiques, des schémas d'emphase, la distribution de marqueurs de discours.

L'avenir nous réserve probablement une sorte de CSI linguistique, où des enquêteurs numériques armés d'algorithmes de plus en plus sophistiqués analyseront des textes à la recherche d'empreintes stylistiques invisibles à l'œil nu. L'épanorthose emphatique pourrait n'être que le premier de nombreux "ADN linguistiques" qui trahissent l'origine artificielle d'un texte.

Mais la leçon la plus importante de cette étude est peut-être que l'IA, en essayant de paraître plus humaine, révèle au contraire à quel point elle est profondément non humaine dans ses schémas d'apprentissage et de reproduction. Comme un acteur qui, en essayant de jouer le rôle d'un humain, finit par mettre l'accent sur les aspects mêmes qui le rendent reconnaissable en tant qu'acteur.

La recherche de Lubrano n'est pas seulement une contribution technique au domaine de la détection de l'IA, mais un memento qui nous rappelle de prêter attention non seulement à ce que les machines disent, mais à la manière dont elles le disent.

Pour paraphraser McLuhan, qui soutenait : "Le média dans lequel nous communiquons est plus important que le contenu même du message", dans le monde de l'intelligence artificielle générative, le média n'est pas seulement le message : c'est la signature.
