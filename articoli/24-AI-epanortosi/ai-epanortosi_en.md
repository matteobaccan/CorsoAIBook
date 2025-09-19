---
tags: ["Research", "Generative AI", "Training"]
date: 2025-09-12
author: Dario Ferrero
---

# The AI's "passion" that gives it away: emphatic epanorthosis
![ai-Shakespear.jpg](ai-Shakespear.jpg)

*"Can you recognize a text made with AI?". This is the question I hear most often during my courses on generative artificial intelligence, whispered with the conspiratorial air of someone searching for the Holy Grail of our digital times. My answer, now as automatic as a conditioned reflex, always points in one direction: "Look for an abundance of bullet points," I say, "if it turns every concept into an ordered list." But what I have always considered the most obvious detail of AI might just be the tip of the stylistic iceberg.*

A [new study](https://zenodo.org/records/16947334) by Filippo Lubrano of H-Farm has indeed identified a much more subtle and pervasive pattern: emphatic epanorthosis, an ancient rhetorical figure that language models have turned into their unwitting stylistic signature. It's as if Data from Star Trek had suddenly developed a linguistic tic that betrays him every time he tries to pretend to be human.

The paper, published in August 2025, reveals data that would make any copywriter shudder: Large Language Models produce this specific rhetorical construction at a frequency 27 times higher than humans. We are not talking about an occasional error, but a true stylistic epidemic that cuts across all major models, from ChatGPT to Claude, including open-source systems.

## What is emphatic epanorthosis

Before delving into the numbers, we need to understand what this rhetorical figure with its seemingly exotic outlines is exactly. Epanorthosis is a figure of speech that indicates an emphatic substitution of words, where "Thousands, no, millions!" is a classic example. But the variant that obsesses modern AIs is more specific: it follows the pattern "Not X, but Y," where a first statement is immediately corrected with a more intense or revealing formulation.

To understand the power of this mechanism, let's think of the literary examples that have made this technique famous. In Shakespeare's "Julius Caesar," Mark Antony uses epanorthosis when he says, "Brutus is an honourable man. So are they all, all honourable men," creating a devastating ironic effect through corrective repetition. In newspaper headlines, the technique abounds: "It's not just bad weather, but climate change knocking at the door." Sports commentators constantly overuse it: "It's not just a goal, but the goal that changes the championship's destiny."

In the AI version, however, this elegant rhetorical figure turns into something mechanical and obsessive. Where a human author would write "The technology is advanced," an LLM will automatically produce: "It's not just about advanced technology, but a revolution that is transforming our way of life." Where a journalist would say "The market is growing," the AI will elaborate: "It's not simply growth, but an unprecedented expansion that is redefining global economic balances."

Everyday examples abound. Imagine asking ChatGPT for a recipe for tomato pasta. Instead of telling you "Heat the oil in a pan," you'll get: "It's not just about heating the oil, but about creating the aromatic base that will elevate your sauce from a simple condiment to a culinary experience." It's like having a chef who can never give an instruction without turning it into an epiphanic revelation.

## The numbers speak for themselves
Lubrano's research analyzed three distinct corpora to quantify the phenomenon. The first consisted of 400,000 sentences randomly sampled from the Common Crawl used to train a major family of models in 2024. The second contained 50,000 responses from ChatGPT and Claude collected between January and May 2025. The third was a control corpus of 100,000 sentences from humanities academic journals (2015-2020) and mainstream journalistic articles (2023-2024).

The results are striking: AI models produce 27 emphatic epanorthoses per 1000 sentences, compared to 9 in the training corpus and just 5 in the human benchmark. But there's more: the analysis also revealed a phenomenon of 'burstiness,' meaning that these constructions cluster at certain points in the text, just like when someone discovers emojis and starts putting three or four in a row in the same message. Responses over 300 tokens showed at least one epanorthotic pair for each topic change, suggesting that the device functions as internal signage in generative planning.

To contextualize this data, the study compared the results with larger human corpora: Wikipedia articles, digitized books, and mainstream journalism all showed significantly lower rates, typically between 4-6 instances per 1000 sentences. The stylistic gap between machine-generated text and conventional human prose is so evident as to be almost embarrassing.

A logistic regression controlling for sentence length, presence of first-person pronouns, and interrogatives maintained epanorthosis as a significant predictor of the model's origin. In blind evaluations with graduate students in linguistics, texts rich in epanorthosis were judged likely to be machine-generated, underscoring the relevance of the stylistic signal.

The most disturbing aspect is that the phenomenon is not limited to English. Preliminary samples in Spanish, French, Mandarin, and Arabic show similar amplifications, suggesting that the effect crosses language families and model architectures of various scales and origins. Like a stylistic virus that replicates across languages and cultures.

## Why RLHF created this monster

The root of the problem lies in Reinforcement Learning from Human Feedback (RLHF), the process that is supposed to make models more useful and aligned with human preferences. Ironically, it is this very attempt to humanize AI that has created the stylistic monster we are analyzing.

The mechanism is perversely elegant. During the fine-tuning phase, models are trained to maximize ratings on usefulness, clarity, and politeness. Human annotators, unconsciously, often reward outputs that introduce a clarifying reformulation, interpreting it as evidence of understanding. The reward signal, mediated over millions of tokens, elevates the pattern to a high-value action.

But there is a second level of amplification. The trope also correlates with high-scoring responses in pre-training data, especially marketing blogs and self-help content known for their persuasive urgency. Once rooted, the habit persists across domains, even when it becomes maladaptive. This is what Lubrano calls the "sloganoid effect": clarity is bought at the cost of nuance.

Web corpora, especially those collected from marketing, self-help, and political commentary, contain above-average rates of negation-substitution structures. These domains prioritize clarity, memorability, and persuasion - qualities easily rewarded in RLHF fine-tuning. Once a reward model assigns high value to a reformulation that seems both clarifying and emphatic, the pattern propagates through unrelated topics.

The phenomenon parallels broader trends in digital rhetoric, where short-form, attention-optimized media reduce complex arguments to binary turns. The repeated use of "Not X, but Y" provides a compressed form of narrative tension and resolution, which algorithms tend to reward for its engagement potential.
![frequenza-epanortosi.jpg](frequenza-epanortosi.jpg)
[Relative frequency of "Not X, but Y" in models. From Filippo Lubrano's paper](https://zenodo.org/records/16947334)

## The self-feeding cultural loop

What makes the phenomenon even more worrying is its self-reinforcing nature. Models absorb patterns from the web, amplify them, and users re-encounter them in generated texts, unconsciously integrating them into their own writing. It's a stylistic snake biting its own tail that risks homogenizing public language.

Online discourse rewards simplified dualisms, partly because social media ranking algorithms elevate polarizing content. Corporate slogans and motivational quotes collected by search engines proliferate negative-positive inversions. Models pick up such material, encoding the device as a mark of persuasive effectiveness.

Journalistic critiques in publications like The Guardian and The Atlantic, as well as ongoing discussions on Wikipedia and Reddit, have popularized the notion of "AI slop" to describe this trend. Reports in AI Flash Report and comments across platforms including Twitter/X further frame it as a cultural, not merely technical, problem, highlighting how stylistic shortcuts proliferate through digital writing feedback loops.

## Towards detective algorithms

This discovery opens up fascinating scenarios for the development of new AI detection systems. The frequency of epanorthosis could serve as a weak but useful feature for AI text detectors, particularly when combined with lexical burstiness and mid-sentence discourse markers.

The [currently available AI detectors](https://gptzero.me/) like GPTZero, which recently released Model 3.7b with drastic improvements on the latest language models from major providers, could integrate this new metric into their analysis algorithms. The machine learning team at GPTZero spent the summer building their best AI detector ever, with this release coming just in time for the new 2025/2026 school year.

The multi-factor approach that characterizes tools like [ZeroGPT](https://zerogpt.org/) could benefit enormously from the inclusion of epanorthotic analysis. The ZeroGPT AI detector uses a multi-factor approach to identify the origin of the content, determining whether it was generated by AI or written by a human.

But there is an important warning. The aggressive penalization of the rhetorical figure could discriminate against communities where the device is culturally embedded. Governance tools designed to diversify the model's style must be sensitive to rhetorical variation while preserving legitimate emphatic correction.

Imagine a detective algorithm that works like Sherlock Holmes in the digital age: it doesn't just look for obvious fingerprints like bullet points, but analyzes subtle linguistic patterns, frequencies of rhetorical constructions, distribution of discourse markers. A system that could assign percentage probabilities: "This text has an 87% probability of being generated by AI, based on the presence of 12 emphatic epanorthoses, repetitive lexical patterns, and a lack of human syntactic variation."

## Mitigation strategies

For model curators and developers, Lubrano suggests several mitigation strategies. Curators can overweight corpora that use alternative emphasis techniques, such as juxtaposition without negation or metaphorical shift. Prompt engineers can instruct models to explicitly vary the connective tissue, requesting concessive clauses or descriptive expansion.

Reward models could penalize repeated epanorthoses within a token window, encouraging syntactic exploration. It's like training a musician not to overuse the same chord progression: the technique is not wrong in itself, but its obsessive repetition impoverishes the final result.

A cinematic analogy could be that of Quentin Tarantino: his distinctive narrative techniques (flashbacks, long dialogues, stylized violence) work perfectly in his films, but if all directors started copying them mechanically, cinema would become a predictable bore. Emphatic epanorthosis is the jump cut of AI: effective when used sparingly, devastating when it becomes the only arrow in one's quiver.

## Implications for the future of writing

The phenomenon of emphatic epanorthosis raises deeper questions about the nature of creativity and expression in the age of AI. If language models are unconsciously pushing towards stylistic homogenization, what does this mean for human expressive diversity?

There is an almost Jorge Luis Borges-like irony in the fact that machines designed to imitate human creativity are instead creating their own rhetorical sub-culture, an artificial dialect that is beginning to influence the way humans themselves communicate. It's as if we have created linguistic aliens who, in an attempt to seem human, have developed their own idiosyncrasies that betray them.

The challenge for the coming years will be twofold: on the one hand, to develop increasingly sophisticated detection systems that can identify these subtle patterns; on the other, to work on the stylistic diversification of the models themselves, preventing the search for "clarity" and "usefulness" from leading to an impoverishing standardization of language.

## The detective of the future

Returning to my students' initial question - "Can you recognize a text made with AI?" - the answer is evolving rapidly. No longer just bullet points and obvious repetitive structures, but a constellation of stylistic micro-signals that include abnormal frequencies of specific rhetorical constructions, emphasis patterns, distribution of discourse markers.

The future will probably bring us a kind of linguistic CSI, where digital investigators armed with increasingly sophisticated algorithms will analyze texts in search of stylistic fingerprints invisible to the human eye. Emphatic epanorthosis may be just the first of many "linguistic DNAs" that betray the artificial origin of a text.

But perhaps the most important lesson from this study is that AI, in its attempt to seem more human, is instead revealing how profoundly non-human it is in its patterns of learning and reproduction. Like an actor who, in an attempt to play the part of a human, ends up emphasizing a-epanortosi_the very aspects that make him recognizable as an actor.

Lubrano's research is not just a technical contribution to the field of AI detection, but a memento that reminds us to pay attention not only to what machines say, but to how they say it.

Paraphrasing McLuhan, who argued, "The medium in which we communicate is more important than the content of the message itself," in the world of generative artificial intelligence, the medium is not just the message: it is the signature.
