# In Praise of Buttons – Part One

In Praise of Buttons – Part One

Form _is_ Function in Graphical User Interfaces

By Nikos Kitsakis, January 2024

In any design discipline there are always certain trends. One of these trends seems to be that buttons are now considered uncool. It doesn’t matter if they are buttons on physical objects or in graphical user interfaces.

Buttons aren’t new. And for exactly that reason, they are uncool. Like hammers and paperclips, they have been around for a long time and they work. In fact, they have been around for a long time _because_ they work.

That is a problem if you’re a dishonest designer. After all, how do you tell your client that you’ve just reinvented the wheel? You can’t just use boring old buttons in your shiny new product. So what do you do? You redesign the look or the function of a button (or both) and sell it as “the newest development in design” – totally dis­re­gar­ding the needs of the user and compromising your integrity as a designer along the way.

Buttons on screens

In graphical user interfaces, we have seen an increase in buttons recently that consist merely of text or icons, without a clear, visible button shape being present. This insipid, uninspired mediocrity, exemplified by Google’s “Material Design” or – even worse – IBM’s “Carbon Design System”, was popularised by Apple’s iOS 7 and its equally miserable “Flat Design” aesthetics. This lazy minimalism is often considered modern and streamlined, but we must ask: Is it also user-friendly?

The answer is clearly: No, it is not!

Consider the image below: In the first row we see a series of icons that are supposed to be buttons. The only way you could potentially recognise them as such, however, would be if they were implemented in a user interface. So it is in fact only the _context_ that lets you recognise them as buttons, not their _appearance_ by themselves.

