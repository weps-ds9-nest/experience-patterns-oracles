# [](https://wattenberger.com/)

[](https://wattenberger.com/)
## Why Chatbots Are Not the Future

Last night, over wine and seafood, the inevitable happened...

Someone mentioned ChatGPT.

I had no choice but to start into an unfiltered, no-holds-barred rant about chatbot interfaces.

Unfortunately for the countless hapless people I've talked to in the past few months, this was inexorable. Ever since ChatGPT exploded in popularity, my inner designer has been bursting at the seams.

To save future acquaintances, I come to you today: because you've volunteered to be here with me, can we please discuss a few reasons chatbots are not the future of interfaces.

## Text inputs have no affordances

When I go up the mountain to ask the ChatGPT oracle a question, I am met with a blank face. What does this oracle know? How should I ask my question? And when it responds, it is endlessly confident. I can't tell whether or not it actually understand my question or where this information came from.

**Good tools make it clear how they should be used.** And more importantly, how they should _not_ be used. If we think about a good pair of gloves, it's immediately obvious how we should use them. They're hand-shaped! We put them on our hands. And the specific material tells us more: metal mesh gloves are for preventing physical harm, rubber gloves are for preventing chemical harm, and leather gloves are for looking cool on a motorcycle.

Compare that to looking at a typical chat interface. The only clue we receive is that we should type characters into the textbox. The interface looks the same as a Google search box, a login form, and a credit card field.

Of course, users can learn over time what prompts work well and which don't, but the burden to learn what works still lies with every single user. When it could instead be baked into the interface.

## Prompts are just a pile of context

LLMs make it too easy: we send them text and they send back text. The easy solution is to slap a shallow wrapper on top and call it a day. But pretty soon, we're going to get sick of typing all the time. If you think about it, **everything you put in a prompt is a piece of context**.

Let's look at a simple example from [Awesome ChatGPT Prompts](https://github.com/f/awesome-chatgpt-prompts):

Who are you?

 I want you to act as a dream interpreter. 
How should you respond?

 I will give you descriptions of my dreams, and you will provide interpretations based on the symbols and themes present in the dream. 
How should you not respond?

 Do not provide personal opinions or assumptions about the dreamer. 
What type of information do I want?

 Provide only factual interpretations based on the information given. 
How should we start?

 My first dream is about being chased by a giant spider.

How can we make it easier for users to provide all of this context?

I'm exploring an AI writing interface focused on making you a better writer. Mimicking a good writing tutor, it suggests improvements to your content. "Try smoothing out this transition" or "add tangible examples here".

But not all writers have the same goals! Not does all content have the same audience or tone. To better tailor the responses, I added a few controls for the user to specify their use case: _What type of writing is this, who are they, what should it feel like, who are their inspirations?_

![Image 1: PenPal interface](https://wattenberger.com/thoughts/chatbots/ai-writing.png)

Even if we're determined to stick with a chat interface, we can make things easier for users. Recently, my team shipped a prototype named [Copilot for Docs](https://githubnext.com/projects/copilot-for-docs/), exploring ways to make technical documentation easier for developers to use.

I think of it in two parts: _finding the most relevant information to a user's question_ and _synthesizing an answer using that information_. When we synthesize an answer, we have a chance to tailor the response to the specific question-asker. As a rough first exploration with this idea, we added a few sliders:

![Image 2: Copilot for docs interface](https://wattenberger.com/thoughts/chatbots/docs.png)

A new developer doesn't want the same responses as an experienced one, or someone who's new to the library, or someone who's in a rush. (Get ready for a future rant: static text is dead.) As the creators of [Copilot for Docs](https://githubnext.com/projects/copilot-for-docs/), we have a good idea of what the tool is best at and what kinds of information will lead to the most helpful responses. Let's take the time to bake as much information into the interface as possible instead of making users hack it into each of their questions.

## Responses are isolated

Natural language is great at rough direction: teleport me to the right neighborhood. But once ChatGPT has responded, how do I get it to take me to the right house?

Say you ask ChatGPT to help improve your writing. Let's use this paragraph from [Walden](https://www.gutenberg.org/files/205/205-h/205-h.htm) as an example:

I have thought that Walden Pond would be a good place for business, not solely on account of the railroad and the ice trade; it offers advantages which it may not be good policy to divulge; it is a good port and a good foundation. No Neva marshes to be filled; though you must every where build on piles of your own driving. It is said that a flood-tide, with a westerly wind, and ice in the Neva, would sweep St. Petersburg from the face of the earth.

We ask ChatGPT to "make this text better". It responds:

I believe that Walden Pond presents a promising opportunity for business, not just because of its proximity to the railroad and the ice trade, but also due to other undisclosed advantages. It boasts excellent port facilities and a solid foundation, without the need to undertake extensive marsh filling like the Neva marshes. However, one should exercise caution in divulging all the unique benefits it offers. Furthermore, it is worth noting that St. Petersburg faces the risk of being devastated by a flood-tide, coupled with a westerly wind and ice in the Neva.

Next, we ask it to "rewrite this text with more active language". It responds:

I envision Walden Pond as an exceptional business destination, not solely due to the railroad and ice trade, but for its undisclosed advantages. It boasts a superb port and a solid foundation, eliminating the need for extensive marsh filling like the Neva marshes. However, one must exercise discretion in revealing its unique benefits. Additionally, it's crucial to acknowledge the peril St. Petersburg faces: a flood-tide, a westerly wind, and ice in the Neva could obliterate the city from existence.

Even with this fairly short example, it's laborious to figure out what concretely has changed. We're forced to scroll back and forth between responses, reading them line by line.

As someone who is always thinking about how AI can help edit code or prose, I can't help but see the inability to have a "working buffer" as a complete non-starter.

## The implementation—evaluation loop

When a painter is working, there are two distinct actions: up close, smooshing paint around on the canvas and stepping back to evaluate and plan. These two modes (implementing and evaluating) are present in any craft: programming, writing, you name it.

**Good tools let the user choose when to switch between implementation and evaluation.** When I work with a chatbot, I'm forced to frequently switch between the two modes. I ask a question (implement) and then I read a response (evaluate). There is no "flow" state if I'm stopping every few seconds to read a response. The wait for a response is also a negative factor here. As a developer, when I have a lengthy compile loop, I have to wait long enough to lose the thread of what I was doing. The same is true for chatbots.

## Avoid No man's land

There's an ongoing trend pushing towards continuous consumption of shorter, mind-melting content. Have a few minutes? Stare at people putting on makeup on TikTok. Winding down for sleep? A perfect time to doomscroll 180-character hot takes on Twitter. Most of the products I've seen built with LLMs push us further down this road: why write words when an AI can write that article for you? Why think when AI can write your code?

When I try these new products, I find myself transported into WALL-E. My brain turns off and I press the magic 🪄 button or mash the Tab key. And when I'm eventually jolted out of my zombie mode, I don't even really like what's been created.

The way I see it, there's a spectrum of **how much human input is required for a task**:

Human task

0%

Tool

50%

Machine

100%

When a task requires mostly human input, the human is in control. They are the one making the key decisions and it's clear that they're ultimately responsible for the outcome.

But once we offload the majority of the work to a machine, the human is no longer in control. There's a [No man's land](https://en.wikipedia.org/wiki/No_man%27s_land) where the human is still required to make decisions, but they're not in control of the outcome. At the far end of the spectrum, users feel like machine operators: they're just pressing buttons and the machine is doing the work. There isn't much craft in operating a machine.

Automating tasks is going to be amazing for rote, straightforward work that requires no human input. But if those tasks can only be partially automated, the interface is going to be crucial.

I want to see more tools and fewer operated machines - we should be embracing our humanity instead of blindly improving efficiency. And that involves using our new AI technology in more deft ways than generating more content for humans to evaluate. I believe the real game changers are going to have very little to do with plain content generation. Let's build tools that offer suggestions to help us gain clarity in our thinking, let us sculpt prose like clay by manipulating geometry in the latent space, and chain models under the hood to let us move objects (instead of pixels) in a video.

You're still with me?

I'm impressed.

Hopefully I've convinced you that chatbots are a terrible interface for LLMs. Or, at the very least, that we can add controls, information, and affordances to our chatbot interfaces to make them more usable. I can't wait to see the field become more mature and for us to start building AI tools that embrace our human abilities.

## Related
[Add wiki-links manually or run update_wikilinks.py]