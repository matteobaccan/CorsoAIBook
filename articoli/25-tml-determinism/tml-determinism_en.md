---
tags: ["Research", "Generative AI", "Training", "Startups"]
date: 2025-09-15
author: Dario Ferrero
---

# LLM: Same question, different answer? Maybe it's the GPUs' fault
![tml.jpg](tml.jpg)

*Imagine having a Michelin-starred chef who, every time you ask for their carbonara recipe, responds with different nuances. Today they add the guanciale first, tomorrow the eggs, the day after tomorrow they change the order of the pasta. The final result is always carbonara, but never exactly the same. This is exactly what happens with Large Language Models: same input, different outputs. Always.*

It's a phenomenon that anyone who has ever chatted with ChatGPT knows well, but which until today was dismissed as an intrinsic feature of artificial intelligence. "It's normal," the experts said, "it's part of the sampling process." As if it were inevitable that a deterministic mathematical system would produce random results.

[Thinking Machines Lab](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/), the startup led by AI veterans that recently attracted significant investment, decided not to settle for this explanation. Their latest paper, published in September 2025, doesn't just identify the problem: it solves it. And the solution is as elegant as it is unexpected.

## When Numbers Become Anarchic

To understand the heart of the problem, we need to take a leap into computer mathematics. As in "Groundhog Day," the film where Bill Murray relives the same day infinitely with imperceptible variations, computers also seem doomed to repeat the same calculations and get slightly different results. But this time there is no existential lesson behind it: there is the physics of processors.

The main culprit is called "non-associativity of floating-point numbers." In mathematics, (a+b)+c should always be equal to a+(b+c). On computers, however, this rule happily jumps out the window. It's as if every time you do a calculation, the order in which you add the numbers changes the final result.

Horace He, the lead researcher at Thinking Machines Lab, explains in the paper that [this phenomenon stems from the way processors handle very large and very small numbers together](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/). It's a bit like trying to average the number of inhabitants of Rome and the weight of a grain of sand: the limited precision of computers means that some details are inevitably lost.

## The Anatomy of Error: Inside the Three Pillars of Indeterminism

To fully understand the scope of Thinking Machines Lab's solution, it is necessary to enter the beating heart of a transformer. Like a watchmaker who disassembles a Patek Philippe to understand why it loses a few seconds a day, the researchers had to dissect every critical component of the model to identify where indeterminism arose.

The architecture of a modern Large Language Model rests on three fundamental pillars, each of which contributes to the problem in a different way. It is like a chamber orchestra where each section has its own peculiarities: the violins (RMSNorm) create subtle dissonances, the brass (matrix multiplications) amplify the errors, and the woodwinds (attention mechanism) transform small variations into dramatic changes in the final harmony.

RMSNorm, an acronym for Root Mean Square Normalization, is perhaps the simplest component to understand and paradoxically the easiest to correct. [Its function is to normalize the input values to stabilize training](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/), a bit like an equalizer that keeps the volume constant regardless of the source's intensity. The problem arises when the "batch size" (the number of requests processed simultaneously) is too small.

Imagine a conductor who has to conduct sometimes 100 musicians, sometimes only 10. With 100 musicians, he can assign a specific role to each section and maintain precise control. With only 10, he has to ask some to double their instruments, inevitably changing the dynamics of the performance. RMSNorm behaves in the same way: when there are few requests to process, it is forced to change its parallelization strategy, introducing variations in the calculations.

The solution from Thinking Machines Lab is as simple as it is radical: ignore the problematic cases. When the batch size is too small to guarantee optimal parallelization, the system accepts a performance loss in order to maintain consistency. It is a profound philosophical choice: it is better to always be consistent than occasionally fast.

Matrix multiplications represent a challenge of a higher complexity. Here it is not just a matter of parallelizing a calculation, but of making the best use of the "tensor cores," specialized computing units present in modern GPUs that can perform thousands of simultaneous operations. It's like moving from using a traditional piano to a church organ with hundreds of stops: the power is immense, but the complexity of control grows exponentially.

The problem arises when the dimensions of the matrices are too small to take full advantage of these specialized units. In these cases, the GPU drivers resort to alternative strategies called "Split-K," where the multiplication is broken down along the reduction dimension instead of along the output dimensions. [It is a brilliant technique for optimizing performance, but it introduces variability in the results](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/) because it changes the order of mathematical operations.

The solution adopted by Thinking Machines Lab is apparently counter-intuitive: always use the same kernel configuration, regardless of the size of the matrices. It is like deciding to always play with the same orchestral formation, even when the musical piece does not require it. Something is lost in efficiency, but predictability is gained.

The third pillar, the attention mechanism, is the one that presents the greatest challenges. It is no coincidence that attention is the heart of the transformer architecture, the component that allows the model to "pay attention" to different parts of the input to generate every single word. It is like a director who has to decide which actors to focus the camera on at every moment of the scene, based on everything that has happened before.

