# What if your client or stakeholder asks to make the dashboard you prepared to be more eye-catching, beautiful, or just cool? They are never led by evil intentions to confuse, distract or annoy the end reader, but out of ignorance, they believe the value of the dashboard lies within good user interface design only.

What if your client or stakeholder asks to make the dashboard you prepared to be more eye-catching, beautiful, or just cool? They are never led by evil intentions to confuse, distract or annoy the end reader, but out of ignorance, they believe the value of the dashboard lies within good user interface design only.

While user interface (UI) is undoubtedly important, some visual enhancements done without thinking about the overall user experience (UX) might lead to [confusion, distraction or frustration](https://chartplanet.net/dataviz-best-practices-three-enemies/) for the end reader.

But we can be sure about one thing — if someone asks for nicer visuals, they will be very unhappy if the report author cannot deliver that. When they ask for nicer visuals, they really want a not boring, nice-to-look-at and easy-to-use product. In such cases, we have one job — a very subtle one — to enhance UI without sacrificing UX, dataviz or information designs, maybe even enhancing them altogether.

In other words — to make the dashboard cooler, but still safe to use. (I’ve heard that exploding pie charts can be found within cool dashboards — beware!)

Here I suggest 10 techniques how to do exactly that, and in my next article, I will describe 9 techniques to better skip.

**1. Draw background separately**

This is the number one visual hack to try. It is probably possible to create various boxes for your visuals, divisions between sections, add logos and icons within the tool you use, but often it’s not that easy and convenient to do so, and after that is done you can accidentally select and drag those background elements, resulting in irresistible urge to never bother yourself again with such annoying work!

The trick is to draw the background in another tool — PowerPoint, Figma, Canva — you name it, save it as a PNG file and import it as a background.

In Power BI upload the canvas background picture and make it fit ([more instructions here](https://guyinacube.com/2019/04/23/power-bi-report-custom-background/)), in Tableau create one tiled image container, and float visuals on top ([more instructions here](https://godatadrive.com/blog/how-to-make-custom-backgrounds-for-your-tableau-dashboard)).

Immediate benefits — those background images are now locked and you will never accidentally select one, also you can reuse the same image on other pages, and finally — since you have fewer objects on a page, the page should load faster.

Less immediate benefits — now you have a part of your workflow solely dedicated to creating a template that you might reuse. This improves consistency. Now you have a part of your workflow solely focused on UI. This improves the visual appeal of the final product no matter what level is your visual skill.

What to add to that background image? Consider several of these components:

*   Logo.
*   The title of the dashboard.
*   Separated section (box) for filters.
*   Separated section (box) for menu.
*   Boxes for visuals.
*   Separators between sections or separate boxes for them.
*   A non-annoying and relevant image for the title.
*   Words that may be repeated on every page, like “Filters”.

_Looks a bit more organized, doesn’t it?_

A few of the next techniques are to enhance a created background even more.

**2. Round corners**

This quite simple technique always adds a bit of playfulness to the dashboard. While straight corners are default options and often look stricter, rounded corners of boxes or sections add a bit softer, bubbly look, without compromising on data accuracy.

_A dashboard you want to cuddle._

To not mess up the view completely, keep the roundness of the corners consistent. And a good thing is, most tools do not allow creating rounded bar charts easily!

**3. Shadows**

This is another simple technique that makes the dashboard look a bit like a real-life thing.

_This is the 3D effect allowed on dashboards._

Still, those shadows need to be consistent, because either they resemble the natural look, or they look messy. The light should come from one side, thus the shadows always drop in the same direction. For an even better effect try emulating natural lighting which happens to be in the office — a lightbulb hanging above. However, if shadows are too big — this implies the element is far from the canvas — this might give a distracting result, elevate them just a few millimetres, which is enough to give a 3D effect.

**4. Use more colours**

Colour in a dashboard is a huge topic and I’ll write an article about that. For now — read [all that Lisa Muth has written for you](https://blog.datawrapper.de/emphasize-with-color-in-data-visualizations/).

The best practice is to use as few colours as possible — this creates that minimalistic Scandinavian look everyone is supposed to love. But not all of us live in Scandinavia, so let’s add more colours to escape the permafrost and embrace other cultures existing on Earth (creating a bit more cool-looking dashboard on the way).

_When minimalism eats itself._

But still, to prevent the visual from looking messy, add colours one by one, and make sure they **encode** something. We can add redundant encoding to different KPIs even if they are in separate charts, add a different colour to the titles, filters, buttons or add more colours to the background distinguishing menu area, title area and area for visuals. How confusing it is when rectangular bars in a bar chart look exactly the same as rectangular buttons and filters and sections and …!

**5. Use icons**

Carefully selected icons really enhance the readability of the report. Use them in places where their meaning is obvious, and would enhance comprehension. Make **text** an addition to the icon instead of the **icon** being a mere illustration of a text.

While icons add benefits for readability, they are also visual elements, so they add to the overall visual experience — if they blend in nicely, the report will look better and more unique.

_Little images to speed up the navigation._

It might be a bit difficult to find an icon that aligns well with the overall style. Try using the [Flaticon](https://www.flaticon.com/) website or refer to your brandbook, sometimes companies have their default set of icons.

**6. Add real buttons**

We can make buttons look like buttons.

Maybe they can have a slight 3D effect to imply they can be pressed. Maybe they can have a background colour to indicate **where** can they be pressed. Maybe they can have a hovering effect, to indicate they’re interactive pressable things. Or they could emulate the look and feel of tabs everyone browsing the internet is so used to. All these enhancements add some usability and convenience, but also look good.

_Can I swipe these?_

Making the buttons too styled when the dashboard itself is plain, will create an imbalanced look. Also heart-shaped or neon-coloured buttons will attract too much attention — we want them to be visible, but not stand out. Even in the example above they stand out a bit too much.

**7. Try the layout not tried before**

Introducing some novelty, and doing things like no one has ever done before definitely adds some cool vibes. But if we try doing something that no one in the **world** has ever done before, this will be extreme and maybe not for every business dashboard. Let’s try doing something new within the company, department, or just within the set of dashboards on the same topic.

One idea might be trying a bit different layout. We all know the standard layout where the menu is at the top, then there are [BANs](https://datavandals.com/B-A-N) and finally the place for charts. Let’s try moving the menu to the left or BANs to the left or putting the main chart in the middle or moving the filters that are rarely used to the very top… I need to stop suggesting here and leave some areas of creativity for you.

_We read from left to right (in most places)._

Ensuring a smooth reading experience is an absolute must here — introducing a novel layout is always a bit disorienting, but let’s be sure it’s worth it. Also, try prototyping — create several options and choose something that really works better — challenge your predefined perceptions, but do not abandon the usability. Finally, specific care needs to be taken not to disrupt user expectations — if all dashboards in the organization really look the same, users might be just used to some layout, and deviating from it might be a huge risk, so introduce one if it really really looks better, and adds to the ease of usability.

**8. Remove some lines**

Lines are usually the default option when constructing a layout — they are useful for the separation of sections, placed around an element they create a border. But they often look like clutter and I don’t know why.

Just try replacing borders with a slight background, separate sections with whitespace and more often than not the dashboard will look better. Having a background instead of a border allows for some freedom to deviate from a strictly rectangular shape.

_I could have picked a heart shape for BANs, but didn’t._

Notice, that in the example gridlines in the bottom right chart also disappeared. But at the same time, the filter at the top gained a border — a bordered area often means input possibility, let’s use this association!

**9. Try fancier fonts for titles**

Titles are usually big texts, so they are always legible, also they are not read as often as labels. To add some cool effect and non-distracting variation we can change the font of the biggest ones.

_An opportunity for Comic Sans._

The font should be still legible, and not interfere with the overall look and feel of the dashboard. Extra bonus if it aligns with the brand very well.

**10. Use combo charts**

A combination of charts might be a very distracting experience if done wrong. But if done well — they will definitely look cool and novel. And even more important — it allows for more data density! Try combining basic charts — bars with dots, clustered bars with simple bars, lines and dots — if the basic data encoding (bars, dots, lines) is there and axes are clear — there should be little compromise on readability.

_Data is repeated because I was too lazy to create more data._

Overdoing combo charts will lead to complex and fancy-looking things that might be just too difficult for business users to understand. Let’s stick to the principle “know your audience” and combine within their level of knowledge!

**Feel free!**

If these techniques are applied carefully still considering the [three enemies of visualization](https://chartplanet.net/dataviz-best-practices-three-enemies/) they might make our dashboard look much cooler to stakeholders and have no usability trade-off for end users.

Staying on the safe side, and just going with perfectly tuned best practices always leads to the feeling of digital sameness, while trying to introduce some variety can lead to bad experiences, so introducing coolness is a risky business. It is just for those who dare!

May these 10 technique ideas guide your decisions and help you create better data products!

_Images created with Power BI._

## Related
[Add wiki-links manually or run update_wikilinks.py]