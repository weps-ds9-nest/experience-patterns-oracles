# The Undo Problem In Ai Products

## _AI products skipped designing undo and shipped branching as the retrofit. The two are not the same thing._

[![Image 1: Adi Leviim](https://miro.medium.com/v2/resize:fill:64:64/1*bYOm68fSxvg4SKIZasXnBg.png)](https://medium.com/@adi_leviim?source=post_page---byline--c90ff080de3b---------------------------------------)

10 min read

May 16, 2026

4

_Editor’s note: I wrote this article from firsthand experience as a founder and engineer. I used Claude Code as a writing assistant for structural feedback and copy editing. All insights, data, decisions, and stories are my own._

_Disclosure: I co-found browser extensions that wrap major AI chat products. Tools that fill UX gaps in those products are commercially aligned with my interests. I disclose this upfront so readers can factor that bias into the arguments below._

Press enter or click to view image in full size

![Image 2](https://miro.medium.com/v2/resize:fit:1000/1*oLledE4mSsbtMj4lfn-x_A.jpeg)

_Apple’s 1987 HIG documented Cmd+Z as part of the standard Mac menu, alongside the keyboard equivalents that defined the system. AI products in 2026 didn’t inherit it. Credit:_ Redrawn by author from Apple Human Interface Guidelines, 1987, Figure 3–22.

Someone left a one-star review last month on an AI productivity tool. One line is worth quoting verbatim: “Even notepad from windows 95 had undo. Please add this its 2026 lol.” They were complaining about a regenerate button, but they were naming something larger. AI products inherited 50 years of text editing without inheriting its most successful primitive.

Cmd+Z is one of the most successful design conventions in the history of personal computing. It works the same way in a 1987 Mac word processor and a 2026 Figma frame. It works in spreadsheets, in IDEs, in photo editors, in text fields on web pages I have never visited. It works without a tutorial, without a settings screen, without a menu. AI products in 2026, the most heavily-funded software category since mobile, do not have it.

## How Cmd+Z became invisible infrastructure

Undo did not arrive fully formed. Its lineage starts at Xerox PARC in the mid-1970s, with [Larry Tesler](https://en.wikipedia.org/wiki/Larry_Tesler) and Tim Mott’s Gypsy editor, the first modeless text editor. Modeless editing made undo possible because it meant the system could keep a single history of what the user had done, not separate histories per mode. Tesler’s [personal account of that period](https://interactions.acm.org/archive/view/july-august-2012/a-personal-history-of-modeless-text-editing-and-cut-copy-paste), published in ACM Interactions in 2012, is the cleanest read on why modeless editing mattered.

Press enter or click to view image in full size

![Image 3: California Sunset-era license plate illustration with a yellow-to-orange gradient, the word California in red script at the top, and NO MODES stamped in tall black sans-serif capital letters across the center](https://miro.medium.com/v2/resize:fit:1000/1*RcU1D04PywbhxiGPukioJQ.jpeg)

Tesler’s NO MODES plate was the design conviction behind the Gypsy editor. Modeless editing is what made a coherent undo history possible in the first place. Credit: Redrawn by author from photographs of Larry Tesler’s personal license plate, ca. 1985 to 2000.

In 1987, the [Apple Human Interface Guidelines](https://andymatuschak.org/files/papers/Apple%20Human%20Interface%20Guidelines%201987.pdf) codified Edit > Undo as a system primitive. Every Mac application that opened a window inherited a Cmd+Z shortcut and an Edit menu item that meant the same thing: take back the last action.

The following year, Don Norman published [The Design of Everyday Things](https://jnd.org/books/the-design-of-everyday-things-1st-ed/) and named the principle that undo most concretely expressed: the system should forgive its user. Errors should be recoverable. Action should not equal commitment. Norman called this design-for-error, and it became one of the load-bearing ideas of consumer software for the next 40 years.

In 1994, Jakob Nielsen condensed it into [Heuristic #3: User control and freedom](https://www.nngroup.com/articles/ten-usability-heuristics/). The NN/G entry is explicit. The heuristic reads “Support Undo and Redo.” Not a suggestion. A heuristic that NN/G has reaffirmed in every refresh of the ten heuristics for three decades.

In 2006, Bret Victor’s [Magic Ink](https://worrydream.com/MagicInk/) made the deeper argument: interactivity is the last resort, and reversibility is the property that makes interactivity tolerable. Then in 2012, his CUSEC talk [Inventing on Principle](https://worrydream.com/) staked the case that creators need immediate, reversible feedback to do their best work.

That is the lineage. Cmd+Z is one of the most academically defended single keystrokes in software design.

## Then AI products shipped without it

Open ChatGPT, Claude, or Gemini today. Generate a paragraph. Press Cmd+Z.

Nothing happens.

You can refresh the page and lose the generation entirely. You can press Regenerate and replace the generation with a different one, which is the closest thing to “go back” the product offers but is actually a forward operation, not a reverse one. You can edit your previous prompt, which produces a new generation and demotes the old one to a tab buried under a chevron. You can copy the output, scroll up, and paste it into your prompt as context. None of these are undo.

Undo means: I made an action a moment ago, and I want to take it back, and I want this to cost me one keystroke, and I want the system to be in the state it was in before I acted. AI products have nothing that satisfies all four properties at once.

This is not a small omission. ChatGPT crossed [900 million weekly active users in February 2026](https://techcrunch.com/2026/02/27/chatgpt-reaches-900m-weekly-active-users/). Google’s Gemini app passed [750 million monthly active users in Q4 2025](https://techcrunch.com/2026/02/04/googles-gemini-app-has-surpassed-750m-monthly-active-users/). The category that absorbed the most active users in the shortest time in the history of software does not have the keystroke that defined the previous 50 years of it.

Press enter or click to view image in full size

![Image 4: Three-panel comparison labeled ChatGPT, Claude, and Gemini, each showing the same prompt In two short sentences what is a sonnet followed by the model’s response and its regenerate button highlighted with a tooltip. ChatGPT labels the button Try again, Claude labels it Retry, Gemini labels it Redo, each sitting among feedback icons like copy and thumbs up.](https://miro.medium.com/v2/resize:fit:1000/1*idzAIgZdTJfbU7janzGZzQ.jpeg)

Three products, three different tooltips for the same destructive action: Try again, Retry, Redo. None of them say undo. Credit: Screenshots by author, captured May 2026.

## What users do when there’s no undo

I co-found browser extensions that sit next to ChatGPT, Claude, and Gemini, and the bias disclosure at the top of this article applies here. I read every user review of those tools. I read them for the obvious commercial reasons, but the underrated reason is that they document, in plain English, the things people do when a product won’t forgive them.

Two specific behaviors recur across thousands of users:

The first is the Cmd+A → Cmd+C reflex. Power users select all and copy the AI’s output to clipboard before they do anything else, every time. They have learned that the next click might be destructive and the keyboard shortcut they grew up on will not save them.

The second is the screenshot reflex. Less technical users take a screenshot of the AI’s response before they type the next message, because they don’t trust that the response will still be there if something goes wrong. The clipboard is too abstract. Pixels are not.

Two anonymized one-star reviews from the last 90 days make the cost legible. Both are quoted verbatim:

> _deleted my work. typed out a huge prompt with all my notes from a meeting, response was actually pretty good, came back this morning and the whole conversation is just gone from my history. how do you lose someones stuff like that. one star until i get my answer back_
> 
> 
> _Needs version history pretty badly. I use this app for writing pitches every day and the amount of times Ive regenerated a response only to immediately wish I had the previous one back is honestly too many to count at this point. Even notepad from windows 95 had undo. Please add this its 2026 lol_

These two users are not making a feature request. They are reporting a violation of an expectation that has been universal in software for 35 years. The interface where they were generating high-stakes work did not let them take back a mistake, and they read that as a betrayal.

Press enter or click to view image in full size

![Image 5](https://miro.medium.com/v2/resize:fit:1000/1*YuXCMCREpYLVWCXzFePWRA.jpeg)

Users naming the problem don’t reach for design vocabulary. They compare 2026 AI products to Notepad in 1995, in lowercase, because they are tired. Credit: Review card recreated by author from a verbatim one-star review of an AI productivity tool, May 2026.

## Branching is not undo

The industry’s response in 2025 and 2026 was branching, not undo. OpenAI shipped [Branch in new chat](https://help.openai.com/en/articles/6825453-chatgpt-release-notes): hover a message, click More actions, fork the conversation into a new thread. Anthropic shipped edit-to-branch in Claude’s web app and added a `/branch` command plus side chats (Cmd+;) in Claude Code. Google shipped [edit-prompt branching](https://support.google.com/gemini/answer/14262426) in Gemini. All three call this their "go back" feature.

## Get Adi Leviim’s stories in your inbox

Join Medium for free to get updates from this writer.

Remember me for faster sign in

Branching is not undo. A branch is heavyweight, deliberate, and navigational. It requires the user to know that branching exists, to find the affordance (usually buried under a hover state or a small icon), to make a decision about whether to preserve the parent, and then to switch between threads. It produces a tree of conversations the user has to maintain. Cmd+Z is none of those things. Cmd+Z is one keystroke at the syntactic level of the output, with no navigation cost.

Press enter or click to view image in full size

![Image 6](https://miro.medium.com/v2/resize:fit:1000/1*gljR_XyvPTKUA6vVitZw-Q.jpeg)

1984 put Undo at the top of the Edit menu. 2026 buried branching two clicks deep under a hover state. The asymmetry is the design. Credit: MacPaint 1.0 screenshot, Apple Computer Inc 1983; ChatGPT screenshot by author, May 2026.

The 2026 move makes the gap clearer. On March 23, 2026, OpenAI restricted ChatGPT’s message editing to the most recent prompt only, according to [release notes coverage at AI Productivity](https://aiproductivity.ai/news/chatgpt-restricts-message-editing-retry/). Editing further-back messages, which had been partial undo for some users, was removed. The industry actively walked back from undo-adjacent behavior in the same quarter it shipped more branching UI.

This is the same pattern that played out for memory and search in 2025, which I [wrote about in this publication earlier this year](https://medium.com/user-experience-design-1/the-forgotten-conversation-problem-in-ai-chat-4d3d0c3ea525). When users complained that AI chat couldn’t find their past conversations, the industry didn’t ship keyword search across message content. It shipped retrieval-augmented memory features. Memory features are useful and they are not search. Search would have been the lightweight primitive; memory was the heavyweight retrofit.

Branching is the same shape. Branching is the heavyweight retrofit; undo would have been the lightweight primitive.

## What undo would look like in an AI product

If a designer working on ChatGPT, Claude, or Gemini sat down today to design undo, four properties would be load-bearing. They follow directly from Norman’s design-for-error principle and Nielsen’s heuristic #3.

The first is reversibility at the output level, not just the conversation level. If a user generates a paragraph, edits two sentences, and presses Regenerate, undo should restore the previous paragraph as a recoverable state, not just the previous turn. Output is the unit of work in an AI product. The conversation is just the container.

The second is one-keystroke ambient access. No menu, no hover state, no chevron. Cmd+Z and Cmd+Shift+Z on every surface, including read-only views of generations, with the same semantics they have in every text field on every operating system. If the keystroke is contextually different from how it works elsewhere, it is not undo.

The third is stack semantics. Multiple undos. The user should be able to press Cmd+Z until they reach a state they want, then continue from there. The branching tree is the wrong data structure for this; a linear stack of states is what undo needs.

The fourth is visibility. Undo only works if the user knows it’s there. Norman’s principle of feedback applies: a small persistent affordance that says “you can come back from this” reduces the anxiety that produces the screenshot reflex and the Cmd+A → Cmd+C reflex. Nielsen’s [heuristic #6, recognition rather than recall](https://www.nngroup.com/articles/ten-usability-heuristics/), is the same point applied to controls.

Press enter or click to view image in full size

![Image 7](https://miro.medium.com/v2/resize:fit:1000/1*F052E-TsTtsKTNCkw76gNg.png)

One data structure costs one keystroke. The other costs four interaction steps plus the memory to maintain a tree. Credit: Diagram by author.

None of these are technically hard. Every property is a design decision the platforms could ship in a quarter if they decided this was a primitive worth designing.

## The deeper failure

Across [the chat box](https://medium.com/user-experience-design-1/the-chat-box-isnt-a-ui-paradigm-it-s-what-shipped-96e931d92769), [the forgotten conversation](https://medium.com/user-experience-design-1/the-forgotten-conversation-problem-in-ai-chat-4d3d0c3ea525), [the empty state](https://medium.com/user-experience-design-1/the-death-of-the-empty-state-in-ai-products-2026-e11439fbb688), and now undo, the same structural failure repeats. The industry inherited a messaging-app skeleton, used it to ship the most consequential creative tooling of the decade, and then retrofitted creative-tool affordances one at a time, late, and partially.

The reason this keeps happening is that the design conversation about AI products is still organized around the model. What can the model do, how fast, how cheaply, how accurately. The interface is treated as a thin transport layer over the model’s capability, which is exactly the framing Vannevar Bush warned against in [As We May Think](https://www.w3.org/History/1945/vbush/vbush.shtml) when he described the Memex as the augmentation of human thought, not the replacement of it. The interface is the augmentation. The model is the engine. We have spent three years polishing the engine and treating the augmentation as solved.

It is not solved. It does not even have undo.

The good news is that the design vocabulary already exists. Fifty years of HCI research, Tesler and Mott’s modeless editing, Apple’s HIG, Norman’s forgiveness, Nielsen’s heuristics, Victor’s reversibility, and a generation of creative tools that got this right. The AI products that win the second half of this decade will be the ones that stop pretending their interface is finished and start treating it as the actual product.

When was the last time you screenshotted an AI response before clicking regenerate?

## Key takeaways

*   Undo is one of the most universal interface conventions in computing, formalized in 1987 by Apple’s HIG, named as a principle by Don Norman in 1988, and codified by Jakob Nielsen as a usability heuristic in 1994.
*   AI products shipped without undo because they inherited a messaging-app interface skeleton, not because of any technical constraint at the model level.
*   Users have invented their own undo stacks through screenshot-before-regenerate and Cmd+A-Cmd+C reflexes. The cost of the missing primitive is paid in cognitive overhead, not in visible feature gaps.
*   Branching, edit-to-fork, and side chats are not undo. They are heavyweight navigation features and they do a different job. Treating them as a substitute is the same pattern as treating RAG-retrofitted memory as a substitute for keyword search.
*   A designed undo for generative output needs four properties: granular reversibility, lightweight invocation, stack semantics, and visible affordance. None of these are hard to ship.

Follow me on Medium for more essays on AI UX and the design reality of building for global audiences.

About the author: Adi Leviim is a full-stack engineer and product builder with 7+ years of experience shipping commercial software to global audiences. He writes about AI UX, the design reality of building for millions of users, and the gap between AI demos and production AI. Follow him on Medium for essays at the intersection of engineering and design.

[Medium](https://medium.com/@adi_leviim) | [LinkedIn](https://www.linkedin.com/in/adi-leviim/)

## Related
[Add wiki-links manually or run update_wikilinks.py]