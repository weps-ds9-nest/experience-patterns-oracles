# Press enter or click to view image in full size

Press enter or click to view image in full size

![Image 1](https://miro.medium.com/v2/resize:fit:700/1*z4c8nlbY6bqOIqDwfHb5mA.png)

[![Image 2: Nick Babich](https://miro.medium.com/v2/resize:fill:64:64/1*DvFE_85Tc3fObRgRww9ZTQ.jpeg)](https://medium.com/@101?source=post_page---byline--633320d0dfea---------------------------------------)

6 min read

Oct 13, 2025

Service design is evolving and we’re quickly moving past static screens and pages toward dynamic, contextual experiences. In my previous article, _Service Design in the Era of AI Agents_, I discussed this evolution in detail.

After reading it, many people reached out with one specific question: _what exact design patterns will we use for GenUI apps?_ In this article, I decided to discuss specific foundational patterns for GenUI apps.

## What is GenUI

GenUI (short for Generative User Interface) is a new paradigm in interface design where AI dynamically generates and adapts user interface elements in real time based on the user’s context, goals, and behavior, instead of designers predefining every layout and interaction manually.

Despite that a concept of a GenUI system sounds fancy, in reality its possible to break it down into 3 foundational elements:

1.   **LLMs models** interpret user goals. This of it as AI ‘brain’ that analyzes user input, behavior, and provided data to understand the context.
2.   **Design systems + tokens.**AI uses pre-defined building blocks such as components, styles, accessibility rules when interacting with users.
3.   **Real-time rendering engines.**AI pairs context with design system elements to assemble layouts dynamically.

## Design patterns for GenUI

Design patterns are _reusable_ solutions we can apply when dealing with specific design challenges. Each pattern includes the **problem** → **solution** → **key guidelines**, allowing you to plug them directly into specs or design systems.

## Foundational patterns to use

Below, I list 6 foundational patterns that can be applied when designing GenUI products. I use ChatGPT’s semi-GenUI to visualize some of them.

### **1) Intent capture**

We use this pattern when the system needs to infer what problem the user wants to solve at the moment. To capture user intent, we combine explicit goal capture (_analyze a prompt submitted by the user_) with analysis of recent intents.

For simple cases, users can express their intent in plain text. For example,

a user provides a prompt such as “_plan a vacation in California_” which gives the LLM a clear idea of the user’s goal.

![Image 3](https://miro.medium.com/v2/resize:fit:444/1*ZrTx6fzRnDmRlZqhC3Fm_Q.png)

User prompt gives LLM a clear idea that the user is planning a vacation in California.

We also keep a visible “_current intent_” text for the user to reassure that the system understands them correctly.

![Image 4](https://miro.medium.com/v2/resize:fit:440/1*CdAMPTI2TzJwA7HcySrZfQ.png)

ChatGPT’s left-hand panel with chat names also reflects this — each chat name gives the user a clear idea of the intention the LLM has for that session.

### **2) Undo / Time-travel**

One of the biggest challenges of many GenUI interfaces is the inability to move backward. Once users provide input, they often don’t know how to undo an action. Even when an Undo feature exists, users may not explore it if it’s not visible or intuitive.

We can address this in two ways:

**A: Explicit prompt editing.**Allow users to edit previously submitted prompts. This gives them flexibility to change the direction of the AI’s response.

Press enter or click to view image in full size

![Image 5](https://miro.medium.com/v2/resize:fit:700/1*r8N--bKCoRCO4I2jwXxGVA.png)

Explicit prompt editing. User can hover of the prompt they’ve submitted and edit it.

**B: History with named checkpoints.**Think of checkpoints as system snapshots (including context, memory, and timestamps) that users can return to. This pattern works especially well for complex tasks requiring multiple paths or iterations.

### **3) Progressive disclosure of AI**

GenUI systems are prone to creating extra cognitive overload. When a system offers too much content or too many options, users can experience decision paralysis.

## Get Nick Babich’s stories in your inbox

Join Medium for free to get updates from this writer.

Remember me for faster sign in

To prevent this, start simple and reveal advanced content or options on demand — a principle borrowed from traditional UX patterns like “More options” links or expandable drawers. For example, when a user asks AI to plan their vacation, the system can create a simple plan for them.

Press enter or click to view image in full size

![Image 6](https://miro.medium.com/v2/resize:fit:700/1*xWLzVe7WsWTYFiLmxYJgyg.png)

ChatGPT responds to the prompt “plan vacation in California”

and at the end of the ouput ask clarification question(s) about the type of vacation they want to have. This helps both prevent the system from offering too much content / too many different options right away.

Press enter or click to view image in full size

![Image 7](https://miro.medium.com/v2/resize:fit:700/1*MxcAMMOgSU_2AU3TPY71jw.png)

Clarification question that AI system asks.

### 4) **Hints / contextual actions**

GenUI systems powered by AI can perform a wide range of tasks — but users often don’t know what the AI can do.

To guide users effectively, offer contextual actions near the prompt area. For instance, after generating a travel plan, you might display:

> _“Calculate the budget for this trip”_

This pattern helps users trigger relevant sub-tasks within their current context.

As a rule of thumb, limit contextual actions to 3–5, and rotate them dynamically based on telemetry or user behavior.

Press enter or click to view image in full size

![Image 8](https://miro.medium.com/v2/resize:fit:700/1*meqWHsXqs5n9iNDQ5WxX4w.png)

Prompt field with contextual recommendations.

### 5) **Stable anchors / Fluid details**

If every part of the UI is dynamically generated by AI, users can easily lose orientation. That’s why even advanced GenUI apps keep a few key static elements, such as a navigation bar or a “_New chat_” button, fixed, while allowing secondary elements to morph.

This segregation of static and dynamic areas helps users maintain a sense of control. Even if the interface changes unexpectedly, users always know how to restart or reorient themselves.

### **6) Harm prevention**

While AI engines offer great versatility, another key design consideration is preventing harmful or accidental actions.

For example, in a GenUI-based travel booking service, you must prevent users from accidentally booking the wrong trip with a single click.

Always use dual control for critical actions — a pattern known as “Propose → Verify.” In traditional UIs we have a pattern known as “_Are you sure_.” This approach prompts users to pause and confirm before proceeding, reducing the risk of irreversible mistakes.

## Foundational patterns you should be careful

### Stable anchors

Once you define where your stable anchors are located, keep them consistent. This helps users build muscle memory, allowing them to rely on past interactions to navigate confidently.

### **Feedback loop**

Many GenUI apps use a simple mechanism to train their LLMs — a feedback loop. After generating an output, the system often displays options such as 👍 _Good_ or 👎 _Bad_ for users to rate the response.

While this seems like a reasonable solution for improving intent understanding, it has a major flaw: users frequently ignore it.

As a result, these buttons can become visual clutter rather than a meaningful feedback channel.

Press enter or click to view image in full size

![Image 9](https://miro.medium.com/v2/resize:fit:700/1*4zuC19mfLLyCQiJoG2yGGw.png)

Another common mistake is asking for feedback after every single interaction. When this happens, users begin to perceive the feedback loop as visual noise, and it quickly turns from _Feedback Loop_ to _Feedback Spam_.

## Related
[Add wiki-links manually or run update_wikilinks.py]