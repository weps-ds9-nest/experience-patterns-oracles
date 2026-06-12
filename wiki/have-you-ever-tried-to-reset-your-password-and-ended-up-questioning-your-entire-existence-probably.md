# Have you ever tried to reset your password and ended up questioning your entire existence? Probably. That wasn’t your fault, but the fault of bad error prevention and handling.

Have you ever tried to reset your password and ended up questioning your entire existence? Probably. That wasn’t your fault, but the fault of bad error prevention and handling.

Error handling is one of those sneaky, underestimated parts of UX—the kind that only gets noticed when it’s done **poorly**. After reading this, though, you’ll know that errors are not just obstacles, they’re opportunities. When things go wrong, your interface can do one of two things: lose trust or **build it!** When done right, it shows empathy, guides the user forward, and creates a sense of calm control.

In this article, we’re going to dive into:

*   Why error handling matters (more than you think)
*   Common UX mistakes that break trust
*   Principles for designing helpful, human, and even charming errors
*   Real examples of what **not** to do, and how to do it better

Whether you’re designing a fintech app, an onboarding flow, or a pizza tracker — this stuff matters.

> Because when everything breaks, your UX shouldn’t.

## Blue screen of death: A UX error horror story

The infamous Blue Screen of Death. If you’ve ever used Windows in the early 2000s, you’ve probably met it. No warning, no option to save your work, just a full-screen message in a cold shade of blue and a string of hexadecimal gibberish.

The Blue Screen of Death: A legendary example of poor error handling in UX: cryptic, cold, and completely unhelpful to the average user.

What does that mean? From the perspective of a common user, who knows? It could be your hard drive, a corrupted update, or just a vengeful computer god. From a developer's point of view, as can be seen above, the message contains technical information that could help debug the problem. A good error message could have had an inclusive message that would have helped communicate the problem to both users.

The first BSOD (shown below) took some iterations to become the current one, which has more helpful information for both users. By following the common UX principles mentioned below, we can dissect this message and understand its good and bad sides and how it created trust within the chaos.

From unreadable to empathtic with automatic problem recovery

## Why error handling matters

Errors are inevitable. Users will mistype, forget passwords, lose connection, or click the wrong button. Software will crash. APIs will fail. The unexpected will happen, but the real question is: how will the product respond in those critical moments?

An error isn’t just a functional interruption; it’s a psychological event. It triggers confusion, frustration, and even panic, especially if the user feels at fault or doesn’t know what to do next. Even the slickest interface becomes a usability nightmare the second it fails to handle errors gracefully. Users don’t remember your fancy animations or pixel-perfect layout; they remember the time spent on your app, enjoyably or badly.

In terms of user experience, bad error handling could lead to Rage quits, uninstallations, and negative reviews, which translates to additional support tickets, additional manpower cost, loss of revenue, trust, and credibility.”

## Principles for handling errors like a boss

