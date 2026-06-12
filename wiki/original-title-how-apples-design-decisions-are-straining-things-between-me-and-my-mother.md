# Original title: “How Apple’s design decisions are straining things between me and my mother”

Original title: “How Apple’s design decisions are straining things between me and my mother”

Ever since buying my mom a 13" iPad pro to replace an aged-out iPad2, the calls have been long and frequent.

It really shouldn’t be that big a transition to switch to a new version of the same device. At first I blamed my mom for being inflexible. Yes, I get there is no longer a home button. Yes, that new gesture _is_ tricky to get right. But can’t we try?

However, I just spent half an hour figuring out exactly how my mom managed to accidentally delete her alarm, then why she was having so much difficulty making a new one. And Apple, we have a problem.

## Exhibit 1: the unnamed button and flat design

Secondary considerations first. The alarm screen behind the dialog in Figure 1 has three main functions: edit an alarm, add a new one, or toggle an existing alarm on and off. The first button is called Edit. Super easy to see and understand. But, um what’s this “cross thing” (mom’s words)?

Figure 1: Part of the Alarm screen on an iPad, with the “+” button activated showing the Add Alarm dialog

The “+” _was_ there on her old iPad’s alarm, but under duress, things we kinda knew become a bit harder. Space isn’t a concern here, so why use text for one button and a symbol for its mate — especially on a touch device, where one can’t hover to see its name via a tooltip? Why not just call it Add? (And whose idea was the “o” in the switch button?).

When I walked mom through this UI and described the actions as being ‘at the top’, my mom then thought “Add Alarm” was a button. Flat design has been with us so long, it’s easy to ignore possible impact if the only thing to distinguish the text that’s a button from text that’s a heading is position and a low contrast difference between white and yellow text. Is there _really_ a good reason not to provide a clear outline on the buttons or something more obvious to help users with poor vision differentiate which text is interactive?

## Exhibit 2: The Save button

What do you think happens when you enter a new time in the above Add Alarm dialog and then press the Save button? My mom thought the new alarm would be saved.

Figure 2: Add Alarm dialog, part 2, with the same Cancel and Save buttons and Time input, plus more options

The real answer is that the Cancel and Save buttons and the Add Alarm title remain exactly as they were. Instead, the lower part of the dialog updates and shows options (Figure 2).

Mom’s confusion is understandable and easy to solve. A Save button shouldsave. How about “Next” on the first dialog?

But I think there’s a bigger problem here. Why a two-part dialog?

Figure 3: The old IPad’s Add Alarm dialog, showing spin buttons for the hour, minutes and AM/PM.

I had a look at her old iPad, to see if I could understand the evolution. There, spin buttons independently set the hours and minutes, with the options persistently displaying underneath (Figure 3). So everything happens in a single dialog.

I suspect someone realized a numeric keypad is a faster input, but then thought the UI was getting too messy. Unfortunately, the result seems half-baked. In fact, if you look at the 12:35 input in Figure 1 (detail below has 8:15), there’s still the ghost of a spin button control above and below the input!

Even with my mom’s large text, there’s room for the numeric input and the options to coexist at the same time. A Save button that doesn’t save seems like a much more disruptive design problem.

## Exhibit 3: Use of colour

Take a look at the use of orange in Figure 1. It’s used for the Cancel and Save buttons. As mentioned, it’s also outlining the Time input, as well as colouring the digits themselves. Seems to be a cue for interaction, right?

Time input (for different alarm) from first save step (Figure 1)

Time input (for different alarm) from second save step (Figure 2)

When the Time input stopped being orange or strongly outlined after pressing Save the first time(Figure 2), my mom assumed wrongly that the numbers were no longer editable. I understand the Time input lost ‘focus’ and is no longer the primary concern after the first Save, but as will be seen, losing that styling makes subsequent interaction less obvious.

## Moving on to using and editing alarms

Once mom understood she has to press the Save button twice — and that she could correct the time even when it seemed like she couldn’t, we moved on to the mystery of how her existing alarm disappeared.

My mom only uses one alarm. She just changes the time for the few occasions when her 8:15 alarm doesn’t make sense. Then she sets it back. I explained the idea of multiple alarms that she can just turn off. She agreed we could add a couple more (Figure 4).

Figure 4: Screen snippet showing 3 alarms for 5:30, 8:15 and 10am, none of which are turned on

This might be the time to mention that mom struggles with tapping. Her attempts tend to vacillate between two extremes: the feathery touch of a butterfly’s hesitant caress, or the emphatic press of a bully rubbing a banana-cream pie into someone’s face. Her intention may not register at all, or she may succeed in rapidly turning the switch on and off again. She can accidentally trigger press-and-hold actions or swipe to another app when she’s just trying to tap.

