Title: Generative AI Design Patterns: A Comprehensive Guide

URL Source: https://towardsdatascience.com/generative-ai-design-patterns-a-comprehensive-guide-41425a40d7d0

Published Time: 2024-02-13T23:19:59+00:00

Markdown Content:
![Image 1](https://towardsdatascience.com/wp-content/uploads/2024/02/12tBQkVvC-_sHACgSs0ouug.png)
_Note: When I initially published this article back in February it was an early thought experiment. Since then I have started working on a book for "Generative AI Design Patterns" with a major publisher. Please follow me to keep updated on updates to my patterns an ideas in this space._

### The Need For AI Patterns

We all anchor to some tried and tested methods, approaches and patterns when building something new. This statement is very true for those in software engineering, however for generative AI and artificial intelligence itself this may not be the case. With emerging technologies such as generative AI we lack well documented patterns to ground our solution’s.

Here I share a handful of approaches and patterns for generative AI, based on my evaluation of countless production implementations of LLM’s in production. The goal of these patterns is to help mitigate and overcome some of the challenges with generative AI implementations such as cost, latency and hallucinations.

### List of Patterns

1.   [Layered Caching Strategy Leading To Fine-Tuning](https://towardsdatascience.com/generative-ai-design-patterns-a-comprehensive-guide-41425a40d7d0#82c6)
2.   [Multiplexing AI Agents For A Panel Of Experts](https://towardsdatascience.com/generative-ai-design-patterns-a-comprehensive-guide-41425a40d7d0#fc13)
3.   [Fine-Tuning LLM’s For Multiple Tasks](https://towardsdatascience.com/generative-ai-design-patterns-a-comprehensive-guide-41425a40d7d0#a0b9)
4.   [Blending Rules Based & Generative](https://towardsdatascience.com/generative-ai-design-patterns-a-comprehensive-guide-41425a40d7d0#19ee)
5.   [Utilizing Knowledge Graphs with LLM’s](https://towardsdatascience.com/generative-ai-design-patterns-a-comprehensive-guide-41425a40d7d0#1b7b)
6.   [Swarm Of Generative AI Agents](https://towardsdatascience.com/generative-ai-design-patterns-a-comprehensive-guide-41425a40d7d0#1575)
7.   [Modular Monolith LLM Approach With Composability](https://towardsdatascience.com/generative-ai-design-patterns-a-comprehensive-guide-41425a40d7d0#682f)
8.   [Approach To Memory Cognition For LLM’s](https://towardsdatascience.com/generative-ai-design-patterns-a-comprehensive-guide-41425a40d7d0#07cb)
9.   [Red & Blue Team Dual-Model Evaluation](https://towardsdatascience.com/generative-ai-design-patterns-a-comprehensive-guide-41425a40d7d0#ee0a)

* * *

### 1) Layered Caching Strategy Leading To Fine-Tuning

![Image 2](https://towardsdatascience.com/wp-content/uploads/2024/02/1JruSgFs4txALlvMTWh94rA.png)
Here we are solving for a combination of factors from cost, redundancy and training data when introducing a caching strategy and service to our large language models.

By caching these initial results, the system can serve up answers more rapidly on subsequent queries, enhancing efficiency. The twist comes with the fine-tuning layer once we have sufficient data, where feedback from these early interactions is used to refine a more specialized model.

The specialized model not only streamlines the process but also tailors the AI’s expertise to specific tasks, making it highly effective in environments where precision and adaptability are paramount, like customer service or personalized content creation.

For getting started there are pre-built services such as [GPTCache](https://github.com/zilliztech/GPTCache) or roll your own with common caching databases such as [Redis](https://redis.io/), [Apache Cassandra](https://cassandra.apache.org/_/index.html), [Memcache](https://memcached.org/)d. Be sure you monitor and measure your latency as you add additional services to the mix.

* * *

### 2) Multiplexing AI Agents For A Panel Of Experts

![Image 3](https://towardsdatascience.com/wp-content/uploads/2024/02/140vNV6n0sHpctSIyUHwEKQ.png)
Imagine an ecosystem where multiple generative AI models orientated to a specific task ("agents"), each a specialist within its domain, work in parallel to address a query. This _multiplexing_ strategy enables a diverse set of responses, which are then integrated to provide a comprehensive answer.

This setup is ideal for complex problem-solving scenarios where different aspects of a problem require different expertise, much like a team of experts each tackling a facet of a larger issue.

A larger model such as a GPT-4 is used to understand context and break this down into specific tasks or information requests which are passed to smaller agents. Agents could be smaller language models such as [Phi-2](https://www.microsoft.com/en-us/research/blog/phi-2-the-surprising-power-of-small-language-models/) or [TinyLlama](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v0.1) that have been trained on specific tasks, access to specific tools or generalized models such as GPT, Llama with specific personality, context prompts and function calls.

* * *

### 3) Fine-Tuning LLM’s For Multiple Tasks

![Image 4](https://towardsdatascience.com/wp-content/uploads/2024/02/1t_peu77E5AaPQDS1Z2-Lgw.png)
Here we fine-tune a large language model on multiple tasks simultaneously instead of a single task. It’s an approach that promotes a robust transfer of knowledge and skills across different domains, enhancing the model’s versatility.

This multi-task learning is especially useful for platforms that need to handle a variety of tasks with a high degree of competence, such as virtual assistants or AI-powered research tools. This could potentially simplify workflows for training and testing for a complex domain.

Some resources and packages for training LLM’s include [DeepSpeed](https://github.com/microsoft/DeepSpeed), and the training functions on [Hugging Face’s Transformer library](https://huggingface.co/docs/transformers/training).

* * *

### 4) Blending Rules Based & Generative

![Image 5](https://towardsdatascience.com/wp-content/uploads/2024/02/1ESI8bYTuDKwTHiOr0tTdDw.png)
A number of existing business systems and organizational applications are still somewhat rules based. By fusing the generative with the structured precision of rule-based logic, this pattern aims to produce solutions that is both creative yet compliant.

It’s a powerful strategy for industries where outputs must adhere to stringent standards or regulations, ensuring the AI remains within the bounds of desired parameters while still being able to innovate and engage. A good example of this is generating intents and message flows for a phone call IVR system or traditional (_non-llm based_) chat bots which is rules based.

* * *

### 5) Utilizing Knowledge Graphs with LLM’s

![Image 6](https://towardsdatascience.com/wp-content/uploads/2024/02/1AfkF7JwB0FFZrhQhP-8gsQ.png)
Integrating knowledge graphs with generative AI models gives them a fact orientated super power, allowing for outputs that are not only contextually aware but also more factually correct.

This approach is crucial for applications where truth and accuracy are non-negotiable, such as in educational content creation, medical advice, or any field where misinformation could have serious consequences.

Knowledge graphs and graph ontologies (_set of concepts for a graph_) allow for complex topics or organizational problems to be broken into a structured format to help ground a large language model with deep context. You can also use a language model to generate the ontologies in a format such as JSON or RDF, [example prompt I created you can use](https://gist.github.com/koconder/c37806ecc2e0a6d1ed3cdfbe4951b199).

Services you can use for knowledge graphs include graph database services such as [ArangoDB](https://arangodb.com/), [Amazon Neptune](https://aws.amazon.com/neptune/), [Azure Cosmos DB](https://azure.microsoft.com/en-us/products/cosmos-db) and [Neo4j](https://neo4j.com/). There are also wider datasets and services for accessing broader knowledge graphs including [Google Enterprise Knowledge Graph API](https://cloud.google.com/enterprise-knowledge-graph/docs/search-api), [PyKEEN Datasets](https://github.com/pykeen/pykeen?tab=readme-ov-file#datasets), and [Wikidata](https://cloud.google.com/enterprise-knowledge-graph/docs/search-api).

* * *

### 6) Swarm Of AI Agents

![Image 7](https://towardsdatascience.com/wp-content/uploads/2024/02/1TpXF89A9GHZchfgbSOxsYQ.png)
Drawing inspiration from natural swarms and heards, this model employs a multitude of AI agents that collectively tackle a problem, each contributing a unique perspective.

The resulting aggregated output reflects a form of collective intelligence, surpassing what any individual agent could achieve. This pattern is particularly advantageous in scenarios that require a breadth of creative solutions or when navigating complex datasets.

An example of this could be [reviewing a research paper from a multiple "experts" point of view](https://www.fieldstudy.ai/), or assessing customer interactions for many use-cases at once from fraud to offers. We take these collective "agents" and combine all their inputs together. For high volume swarm’s you can look at deploying messaging services such as [Apache Kafka](https://kafka.apache.org/) to handle the messages between the agents and services.

* * *

### 7) Modular Monolith LLM Approach With Composability

![Image 8](https://towardsdatascience.com/wp-content/uploads/2024/02/1HuFhp3Zjnp6ad38m249Nog.png)
This design champions adaptability, featuring a modular AI system that can dynamically reconfigure itself for optimal task performance. It’s akin to having a Swiss Army knife, where each module can be selected and activated as needed, making it highly effective for businesses that require tailor-made solutions for varying customer interactions or product needs.

You can deploy the use of various autonomous agent frameworks and architectures to develop each of your agents and their tools. Example frameworks include [CrewAI](https://github.com/joaomdmoura/crewAI), [Langchain](https://www.langchain.com/), [Microsoft Autogen](https://www.microsoft.com/en-us/research/project/autogen/) and [SuperAGI](https://superagi.com/).

For a sales modular monolith this could be agents focused on prospecting, one handling bookings, one focused on generating messaging, and another updating databases. In future as specific services become available from specialized AI companies, you can swap out a module for an external or 3rd party service for a given set of tasks or domain specific problems.

### 8) Approach To Memory Cognition For LLM’s

![Image 9](https://towardsdatascience.com/wp-content/uploads/2024/02/1WGV1UYO6dAnbaq37w44Kgg.png)
This approach introduces an element of human-like memory to AI, allowing models to recall and build upon previous interactions for more nuanced responses.

It’s particularly useful for ongoing conversations or learning scenarios, as the AI develops a more profound understanding over time, much like a dedicated personal assistant or an adaptive learning platform. Memory cognition approaches can be developed through summation and storing key events and discussions into a vector database over time.

To keep compute of summaries low, you can leverage summation through smaller NLP libraries such as [spaCy](https://spacy.io/), or [BART language models](https://huggingface.co/docs/transformers/model_doc/bart) if dealing with considerable volumes. Databases used are vector based and retrieval during prompt stage to check the short-term memory uses a similarity search to locate key "facts". For those interested on a working solution there is an open-sourced solution following a similar pattern called [MemGPT](https://memgpt.readme.io/docs/index).

* * *

### 9) Red & Blue Team Dual-Model Evaluation

![Image 10](https://towardsdatascience.com/wp-content/uploads/2024/02/17D_yQ8TZ7QmzV9BRQt55JA.png)
In the Red and Blue team evaluation model, one AI generates content while another critically evaluates it, akin to a rigorous peer-review process. This dual-model setup is excellent for quality control, making it highly applicable in content generation platforms where credibility and accuracy are vital, such as news aggregation or educational material production.

This approach can be used to replace parts of human feedback for complex tasks with a fine-tuned model to mimic the human review process and refine the results for evaluating complex language scenarios and outputs.

* * *

### **Takeaways**

These design patterns for generative AI are more than mere templates; but the frameworks upon which the intelligent systems of tomorrow will grow. As we continue to explore and innovate, it’s clear that the architecture we choose will define not just the capabilities but the very identity of the AI we create.

By no means this list is final, we will see this space develop as the patterns and use cases for generative AI expands. _This write-up was inspired by the [AI design patterns](https://tomtunguz.com/ai-design-patterns/) published by Tomasz Tunguz._

* * *

### Enjoyed This Story?

Vincent Koc is a highly accomplished, commercially-focused technologist and futurist with a wealth of experience focused in data-driven and digital disciplines.

[Subscribe for free](https://medium.com/subscribe/@vkoc) to get notified when Vincent publishes a new story. Or follow him on [LinkedIn](https://www.linkedin.com/in/koconder/) and [X](https://twitter.com/koconder).

> [**Get an email whenever Vincent Koc publishes.**](https://medium.com/subscribe/@vkoc)

_Unless otherwise noted, all images are by the author_
