# If you have designed apps, or are planning to design one, chances are at some point the option to include swipe actions will come up. They may seem simple, but theres some big pitfalls that can trip you up. So without further edu here are a some of the most common mistakes and how to avoid them.

If you have designed apps, or are planning to design one, chances are at some point the option to include swipe actions will come up. They may seem simple, but theres some big pitfalls that can trip you up. So without further edu here are a some of the most common mistakes and how to avoid them.

## What is a swipe action?

Before we get into the nitty gritty, let’s go back to the basics. Swipe actions provide contextual actions to a user focused on a single item, whether it’s a card or a list entry. They’re fast, un-intrusive and _should be_ ubiquitous across iOS and Android. Sounds great, right? But implement them wrong and you not only create a slow, overcomplicated addition to your app, but one that makes the user nervous to use it.

## 1. Including more than one option on each swipe

The biggest upside to a swipe action is the **speed** at which a user can action something, you can work through a whole list of items in seconds by just swiping left and right. Its understandable then that you get tempted to include even more actions as you realise all the possible things a user *could* want to do quickly.

This can manifest in either one of two ways; swiping and then a set of options appearing to the user, or distinguishing between short or long swipes and changing the action.

The former **slows the user down** by increasing the steps they need to take to complete an action. Also don’t underestimate the impact of having the details of the item of the screen when trying to make a decision, it inevitably leads to a situation where the user abandons the action because they forgot what item they were currently actioning.

The latter is essentially impossible for a user to execute efficiently, leading to them either **swiping too little or too much** and triggering the wrong action. This is arguably the worst option of the two, at least the former won’t cause you to delete that item you originally meant to archive.

Mail by Apple: Apple seem to be insistent on including everything they could possibly imagine in their swipe actions. The right swipe not only provides you with either Archive or Flag but also a more button presenting you with every action imaginable, all while obscuring the emails limited information. You can also long swipe to activate delete over any of the other actions. Things get even murkier when the Archive action switches to Delete, which you have to guess is based on the mailbox it was sent to. The read/unread left swipe is implemented well, but at this point just adds further confusion by breaking the internal logic of the app.

### How to solve it

Simply force yourself to stick to **one action per swipe**. This may seem limiting, but take a step back and look at what information the user has at that point in time. With that amount of information what could a user want to do 80% of the time? If answered truthfully you should be able to get the options down to two and honestly if you’re still having problems then you have deeper issues.

Spark by Readdle: Readdle’s email app has to have some of the worst example of long/short swipes I have ever encountered. The left swipe starts by pinning an item, one would assume because it’s important and you wish to save it for later, but part way through a swipe it suddenly becomes delete, pretty much the opposite outcome you could want given what the swipe originally indicated. The right swipe isn’t much better as you can banish an email to the archive folder when trying to mark something as read. You can argue that a user could change these options in the settings, but what’s the likelihood of that really?

## 2. Switching up the rules of the game

This may seem obvious, but anyone using your app for the first time won’t have the foggiest what your swipe actions are, or if you even have them. For this to work you need to rely on the user discovering them while they use your app.

Luckily swipe actions are one, if not _the_, most commonly known gestures so chances are a user will at least try to swipe on an item at some point. This is a double edged sword though, users may be used to swiping, but they’re also used to the kinds of actions that happen when they swipe; **it’s standard to swipe left to complete a destructive action and swipe right for a positive action.**

Its all to easy to forget this when you’re just focused on what your app can do, but switching these around or in general going against the grain won’t end well in this context. You will either lead people to not discover the action or, arguably worse, set out to do another action and end up with the opposite result and one very frustrated user.

Spotify: Both actions are not only ambiguous, especially the plus which could mean anything at this stage, but both seem positive at first glance. Its only after you swipe that you’re told what you did and theres no obvious undo functionality to let you reverse the action. You have to somehow guess that you can swipe left again to remove the song from your library when the right swipe stays exactly the same! When you then add on the questionable usefulness of adding something to your library, from your own playlists no less, and its a big fat NO from me Spotify.

### How to solve it

Don’t be tempted to include an action **if it doesn’t fit with what users currently expect.** If you have an action that you think or know your users conduct most of the time and it doesn’t fit the expectations of a swipe action then chances are there’s a better way to implement it.

## Related
[Add wiki-links manually or run update_wikilinks.py]