Technology is against her here. My mom has drier skin, which makes it harder to register touches on the [capacitive touchscreen](https://www.consumerreports.org/cro/news/2015/06/zombie-finger-and-touchscreens/index.htm). It’s just one of the myriad ways [older users are challenged by touch screens](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7924826/). Combined with her poor vision, it makes for an amazingly inconsistent experience.

When I assured her that the _only_ thing she could interact with on each alarm tile was the on/off switch, it made it easier and reassuring.

## Exhibit 3: The delete mechanism

Reassuring, that is, until we got to editing the alarms.

When someone presses the Edit button in Figure 4, the alarms undergo minor visual changes. All the tile text remains the same, but the on/off switches disappear and new red circles appear to the left of each alarm time (Figure 5).

Figure 5: Alarm screen after Edit is selected, showing the Red delete icons to the left of the alarm times

These minor visual changes don’t convey the extent of the interactive changes. The entire button is now interactive for editing, which to my mom’s credit, she figured out. What she hadn’t understood is that the button actually contains _multiple_ targets which carry out different functions, one to edit, one to delete.

So, when she went to tap the alarm to change its time, she accidentally activated the little red circle which deleted the alarm immediately, with no prompt. Confirming deletions is a [requirement in WCAG](https://www.w3.org/WAI/WCAG21/Understanding/error-prevention-legal-financial-data) for critical data. Although an alarm doesn’t qualify as critical, as a general rule it’s good to confirm deletions.

Incidentally, that delete button is so small, it will fail the draft [Target Size](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html) requirement in WCAG 2.2. It doesn’t meet Apple’s [existing guidelines](https://developer.apple.com/design/human-interface-guidelines/ios/visual-design/adaptivity-and-layout/) either.

## Exhibit 4: The edit experience

Remember my comments on the half-baked alarm UI? Here’s what happens when you tap anywhere on an alarm in Edit mode (Figure 6). Anyone see the confusion my mom faced?

Figure 6: Edit alarm screen, showing numeric keypad over top the Cancel and Save buttons.

My mom changed the time from 8:15 to 8:30, and then didn’t know what to do.

There is no Save or ‘do’ button.

The numeric keypad has been positioned such that it will always cover the Save and Cancel buttons.

Most experienced users would try tapping outside the dialog to see what happens, at which point the numeric keypad “dialog” collapses and the user finds themselves back at an Edit Alarm screen (Figure 7). But it seems to me a better experience would be _start_ with Figure 7.

Figure 7: The Edit Alarm dialog, part 2, which only presents after a user clicks outside the dialog in the Figure 5 view.

Apple _could_ make a clearer affordance for the Time input, if that’s the intended primary operation. But more critically, when it’s chosen, expose the numeric keypad underneath (or at least not _above_ the input). That would allow a user to modify only the time and save it. (Or, how about adding an Enter on the numeric keypad?)

There are also other housecleaning items to tackle here. I mentioned the odd “o” label on the off position of a toggle button in Figure 1. It’s matched by an equally cryptic (and low contrast) “l” in the Snooze button when it is on, in Figure 7. Part of me assumes this is meant to convey (or suggest) a binary 1, with maybe the o suggesting a 0 (zero)? Honestly don’t know. Apple’s guidance on switches is to [avoid labels](https://developer.apple.com/design/human-interface-guidelines/ios/controls/switches/). But if a label is going to be used, there _is_ room for a slightly wider button to say “off” and “on”.

## Epilogue

Apple has a reputation for ease of operation. There are a lot of us who have given our aging parents iPads because they were easier for them to understand and operate than a desktop computer.

Any one of my mom’s disabilities, as well as her circumstances as a digital non-native, puts her at a disadvantage. Compounded, they represent a significant barrier to her participation. There are seeming changes afoot throughout the iPad UI which threaten to exacerbate this divide, not reduce it: when a Save button doesn’t save; when basic contrast minimums are ignored; when a label is reduced to a meaningless single character; when designs cover up essential controls…

The good news in all this is I’m able to take the time to understand the design problems and tell my mom that it’s not just her. It’s her iPad. That is hopefully a lot more reassuring to her than it is to Apple.

_2024 Epilogue: I began this article almost three years ago and left it in draft; I probably had some more points to raise. Coming across it today, I feel like the considerations it documents are still valid and useful, even if Apple’s UI has_ hopefully _improved since._

## Related
[Add wiki-links manually or run update_wikilinks.py]