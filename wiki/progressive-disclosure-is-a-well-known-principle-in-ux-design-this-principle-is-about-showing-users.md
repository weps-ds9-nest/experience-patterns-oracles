# Progressive disclosure is a well-known principle in UX design. This principle is about _showing users only what they need right now_, and _revealing more options or information gradually_ as they interact or gain context. The goal is to reduce cognitive load, keep interfaces clean and approachable, and still support advanced use cases when needed.

Progressive disclosure is a well-known principle in UX design. This principle is about _showing users only what they need right now_, and _revealing more options or information gradually_ as they interact or gain context. The goal is to reduce cognitive load, keep interfaces clean and approachable, and still support advanced use cases when needed.

The principle of progressive disclosure can be applied not only to the user interfaces we design, but also AI tools we use. In this article, I will show you how to use progressive disclosure to maximize the efficiency of your AI tools.

## Why use progressive disclosure?

Before we dive into how-to, it’s important to answer a key question: “ _Why do we want to use progressive disclosure in the first place?_” The reason for using the principle is pretty much the same as for UX design: to keep context clean and relevant to the task at hand. And by ‘ _context_ ’ I mean the context window that the AI tool uses when it processes your task.

> Context window is the maximum amount of information an AI model can “see”, remember, and reason over at one time, including your prompt, instructions, conversation history, and any pasted documents.

Think of context window as the AI’s working memory.

There are two main problems with the context window:

*   _Limited size._ Context window has a limited number of tokens. For example, Claude 4.5 has a standard context window of 200,000 tokens (approximately 150,000 words or over 500 pages of material). Once you exceed this limit, older or extra information is ignored, truncated, or summarized, which can directly affect output quality.
*   _Too much noise._ The context window can be populated with irrelevant data over time. AI will use all the data you provide when generating output, and if you have a lot of irrelevant data, it will lead to poor quality output (this is known as “garbage in, garbage out”).

Progressive disclosure can help with both problems.

## How to use progressive disclosure

I will demonstrate how to use progressive disclosure using NotebookLM for user research of a digital product.

## Related
[Add wiki-links manually or run update_wikilinks.py]