# Designing Better Hyperlinks A Detailed Guide

## USER INTERFACES

## Why are “click here” and “by this link” poor choices? And is it acceptable to use “read more”?

All these phrases have become so common that many people don’t see any problems with them. How many times have you encountered or composed the following on websites, in emails, or on intranets? In this article, I’ll explain popular wording and formatting mistakes and will show more accessible and informative alternatives.

If something is widely spread, it doesn’t mean it’s right.

_By the way, you can_[_read this article in Ukrainian_](https://telegraf.design/dyzajn-posylan-na-sajtah-i-v-lystuvanni-instruktsiya-vid-a-do-ya/)_. Originally published in_[_Smashing Magazine_](https://www.smashingmagazine.com/2021/12/designing-better-links-websites-emails-guideline/)_._

## 1. Meaningful links

First things first. What exactly is a hyperlink? It’s a combination of a web address (URL) and a clickable element (oftentimes a word or phrase, sometimes an image). While this is a vast topic, we’ll focus on text links, namely their usability and accessibility.

Thoughtfully composed links express respect to readers, whereas jumbled-up ones cause confusion and suspicion. When a link is presented as “here” or “this,” it’s harder to aim it with a cursor or finger. Also, it lacks transparency. What is hidden behind it: a page or file, an article or web form? One should re-read the whole sentence or paragraph to guess.

Links embedded into meaningful phrases are more comprehensible.

On the contrary, URLs attached to concise self-explanatory phrases inform people about the destination and are more convenient targets for clicking or tapping. Moreover, a well-composed link makes sense out of context and typically combines a topic (_for example, security, brand, marketing_) and format (_questionnaire, request form, guideline, policy, and so on_).

A well-composed link text usually makes sense out of context.

## 2. Exposing URLs

If a web address is short and doesn’t look like _“M$c0P88%X4LHr&dxQ1A,”_ then exposing it right away will work quite well, too, especially if the audience is supposed to copy it and paste it somewhere else.

In many cases, there is nothing wrong with exposing short URLs; however, it won’t be the most elegant solution from a visual standpoint.

And if you’ve got a long indecipherable chain of symbols, exposing it isn’t a great idea in most situations. In this case, consider embedding a URL into a succinct phrase or shortening the address in tools like [Bitly](https://bitly.com/) or [Cuttly](https://cutt.ly/).

However, these tools aren’t silver bullets: you do get a shorter link, but its meaningful parts will be replaced with random symbols, which are suspicious and not informative. Customizing shortened URLs is possible, but it’s typically a paid feature. Compare the following examples:

*   `bit.ly/30SjUa4y` (suspicious and unreadable);
*   `bit.ly/smashing-books` (readable topic);
*   `smash.ing/30SjUa4y` (recognizable domain);
*   `smash.ing/books` (fully transparent).

Long “gibberish” URLs occupy much space and are hard to memorize. However, they might become a non-fancy yet practical solution for copy-pasting.

**_Note:_**_while we covered a pretty rare copy-paste scenario, let’s also be mindful of accessibility, which I explain in Chapter 6._

## 3. Download links

A link that guides to some downloadable resource needs a slightly different treatment. Besides embedding it into a meaningful phrase, you should also inform users about the file format and size:

*   The format gives clues to what you can do with this data (e.g. if the information is read-only or editable);
*   The file size is crucial for people with costly internet, slow connection, or limited local storage.

A good practice for download links is to show the file format and size.

When you share a bunch of files (let’s say in different formats or versions), it’s not enough to design each link correctly. The whole series should be well-scannable and easy to use.

More with less: try to edit out repeated words and keep the list compact.

As you might notice in the picture above, repeated elements are not part of hyperlinks. Although this practice makes links look cleaner for sighted users, it may be harmful to visually impaired people. In chapter 6 of this article, I explain how you can keep blocks of links visually minimalistic, but at the same time leave enough guidance for assistive technology users.

## 4. “Buttonizing” important links

Not all links on a page or in an email are equally important. Authors often want their audience to click on the primary link, whereas other links can be skipped. If you’re going to draw people’s attention to the main action, think of presenting it as a button: _“Subscribe to the newsletter,” “Buy tickets,”_ _“Get the whitepaper,”_ or _“Download the recording.”_

The key link deserves to be a well-noticeable button.

And since I don’t want to be beaten by my accessibility colleagues for this advice, **beware of confusing buttons and links** semantically, in the HTML code. What I’m talking about here is the visual “buttonizing” of the key links, which makes sense to sighted people whose attention you want to attract. However, people who use assistive technology (namely screen readers) will be very confused to encounter a button instead of a link.

Here is a simple distinction of these HTML elements:

*   `<button>` = a button; executes an action on the current page (_for example, save, submit, refresh, duplicate_).
*   `<a>` = a link; directs you to another page, or a file outside of this page, or to a different section within the page (anchor links).

If you cannot create a “button” because of technical or time constraints, go for a quick-and-dirty solution: put that link in a separate line, make it bold, add spacing above and below, and so on.

The main link can also be located on a separate line with spacing from the rest of the text.

Of course, “button” text should follow corresponding patterns:

*   Be concise (up to 4–5 words);
*   Ideally, start with a verb (_get, buy, download, apply for, etc._);
*   Call the action honestly (avoid hushing up unpleasant steps like watching ads, registration, submitting personal data, etc.).

Compare _“Download the whitepaper,”_ which assumes that downloading starts immediately after clicking, and _“Get the whitepaper,”_ when a user downloads the file in exchange for their name and contact details.

Prominent buttons are suitable until they turn into aggressive banners.

## 5. Link-rich texts

Links enable the functioning of the internet; however, vigorously pumping URLs into each sentence isn’t a good practice (of course, unless you contribute to a Wikipedia-like knowledge base that is cross-connected by nature).

Step zero is to make sure you really need all the links. If you can edit something out, there won’t be a problem to solve. Otherwise, try to group the links: as a bulleted list, on the side of related paragraphs, or under a suitable title (_for example, “Recommended materials,” “Resources”_).

Link-crowded texts overwhelm the audience with too many options. Moreover, it’s challenging to formulate links when as part of a sentence.

Grouping the links helps a lot, but if the goal is to trigger action, the primary link should stand out.

The more eye-catching a link is, the more it encourages clicking/tapping on it.

In the previous sections, we figured out how descriptive links increase usability. At the same time, such links are longer, and consequently, can appear divided in a paragraph, when the first part of a link remains at the end of the previous line, and the second part jumps to the next line. It seems trivial compared to bigger flaws, but distorted links feel a bit annoying in link-crowded texts.

Split links are a bit harder to perceive than the ones that fit into corresponding lines.

If a paragraph width is fixed, compose text the way all links fit into lines, for example, try to start a paragraph with a link. However, browsers and devices render content differently, and links will still shift for some users. That’s why lists are a safer option for a set of links.

Cholmondeley Ladies: a contemporary version.

## 6. Link accessibility

Accessible links are not only the ones that look tidy and clear; they should also be properly working. [Web Content Accessibility Guidelines](https://www.w3.org/TR/WCAG21/) (WCAG), the world’s most famous digital accessibility standard, includes recommendations about hyperlinks, including some non-visual features.

### Distinction

One of the WCAG requirements is [not to rely on color only](https://www.w3.org/TR/WCAG20-TECHS/F73.html) when you want to distinguish a button or link from the rest of the text. Painting links in blue or another color doesn’t suffice since it still might not be visible for people with color blindness. The most typical method is underlining links; they can also appear in bold font.

Links should differ from the rest of the text by at least one more feature except for color.

### Color contrast

Links are essential interactive elements and have to comply with contrast recommendations. WCAG has two levels of contrast compliance:

*   **AA**: medium, used by many websites for a mass audience;
*   **AAA**: high, primarily applied on governmental sites and by communities of people with disabilities.

For example, the AA level requires maintaining a contrast between a link and background of at least `4.5:1` for normal font size and `3:1` for large text.

**Note**: _You can always check your colors with the help of the online_[_Contrast Checker_](https://webaim.org/resources/contrastchecker/)_or Figma’s_[_Contrast plugin_](https://www.figma.com/community/plugin/733159460536249875)_._

Measuring contrast by the eye doesn’t always work: for example, green should be darker and more saturated than blue to pass the requirement.

### Focus state

Like all interactive components, [links should have a visible keyboard focus](https://www.w3.org/WAI/WCAG21/Understanding/focus-visible.html). All popular browsers have an embedded accessible focus by default (you might have seen this bold blue frame around input fields, dropdowns, buttons, and links in Google Chrome).

Unfortunately, on some sites, focus gets manually removed or customized so that a focused link looks even less noticeable, for example, faded out.

If you don’t have inspiration for creating a custom focus state, at least keep the standard one.

### Optimization for screen readers

Users with severe visual impairments, including blindness and low vision, don’t see the web in the traditional sense — they listen to it by means of “screen readers,” assistive programs that transform a written text into fast robotic speech. They navigate with a keyboard and remember dozens of handy shortcuts to jump between headings, buttons, or links instead of obediently listening to the entire content on a page.

So, when you remove wordiness for sighted people (for example, in the lists of different language versions or formats), it’s important to keep links clear for screen reader users, too. Otherwise, they will hear the following:

> “Ukrainian — link, English — link, German — link…”

And here are examples of self-explanatory links they should get instead:

> “Download project plan template in Ukrainian — link, download project plan template in English — link…”

But probably the most annoying thing on news websites is this:

> “Read more — link, read more — link, read more — link…”

There are two main ways to put a link on a news page: make each title a link or add auxiliary phrases like “Read more…”

Sighted people can guess that “Read more…” relates to the nearest title, and screen reader users need individualized _read-mores_. Fortunately, the HTML attribute `aria-label` comes in handy here; it enables attaching explanatory text for screen reader users.

In small and medium teams without a separate accessibility function, It’s often a designer’s responsibility to compose accessibility-related text and collaborate with a developer around optimal implementation, so here is a simplified code example:

```
<h4>News</h4><p>Eleks Design Team will participate in the Space Hackathon.
<a href="aerospace-hackathon.html" aria-label="Read more about Eleks participation in the Space Hackathon">Read more...</a>
</p><p>Projector Tech and Creative Institute launches five courses on web accessibility this year.
<a href="new-courses.html" aria-label="Read more about new courses on accessibility by Projector Institute">Read more...</a>
</p>
```

As you can see, each “Read more” has an extended explanation for screen readers. However, you won’t need to take care of article links with `aria-label` if each title is a link itself.

```
<h4>News</h4><h5><a href="aerospace-hackathon.html">Eleks Design Team will participate in the Space Hackathon</a>
</h5><h5><a href="new-courses.html">Projector Tech and Creative Institute launches five courses on web accessibility this year</a>
</h5>
```

### Duplicated links

Multiple identical links are yet another widespread controversial practice. For example, on a web page, it means that the same web address is attached to an article title, hero image, and intro sentence. At first glance, nothing’s wrong: wherever you click — you get to the article. But for screen reader users, it means repeating the same information thrice, which extends the time they need to sift through content to what they are interested in.

It’s better to make the whole block a link rather than create multiple links that guide to the same destination.

**Note:** we are now talking about identical destinations, but a card can include different ones, for instance, a link to the article, author’s profile, and tags. In this case, elements with minor links can appear “wrapped” in the main one.

The click area of the primary link “wraps” the auxiliary ones (author’s profile and tags).

Now, emails. Let’s say we have an invitation to some online event, where a Zoom link repeats several times. In the event description, “what-when-where” section, and closing part. Not only will it create an impression of a mess for sighted users, but also visually impaired users will be troubled with jumping between duplicated links.

One prominent link speaks louder than a bunch of scattered ones.

## Related
[Add wiki-links manually or run update_wikilinks.py]