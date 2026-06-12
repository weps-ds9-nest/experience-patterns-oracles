# The Ux Of Ai

## Start with the user

The technology you use should be guided by the user experience you want to achieve. Instead of diving headfirst into algorithms, think about how people do the task today. Figure out what’s valuable, and how you can enhance the experience. Along the way, you might find a solution without AI that is easier to build or understand. The same goes for marketing: Talk about the user benefits, not the AI technology.

* * *

[Human-Centered Machine Learning](https://medium.com/google-design/human-centered-machine-learning-a770d10562cd)

## Set the right expectations

Since everything from self-driving cars to smoothie makers calls itself AI, expectations for what that means are all over the place. People will expect your AI to be both smarter and dumber than it is. Try to explain in plain language what your AI can do, and where its limitations are. Generally, under-promising and over-delivering is a good way to build trust. Over time, users will learn how to best integrate the AI into their workflow.

* * *

[How to Meet User Expectations for Artificial Intelligence](https://medium.com/salesforce-ux/how-to-meet-user-expectations-for-artificial-intelligence-a51d3c82af6)[Don’t Call AI “Magic”](https://points.datasociety.net/dont-call-ai-magic-142da16db408)

## Explain the results

AI is only useful if we understand its decisions. Ideally, the user should be able to trace any result back to the supporting data points. If that’s not possible, explain the basic operation of the algorithm. Lay out which data sources you use, and which qualities the AI focuses on. If you aggregate data from multiple sources, break them down to let the user reproduce the result. This information should be available as part of the user flow through a consistent interface.

* * *

[Interpretable Machine Learning](https://christophm.github.io/interpretable-ml-book/)[The Building Blocks of Interpretability](https://distill.pub/2018/building-blocks/)[The Dark Secret at the Heart of AI](https://www.technologyreview.com/s/604087/the-dark-secret-at-the-heart-of-ai)[Machine Learning is Very Much a UX Problem](https://medium.com/@yaelg/product-manager-guide-part-5-machine-learning-is-very-much-a-user-experience-ux-problem-82ad312678ae)

## Communicate your confidence

Users rely on your AI to make decisions. They have to understand the quality of results to trust them. If the confidence of your algorithm varies, indicate the confidence for each result. You could show a percentage, or try a more abstract visualisation (e.g. star ratings, colored indicators). For results that have multiple parts, break down the confidence for each. Additionally, consider showing multiple results ordered by confidence, and giving the user the final say.

* * *

[Design in the Era of the Algorithm](https://bigmedium.com/speaking/design-in-the-era-of-the-algorithm.html)

## Degrade gracefully

Designing for AI means designing for many different outcomes. When the input is clear and the answer certain, you don’t want the user to hesitate. Less confident results need to be presented differently. You could start by toning down the boldness of your visual design, or altering the layout and copy that frames the result. Above all, don’t be afraid to say when you don’t have an answer. It’s okay for an AI to fail, as long as you design for it.

* * *

[Systems Smart Enough To Know When They’re Not Smart Enough](https://bigmedium.com/ideas/systems-smart-enough-to-know-theyre-not-smart-enough.html)

## Know what not to automate

Not everything should be automated. Most tasks have some parts that are a good fit for AI, and ones that should be left to humans. Reasons not to use AI could be that the task requires abilities that are unique to humans (e.g. understanding emotions or motivations), that there is an intrinsic value to the manual process (e.g. it provides dignity or enjoyment), that it requires subjective evaluation (e.g. ethical or moral decisions), or that it has far-reaching consequences for an affected party.

* * *

[Applications of Machine Learning for Designers](https://www.smashingmagazine.com/2017/04/applications-machine-learning-designers/)[Design in the Era of the Algorithm](https://bigmedium.com/speaking/design-in-the-era-of-the-algorithm.html)

## Keep the user in control

Instead of an AI that replaces humans, think of ways to amplify and augment our abilities. Don’t turn us into spectators. Ultimately, the user should be the one in control. That means being able to intervene, provide feedback, reverse bad actions and reward good ones. AI is more empowering when it works with the user, not for the user.

* * *

[Human-centered Machine Learning: a Machine-in-the-loop Approach](https://medium.com/@ChenhaoTan/human-centered-machine-learning-a-machine-in-the-loop-approach-ed024db34fe7)[The incredible inventions of intuitive AI](https://www.ted.com/talks/maurice_conti_the_incredible_inventions_of_intuitive_ai)[Using Artificial Intelligence to Augment Human Intelligence](https://distill.pub/2017/aia/)

## Build trust over time

Be careful when introducing your AI to new users. Make sure it doesn’t require much existing personal data. Lean towards making suggestions instead of decisions. As your AI gets to know the user, you can automate more and ask for permission less. This gives the user time to understand how the AI works, and your algorithms can gradually learn along with them.

* * *

[UX for AI: Building Trust as a Design Challenge](https://experience.sap.com/skillup/ux-for-ai-building-trust-as-a-design-challenge/)

## Help your users grow

Over time, the AI will have to adapt to changing behaviour of your users. This happens for each user, but also for your user base as a whole. Even the values and needs of our society change over the years. If your AI is stuck with what it has learned in the past, it will hinder progress. Even ideas that are universal today might not be part of the future we are working towards. Your AI should aim ahead of the curve, without forcing your own values on users.

## Balance predictability and serendipity

Any personalised AI adopts the user’s bias. This is great for tasks that require predictability, where you need consistently effective results. But for other tasks, it limits our curiosity. It constrains us to options inside our comfort zone. Part of being humans is following your intuition off the beaten path,even if it might lead nowhere. You can tweak your algorithms to find the right balance, and maybe even design your interface to offer ways to escape the filter bubble.

* * *

[Predictably Smart](https://design.google/library/predictably-smart/)

## Escape the personality cult

AI should feel at home with the rest of your product. Don’t try to make features feel “more human” through a witty personality. This will only confuse your users and set expectations you can’t meet. Instead, stick with your existing brand values.

* * *

[Robots that act like humans are a waste of time](https://thenextweb.com/artificial-intelligence/2018/01/24/robots-that-act-like-humans-are-a-waste-of-time/)

## Avoid chatbots for single tasks

Chatbots are inherently limited in their capabilities, but they dress up as if they aren’t. The resulting uncertainty can frustrate or alienate users. In many cases, a few forms fields and buttons will be a better experience.

* * *

[Bots won’t replace apps. Better apps will replace apps.](http://dangrover.com/blog/2016/04/20/bots-wont-replace-apps.html)[Principles of bot design](https://www.intercom.com/blog/principles-bot-design/)

## Prototype with real data and fake AI

Using real user data for early prototypes helps you build your machine learning model on the right assumptions. You can use the [wizard-of-oz](https://en.wikipedia.org/wiki/Wizard_of_Oz_experiment) method to get the user experience right before actually building the AI.

* * *

[The UX of AI (Google Design)](https://design.google/library/ux-ai/)

## Work with everyone

AI impacts everyone. All of us should be part of the discussion of what we want AI to be. This means working with a diverse team. AI is shaped by the experiences and values of the people that make it. As we are still figuring out the foundations of AI design, collaboration is more important than ever. Data analysts, researchers, developers, marketers and designers all need to work together to build a cohesive product. Domain experts should be deeply involved in the design of both the ML model and the user interface. It’s your job to translate their expertise into a shared understanding that your team can build on.

* * *

[Fair Is Not the Default](https://design.google/library/fair-not-default/)[Why AI Is Still Waiting For Its Ethics Transplant](https://www.wired.com/story/why-ai-is-still-waiting-for-its-ethics-transplant/)

Transparency extends beyond the product. Tell users how their data is gathered, handled and processed. Explain the choices you made when developing the model and designing the interface. Consider open-sourcing the AI of systems that make critical decisions. Sharing insights with your users and the community builds trust and goodwill.

## Avoid collecting user data

Users own their data. Don’t collect it if you don’t need to (use on-device ML instead). When the user controls their data, they can decide what the AI learns. If you do need to collect data, explicitly ask for permission and explain what you need the data for. Once user data is on your servers, you have the responsibility to protect it. Determine exactly which data you need, how long you need to keep it and who needs access to it.

* * *

[Guide to the General Data Protection Regulation](https://ico.org.uk/for-organisations/guide-to-the-general-data-protection-regulation-gdpr/)

## Related
[Add wiki-links manually or run update_wikilinks.py]