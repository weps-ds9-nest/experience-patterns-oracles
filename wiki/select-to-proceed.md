# Select To Proceed

## A guide to designing and using selection controls

Whether it’s to personalize content, rate an experience or meet legal requirements, forms play a starring role in our products. Choosing the right selection control for a particular question can be more tricky than you think. Vertical height restraints, copy length, imagery and number of options are all crucial factors.

To help break it down, here is a decision tree.

## Single Selection

### Segmented Control

A segmented control should be used to make a single selection out of 2–6 options. It is best used for iconography, small numbers or short words. It’s design consists of a horizontal container that houses equidistant options with one selected.

Iconography and Short Words vs Currency. Iconography by Meg

**Pros** Putting all of the options on a single line works well for layouts with limited vertical space. The contained background with inset dividers visually connects all of the options.

**Cons** It does not work well for long words or numbers, phrases or prices. If you do choose to put those inside, plan for localizationby offering less options. The horizontal space is very limited and even with less options you’ll still need to decide how your text will truncate.

_Where did the 6 maximum come from? Each option within a segmented control needs to be greater or equal to the minimum tap target size. Math!_

### Radio Buttons

A radio button within a list item should be used for single selections of more than 6 options, a whole lotta content and/or unlimited vertical space. They are most commonly a circle outline that becomes filled upon selection at the start of the list item. iOS has created a new paradigm with the same meaning by putting a checkmark at the end and modern designs have adopted a highlighted stroke that goes around the list item to save horizontal space.

Android & Web vs iOS vs Alternate Pattern

**Pros** Radio buttons inlist items give content the space it needs to breathe. They’re recognizable, can hold multiple text strings, text can wrap and imagery can be large.

**Cons** They are large and in charge. They take up valuable screen real estate and don’t work well for designs with vertical height constraints.

[_Fun fact!_](https://en.wikipedia.org/wiki/Radio_button)_Radio buttons were named after the physical buttons used on older radios to select preset stations — when one of the buttons was pressed, other buttons would pop out._

## Multi Selection

### Choice Chips

Choice chips should be used to make multiple selections out of ~3–6 options. They are best used for one to two short words or numbers. Their design is similar to a small button with a shift in background color for ‘on’ and ‘off’, typically the minimum tap target height.

Although [Material Design](https://material.io/design/components/chips.html#choice-chips) recommends a checkmark at the front of a multi selection chip, I chose to not include it because the most familiar chips are email addresses and they don’t have it either. It also saves on horizontal space.

Short Options vs Long Options vs Wrapping & Shrinking

**Pros** To save space the chips stack in a masonry pattern and their size is determined by the length of text inside. They feel lightweight and fun to interact with.

**Cons** They have similar text length challenges as the segmented control, as in they do not work well for long words or phrases. Text wrapping or resizing is not recommended because it looks unintentional or broken. Using more than two rows of chips can make each button harder to scan.

### Checkmarks

Checkmarks in list items should be used for multi selections of more than 6 options, a whole lotta content and/or unlimited vertical space. They are denoted by a square outline that becomes filled with a checkmark upon selection at the start of the list item.

Checkmark in a List Item

**Pros & Cons** They have the same benefits and challenges as the radio button.

## All Together Now!

It’s easy to get caught up in the design of a particular component, so I find it best to start with the big picture — the form. Through this we can make thoughtful decisions on which option is best for coherency, differentiation and hierarchy.

### Segmented Control & Choice Chips

The background is the biggest differentiator between segmented controls and toggle buttons. A connected background helps the user understand they must choose one, while a separated background indicates they can choose many.

Similar Treatments vs Dissimilar Treatments

The design of the Segmented Control and Choice Chip should feel visually similar to each other and dissimilar to text fields and buttons to aid in hierarchy and visual separation of different interactions.

Dissimilar Treatments vs Similar Treatments

### Radio Buttons & Checkmarks

With so many radio button options to choose from, I find it best to design radio buttons and checkmarks next to each other. The iOS end radio button checkmark and highlighted list item are great alone, but when paired with a checkmark — the radio button wins for consistent placement. It’s confusing to have two checkmarks, you know what I mean?

Android & Web vs iOS vs Alternate Pattern

Last, but not least, imagery position. Selection controls are traditionally in the start position, however, there is a new pattern emerging to place it in the end position when the list is images. We keep the selection control in the starting position because the control and copy are mandatory while the imagery is optional and additive.

Image in the End vs Start Position

### Last Thoughts

Another great single selection control is a [picker](https://developer.apple.com/design/human-interface-guidelines/ios/controls/pickers/). It can be used for when you have many short words or phrases and limited vertical space. It is recommended to place only text in a tumbler, therefore it’s use is very specialized and they are complex to customize in both Android and iOS.

Any controls I forgot and you’d like to share? Please respond below!

_Huge shout out to_[_Yudi_](https://www.linkedin.com/in/yudisun/)_,_[_Assaf_](https://www.linkedin.com/in/assaf-shalev-3a161b2a/)_,_[_Harel_](https://www.linkedin.com/in/harel-sheniak-012b7788)_,_[_Sam_](https://soff.es/)_and_[_Meg_](https://medium.com/@megdraws)_for their thoughts on this! I’m Linzi Berry, currently design systems manager at Lyft. I sweat the details so you don’t have to. Please subscribe!_

## Related
[Add wiki-links manually or run update_wikilinks.py]