# By default, form buttons aren't disabled. When you render a form, everything "just works". That is, until, a web developer decides to get "clever" and starts disabling buttons, pending some desired form state. Unfortunately, many developers are not quite as clever as they _think they are_; and, buttons often remain disabled even when a form has been completed filled-out. This obviously leads to a terrible user experience (UX).

By default, form buttons aren't disabled. When you render a form, everything "just works". That is, until, a web developer decides to get "clever" and starts disabling buttons, pending some desired form state. Unfortunately, many developers are not quite as clever as they _think they are_; and, buttons often remain disabled even when a form has been completed filled-out. This obviously leads to a terrible user experience (UX).

![Image 1: Alexa from Schitt's Creek saying: Oh my god, can you stop this please.](https://bennadel-cdn.com/resources/uploads/2023/oh-my-god-can-you-stop-this-please-alexis-rose-optimized.gif)

This is not a theoretical problem. I run into this scenario often enough, most frequently on my mobile browser. A form will be auto-filled, or I'll paste-in a password, and some mobile form thinks that I have yet to touch any of the inputs. And so, the "Login" button remains disabled for some unknown reason (until I manually add — _and then remove_ — a character).

Let's assume for a moment that the web developer is _actually intending_ to provide a better user experience by not allowing a user to submit invalid data. To that I would posit that if a user _wants to submit_ an incomplete form, the form **already has a bad user experience**. Meaning, something about the form itself **lacks affordance**. Something about the form is leading the user to _think_ that the form is ready to be submitted even when it isn't.

So, by disabling buttons you're actually solving the _wrong problem_. And, you're (potentially) creating _new problems_ in the meantime.

And to what end? Ultimately, you're already performing server-side validation and showing user-friendly error messages (I hope). As such, your desire to disable buttons and prevent form submission isn't actually creating any new value.

In web development, there is a concept known as the [**Robustness Principle**](https://en.wikipedia.org/wiki/Robustness_principle). It states:

> "Be conservative in what you do, be liberal in what you accept from others."

Unfortunately, we often see this principle being ignored on the web. Every time a phone number input _requires dashes_ or a social security number input _restricts dashes_ or a date input only works with dashes and not slashes, this is the Robustness Principle being needlessly tossed to the side.

I would argue that a disabled button is also a violation of the Robustness Principle: You are unnecessarily restricting what a user can do even when your (sever-side) control-flow is already designed to handle incomplete submissions.

On top of this — and maybe I can only speak for myself here — there is something **subtly off-putting** about the visuals of a disabled button. I know that when I load a form and the submit button is disabled by default, some _tiny part_ of my brain wonders if I'm even allowed to submit this form. I might even wonder if the form is perhaps not loading properly. After all, why would the button be disabled if the application _wants me_ to use this form?

I do believe that web developers are honestly trying to act in the best interest of their users when they disable form submission buttons. But, this effort is, unfortunately, counterproductive. The good news is, leaving buttons disabled is _easy to do_. So, developers can immediately create a better user experience by _reducing complexity_ and _lowering the level of effort_ that they have to put in their web forms. That's a win-win!

[https://bennadel.com/4419](https://bennadel.com/4419)

> I believe in **love**. I believe in **compassion**. I believe in **human rights**. I believe that we can afford to give more of these gifts to the world around us because it _costs us nothing_to be decent and kind and understanding. And, I want you to know that when you land on this site, **you are accepted for who you are**, no matter how you identify, what truths you live, or whatever kind of goofy shit makes you feel alive! Rock on with your bad self!

 — [Ben Nadel](https://www.bennadel.com/about/about-ben-nadel.htm "Learn more about Ben Nadel, Co-founder of InVision App, Inc.")

 Managed [ColdFusion hosting](https://www.xbytecloud.com/coldfusion/hosting/coldfusion-cloud-hosting?source=bennadel.com) services provided by: 

[![Image 2: xByte Cloud Logo](https://bennadel-cdn.com/images/global/xbyte-cloud.png)](https://www.xbytecloud.com/?source=bennadel.com)

## Related
[Add wiki-links manually or run update_wikilinks.py]