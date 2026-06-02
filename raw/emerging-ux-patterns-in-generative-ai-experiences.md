Title: Article from uxdesign.cc

URL Source: https://smry.ai/https:/uxdesign.cc/emerging-interaction-patterns-in-generative-ai-experiences-8c351bb3392a

Markdown Content:
## Looking back at history to help us design for the future.

Ever been greeted by a barista who already knows your coffee order? It's great getting your coffee without detailing every aspect — temperature, brew time, water volume, bean origin, grind size, roast, etc. This illustrates the spectrum we’re navigating with AI today.

This article is not about coffee; it’s about how user interactions change and adapt, how generative AI user interactions may evolve based on previous trends in the GUI and new trends emerging in generative AI interaction. We will look at the value of context bundling, user curation, trust, and ecosystems as key trends for AI user experience.

## From Commands to Conversations

Let’s rewind to the dawn of computing when using a computer meant typing precise commands in a [Command-Line Interface (CLI)](https://www.freecodecamp.org/news/shells-a-history-of-human-computer-interfaces/). Imagine the challenge of remembering the exact command to open a file or copy data, not to mention locating your “homework” folder. Not everyone was cut out to be a programmer. For wider usability, a shift was necessary.

Enter [ELIZA](https://en.wikipedia.org/wiki/ELIZA) in 1964, an early attempt at natural language processing, engaging users with basic conversations through keyword recognition and scripted responses. Although groundbreaking, ELIZA’s interactions were far from flexible or scalable.

Around the same time, [Xerox PARC was developing the Graphical User Interface (GUI)](https://ohiostate.pressbooks.pub/graphicshistory/chapter/16-1-xerox-parc/), later brought to the masses by [Apple in 1984](https://akshayparakh.medium.com/a-brief-history-of-apple-computer-inc-and-the-graphic-user-interface) and [Microsoft thereafter](https://en.wikipedia.org/wiki/Windows_1.0). GUIs transformed computing, replacing complex commands with icons, menus, and windows, navigable by a mouse. This innovation made computers accessible and intuitive for everyday tasks, setting the stage for the universal role technology has in our lives.

Examples of different interfaces. ChatGPT’s primary interaction is text-based, how might it evolve?

Look at the example image above. We’re witnessing a parallel evolution today. [User prompts are basically mini-programs crafted in natural language](https://balajis.com/p/prompts-are-tiny-programs), with the quality of outcomes depending on our prompt engineering skills. Just as [early computing transitioned from the complexity of CLI to the simplicity of GUIs](https://bootcamp.uxdesign.cc/the-evolution-of-programming-ux-ui-from-command-line-to-graphical-interfaces), [making technology accessible to everyone](https://www.sciencedirect.com/topics/computer-science/graphical-user-interface), we’re seeing a similar trend emerging generative AI with the move towards bundling complex inputs into simpler, more user-friendly interfaces with a complexity in the background.

Image generators, shown above, like [Stable Diffusion WebUI](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&cd=&cad=rja&uact=8&ved=2ahUKEwiYyOzWqs6EAxXGADQIHe8IBUsQFnoECAYQAQ&url=https%3A%2F%2Fgithub.com%2FAUTOMATIC1111%2Fstable-diffusion-webui&usg=AOvVaw285bGGkCng3H5xt_oBrds1&opi=89978449), [Mid Journey,](https://docs.midjourney.com/docs/midjourney-discord) and [DALL·E 3](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&cd=&cad=rja&uact=8&ved=2ahUKEwjHnpLkqs6EAxXMAzQIHVk8ABAQFnoECAYQAQ&url=https%3A%2F%2Fopenai.com%2Fdall-e-3&usg=AOvVaw3IwHgRCpmR8K01t-OrugMO&opi=89978449), demand different levels of precision in their prompts to get results. While Mid Journey and DALL·E are easier to use, Stable Diffusion allows for much more specific outputs. However, the more we know about our users the more easily we provide a simple experience while maintaining their desired specificity.

### Context Bundling

Context bundling simplifies interactions by combining related information into a single command, addressing the challenge of conveying complex instructions to achieve desired outcomes. This enhances efficiency and output quality by aligning user intent and machine understanding in one go, removing the need for manual user prompt writing.

We’ve seen this emerge across generative AI tools like sample prompts in Edge, [Google chrome’s tab manager,](https://blog.google/products/chrome/google-chrome-generative-ai-features-january-2024/#organize-tabs) and trigger-words in Stable Diffusion are [special tokens in a prompt](https://stable-diffusion-art.com/embedding/) may that fine-tunes with a textual inversion, LoRa, model, or other refinements.

In context bundling, “Conversational” AI doesn’t always mean conversation. It’s about the outcome the user is trying to get beyond relying on text-based prompting. Context bundling provides users a [shortcut to the desired outputs without the need to engage in lengthy conversation](https://www.nngroup.com/articles/ui-accelerators/). The user experience no longer hinges on a general conversational interface. Differentiation is driven by specific data, and more specialized experiences.

Examples of this specificity include [Miro Assist](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&cd=&cad=rja&uact=8&ved=2ahUKEwj4_9Kw7tCEAxXFOTQIHTtLCSoQFnoECA4QAQ&url=https%3A%2F%2Fmiro.com%2Fassist%2F&usg=AOvVaw1_GyTx9CaXLjwbYPL1XFee&opi=89978449), [Clay AI formula generator,](https://www.clay.com/learn/how-to-use-the-ai-formula-generator-and-conditionally-run-integrations) and [SCOPUS AI](https://www.elsevier.com/products/scopus/scopus-ai). Each simplify interactions by combining related information into specific single commands.

Another way to extend context bundling is to let users define properties of these bundles. User adjustable preferences and personalization are bundled into the context, [providing users with more productive and relevant interactions later in the product](https://business.adobe.com/ca/index/topics/ai-personalization.html).

Context bundling isn’t just about simplifying conversations; it’s about helping users directly achieve their goals, whether through search queries, summaries, or some other specific tasks. It turns detailed instructions into simple user-friendly interactions, [particularly beneficial for straightforward or repetitive tasks](https://www.nngroup.com/articles/ui-accelerators/). But what about for more open ended tasks like explorations, or goals where refinement is desirable? This is where continuous user feedback mechanisms, or feedback loops are needed.

### User Curation

Despite advancements in making AI interactions more intuitive, there remains a spectrum of needs where [users must refine outputs to achieve their specific goals](https://www.nngroup.com/articles/ai-paradigm/). This is especially true in activities like [researching, brainstorming, creating creative content, refining images, or even editing](https://www.nngroup.com/articles/AI-conversation-types). The ever-increasing context windows and multi-modal capabilities, make guiding users through the complexity even more important.

Whether aware or not, we as humans are [constantly curating our experience of the world](https://www.researchgate.net/publication/229101074_Information_Foraging) (above image). This curation may look like highlighting or picking our certain keywords of interest in a conversation or manually highlighting in a book. While observing users using ChatGPT for brainstorming, I noticed this similar highlighting behaviour. Users, at the time, couldn’t interact with the highlights, but used parts of it to guide their next steps. This showed that, while the initial output may not fully meet the user’s needs, it serves to provide tangible anchors for next actions. Making it easier for users to curate and refine their outputs allows both the user and machine to get higher-quality results.

In the above image, [inpainting](https://wandb.ai/ayush-thakur/image-impainting/reports/Introduction-to-Image-Inpainting-with-Deep-Learning--Vmlldzo3NDIwNA), threaded conversations, and highlighting interactions are all emergent examples that show how users can curate specific parts of the information to create more relevant context and get better outcomes.

## Get Ryan Tang’s stories in your inbox

Join Medium for free to get updates from this writer.

Take writing a well-researched report as another example. A user’s journey often begins with broad research, leading to the discovery of key points that warrant deeper investigation. As they gather and assess information, they gradually compile and [synthesize it into their final piece](https://www.elsevier.com/connect/11-steps-to-structuring-a-science-paper-editors-will-take-seriously). In this process, moments of highlighting or selecting specific content act as crucial anchors, guiding the AI to deliver more pertinent results and context. This path requires ways for users to both save and consume highlights.

Users need to save specific highlights, and also use those highlights to refine their experience. This requires deep understanding of user outcomes and creating feedback mechanisms to capture this.

User curation reveals that for generative AI to effectively support complex creative tasks, it must not only understand but [also anticipate the nuanced ways users interact with information](https://www.nngroup.com/articles/perplexity-henry-modisett/). By recognizing and responding to these ‘curation signals,’ AI tools can offer more targeted assistance, enriching the overall user experience and outcome.

### Designing for Just Enough Trust

While generative AI has made interacting with technology easier for users, [trust remains a significant barrier to widespread adoption](https://www.weforum.org/agenda/2024/01/davos24-trust-ai-right-foundations-determine-its-future/). This has been [true in the past](https://en.wikipedia.org/wiki/Luddite) and remains true today. Addressing trust is key to building and encouraging the adoption of new AI tools.

Among the many frameworks for understanding how people accept and use new technology, two frameworks were particularly inspiring: the [Unified Theory of Acceptance and Use of Technology (UTAUT)](https://open.ncl.ac.uk/theories/2/unified-theory-of-acceptance-and-use-of-technology/) and [Fogg’s Behavior Model (FBM)](https://behaviormodel.org/).

As a useful oversimplification: UTAUT suggests that usage intention is influenced by performance expectancy, effort expectancy, social influence, and facilitating conditions. For example, someone might decide to start using a client management tool because they believe it will effectively help them achieve their sales goals (performance expectancy), they find the app straightforward and user-friendly (effort expectancy), their co-workers and mentors also use and recommend it (social influence), and their organization database is accessible through it (facilitating conditions).

A parallel theory, FBM, simplifies behavior into a function of motivation, ability, and a prompt (or trigger). For example, the act of buying coffee is driven by the desire for caffeine, the presence of money and a nearby coffee shop, and the coffee shop sign serving as a prompt.

Generative AI reduces the perceived effort required to achieve outcomes. Anecdotally, many users have overcome activation inertia with generative AI. However, ensuring more user try and stay engaged is where trust plays a crucial role.

In the context of designing for trust, there are many perspectives and frameworks like the ones mentioned above. Here we will further simplify and think about trust as being shaped by: previous experiences, risk tolerance, interaction consistency, and social context.

**Previous Experiences:** We must recognize that users have baggage. They come into experiences with context created by previous experiences. To influence this foundation of trust, we simply need to [not re-invent the wheel](https://lawsofux.com/jakobs-law/). Familiar interfaces and interactions allow users to transfer the trust of the past into the present. It is much easier to build on this trust foundation rather than working against it. An example in the context conversational AI, rather than telling a user to input a prompt, we can leverage [subconscious tendencies to mirror in conversation](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&cd=&cad=rja&uact=8&ved=2ahUKEwi1hLa-4cGEAxVyHjQIHQJJB1AQFnoECA0QAw&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FMirroring&usg=AOvVaw08yRZPjdzDG8n_U06B0okV&opi=89978449) by using responses to influence the way users interact.

**Risk Tolerance:** Understand that users want to avoid negative outcomes. The key to this is understanding which risks users will not take. We must bring risk below the users risk tolerance. Some methods to influence risk tolerance include: increasing transparency, user control, user consent, compliance. Creating polished experiences can leverage [aesthetic usabilit](https://www.nngroup.com/articles/aesthetic-usability-effect/) y to [decrease the risk expectation](https://www.nngroup.com/articles/negativity-bias-ux/). However, product-specific approaches are always going to be more effective. As an example, imagine a conversational AI for doctors providing diagnostics. The risk tolerance is very low. A misdiagnosis would be extremely consequential for both the doctors and patients. Ensuring output transparency with references, prompt break downs, and conflicting perspectives would be effective in reducing the risk.

**Interaction Consistency:** Interaction is both the output and the way a user arrives there. [Users shouldn’t have to wonder whether different words, situations, or actions mean the same thing.](https://www.nngroup.com/articles/consistency-and-standards/) To improve interaction consistency, ensure that internal and external consistency is maintained from the layouts to the button text. In the context of a conversational AI, interaction consistency may look like responses having the similar formats and words having the same meaning across the conversation. If a user requests a summary of a topic it should not look like an essay in one interaction and a bullet list in another, unless the user specifically asks.

**Social Context:** Potentially the most visible layer. Social context can include endorsements from trusted sources like a manager, or facilitation within a trusted network like being connected with pre-approved enterprise software. Social context can be influenced by [social proofing strategies](https://buffer.com/library/social-proof/), and creating social proofing opportunities within interaction. In the context of an LLM for internal databases, this may mean highlighting work done by the user and their direct team. Pointing out that the system has visibility of internal data helps to further build trust that the system is approved within this social context.

When designing for trust in an AI experience, it is worth considering which of these factors ought to be the immediate focus. By understanding and designing for these aspects of trust, AI experiences can align with users’ expectations and needs, increasing general adoption and acceptance. Addressing trust is not just beneficial; it’s necessary for the future integration and acceptance of generative AI tools.

### Context Ecosystems

This article has covered emerging trends of context bundling, and user curation, as well as designing for trust. As a whole generative AI has revolutionized productivity by [lowering the barrier](https://hbr.org/2023/04/how-generative-ai-could-disrupt-creative-work) for everyday users to start on tasks, this mirrors the benefits and journey of the GUI. However, modern UX has evolved far beyond windows and pointers. So where might generative AI be going next?

GUIs facilitated deeper and more efficient user interactions by supporting multiple program interfaces. This allowed users to seamlessly transition between different tasks — like accounting in one application and reporting in a presentation in another application. Managing and acting across different contexts underscored the productivity gains from bridging various user intentions and applications.

Emergent examples, shown above, include Edge, Chrome, and Pixel Assistant integrating AI functionality to allow user to use generative AI to interface with their software. In this case, the LLM is aware of the software, something beyond a conversational window previous applications confined it to.

Looking at the past, we see how the GUI created a digital canvas for the user to create. The advantages of this over the physical world: improved efficiency, scalability, and productivity. It is very likely that generative AI will go down a similar route, where AIs become collaborators that turn our day-to-day lives into a shared experience. The future may be an augmented ecosystem where conversational and generative AI tools will connect specialized agents within a cohesive workflow. This ecosystem approach could further deepen user interactions, allowing for a more integrated and productive experience across various digital and real world environments.

Future trends are not just conversational or companion experiences. Similar to what we see today, generative AI will work directly to create outputs. Currently users engage with the outputs, but the creator and owner of the canvas is ultimately the AI. As we mature with human-centred AI products, the next steps will be creating spaces where the AI and user can collaborate on the same canvas. We’ve seen it in older tools like Grammarly, and in [emerging in generative tools like Github Copilot](https://githubnext.com/projects/copilot-workspace/). We see generative AI collaborating as a contributor, with the user ultimately creating and owning the workspace. As our comfort and technology continues to evolve, we may see generative AI play a bigger role in managing both the digital and physical aspects of our daily lives (IoT); augmenting reality and redefining our approach to life and productivity.

Evolving generative AI interactions are repeating human-computer interaction history. As we create better experiences that bundle context into simpler interactions, empower users to curate their experience, and augment known ecosystems, we’ll make generative AIs more trustworthy, accessible, usable, and beneficial for everyone.

If you’re interested in exploring this topic, here are some resources for further reading:

*   “ [The 1984 Apple Macintosh — How does it look today?](https://bootcamp.uxdesign.cc/the-evolution-of-programming-ux-ui-from-command-line-to-graphical-interfaces)”
*   “ [AI: First New UI Paradigm in 60 Years](https://www.nngroup.com/articles/ai-paradigm/) ”
*   “ [The Evolution of Programming UX/UI: From Command Line to Graphical Interfaces](https://bootcamp.uxdesign.cc/the-evolution-of-programming-ux-ui-from-command-line-to-graphical-interfaces-c45b95fae9ba) ”
*   “ [Designing for AI: beyond the chatbot](https://medium.com/user-experience-design-1/designing-for-ai-beyond-the-chatbot-5edc0efe84a3) ”
*   “ [Decoding The Future: The Evolution Of Intelligent Interfaces](https://uxdesign.cc/decoding-the-future-the-evolution-of-intelligent-interfaces-ec696ccc62cc) ”
*   “ [Prompts are Tiny Programs](https://balajis.com/p/prompts-are-tiny-programs) ”
*   [“People + AI guidebook](https://pair.withgoogle.com/guidebook) ”
*   [“Introduction to guidelines for human-AI interaction”](https://learn.microsoft.com/en-us/ai/guidelines-human-ai-interaction/)
