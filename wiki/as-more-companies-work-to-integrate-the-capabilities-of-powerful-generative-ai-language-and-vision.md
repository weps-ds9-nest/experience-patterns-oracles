# As more companies work to integrate the capabilities of powerful generative AI language and vision models into new and existing software, high-level interaction patterns are emerging. I've personally found these distinct approaches to AI integration useful for talking with folks about what might work for their specific products and use cases.

As more companies work to integrate the capabilities of powerful generative AI language and vision models into new and existing software, high-level interaction patterns are emerging. I've personally found these distinct approaches to AI integration useful for talking with folks about what might work for their specific products and use cases.

In the first approach, the primary interface affordance is an input that directly (for the most part) instructs an AI model(s). In this paradigm, people are authoring prompts that result in text, image, video, etc. generation. These prompts can be sequential, iterative, or un-related. Marquee examples are OpenAI's [ChatGPT](https://openai.com/blog/chatgpt) interface or Midjourney's [use of Discord](https://docs.midjourney.com/docs/midjourney-discord) as an input mechanism. Since there are few, if any, UI affordances to guide people these systems need to respond to a very wide range of instructions. Otherwise people get frustrated with their primarily hidden (to the user) limitations.

[![Image 1: UI paradigm where controlling an AI model is the primary interaction](https://static.lukew.com/ai_ui1_2x.png)](https://static.lukew.com/ai_ui1_2x.png)

The second approach doesn't include any UI elements for directly controlling the output of AI models. In other words, there's no input fields for prompt construction. Instead instructions for AI models are created behind the scenes as people go about using application-specific UI elements. People using these systems could be completely unaware an AI model is responsible for the output they see. This approach is similar to YouTube's use of AI models (more machine learning than generative) [for video recommendations](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/45530.pdf).

[![Image 2: UI paradigm where AI models work behind the scenes to control the output of an interface](https://static.lukew.com/ai_ui4_2x.png)](https://static.lukew.com/ai_ui4_2x.png)

The third approach is application specific UI with AI assistance. Here people can construct prompts through a combination of application-specific UI and direct model instructions. These could be additional controls that generate portions of those instructions in the background. Or the ability to directly guide prompt construction through the inclusion or exclusion of content within the application. Examples of this pattern are Microsoft's [Copilot suite](https://www.microsoft.com/en-us/microsoft-365/blog/2023/03/16/introducing-microsoft-365-copilot-a-whole-new-way-to-work/) of products for GitHub, Office, and Windows.

[![Image 3: AI models in software](https://static.lukew.com/ai_ui2_2x.png)](https://static.lukew.com/ai_ui2_2x.png)

These entry points for AI assistance don't have to be side panels, they could be overlays, modals, inline menus and more. What they have in common, however, is that they supplement application specific UIs instead of completely replacing them.

[![Image 4: AI models in software](https://static.lukew.com/ai_ui3_2x.png)](https://static.lukew.com/ai_ui3_2x.png)

Actual implementations of any of these patterns are likely to blur the lines between them. For instance, even when the only UI interface is an input for prompt construction, the system may append or alter people's input behind the scenes to deliver better results. Or an AI assistance layer might primarily serve as an input for controlling the UI of an application instead of working alongside it. Despite that, I've still found these three high-level approaches to be helpful in thinking through where and how AI models are surfaced in software applications.

## Related
[Add wiki-links manually or run update_wikilinks.py]