![Image 1: Two rows of buttons. The first looking only like icons, the second like actual buttons.](https://www.nubero.ch/blog/009/pictures/buttons_a.png)

Two rows of buttons. Which appear more inviting to interact with?

Compare the icons in the upper row with their counterparts in the lower row. Here, these same icons are embedded in button shapes. This does several things at the same time. First, the button shapes act as _signifiers_. That means that they let the user know that an action can occur there. The icons in the upper row do no such thing. They don’t commun­icate their ability to be pressed – to be _used_ really – in any way.

How important signifiers are becomes clear when you look at the physical objects around you. Take the Swiss Army Knife in the picture below for example. The small groove that you see in the main blade (and in almost every hinged tool of a Swiss Army Knife) is called the “nail nick”. Not only does this nail nick allow you to insert your finger­nail and pull the tool out, it also _looks like it allows for precisely that._ Pay attention to its exact shape too. It mirrors the slight curvature of a fingernail. And it doesn’t stop there: The angles of the walls _inside_ the groove are contoured in such a way that your fingernail is guided deeper into the nail nick, ensuring a secure hold for pulling.

![Image 2: A Swiss Army Knife showing the nail nick in the main blade.](https://www.nubero.ch/blog/009/pictures/sakb.jpg)

This is the nail nick in the main blade of a Swiss Army Knife. It gives the user a clue that an action can occur here and that this action probably involves a fingernail.

This should make it clear why there is a reason that the virtual buttons in our graphical user interface should indeed look like buttons: They should commu­nicate that they can be used. When they just look like icons, they don’t do that.

Look at the image of the buttons once more, and this time, try to find groups that belong together. The icons for plus and minus and for left and right for instance form two groups while the magnifying glass stands separated. In the lower row, where the buttons have uniform shapes, it’s easier to notice the differences in spacing between them.

There is another thing to consider. Take a look at the next picture.

![Image 3: The two rows of buttons again. Now with a pink highlight to show where they can be clicked or touched, respectively](https://www.nubero.ch/blog/009/pictures/buttons_b.png)

The buttons in the upper row not only _communicate_ what they do badly, they _function_ badly as well.

The pink colour shows where a button can actually be clicked or touched, that is to say, it shows the region where the software will register an input. In the upper row, that is quite a small area if you think of it in terms of square-pixels. That being said, the clickable area in mouse-interfaces _might_ sometimes be the same in the upper row as in the lower row[¹](https://www.nubero.ch/blog/009/#footnote01). In touch interfaces however, that is often not the case. There, the actual outline of the graphic – let’s say the minus – is often the only thing that can be touched. So when you quickly tap your screen and don’t hit the target precisely, you might completely miss the button.

Text in buttons

The importance of button shapes becomes even more apparent, when the buttons are actually just words, not icons. The example below shows the Terms and Conditions of an iOS update. You can see that the two words, “Agree” and “Disagree”, don’t stick out too much in an environment that already has a lot of text in it. Apple’s way of showing the user that the two words are actually buttons is done solely with colour. The default option of agreeing is also not differentiating itself enough from the disagree option. The only difference is a slightly bolder (but not really bold) typeface. And lastly, speaking of type­faces, the one that Apple chose – specially designed actually – is also not the best for user interfaces.

![Image 4: The Terms and Conditions as they appear in iOS 16](https://www.nubero.ch/blog/009/pictures/tca.png)

Everything that can go wrong, will go wrong: The people who designed this blindly followed the notion, that removing everything they perceived as ornamental would result in simplicity.

Now compare the example from Apple above with my redesign below. Look at the difference that the button shapes and a better choice of typeface make. The typeface in question is called “FF Unit” and has less ambiguous letter shapes than Apple’s “San Francisco”. Granted, this is less important in long text than it is in individual words, but since we want the same typeface for both our buttons and the legal text, choosing a typeface _like_ FF Unit becomes rather obvious. Lastly, I used a slight shadow to set apart the scrollable text of the Terms and Conditions from the surrounding interface. This too makes for a better visual distinction between the different elements on screen.

![Image 5: The Terms and Conditions redesigned](https://www.nubero.ch/blog/009/pictures/tcb.png)

Just because a user interface uses 3D-buttons and some shading doesn’t mean that it has to look tacky. In fact, if you have to make the choice between tacky-but-usable and minimalistic-but-hard-to-use, tacky is the way to go. You don’t have to make that choice though: It’s perfectly possible to create something that is both good-looking _and_ easy to use.

Direct manipulation

The physical world that we evolved in is one where every action has an effect. When you push the coffee mug on your desk and it moves away from you, it will make a sound. You might also be able to see little waves forming in your coffee as the small vibrations from the mug sliding on the desk transmit to the liquid. All of this feedback is expected by our brain to come to us through our different senses.

Researching and writing these essays takes a lot of time. So if you enjoy them, consider supporting this work with a small donation.

[Support!](https://buymeacoffee.com/nuberodesign)

Think about what this means: You will get haptic feedback through your fingertip, giving you information about weight, temperature and texture. There will be acoustic feedback from the ceramic sliding on your desk. And you will get visual feedback from seeing your finger and the mug moving, and the little waves on the surface of the coffee. Since our brain builds a model of the world and then compares reality to it[²](https://www.nubero.ch/blog/009/#footnote02), these different feedbacks are both _expected_ and _interconnected_. It would be extremely weird, for example, if the mug did not make any noise at all while it slides across the table or if the liquid wouldn’t move inside the mug[³](https://www.nubero.ch/blog/009/#footnote03).

A button in a graphical user interface that has no button shape will likely give you no feedback either. While it might actually have an alternative state that gets activated when you touch it (a change of colour for instance), you are probably going to obstruct that with your finger. This is another advantage of buttons that look like buttons. Because they usually stick out from under a fingertip, you can see the press-down animation clearly. Direct feedback from direct manipulation. See the animation below:

While the user cannot be sure that his tap on the upper arrow was registered by the device (and might therefore try multiple times), the “button depressed” state of the 3D-button signals to him that his action was successful.

Why is this important? First of all, it should be self-evident that a feature of the world that our brains evolved around, namely feedback, should not be removed just to satisfy a fashionable trend. As mentioned above, we expect some sort of feedback from practically everything in the world. But there’s another thing to consider: The button you just pressed might make some webpage load or do something else which will take a second or more before its effect is apparent. While you wait for that to happen, a button that showed you that it got pressed – that gave you feedback – is going to give you reassurance that you actually tapped it correctly.

Visual feedback is, of course, just one way to solve this. Acoustic or haptic feedback also works well. Even better is a combination of these. Remember the coffee mug, whose weight and vibration you can feel, while you also see it moving and hear it sliding across the table. This sort of multi-sensory feedback is what you should be going for – if the circumstances allow it.

![Image 6: Album buttons](https://www.nubero.ch/blog/009/pictures/gallery1/image1.jpg)

One last example: Here you can see the Photos app as it appears in iOS 17, and a redesign done by me. Apple is using lazy button shapes for “Select” and the ellipsis character (…) on the right. On the left however, the button for going to your albums is just the word “Albums” and a little blue arrow shape. Why those two different concepts on the same screen? In the redesign, everything that works like a button also looks like one. This, in my opinion, is how it should be done.

Misguided sentimentalism?

Critics of my position may point to what they believe is some sort of sentimentalism for old user interfaces on my part. It’s true that the problems I point to in this piece are of the kind that I consider solved in many of the older user interfaces. That has nothing to do with being sentimental however. Products have to work properly. If a button is the right choice, use a button. If it’s not, don’t. But if you are going to implement a design element that _works_ like a button, it should _look_ like one too.

1.   [](https://www.nubero.ch/blog/009/)In many graphical interfaces that expect a mouse as input, the programmers will make the clickable area of the upper row buttons the same as the lower row ones, although this will be invisible at first. You can hover with your mouse over the buttons and _then,_ magically, a button shape will appear. It’s not going to be a nice 3D-button shape however but just an outline. This serves no functional purpose. For instead of showing the user where all the buttons are from the outset, the whole affair becomes sort of a hide and seek game, where users have to guess which item they might be able to click.[↑](https://www.nubero.ch/blog/009/#footnote01Source)
2.   [](https://www.nubero.ch/blog/009/)There’s a very good book by Jeff Hawkins on the topic of how our brain works called [“On Intelligence”](https://en.wikipedia.org/wiki/On_Intelligence). I highly recommend reading it. You will learn a lot about pattern recognition, feedback and many other topics that will be of use to you as a designer.[↑](https://www.nubero.ch/blog/009/#footnote02Source)
3.   [](https://www.nubero.ch/blog/009/)The scene with the blood coming out of the elevator in “The Shining” is eerie for that reason: You would expect that a large amount of liquid makes a tremendous noise but there are no sound effects, only some weird music – or rather sound – in the background. So what you get as feedback from that scene doesn’t match your experience of reality, taking you to a different realm that feels somehow off. Good in a spooky film, bad in a product you are supposed to use.[↑](https://www.nubero.ch/blog/009/#footnote03Source)

Does _every_ virtual button – every button in a graphical user interface – have to look like a pressable, physical 3D button? Of course not. They also don’t need to look exactly like my redesigns either. On a case-to-case basis it might even be better to do some­thing else entirely. I’m using lazy button shapes myself on this website. But a website is not an operating system.

The whole idea is to reduce cognitive load. And since the brain works by recognising patterns and dividing the environment up into areas, this reduction is best done by making elements with different functions appear markedly distinct from one another. It is, in other words, a fallacy to believe, that the brain has an easier time if everything looks “simplified” in the way which happens with the flat design doctrine. The opposite is the case.

There is a discussion about this article on [Hacker News](https://news.ycombinator.com/item?id=39201772). Also, if you would like to share it on social media you can do so on [Twitter/X](https://x.com/nuberodesign/status/1749861418172604545) or [Instagram](https://www.instagram.com/p/C2cV2TBKfjZ/?igsh=MXZpN2FkMmc4ZHlzMg==).

Founded by Nikos Kitsakis in 2016, Nubero­design spe­cia­lises in vis­ual com­mu­ni­ca­tion, user ex­pe­ri­ence, and product de­sign. Write us [a message](mailto:contactATnuberoDOTch)!

Researching and writing these essays takes a lot of time. Please consider supporting this work with a small dona­tion.

[Support!](https://buymeacoffee.com/nuberodesign)

## Related
[Add wiki-links manually or run update_wikilinks.py]