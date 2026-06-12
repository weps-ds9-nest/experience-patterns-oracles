# Usable Ai Chat Ibm Design Medium

## Challenges and wins for accessibility

A illustration with abstract representations of a chat interface, an eye, and screen reader output.

How we chat with an artificial intelligence (AI) is different than how we chat with people.

The differences affect everything from how a user provides input, to how the responses are displayed and how resulting processes flow.

So although we still call it _chat_, it’s dangerous if we assume we already understand the interaction. This is especially the case when we consider the needs of users with disabilities. (That’s a theme that continues from my [prior AI article](https://medium.com/design-ibm/the-quest-for-usable-ai-e649b6cb9e9a).)

## Input changes

Traditionally, a user’s chat input is always available. I can start typing and send a message any time. I can send quick messages in succession, regardless of whether I’ve heard any response from a user. Likewise, I may receive a message anytime; it’s not necessarily a response to any conversation I’ve initiated.

A typical lopsided conversation between two people, where I enter two messages in succession, and can send another whenever I want, regardless of what the respondent is doing.

But chat exchanges in AI are regimented. I send a message, the AI responds. At least for now, I cannot send a follow up until the AI response is done. Also, AI does not initiate conversations (except maybe in a Stephen King story).

### Disabled Submit

A design solution to this response-only AI interaction has been to disable the Submit button. This is a better approach than disabling the text input, since it allows someone to queue up a new query (or even paste in their old one and modify it).

It’s easy to “grey out” the Submit button to visually tell a user it has been disabled. It’s more of a challenge to convey that elegantly to a blind user. This is because keyboard users (including blind users) never actually need to select the Send button. They simply press Enter on their keyboard and, since the Send button is the primary (default) button, the message gets sent. When the Submit button is disabled and someone presses Enter, nothing happens. Unfortunately this absence of a submit action is not announced to a blind user by their screen reader technology. They won’t know the Submit button is unavailable unless they try to navigate to it.

While the AI response is taking place, the Send button is disabled, preventing me from sending another message.

## Response changes

Another difference between chatting with a person and AI is that the AI can be long-winded. People tend to talk in quick bursts of text. Not AI. Once it gets going, the responses are not typically brief.

### The Stop button

Enter the Stop button. This is handy in a few situations: the AI is taking too long beginning a response; the AI won’t shut up; or the AI response is going in the wrong direction. Now a user can halt the response and send a new message.

The same AI chat conversation as the prior illustration, but the disabled Send button has been replaced by a functioning Stop button.

Some AI chat interfaces use the same button position for Send and Stop, simply renaming it when its function changes. This can be quite elegant, since (at this point in AI ability) the user option is binary: either the AI response has ended and I can send a message, or the response is still ongoing, so all I can do is wait or stop it.

There is still the challenge of how to elegantly convey the change of the button’s name/state to a blind user. One option is to send a status message to the screen reader when the Stop button appears, such as “Press Stop to halt response in progress.”

This use of a status message may also be a way of solving another AI chat challenge for blind users: AI responses aren’t like people’s.

### Human responses

In a traditional chat, screen readers simply announce text messages as they appear. As I mentioned, texts between two people happen in bursts. The messages are short _and,_ despite being called “real-time,” each message is actually received as a complete chunk. No one receives part of the message while it’s being composed. Remember, too, that an incoming message can arrive unprompted. It’s not necessarily a _response._

This means that a screen reader’s automatic reading of a new chat makes sense. Announcing the message provides both a status update and the content. But that doesn’t work so well with AI responses for a few reasons.

### AI response novelties

An AI reply begins streaming onto the chat screen as soon as the AI has something to say in response to my prompt. It doesn’t send messages in discrete chunks, like a human response. Text appears more like fast, real-time ‘typing’.

When I send my comment “Tell me about the theory of relativity”, the Send button becomes a Stop button, my entry is repositioned to the top of the chat window, and then a response begins streaming down the page. When it fills the visible window, a small down arrow appears. I activate the arrow, which causes the window to reposition to the next screen of the response. When the response is complete, the stop button is replaced, but my position in the middle of the response is not altered.

AI responses can also _update_ in real-time. That is, the text that initially appears is not necessarily static. Words, phrases and whole sentences may morph for an uncertain period of time before settling down to something stable. This disrupts the ability to surface new content to screen readers using a common approach, ARIA live regions.

Finally, the AI responses populate the chat history differently than human chat. Each response from a person pushes the prior messages up the page. You’re always looking at the bottom of the last communication in the feed. With AI, the new information flows _down_ the screen. My latest chat ‘request’ is typically relocated to the top of the viewport, and the response flows down through the chat area — and long responses _keep populating_ below the visible screen. There is little or nothing to cue any user that the response is still unspooling; many UIs do not even include a vertical scrollbar. (Often the only sign is a little downward pointing arrow, to tell users there is information out of sight below.)

The length, feed direction, and instability of the responses, along with the state of the Send button, combine to create real challenges, especially for screen reader users.

## Potential solutions

Attempts to address these shortcomings have so far been cumbersome. Some implementations have forced the screen reader to announce “still composing” every 5 seconds while a response is being prepared. Then the screen reader is caused to announce the response in its entirety — potentially a _lot_ of information — after it’s completed. Sighted users can begin reading a response from the moment it begins appearing on screen and follow along through the course of its composition at their own pace; the feast-or-famine experience for a screen reader user is hardly equitable. It also ignores the fact that if a screen reader user tries to navigate into the chat and consume the response before it is complete, the cycling “busy” messages are disruptive — like an exceptionally repetitive on-hold announcement.

Fortunately, very recent developments promise to improve the experience.

### Stop button, part 2

First, I mentioned the use of the Stop button. For those times when the response flows below the visible viewport, a Stop button serves as visual cue that the AI is still responding. When complete, the Stop button gets replaced by the Send button. This is a useful cue for many users. Screen Reader users can also benefit, by being able to quickly check the name/state of a single button (such as by arrowing down with the virtual cursor).

 When a response is complete and the button is renamed Send, a status message could also be generated (for example, “response complete”). That way, a multi-tasking screen reader user would know when they could send another message (or start or finish reading the response).

### Reasoning traces

A very recent development to do with agentic AI also promises real value to screen reader users. The use of “reasoning traces” provides a high-level summary of an AI’s progress. Each trace represents a step in the AI process, usually given as a text-based statement, such as “Convert requirements to git issue”. Together the traces provide context (and reassurance that the system hasn’t just stalled). Once the actual response begins unspooling, the reasoning traces collapse into one or more expandable sections preceding the AI response.

A simulated reasoning trace, showing an initial user request to “Create a template for a new feature request with requirments.” The AI displays the message “Reasoning…” and then displays a series of three generic messages: “Step details go here”, “Convert requirements to formatted git issue,” and “Step details go here”. After a brief animated ellipsis, a full response appears. At the same time, the reasoning traces are collapsed inside an expandable section which reads “Show reasoning”

Designs vary in how much information is provided to the user, but to me the most advantageous are those designs where the trace summary is very high level, with a mechanism for the user to drill down if they like. If each high-level trace is treated as a status message, screen reader users are given a nice, succinct play-by-play of progress.

### Personalization

I’m delighted to see more agency being considered for all users as AI chat matures. As designers recognize that not all users may want the same level of response trace detail, for instance, the notion that users could personalize such a feature is gaining traction. For response traces, this might let the user control the ‘volume of noise’ — whether you want a highly verbose trace, or just want to see progress represented by a growing line of dots.

Personalization can also benefit a number of other parts of the AI experience. I’ll tackle some considerations in a [future article](https://medium.com/design-ibm/catching-up-on-accessibility-with-ai-chat-1129be33c184), along with some trends in AI chats that have the potential to reduce accessibility.

_Michael Gower is a Senior Consultant in Accessibility in IBM Design. Illustrations by IBM Visual Designer_[_Thy Do_](https://medium.com/@thy.hm.do)_. The above article is personal and does not necessarily represent IBM’s positions, strategies, or opinions._

## Related
[Add wiki-links manually or run update_wikilinks.py]