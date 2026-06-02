Title: 20+ GenAI UX patterns, examples and implementation tactics

URL Source: https://uxdesign.cc/20-genai-ux-patterns-examples-and-implementation-tactics-5b1868b7d4a1

Published Time: 2025-05-19T22:58:17Z

Markdown Content:
## A shared language for product teams to build usable, intelligent and safe GenAI experiences beyond just the model

[![Image 1: Sharang Sharma](https://miro.medium.com/v2/resize:fill:64:64/1*qPk4Z8BYN6qYzwBK6Frc7g.png)](https://medium.com/@Zeppeppers?source=post_page---byline--5b1868b7d4a1---------------------------------------)

19 min read

May 19, 2025

--

Press enter or click to view image in full size

Generative AI introduces a new way for humans to interact with systems by focusing on [**intent-based outcome specification**](https://www.nngroup.com/articles/ai-paradigm/). GenAI introduces novel challenges because its outputs are probabilistic, requires understanding of variability, memory, errors, hallucinations and malicious use which brings an [essential need to build principles and design patterns](https://dl.acm.org/doi/10.1145/3613904.3642466#sec-3) as described by IBM.

Moreover, any [AI product is a layered system](https://www.linkedin.com/posts/balajivi_most-people-still-cant-tell-the-difference-activity-7328857230278123520-52_N?utm_source=share&utm_medium=member_desktop&rcm=ACoAAAPfVd4BN_HlyZmqgQC5wP-wQBgEIDjdSxs) where LLM is just one ingredient and memory, orchestration, tool extensions, UX and agentic user-flows builds the real magic!

This article is my research and documentation of evolving GenAI design patterns that provide a **shared language**for product managers, data scientists, and interaction designers to create products that are human-centred, trustworthy and safe. By applying these patterns, we can bridge the gap between user needs, technical capabilities and product development process.

### **Here are 21 GenAI UX patterns**

1.   GenAI or no GenAI
2.   Convert user needs to data needs
3.   Augment or automate
4.   Define level of automation
5.   Progressive AI adoption
6.   Leverage mental models
7.   Convey product limits
8.   Display chain of thought (CoT)
9.   Leverage multiple outputs
10.   Provide data sources
11.   Convey model confidence
12.   Design for memory and recall
13.   Provide contextual input parameters
14.   Design for coPilot, co-Editing or partial automation
15.   Define user controls for Automation
16.   Design for user input error states
17.   Design for AI system error states
18.   Design to capture user feedback
19.   Design for model evaluation
20.   Design for AI safety guardrails
21.   Communicate data privacy and controls

Press enter or click to view image in full size

## 1. GenAI or no GenAI

Evaluate whether GenAI **improves UX or introduces complexity**. Often, heuristic-based (IF/Else) solutions are easier to build and maintain.

### **Scenarios when GenAI is beneficial**

*   Tasks that are open-ended, creative and augments user.

_E.g., writing prompts, summarizing notes, drafting replies._
*   Creating or transforming complex outputs (e.g., images, video, code).

_E.g., converting a sketch into website code._
*   Where structured UX fails to capture user intent.

### **Scenarios when GenAI should be avoided**

*   Outcomes that must be precise, auditable or deterministic. 

_E.g., Tax forms or legal contracts._
*   Users expect clear and consistent information.

_E.g. Open source software documentation_

### **How to use this pattern**

1.   Determine the **friction points** in the customer journey
2.   **Assess technology feasibility:**Determine if [AI can address the friction point](https://medium.com/google-design/human-centered-machine-learning-a770d10562cd). Evaluate scale, dataset availability, error risk assessment and economic ROI.
3.   **Validate user expectations: 

-**Determine if the AI solution erodes user expectations by evaluating whether the system augments human effort or replaces it entirely, as outlined in **pattern 3, Augment vs. automate**. 

- Determine if AI solution erodes **pattern 6, Mental models**

Press enter or click to view image in full size

## 2. Convert user needs to data needs

This pattern ensures GenAI development begins with user intent and data model required to achieve that. 

GenAI systems are only as good as the data they’re trained on. But real users don’t speak in rows and columns, they express goals, frustrations, and behaviours. If teams fail to translate user needs into structured, model-ready inputs, the**resulting system or product may optimise for the wrong outcomes and thus user churn.**

### How to use this pattern

1.   Collaborate as a cross-functional team of PMs, Product designers and Data Scientists and align on user problems worth solving.
2.   **Define user needs**by using **triangulated research:** Qualitative (Market Reports, Surveys or Questionnaires) + Quantitative (User Interviews, Observational studies) + Emergent (Product reviews, Social listening etc.) and **synthesising user insights using**[JTBD framework](https://jobs-to-be-done.com/the-jobs-to-be-done-canvas-f3f784ad6270), [Empathy Map](https://maze.co/blog/empathy-mapping/) to visualise user emotions and perspectives. [Value Proposition Canvas](https://www.strategyzer.com/library/the-value-proposition-canvas) to align user gains and pains with features
3.   [**Define data needs and documentation**](https://arxiv.org/pdf/2010.13561)by selecting a suitable data model, perform gap analysis and iteratively refine data model as needed. Once you **understand the _why_**, **translate it into the _what_ for the model.** What [features, labels, examples, and contexts](https://scale.com/guides/data-labeling-annotation-guide) will your AI model need to learn this behaviour? Use structured collaboration to figure out.

Press enter or click to view image in full size

## 3. Augment vs automate

One of the critical decisions in GenAI apps is **whether to fully automate a task or to augment human capability**. Use this pattern to to align with user intent and control preferences with the technology.

**Automation** is best for tasks users prefer to delegate especially when they are tedious, time-consuming or unsafe. _E.g.,_[_Intercom FinAI_](https://www.intercom.com/drlp/ai-agent?utm_source=google&utm_medium=sem&utm_campaign=20834473821&utm_term=fin+chatbot&utm_ad_collection=174923193757&utm_ad=733029438155&utm_geo=1007768&gad_source=1&gad_campaignid=20834473821&gbraid=0AAAAAoKeDyI53zLHiic9KeaA7hFOxJZ8Q&gclid=CjwKCAjwiezABhBZEiwAEbTPGNHNU2vunHHT6EjL8shU5Z-fPLTTcZfbIuAoAsyOKEGOqeLDsoKychoC_nEQAvD_BwE)_automatically summarizes long email threads into internal notes, saving time on repetitive, low-value tasks._

**Augmentation** enhances tasks users want to remain involved in by increasing efficiency, increase creativity and control. _E.g.,_[_Magenta Studio_](https://magenta.tensorflow.org/studio/ableton-live/)_in Abelton support creative controls to manipulate and create new music._

### How to use this pattern

1.   To select the best approach, evaluate user needs and expectations using research synthesis tools like [**empathy map**](https://maze.co/blog/empathy-mapping/) (visualise user emotions and perspectives) and [**value proposition canvas**](https://www.strategyzer.com/library/the-value-proposition-canvas) (to understand user gains and pains)
2.   Test and validate if the approach erodes user experience or enhances it.

Press enter or click to view image in full size

## 4. Define level of automation

In AI systems, automation refers to how much control is delegated to the **AI vs user.**This is a strategic UX pattern to decide degree of automation based upon user pain-point, context scenarios and expectation from the product.

### Levels of automation

1.   **No automation (AI assists but user decides)**

The AI system provides assistance and suggestions to the user but requires the user to make all the decisions. _E.g.,_[_Grammarly_](http://grammarly.com/)_highlights grammar issues but the user accepts or rejects corrections._
2.   **Partial automation/ co-pilot/ co-editor (AI acts with user oversight)**The AI initiates actions or generates content, but the user reviews or intervenes as needed. _E.g.,_[_GitHub Copilot_](https://github.com/features/copilot)_suggest code that developers can accept, modify, or ignore._
3.   **Full automation (AI acts independently)**The AI system performs tasks without user intervention, often based on predefined rules, tools and triggers. Full automation in GenAI are often referred to as [Agentic systems](https://www.ibm.com/think/topics/agentic-ai). _E.g.,_[_Ema_](http://ema.ai/)_can autonomously plan and execute multi-step tasks like researching competitors, generating a report and emailing it without user prompts or intervention at each step._

### How to use this pattern

1.   **Evaluate user pain point to be automated and risk involved:**Automating tasks is most effective when the associated risk is low without severe consequences in case of failure. **Low-risk tasks** such as sending automated reminders, promotional emails, filtering spam emails or processing routine customer queries can be automated with minimal downside while saving time and resources. **High-risk tasks** such as making medical diagnoses, sending business-critical emails, or executing financial trades requires careful oversight due to the potential for significant harm if errors occur.
2.   **Evaluate and design for particular automation level:** Evaluate if user pain point should fall under — _No Automation, Partial Automation or Full Automation_ based upon user expectations and goals.
3.   **Define user controls for automation (refer pattern 15)**

Press enter or click to view image in full size

## 5. Progressive GenAI adoption

When users first encounter a product built on new technology, they often wonder what the system can and can’t do, how it works and how they should interact with it.

This pattern offers _multi-dimensional strategy to_ help user onboard an AI product or feature, mitigate errors, aligns with user readiness to deliver an informed and human-centered UX.

### How to use this pattern

This pattern is a culmination of many other patterns

1.   **Focus on communicating benefits from the start:**Avoid diving into details about the technology and highlight how the AI brings new value.
2.   **Simplify the onboarding experience** Let users experience the system’s value before asking data-sharing preferences, give instant access to basic AI features first. Encourage users to sign up later to unlock advanced AI features or share more details. _E.g.,_[_Adobe FireFly_](http://firefly.adobe.com/)_progressively onboards user with basic to advance AI features_
3.   **Define level of automation (refer pattern 4)**and gradually increase autonomy or complexity.
4.   Provide explainability and trust by **designing for errors****(refer pattern 16 and 17).**
5.   **Communicate data privacy and controls (refer pattern 21)**to clearly convey how user data is collected, stored, processed and protected.

Press enter or click to view image in full size

## 6. Leverage mental models

[Mental models](https://www.nngroup.com/articles/mental-models/) help user predict how a system (web, application or other kind of product) will work and, therefore, influence how they interact with an interface. When a product aligns with a user’s existing mental models, it feels intuitive and easy to adopt. When it clashes, it can cause frustration, confusion, or abandonment​.

_E.g._[_Github Copilot builds upon developers’ mental models from traditional code autocomplete_](https://imaginet.com/2024/imaginets-experience-with-github-copilot/)_, easing the transition to AI-powered code suggestions_

_E.g._[_Adobe Photoshop builds upon the familiar approach of extending an image using rectangular controls_](https://www.adobe.com/products/photoshop/generative-expand.html)_by integrating its Generative Fill feature, which intelligently fills the newly created space._

### How to use this pattern

Identifying and build upon existing mental models by questioning

1.   What is the user journey and what is user trying to do?
2.   What mental models might already be in place?
3.   Does this product break any intuitive patterns of cause and effect?
4.   **Are you breaking an existing mental model?**If yes, clearly explain how and why. Good onboarding, microcopy, and visual cues can help bridge the gap.

Press enter or click to view image in full size

## 7. Convey product limits

This pattern involves clearly conveying what an AI model can and cannot do, including its knowledge boundaries, capabilities and limitations.

It is helpful to builds user trust, sets appropriate expectations, prevents misuse, and reduces frustration when the model fails or behaves unexpectedly.

### How to use this pattern

1.   **Explicitly state model limitations:** Show contextual cues for outdated knowledge or lack of real-time data. _E.g.,_ _Claude_ _states its knowledge cutoff when the question falls outside its knowledge domain_
2.   **Provide fallbacks or escalation options** when the model cannot provide a suitable output. _E.g.,_[_Amazon Rufus_](https://www.aboutamazon.com/news/retail/how-to-use-amazon-rufus)_when asked about something unrelated to shopping, says “it doesn’t have access to factual information and, I can only assists with shopping related questions and requests”_
3.   **Make limitations visible** in product marketing, onboarding, tooltips or response disclaimers.

Press enter or click to view image in full size

## 8. Display chain of thought (CoT)

In AI systems, [**chain-of-thought (CoT)**](https://www.ibm.com/think/topics/chain-of-thoughts)prompting technique enhances the model’s ability to solve complex problems by mimicking a more structured, step-by-step thought process like that of a human.

**CoT display**is a UX pattern that improves transparency by revealing how the AI arrived at its conclusions. This fosters **user trust, supports interpretability, and opens up space for user feedback** especially in high-stakes or ambiguous scenarios.

_E.g._, [**_Perplexity_**](https://www.perplexity.ai/)_enhances transparency by displaying its processing steps helping users understand the thoughtful process behind the answers._

_E.g._, [**_Khanmigo_**](http://khanmigo.ai/)_an AI Tutoring system guides students step-by-step through problems, mimicking human reasoning to enhance understanding and learning._

### How to use this pattern

1.   **Show status**like“researching” and “reasoning to communicate progress, reduce user uncertainty and wait times feel shorter.
2.   **Use progressive disclosure:**Start with a high-level summary, and allow users to expand details as needed.
3.   **Provide AI tooling transparency:** Clearly display external tools and data sources the AI uses to generate recommendations.
4.   **Show confidence & uncertainty:** Indicate AI confidence levels and highlight uncertainties when relevant.

Press enter or click to view image in full size

## 9. Leverage multiple outputs

GenAI can produce varied responses to the same input due to its probabilistic nature. This pattern exploits variability by presenting multiple outputs side by side. Showing diverse options helps users creatively explore, compare, refine or make better decisions that best aligns with their intent. _E.g.,_[_Google Gemini_](https://gemini.google.com/)_provides multiple options to help user explore, refine and make better decisions._

### How to use this pattern

1.   **Explain the purpose of variation:** Help users understand that differences across outputs are intentional and meant to offer choice.
2.   **Enable edits:** Let users rate, select, remix, or edit outputs seamlessly to shape outcomes and provide feedback. _E.g.,_[_Midjourney helps user adjust prompt and guide your variations and edits using remix_](https://docs.midjourney.com/hc/en-us/articles/32799074515213-Remix)

Press enter or click to view image in full size

## 10. Provide data sources

Articulating data sources in a GenAI application is essential for transparency, credibility and user trust. Clearly indicating where the AI derives its knowledge helps users assess the reliability of responses and avoid misinformation.

## Get Sharang Sharma’s stories in your inbox

Join Medium for free to get updates from this writer.

Remember me for faster sign in

This is especially important in **high stakes factual domains** like healthcare, finance or legal guidance where decisions must be based on verified data.

### How to use this pattern

1.   **Cite credible sources inline:**Display sources as footnotes, tooltips, or collapsible links. _E.g.,_[_NoteBookLM_](https://notebooklm.google/)_adds citations to its answers and links each answer directly to the part of user’s uploaded documents._
2.   **Disclose training data scope clearly:**For generative tools (text, images, code), offer a simple explanation of what data the model was trained on and what wasn’t included. _E.g.,_[_Adobe Firefly_](https://www.adobe.com/products/firefly.html)_discloses that its Generative Fill feature is_[_trained on stock imagery, openly licensed work and public domain content_](https://www.adobe.com/ai/overview/firefly/gen-ai-approach.html#:~:text=training%20Adobe%20Firefly.-,Adobe%20Firefly%20models%20are%20trained%20on%20a%20dataset%20of%20licensed,the%20use%20of%20the%20content.)_where the copyright has expired._
3.   **Provide source-level confidence:**In cases where multiple sources contribute, visually differentiate higher-confidence or more authoritative sources.

Press enter or click to view image in full size

## 11. Convey model confidence

AI-generated outputs are probabilistic and can vary in accuracy. Showing confidence scores communicates how certain the model is about its output. This helps users assess reliability and make better-informed decisions.

### How to use this pattern

1.   **Assess context and decision stakes**: Showing model confidence depends on the context and its impact on user decision-making. **In high-stakes scenarios** like healthcare, finance or legal advice, displaying confidence scores are crucial. However, in **low stake scenarios** like AI-generated art or storytelling confidence may not add much value and could even introduce unnecessary confusion.
2.   **Choose the right visualization:**If design research shows that displaying model confidence aids decision-making, the next step is to select the right visualization method. [Percentages, progress bars or verbal qualifiers](https://pair.withgoogle.com/chapter/explainability-trust/#section4) (“likely,” “uncertain”) can communicate confidence effectively. The apt visualisation method depends on the application’s use-case and user familiarity. _E.g.,_[_Grammarly_](https://www.grammarly.com/)_uses verbal qualifiers like “likely” to the content it generated along with the user_
3.   **Guide user action during low confidence scenarios**: Offer paths forward such as asking clarifying questions or offering alternative options.

Press enter or click to view image in full size

## 12. Design for memory and recall

[Memory and recall](https://teaching.berkeley.edu/resources/learn/memory-and-recall) is an important concept and design pattern that enables the AI product to store and reuse information from past interactions such as user preferences, feedback, goals or task history to improve continuity and context awareness.

*   **Enhances personalization**by remembering past choices or preferences
*   **Reduces user burden** by avoiding repeated input requests especially in multi-step or long-form tasks
*   **Supports complex tasks**like longitudinal workflows like in project planning, learning journeys by referencing or building on past progress.

Memory used to access information can be **ephemeral** (**short-term within a session)** or **persistent** (**long-term across sessions)** and may include conversational context, behavioural signals, or explicit inputs.

### How to use this pattern

1.   **Define the user context and choose memory type**Choose memory type like ephemeral or persistent or both based upon use case. A shopping assistant might track interactions in real time without needing to persist data for future sessions whereas personal assistants need long-term memory for personalization.
2.   **Use memory intelligently in user interactions**Build base prompts for LLM to recall and communicate information contextually _(E.g., “Last time you preferred a lighter tone. Should I continue with that?”)_.
3.   **Communicate transparency and provide controls**Clearly communicate what’s being saved and let users view, edit or delete stored memory. Make “delete memories” an accessible action. _E.g._[_ChatGPT offers extensive controls across it’s platform to view, update, or delete memories anytime_](https://openai.com/index/memory-and-new-controls-for-chatgpt/)_._

Press enter or click to view image in full size

## 13. Provide contextual input parameters

Contextual Input parameters enhance the user experience by streamlining user interactions and gets to user goal faster. By leveraging user-specific data, user preferences or past interactions or even data from other users who have similar preferences, GenAI system can tailor inputs and functionalities to better meet user intent and decision making.

### How to use this pattern

1.   **Leverage prior interactions:** Pre-fill inputs based on what the user has previously entered. **Refer****pattern 12, Memory and recall.**
2.   **Use auto complete or smart defaults:** As users type, offer intelligent, real-time suggestions derived from personal and global usage patterns. _E.g.,_[_Perplexity_](http://perplexity.ai/)_offers smart next query suggestions based on your current query thread._
3.   **Suggest interactive UI widgets:** Based upon system prediction, provide tailored input widgets like toasts, sliders, checkboxes to enhance user input. _E.g.,_[_ElevenLabs_](https://elevenlabs.io/?utm_source=google&utm_medium=cpc&utm_campaign=india_brandsearch_brand_english&utm_id=22349493305&utm_term=elevanlabs&utm_content=brand_-_brand_misspellings&gad_source=1&gad_campaignid=22349493305&gbraid=0AAAAAp9ksTFjCULq6zxDkEhMgs_R1Sbq_&gclid=Cj0KCQjw5ubABhDIARIsAHMighZdog3LFx9WDLNUN9CDV5VvbTrnYjip5Qa4ywaPWMSo26oupqKWUGgaAhkoEALw_wcB)_allows users to fine-tune voice generation settings by surfacing presets or defaults._

Press enter or click to view image in full size

## 14. Design for co-pilot / co-editing / partial automation

Co-pilot is an **augmentation pattern** where AI acts as a collaborative assistant, offering contextual and data-driven insights while the user remains in control. This design pattern is essential in domains like strategy, ideating, writing, designing or coding where outcomes are subjective, users have unique preferences or creative input from the user is critical.

Co-pilot speed up workflows, enhance creativity and reduce cognitive load but the **human retains authorship and final decision-making**.

### How to use this pattern

1.   **Embed inline assistance**: Place AI suggestions contextually so users can easily accept, reject or modify them. _E.g.,_[_Notion AI helps you draft, summarise and edit content_](https://www.notion.com/help/guides/notion-ai-for-docs)_while you control the final version._
2.   **Save user intent and creative direction**: Let users guide the AI with input like goals, tone, or examples, maintaining authorship and creative direction. _E.g.,_[_Jasper AI allows users to set brand voice and tone guidelines_](https://www.jasper.ai/brand-voice)_, helping structure AI output to better match the user’s intent._

Press enter or click to view image in full size

## 15. Design user controls for automation

Build UI-level mechanisms that let users manage or override automation based upon user goals, context scenarios or system failure states.

No system can anticipate all user contexts. Controls give users agency and keep trust intact even when the AI gets it wrong.

### How to use this pattern

1.   **Use progressive disclosure:**Start with minimal automation and allow users to opt into more complex or autonomous features over time. 

_E.g.,_[_Canva Magic Studio_ _starts with simple AI suggestions like text or image generation_](https://www.canva.com/en_in/magic/)_then gradually reveals advanced tools like Magic Write, AI video scenes and brand voice customisation._
2.   **Give users automation controls:** UI controls like toggles, sliders, or rule-based settings to let users choose when and how automation can be controlled. _E.g.,_[_Gmail lets users disable Smart Compose._](https://zapier.com/blog/turn-off-smart-compose/)
3.   **Design for automation error recovery:**Give users correction when AI fails ([false positives/negatives](https://en.wikipedia.org/wiki/False_positives_and_false_negatives)). Add manual override, undo, or escalate options to human support. _E.g.,_[_GitHub Copilot suggests code inline, but developers can easily reject, modify or undo suggestions when output is off._](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot)

Press enter or click to view image in full size

## 16. Design for user input error states

GenAI systems often rely on interpreting human input. When users provide ambiguous, incomplete or erroneous information, the AI may misunderstand their intent or produce low-quality outputs.

Input errors often reflect a**mismatch between user expectations and system understanding**. Addressing these gracefully is essential to maintain trust and ensure smooth interaction.

### How to use this pattern

1.   **Handle typos with grace**: Use spell-checking or [fuzzy matching](https://dataladder.com/fuzzy-matching-101/) to auto-correct common input errors when confidence is high (_e.g., >80%_), and subtly surface corrections (_“Showing results for…”_).
2.   **Ask clarifying questions**: When input is too vague or has multiple interpretations, prompt the user to provide missing context. In Conversation Design, these types of errors occur when the intent is defined but the entity is not clear. Know more about [entity and intent](https://www.verloop.io/blog/intents-and-entities/). _E.g., ChatGPT when given low-context prompts like “What’s the capital?”, it asks follow-up questions rather than guessing._
3.   **Support quick correction**: Make it easy for users to edit or override your interpretation. _E.g., ChatGPT displays an edit button beside submitted prompts, enabling users to revise their input_

Press enter or click to view image in full size

## 17. Design for AI system error states

GenAI outputs are inherently probabilistic and subject to errors ranging from hallucinations and bias to contextual misalignments.

Unlike traditional systems, GenAI error states are hard to predict. Designing for these states requires transparency, recovery mechanisms and user agency. A well-designed error state can help users understand AI system boundaries and regain control.

A [Confusion matrix](https://en.wikipedia.org/wiki/Confusion_matrix) helps analyse AI system errors and provides insight into how well the model is performing by showing the counts of 

- **True positives** (correctly identifying a positive case) 

- **False positives** (incorrectly identifying a positive case) 

- **True negatives** (correctly identifying a negative case)

- **False negatives**(failing to identify a negative case)

### Scenarios of AI errors and failure states

1.   **System failure (wrong output)**

False positives or false negatives occur due to **poor data, biases or model hallucinations**. _E.g., Citibank financial fraud system displays a message “Unusual transaction. Your card is blocked. If it was you, please verify your identity”_
2.   **System limitation errors (no output)**

True negatives occur due to **untrained use cases or gaps in knowledge**. _E.g., when an ODQA system is given a user input outside the trained dataset, throws the following error “Sorry, we don’t have enough information. Please try a different query!”_
3.   **Contextual errors (misunderstood output)**

True positives that **confuse users due to poor explanations** or conflicts 

with user expectations comes under contextual errors. _E.g., when user logs in from a new device, gets locked out. AI responds: “Your login attempt was flagged for suspicious activity”_

### How to use this pattern

1.   **Communicate AI errors for various scenarios**: Use phrases like 

“This may not be accurate”, “This seems like…” or surface confidence levels to help calibrate trust.
2.   Use pattern **convey model confidence** for low confidence outputs.
3.   **Offer error recovery**: Incase of System failure or Contextual errors, provide clear paths to override, retry or escalate the issue. 

_E.g., Use way forwards like “Try a different query,” or “Let me refine that.” or “Contact Support”._
4.   **Enable user feedback**: Make it easy to report hallucinations or incorrect outputs. Read more about **pattern****19. Design to capture user feedback**.

Press enter or click to view image in full size

## 18. Design to capture user feedback

Real-world alignment needs direct user feedback to improve the model and thus the product. As people interact with AI systems, their behaviours shape and influence the outputs they receive in the future. Thus, creating a continuous feedback loop where both the system and user behaviour adapt over time. _E.g.,_[_ChatGPT_](http://chatgpt.com/)_uses Reaction buttons and Comment boxes to collect user feedback._

### How to use this pattern

1.   **Account for implicit feedback**: Capture user actions such as skips, dismissals, edits, or interaction frequency. These passive signals provide valuable behavioral cues that can tune recommendations or surface patterns of disinterest.
2.   **Ask for explicit feedback:** Collect direct user input through thumbs-up/down, NPS rating widgets or quick surveys after actions. Use this to improve both model behavior and product fit.
3.   **Communicate how feedback is used:** Let users know how their feedback shapes future experiences. This increases trust and encourages ongoing contribution.

Press enter or click to view image in full size

## 19. Design for model evaluation

Robust GenAI models require continuous evaluation during training as well as post-deployment. Evaluation ensures the model performs as intended, identify errors and hallucinations and aligns with user goals especially in high-stakes domains.

### How to use this pattern

There are [three key evaluation methods](https://www.lennysnewsletter.com/p/beyond-vibe-checks-a-pms-complete) to improve ML systems.

1.   **LLM based evaluations (LLM-as-a-judge)**A separate language model acts as an automated judge. It can grade responses, explain its reasoning and assign labels like helpful/harmful or correct/incorrect.

_E.g.,_[_Amazon Bedrock uses the LLM-as-a-Judge approach_](https://aws.amazon.com/blogs/machine-learning/llm-as-a-judge-on-amazon-bedrock-model-evaluation/)_to evaluate AI model outputs.A separate trusted LLM, like Claude 3 or Amazon Titan, automatically reviews and rates responses based on helpfulness, accuracy, relevance, and safety. For instance, two AI-generated replies to the same prompt are compared, and the judge model selects the better one.This automation reduces evaluation costs by up to 98% and speeds up model selection without relying on slow, expensive human reviews._
2.   **Enable code-based evaluations:**For structured tasks, use test suites or known outputs to validate model performance, especially for data processing, generation, or retrieval.
3.   **Capture human evaluation:**Integrate real-time UI mechanisms for users to label outputs as helpful, harmful, incorrect, or unclear. Read more about it in **pattern****19. Design to capture user feedback**
4.   **A hybrid approach** of LLM-as-a-judge and human evaluation [drastically boost accuracy to 99%](https://sanand0.github.io/llmevals/double-checking/).

Press enter or click to view image in full size

## 20. Design for AI guardrails

Design for [AI guardrails means building practises and principles in GenAI models to minimise harm, misinformation, toxic behaviour and biases](https://www.ibm.com/think/topics/ai-safety). It is a critical consideration to

*   **Protect users and children from**harmful language, made-up facts, biases or false information.
*   **Build trust and adoption:** When users know the system avoids hate speech and misinformation, they feel safer and show willingness to use it often.
*   **Ethical compliance:** New rules like the [EU AI act](https://www.europarl.europa.eu/topics/en/article/20230601STO93804/eu-ai-act-first-regulation-on-artificial-intelligence) demand safe AI design. Teams must meet these standards to stay legal and socially responsible.

### How to use this pattern

1.   **Analyse and guide user inputs:** If a prompt could lead to unsafe or sensitive content, guide users towards safer interactions. _E.g._,_when_[_Miko robot_](http://miko.ai/)_comes across profanity, it answers“I am not allowed to entertain such language”_
2.   **Filter outputs and moderate content:** Use [real-time moderation](https://openai.com/index/upgrading-the-moderation-api-with-our-new-multimodal-moderation-model/) to detect and filter potentially harmful AI outputs, blocking or reframing them before they’re shown to the user. _E.g._,_show a note like: “This response was modified to follow our safety guidelines._
3.   **Use pro-active warnings:** Subtly notify users when they approach sensitive or high stakes information. _E.g._,_“This is informational advice and not a substitute for medical guidance.”_
4.   **Create strong user feedback:** Make it easy for users to report unsafe, biased or hallucinated outputs to directly improve the AI over time through active learning loops. _E.g.,_[_Instagram provides in-app option_](https://help.instagram.com/2442045389198631/)_for users to report harm, bias or misinformation._
5.   **Cross-validate critical information:** For high-stakes domains (like healthcare, law, finance), back up AI-generated outputs with trusted databases to catch hallucinations. **Refer pattern 10,****Provide data sources.**

Press enter or click to view image in full size

## 21. Communicate data privacy and controls

This pattern ensures GenAI applications clearly convey how user data is collected, stored, processed and protected.

GenAI systems often rely on sensitive, contextual, or behavioral data. Mishandling this data can lead to user distrust, legal risk or unintended misuse. Clear communication around privacy safeguards helps users feel safe, respected and in control. _E.g.,_[_Slack AI clearly communicates_](https://slack.com/intl/en-in/blog/news/how-slack-protects-your-data-when-using-machine-learning-and-ai)_that customer data remains owned and controlled by the customer and is not used to train Slack’s or any third-party AI models_

### How to use this pattern

1.   **Show transparency:**When a GenAI feature accesses user data, display explanation of what’s being accessed and why.
2.   **Design opt-in and opt-out flows:**Allow users to easily toggle data sharing preferences.
3.   **Enable data review and deletion:**Allow users to view, download or delete their data history giving them ongoing control.

## Conclusion

These GenAI UX patterns are a starting point and represent the outcome of months of research, shaped directly and indirectly with insights from notable designers, researchers, and technologists across leading tech companies and the broader AI communites across Medium and Linkedin. 

I have done my best to cite and acknowledge contributors along the way but I’m sure I’ve missed many. If you see something that should be credited or expanded, please reach out.

Moreover, these patterns are meant to grow and evolve as we learn more about creating AI that’s trustworthy and puts people first. If you’re a designer, researcher, or builder working with AI, take these patterns, challenge them, remix them and contribute your own. Also, please let me know in comments about your suggestions. If you would like to collaborate with me to further refine this, please reach out to me.