One of Jakob Nielsen’s Principles in his [Usability Heuristics for User Interface Design](https://www.nngroup.com/articles/ten-usability-heuristics/) is “Help Users Recognize, Diagnose, and Recover from Errors.” With these three easy steps, we can ease our users' frustration when they encounter an error.

Form NN/g’s 10 Usability Heuristics for User Interface Design (Image: NN/g)

1.   **Tell your users that an error has occurred** Messaging and visual treatment: Red text error message and an icon of a warning sign
2.   **Tell them what went wrong** With clear and consistent wording in a language that they will understand. Preferably not in technical terms or jargon
3.   **Help them recover from the error** Instructions on how to fix the error, alternatives (If applicable), and a clear CTA (When relevant) to click now and fix the problem

> _The best way of helping users fix an error, is to prevent it in the first place, that is of course,_ Jakob Nielsen’s [5th principle: 5: Error Prevention](https://www.nngroup.com/articles/slips/)

Some nice examples of form errors are from ASOS and Shopify. As you can see, the errors are shown at the location where they happen, with a clear red visual indication and text telling the user what needs to be done. Asos took a more friendly and relaxed tone, “We need your first name—it’s nicer that way,” while Shopify took the most direct approach, telling the users, “Enter a first name.”

A key point here that can be emphasized is that both forms showed the error only when the user made a mistake and tried to advance to the next screen.

## Slips vs Mistakes

Not all errors are created equal. In UX, Don Norman distinguishes between **slips** and **mistakes**, and understanding this difference is crucial for designing helpful error handling. A **slip** happens when the user’s intention is right, but their execution falters. Think of accidentally clicking the wrong button, closing a dialog instead of saving, or mistyping an email address. The goal was correct, but the action misfired. A **mistake**, on the other hand, occurs when the user’s goal or plan is flawed due to a misunderstanding of the system. For example, trying to change settings in the wrong menu, misinterpreting an icon, or assuming a decorative image is interactive. In these cases, the action is carried out flawlessly — but toward the wrong objective.

The user’s intention is right, but their execution falters.

### Why should we tell them apart?

Because the solutions differ, **Slips** are best handled by making interfaces forgiving and resilient: features like undo, confirmation dialogs for destructive actions, input validation, autocorrect, and search suggestions all help users recover from momentary lapses without punishment. It’s worth mentioning that sometimes, the user is not to blame; a contributing factor to slips might be a UX flaw. For example, a button could be too small, have vague or misleading copy, or just be near another one that has a different action.

**Mistakes**, by contrast, demand clearer communication and better alignment with mental models. This might mean refining labels, making icons unambiguous, offering contextual help, or using error messages that don’t just say what went wrong but also explain why and how to fix it.

> _“Slips happen when people do the wrong thing while intending to do the right thing. Mistakes happen when the intention itself is wrong.”_[Slips vs. Mistakes by Aurora Harley](https://www.youtube.com/watch?v=s0hStSMc_Rs)

By separating slips from mistakes, designers can move beyond treating all errors the same. Instead, they can anticipate where users will falter, design safety nets for slips, and provide clarity to prevent mistakes. The result is not just fewer errors, but interfaces that feel empathetic, supportive, and trustworthy, even when things don’t go as planned.

## The right moment and the right place

Following Jakob Nielsen’s Usability Heuristic, when designing an interaction with the possibility for user error, like the form we mentioned before, keep these in mind:

### Don’t scold prematurely

Allow users to make mistakes, and when they do, show them where they err. In this example, a user didn’t enter an email address. The UI doesn’t say explicitly that it is required, but **the user gets notified only on submission**. On the other hand, don't scold prematurely: A user unfocuses from the field and gets an error message. We can’t assume that the user is done with entering the email value, and so, the email **validation should only happen after submitting the form**

Wait for the user to finish: errors should guide, not scold

### Connect the error to its origin

Placing the error message directly next to the relevant field improves visibility and helps users immediately understand where the problem is. This reduces cognitive load and mental effort by guiding users precisely to the area that needs attention.

 The example below illustrates how poor placement of an error message can lead to confusion and unnecessary friction.

Keep error messages close to where the error happened.

### Don’t block the flow

Keep the main action button (e.g., submit or continue) **enabled** to allow users to proceed. If there are issues, display clear error messages after submission.

 Disabling the button preemptively creates confusion - users won’t know which validation criteria are missing, which increases frustration and cognitive load.

 The example below highlights how disabling the main action button can make it unclear what’s preventing progress, making it harder for users to understand how to move forward.

Let users make mistakes: and guide them through recovery

> Errors come in many shapes, and good UX can make each one feel less like a roadblock and more like a guide through the process, clear and actionable.

Errors come in many shapes

In the example above, the system shows different error states: a required field left blank, an invalid email format, an email that already exists, and a submission failure. Notice how each message explains **what** happened — and, when possible, **how to fix it**. “An email address is required” tells the user exactly what to add. “Please enter a valid email address” highlights the format issue. “Email already registered” suggests using another address or logging in. And when the issue is out of the user’s hands, like a system error, the message shifts to guidance: try again or contact support. By tailoring each error to its shape, we make forms feel less like a roadblock and more like a guide through the process.

## 3 Levels of errors - and how to handle them

Errors might differ in origin and appear in odd situations. To design the most effective and supportive error experiences, we need to understand **where** the error originates and **who (or what)** is responsible.

Here are the three primary types of errors you’ll encounter, each with its own design implications:

### 1. User-generated errors

Errors caused by the user’s action, usually unintended, such as missing information, invalid input, or interacting with the wrong element.

Form field for entering an email address. The input shows “matanrosen#gmail.com” with an error state highlighted in red and a message below that says “Please enter a valid email address.”

**Common examples:**

*   Leaving a required field blank in a form
*   Entering text into a number-only field
*   Typing an email address without “@”
*   Selecting a date in the past for a delivery form

**How to handle it like a boss:**

*   Use inline validation as the user types (but not too early!)
*   Be specific and helpful: “Please enter a valid phone number, like 054–6987411”
*   Highlight the exact field with the issue
*   Offer smart defaults or constraints to reduce the chance of error (e.g., date pickers, input masks)

_Your goal: help users recover gracefully without feeling stupid._

### 2. Environmental errors (External factors)

Errors caused by the user’s **environment or device state**, often outside of their control.

Screenshot of a Chrome browser error page with a pixelated dinosaur icon and the message “There is no Internet connection.” It suggests checking cables, reconnecting to Wi-Fi, or running Windows Network Diagnostics, followed by the error code “DNS_PROBE_FINISHED_NO_INTERNET.”

**Common examples:**

*   No internet connection
*   The device is in airplane mode
*   GPS or camera permissions denied
*   Battery saver is blocking background sync

**How to handle it like a boss:**

*   Detect and **communicate the issue clearly** (e.g., “You’re offline — changes will be saved once you’re back online.”)
*   Offer offline support or retry mechanisms when possible
*   Don’t blame the user — use neutral, empathetic language
*   Use icons or visuals to reinforce the issue (e.g., a signal bar with a red X)

_Your goal: show awareness of real-world conditions and offer a smooth fallback when things go wrong._

### 3. System error

Errors caused by the system or software itself — including bugs, failed API calls, server crashes, or unexpected conditions the app wasn’t built to handle.

**Common examples:**

*   500 Internal Server Error
*   “Something went wrong” (with no useful detail…)
*   Slow or failed responses from third-party services
*   App crashes on startup or after an update

**How to handle it like a boss:**

*   Show a **friendly, non-technical message** (avoid hex codes unless you’re building for devs)
*   Give users a path forward: retry, contact support, or save their progress
*   Use humor or personality if appropriate, but **never** at the user’s expense
*   Log the error quietly for your dev team — the user doesn’t need to see your stack trace

_Your goal: reassure the user, hide the chaos, and recover fast._

### Additional and notable error types

**4. Security or Permission-Based Errors:** These often feel like user errors but are policy-driven. Clarity and next steps are essential.

**Common examples:**

*   Access denied (unauthorized action)
*   Permission blocked (e.g., camera, location)
*   Session expired (e.g., for inactivity)

**5. Business Logic Errors:** These need clear explanations and a friendly tone — the user didn’t “mess up,” they just hit a rule.

**Common examples:**

*   “This coupon code has expired.”
*   “You’ve reached the limit of 5 uploads.”
*   “You cannot schedule meetings in the past.”

And now, for a different angle on error handling:

## Engineering Resilience: How Smart Backend Design Supports UX

Now, let’s take a quick detour from UX into the world of code, where error handling also plays a vital role. Think of a long-running backend process composed of multiple asynchronous or synchronous steps: if a minor task fails, should the system abort everything, or proceed and present the issues later? This programming dilemma mirrors user flow design: sometimes it’s critical to stop and alert the user immediately, but often it’s better to **keep the process going**, record errors, and address them in context at the end.

Think of a backend process as a journey: one involving multiple steps, some asynchronous, others synchronous. If one minor step fails, should the whole journey collapse, or do we keep going and surface the errors at the end, guiding users through recovery? This mirrors the **fail-fast versus fail-safe** debate in programming, as Shai Almog [mentioned here](https://medium.com/javarevisited/failure-is-required-understanding-fail-safe-and-fail-fast-strategies-ac9112fe056d). A **fail-fast** approach halts immediately on error, like when an API immediately rejects a request with an error (e.g., invalid authentication token) instead of continuing the process and failing later. Simplifying debugging and preventing cascading failures, but risking user disruption if something minor breaks early

> _“Failure isn’t something we can avoid, predict or fully test against. The only thing we can do is soften the blow when a failure occurs.“_
> 
>  Shai Almog — [Failure is Required: Understanding Fail-Safe and Fail-Fast Strategies](https://medium.com/javarevisited/failure-is-required-understanding-fail-safe-and-fail-fast-strategies-ac9112fe056d)

Watercolor illustration of a man with brown hair sitting at a laptop, looking concerned. Next to him is a flowchart showing a process: “Start” → “Step 1” → if critical failure then “Stop,” otherwise “Log error” and continue to “Step 2” → “Finish” → “Present errors.” The chart represents handling failures by either stopping on critical errors or continuing and reporting minor ones later.

In contrast, a **fail-safe** method perseveres, like if a file upload process fails at the virus scan step, the system still stores the file in quarantine and lets the user know, instead of canceling the entire upload. Completing the larger process and collecting errors to present at the end all at once. This protects the user flow but can hide issues that accumulate and become harder to resolve. UX-wise, the sweet spot is often a hybrid: design backend workflows to tolerate minor hiccups: retrying failed steps, gracefully degrading, and logging errors: without blocking the user journey. Then, at completion, surface-friendly, actionable messages that keep the user in control. This way, even backend failures feel like manageable detours, not dead ends.

Consider the following two examples:

 File upload process: Should we wait for the upload process to start and then notify the user of errors, or should we validate before it starts?

Uploading multiple files — MOTIF: The FOLIO design system

And for a deletion confirmation: once a deletion sequence has started, should we stop it for each file that fails? Or should we show each file’s status as we go through the sequence?

Deletion confirmation — MOTIF: The FOLIO design system

## Checklist: Error Handling Like a Boss

Errors are inevitable, but bad experiences don’t have to be. Instead of treating errors as dead ends, treat them as design opportunities to build trust and translate the error into a guide, moving users forward.

**Use this checklist to make sure your error states support, rather than frustrate.**

☑ Communicate in a clear and specific manner that an error has occurred 

 ☑ Briefly describe what went wrong 

 ☑ Set a clear message with language users can understand 

 ☑ Make it all visually noticeable 

 ☑ Set the error message relatively close to the origin (when applied) 

 ☑ Offer a direct solution to help users recover from the error

## Closing Thoughts

Error handling may look like a small detail in UX, but it’s where products often reveal their true character. A poorly written error can frustrate and alienate, while a thoughtful one that shows the right mitigation can reassure, guide, and even strengthen trust. We’ve looked at why error handling matters, the pitfalls to avoid, the principles that create clarity and empathy, and the different levels of errors that require different approaches. The key takeaway is simple: errors are not just interruptions; they are opportunities. Opportunities to support users, reduce stress, and show that your product has their back even when things go wrong. If you design errors with empathy, clarity, and recovery in mind, your users won’t just forgive mistakes — they’ll trust you more for handling them like a boss.

_*All images in this article were created with AI. The writing text was not (:_

## Related
[Add wiki-links manually or run update_wikilinks.py]