The attention mechanism introduces two additional levels of complexity. First, it must handle reductions along both the feature dimension and the sequence dimension, creating an intertwining of dependencies that makes it almost impossible to maintain a fixed calculation order. Second, it must interface with all modern inference optimizations: chunked prefill (where long sequences are processed in pieces), prefix caching (where common parts of conversations are reused), and parallel decoding.

[The most insidious problem emerges in the so-called "decode stage"](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/), when the model generates one word at a time. In this phase, the query length is typically very small (often just one token), but the key and value cache can be huge (thousands of tokens of previous context). It's like asking a solo singer to perform accompanied by a symphony orchestra: the balance of power is completely skewed.

To maintain acceptable performance, systems resort to techniques called "Split-KV" or "FlashDecoding," which parallelize processing along the cache dimension. But once again, this parallelization introduces variability in the order of calculations. The solution from Thinking Machines Lab requires a profound modification of these algorithms, adopting a "fixed split size" strategy instead of a "fixed number of splits" strategy.

It is a subtle but fundamental distinction. Instead of saying "always divide into 8 parts," the system says "each part must always be 256 elements." In this way, the order of operations remains identical regardless of the total length of the sequence. It's like deciding that each musician must always play for exactly 4 bars, regardless of the length of the piece.

The elegance of this solution lies in its universality: once all three pillars have been made "batch-invariant," the entire system becomes deterministic. There is no need to redesign the transformer architecture or invent new algorithms. It is enough to ensure that each component always behaves in the same way, regardless of the context in which it is executed.
![inference.jpg](inference.jpg)
[From thinkingmachines.ai](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/)

## Batch Invariance: The Secret Key

But here's the plot twist worthy of a tech thriller: the real problem doesn't lie in the competition between GPU processors, as previous theories claimed. It's something much more subtle and, paradoxically, easier to solve.

The discovery of Thinking Machines Lab is that the behavior of LLMs changes depending on how many requests are processed together. It's as if our Michelin-starred chef changed the recipe depending on how many covers he had to prepare at the same time. Same dish, same ingredients, but the final result depends on the workload of the moment.

This phenomenon has a technical name: lack of "batch invariance." In simple terms, it means that processing one request alone or together with 100 others can produce different answers to the same question. [The researchers demonstrated this effect with surprising experiments](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/): by asking the same question about Richard Feynman 1000 times to a Qwen model, they obtained 80 different answers, with the first divergence appearing at exactly the 103rd token.

The solution proposed by Thinking Machines Lab is elegant in its simplicity: modify the "kernels" (the fundamental computing blocks) so that they always produce the same results, regardless of how many other operations are performed in parallel. It's like teaching our chef to always follow the same sequence of steps, whether he's cooking for one or for a hundred.
![batch.jpg](batch.jpg)
[From thinkingmachines.ai](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/)

## The Price of Consistency

As in any story of technological innovation, the solution involves compromises. The "batch-invariant" kernels developed by the team are slower than the standard ones. Not by much, fortunately: in tests conducted on a single GPU server using the Qwen-3-8B model, the slowdown was around 60% compared to the optimized version, dropping to 30% with some improvements to the attention implementation.

