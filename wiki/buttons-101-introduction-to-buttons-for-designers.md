# Buttons 101 Introduction To Buttons For Designers

## Buttons: The Beginning (hehe…Bahubali reference)

Welcome to Button 101!!! We’re starting with the fundamentals of buttons. If you haven’t read my previous article, [here’s the link](https://medium.com/@laxmanradhin/everything-about-buttons-youll-ever-need-to-know-be359612161f). Go check it out!

## What are Buttons?

At their essence, **buttons are one of the primary UI elements in interactive design.** Let’s cut the bullshit. A button is a graphical user interface (GUI) element used to **initiate an action or process**. With their distinctive visual appearance, buttons guide users through an interface, whether it’s executing a command, submitting a form, or navigating to the next step.

In simple terms, **a button is a design element that allows users to take action.** Every click moves the user closer to achieving their goal.

> Google defines effective button design with **three key principles**:
> 
> 
> **Identifiable** — Users should **immediately recognise** it as a button.
> 
> 
> **Findable** — It should be **easy to locate** within the interface.
> 
> 
> **Clear** — The **action** it performs must be **obvious**.

## Anatomy of a Button

### 1. Color / Background Color of the Button

Web Content Accessibility Guidelines (WCAG) provide established standards that designers must follow to create inclusive digital experiences.

To verify your designs meet these standards, use [online contrast checkers](https://webaim.org/resources/contrastchecker/) and ensure WCAG 2.0 compliance during the design phase. This prevents accessibility issues from reaching your users and saves costly revisions.

**Breaking established colour conventions creates unnecessary cognitive friction.** Consider the confusion a green “Delete” button would cause, or the hesitation users would feel encountering a red “Save” button. These unexpected colour choices force users to pause, read carefully, and question their assumptions, adding unnecessary steps to what should be intuitive interactions.

Despite their advantages, rounded corners aren’t universally appropriate. **Pill-shaped buttons can sometimes be mistaken for tags, filters, or labels, creating confusion about their interactive nature.** Users may hesitate, wondering whether these elements are meant to be clicked or simply provide information.

Practical layout considerations also matter. When multiple buttons need vertical stacking, **sharp or slightly rounded edges tend to align more cleanly, creating tidier visual arrangements**. Excessive rounding can make precise alignment challenging and create awkward spacing issues.

> Design systems provide guidance on appropriate corner radius usage. For instance, Apple’s Human Interface Guidelines **discourage using fully rounded buttons as primary actions**.
> 
> 
> Their concern centres on maintaining clear distinctions between buttons and other UI elements — when everything becomes too rounded, users lose important visual cues about element hierarchy and function.

### 3. Shadow

Shadows serve as powerful visual tools that **transform flat interface elements into dimensional, engaging components**. When applied to buttons, shadows **create the illusion that elements are floating above the page surface**, naturally drawing user attention and establishing clear interaction cues.

This effect taps into our **internalised mental framework of real-life push buttons**, leveraging familiar physical interactions to create that authentic feeling in digital space.

> Higher button elevation levels produce stronger shadows, while lower elevation levels create weaker shadows.

This **shadow intensity** directly communicates importance, helping users **immediately identify which elements deserve the most attention**. The elevation system creates an intuitive visual language where **shadow strength correlates with action priority.**

> Primary call-to-action buttons receive the strongest shadows, secondary actions get moderate elevation, and tertiary options use minimal shadow effects, creating a clear visual ranking system.

Shadows can also be used to indicate different states. [Material Design](https://material.io/design/environment/elevation.html#depicting-elevation) does this particularly well by making the **button come ‘closer’ to you on hover.**

**Inner shadow is a great way to add depth and dimension, especially in dark themes**, making the whole product experience smooth and enjoyable. Such a visual trick embedded into a button provides a subtle visual cue to the user, indicating that this UI element is clickable.

### 4. Labelling

Effective button labelling begins with one fundamental principle: **clarity**.

Users should instantly understand what will happen when they interact with a button. A “Download” button should lead to downloading content, while an “Add to Cart” button should add items to a shopping cart. This **clarity eliminates confusion, creating a smoother user experience.**

The key to achieving this clarity lies in consistency. **Establishing labelling rules** early in a project saves countless hours of revision later. These rules should cover everything from **word count to case style**, creating a cohesive system that users can learn and rely on.

> Establishing consistency requires making deliberate choices about 4 **key elements:**
> 
> 
> **Word count**: Decide whether your buttons will use one word, two words, or longer phrases. Stick to this decision across your entire interface.
> 
> 
> **Case style**: Choose one case approach and apply it universally. Mixing case styles within the same interface creates visual chaos.
> 
> 
> **Label structure**: Define whether you’ll use simple verbs (“Save”), verb-noun combinations (“Save post”), or other structures. Consistency in structure helps users predict button behaviour. Most effective buttons contain **action verbs** that clearly indicate their function. Words like “Save,” “Publish,” and “Edit” immediately **communicate the button’s purpose**.
> 
> 
> Consider using a **“verb + noun” structure for maximum clarity**. “Save post” is more descriptive than simply “Save,” and “Next step” provides better context than just “Next.” This approach makes actions more prescriptive and reduces user uncertainty.
> 
> 
> **Font style:** The visual presentation of button labels has a direct impact on usability. **When selecting fonts, prioritise legibility above all else**.

**Case Style Guidelines:** The choice of case style should align with your platform’s personality:

> **All caps (e.g., “NEXT SECTION”)** work well for **professional platforms**. Material Design demonstrates how **uppercase labels can create a clean, authoritative appearance.**
> 
> 
> **Sentence case (e.g., “Next section”)** creates a **friendly, conversational tone**. This approach feels more approachable and works particularly well for **consumer-facing applications**. Note that despite being called “sentence case,” you should avoid adding periods to button labels.
> 
> 
> **Title case (e.g., “Next Section”)** falls **between professional and conversational tones**, though it can be less readable than sentence case.
> 
> 
> **Lower case (e.g., “next section”)** creates the **most casual tone** but should be used sparingly, as it may appear unprofessional in many contexts.

### 5. Padding

**Vertical:** Most designers will say something like, “Buttons should have a height of 36 pixels”. This isn’t the best approach. People with visual impairments may increase the font in their browser, and consequently, they need the font size to change without the button height cutting it off.

Developers create buttons by adding **padding to their div containers, not height.**

**Horizontal padding:** There are 2 ways to approach horizontal padding.

**First option: Make the button width align with the grid**. This is a nice way of keeping all your buttons a consistent length. It does, however, limit the number of words you can use.

**Second option: Have fixed padding on the sides**. I also usually add a clause for a minimum width of a button, to avoid really small buttons. While this allows for the case where you can have different amounts of text, it can make your buttons very uneven.

### 7. Button Size

The size of a button directly impacts how **easily users can find it, identify its purpose, and successfully interact with it**. This becomes particularly crucial on mobile devices, where buttons function as tappable elements that must work within the physical constraints of human fingers.

When mobile buttons are too small, users face a cascade of frustrations: **missed taps, accidental selections, and unintended interactions**. These seemingly minor issues can quickly escalate from mild annoyance to serious problems during critical moments like checkout.

The solution is straightforward: **ensure important buttons are appropriately sized and follow established accessibility guidelines.** This approach not only enhances user experience but also eliminates friction in essential user journeys.

MIT’s Touch Lab conducted foundational research in 2003 that revealed **most fingertips measure 8–10mm in width**. This physical constraint became the basis for modern touch target recommendations, establishing minimum sizes that accommodate real human interaction patterns.

[https://uxdesign.cc/button-design-user-interface-components-series-85243b6736c7](https://uxdesign.cc/button-design-user-interface-components-series-85243b6736c7)

Based on platform guidelines and usability research, aim for touch targets of at least **44x44 pixels, with 54 pixels being a more comfortable minimum for most users**. This sizing reduces user errors and creates more confident interactions.

For desktop interfaces, while smaller sizes are technically feasible, consider maintaining larger sizes for important actions. The slight increase in button size often improves usability without significantly impacting layout efficiency.

**iOS Touch Standards:** Apple’s Human Interface Guidelines recommend a **minimum target size of 44 pixels wide by 44 pixels tall**. However, many designers consider this truly a minimum threshold. In practice, **this size can still feel cramped for reliable interaction**. The physical limitations of adult fingers suggest that larger targets often provide better user experiences.

Apple’s approach **emphasises consistency across its ecosystem**, ensuring that users develop reliable interaction patterns that work across different iOS applications and screen sizes.

**Android Material Design Standards:** Google’s Material Design takes a slightly different approach, recommending touch targets of **at least 48 x 48 density-independent pixels (dp)**. This sizing translates to approximately **9mm in physical space, regardless of screen size or pixel density**. The **guidelines suggest that 7–10mm represents the ideal range for touchscreen elements.**

Material Design also acknowledges that **larger targets may be appropriate for specific user groups, such as children developing motor skills or users with accessibility needs**. This flexibility allows designers to adapt standards based on their specific audience requirements.

[https://uxdesign.cc/button-design-user-interface-components-series-85243b6736c7](https://uxdesign.cc/button-design-user-interface-components-series-85243b6736c7)

### 8. Icon

In a button, you have the label text and a placeholder for the icon. These two elements can be rearranged in different ways to create effective designs.

Start by deciding on the padding: left, right, top, and bottom. When you have a trailing or leading icon, you might want to keep the left and right padding consistent with text-only buttons.

However, icons can create symmetry issues because they sit within their own frames with additional padding, which compounds with the button’s padding.

Text line height also affects visual balance, often requiring extra padding to achieve optical symmetry.

**Icon Sizing Strategy**

The trickiest aspect when combining icons and labels is determining the proper icon size relative to the font. You have two viable options:

*   **Option 1:** Make the **icon size similar to the cap height of the font**
*   **Option 2:** Make the **icon significantly larger than the line height.**

**Critical warning:** If the icon is only slightly bigger than the cap-height, it will look unbalanced or like a mistake. Icons should either match the cap-height approximately or be much larger — avoid anything in between.

The icon’s meaning must be crystal clear to users. When users don’t understand an icon’s meaning, they tend to avoid interacting with it. This is why many designers say “the best icon is a text label.”

**Choosing the Right Icon Pack**

Select icon packs that meet these criteria:

1.   Open-source Figma community file availability
2.   NPM compatibility
3.   Both solid and line-based icon variants

**Recommended packs:** Remix Icons, Box Icons, and Feather Icons all meet these requirements through Figma Community and npm distribution.

That’s the end of our first module. I hope you learned something new from this blog. If you could please share your thoughts so that I can improve to do better next time. The next article will be on button styles and states. Till then, bye-bye!

## Related
[Add wiki-links manually or run update_wikilinks.py]