It might seem like a high price to pay, but consider the implications. [The indeterminism of LLMs is not just an aesthetic nuisance](https://dataconomy.com/2025/09/11/tml-defeating-nondeterminism-in-llm-inference/): it compromises scientific reproducibility, makes accurate debugging impossible, and, above all, transforms what should be "on-policy" reinforcement learning into something completely different.

It's a bit like trying to train a Formula 1 driver on a simulator that changes the laws of physics every time it's turned on. The driver learns to adapt to the variations, but doesn't really learn to drive that specific car.

## The Silent Revolution of RL

This is where one of the most interesting aspects of Thinking Machines Lab's research comes into play. Reinforcement learning, the technique behind the most advanced models like ChatGPT, is based on the idea that AI learns from its own experiences. But if every time the AI "tries" the same action it gets a slightly different result, is it really learning from the same experience?

The researchers have shown that [indeterminism subtly transforms "on-policy" learning into "off-policy" learning](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/), creating a discrepancy between what the model does during training and what it does when it is used. It's as if a musician practices on an out-of-tune piano and then performs on a tuned one: the difference is subtle but fundamental.

With the deterministic kernels from Thinking Machines Lab, this problem disappears. In their experiments on an RL setup applied to the Bigmath dataset, the team obtained a perfectly flat KL divergence at zero, indicating a perfect match between training and inference. It is the Holy Grail of machine learning: a system that behaves exactly as it was trained to do.

## The Industrial Landscape: Who Will Win the Reproducibility War

In the world of artificial intelligence, where tech giants challenge each other with ever larger and more powerful models, Thinking Machines Lab has chosen to fight a different battle. While OpenAI, Google, and Anthropic focus on the raw power of their systems, this relatively small team has decided to focus on precision. It is the classic story of David versus Goliath, but this time David's sling is pure mathematics.

The startup, founded by former researchers from some of the most prestigious companies in the sector, represents a completely different approach to AI research. [It's not about creating the biggest or fastest model, but about understanding in depth how these systems really work](https://americanbazaaronline.com/2025/09/11/inside-thinking-machines-lab-muratis-12-billion-ai-startup-tackles-reproducibility-467536/). It's a bit like the difference between building an increasingly powerful racing car and understanding why the car sometimes goes left when it should go straight.

The timing of this research is not accidental. The AI industry is at a crucial turning point, where the race for pure performance is giving way to more mature considerations of reliability, safety, and predictability. It is the moment when an adolescent sector begins to behave like an adult, and reproducibility is one of the first signs of this maturation.

The most critical sectors are already raising their voices. In the world of healthcare, where AI algorithms are increasingly used for diagnoses and treatment plans, the idea that the same symptom can produce different assessments is simply unacceptable. It's like having a thermometer that gives different temperatures every time you use it: maybe the fever is always there, but not knowing if it's 38 or 39 degrees makes the difference between a paracetamol and a trip to the hospital.

The financial sector is no different. Automated trading algorithms and risk assessment systems must operate in a world where reproducibility is not a preference, but a regulatory requirement. [Supervisory authorities are beginning to require that AI models used for credit or investment decisions produce traceable and verifiable results](https://dataconomy.com/2025/09/11/tml-defeating-nondeterminism-in-llm-inference/). It is impossible to explain to a judge why the same algorithm gave different opinions on two identical mortgage applications.

The world of scientific research is also becoming aware of the problem. When a scientific paper claims to have obtained certain results using an AI model, other researchers must be able to replicate those experiments exactly. It is the very foundation of the scientific method, called into question by the indeterminism of LLMs. As if every time you replicate a physics experiment, gravity were slightly different.

But the implications go far beyond these obviously critical sectors. Think about the impact on debugging and software development. Currently, when an AI-based application behaves unexpectedly, developers find themselves in a Kafkaesque situation: the bug could be in their code, or it could simply be yet another manifestation of the model's indeterminism. It's like trying to fix a watch that sometimes decides on its own to go faster or slower.

The solution from Thinking Machines Lab promises to transform this ghost hunt into a normal debugging process. If the model always produces the same outputs for the same inputs, any anomalous behavior is necessarily due to a real error, not a random fluctuation. It is the difference between being a detective in a world where evidence changes spontaneously and being a detective in a world where evidence remains consistent.

The most interesting aspect of this dynamic is that none of the major players in the sector seem to have prioritized this problem. OpenAI, Google, Meta, and the other giants are all obsessed with the race for performance, while the issue of reproducibility has remained in the background. It is one of those rare situations in the tech world where a startup can actually beat companies with a hundred times more resources, simply because it has identified the right problem at the right time.

Of course, convincing the industry to adopt a solution that involves a 30-60% slowdown will not be easy. In the world of AI, where milliseconds of latency can make the difference between the success and failure of a product, any compromise on performance is viewed with suspicion. But the signs of change are already there.

Some pioneering companies are beginning to experiment with "deterministic" versions of their systems for specific applications. Not surprisingly, the first adopters are precisely those operating in highly regulated sectors, where the cost of indeterminism far outweighs the benefit of a few milliseconds less latency.

## Towards a Deterministic Future

The real game will be played when the batch-invariant kernels from Thinking Machines Lab are optimized to the point of significantly reducing the performance gap. At that point, the question will no longer be "can we afford to be deterministic?" but "can we afford not to be?".

The solution proposed by Thinking Machines Lab is not yet ready for large-scale production. The code is available on GitHub as a proof of concept, but it requires significant changes to existing inference pipelines. However, the implications are enormous.

Think of a world where LLMs always produce the same answer to the same question. We are not talking about less creative or more rigid AIs, but about more reliable and predictable systems. A virtual assistant that always gives you the same medical advice for the same symptom. A translation system that doesn't change the version of the text every time you restart it. A financial analysis model that always produces the same assessment for the same data.

It is interesting to note how this research fits into a broader trend towards what we might call "responsible AI." After years of a frantic race towards ever larger and more powerful models, the industry is beginning to ask itself more mature questions: not only "what can we do?" but also "what should we do?" and "how can we do it better?".

In this context, Thinking Machines Lab could find itself in the enviable position of having arrived before others at an awareness that will become inevitable. As often happens in technology, what today seems like a niche requirement could become the industry standard tomorrow. And whoever invested first in this direction will find themselves with a significant competitive advantage.

The most fascinating aspect of this story is that the solution does not require technological revolutions or scientific breakthroughs. It is a problem of pure engineering, solved with mathematical rigor and attention to detail. In an era where AI seems increasingly magical and incomprehensible, Thinking Machines Lab reminds us that behind every intelligent algorithm there is always solid mathematics and precise implementations.

Perhaps the real lesson of this research is not so much about LLMs as it is about the maturity of an entire sector. We have reached the point where it is no longer enough for artificial intelligence to work: it must work in a predictable, traceable, and reproducible way. It is the transition from art to science, from alchemy to chemistry.

After all, who would have thought that the real evolutionary leap in AI would not come from larger models or more sophisticated algorithms, but from the simple ability to always do the same thing in the same way? As in the best movie plot twists, the answer was hidden in plain sight. You just had to have the courage to look for it.
