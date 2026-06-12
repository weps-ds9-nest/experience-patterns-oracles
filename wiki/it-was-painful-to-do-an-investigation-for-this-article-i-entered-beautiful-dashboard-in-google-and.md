# It was painful to do an investigation for this article — I entered “beautiful dashboard” in Google and my eyes started burning — so many disastrously ugly and barely readable dashboards were marketed as “attractive and beautiful”, so many vendors claim to provide you with “stunning data visualizations”, and when I see those visualizations — I’m really stunned because I have no idea how to read them.

It was painful to do an investigation for this article — I entered “beautiful dashboard” in Google and my eyes started burning — so many disastrously ugly and barely readable dashboards were marketed as “attractive and beautiful”, so many vendors claim to provide you with “stunning data visualizations”, and when I see those visualizations — I’m really stunned because I have no idea how to read them.

And the worst of the worst are AI-generated dashboards — beautiful they really are, AI is not even trying to make any sense in them.

5 out of 8 first results had a donut chart, and 6 had area charts. Are those the most beautiful charts?

We do want to make beautiful dashboards because beauty is attractive, looks tidy, reliable and helps to create impact with our visualizations. But beauty is also just a package — the value of a dashboard is in the way it helps to read the data intuitively. Forgetting all other things except beauty might lead to poor readability and a confusing experience overall, making users more frustrated than happy.

In my previous article where I suggested techniques [for making dashboards look cool (and beautiful)](https://chartplanet.net/cool-dashboard/) I added some words of warning for every suggestion. In this article, I will simply forbid you from doing some things. Of course, I am not in a position to forbid anything to anyone … but you have been warned.

So here are the 8 techniques to avoid if you do not want to break the readability and overall user experience in your dashboard.

## 1. Use cool charts just because they are cool

So you want to make a dashboard look cool and you start thinking — what cool chart should I try this time? — STAHP!

While cool charts might look more beautiful than simple charts, the reason they’re rare is because they are harder to read and harder to comprehend. The data literacy of business users reading those dashboards varies a lot, and most of them are only comfortable reading bars, dots and lines.

Some people think, that pie charts are bad, and instead opt in for a cooler and “not-that-bad” option — a treemap. This cool chart serves quite a different purpose, shows hierarchy, so it makes the original intent — part-to-whole comparison more difficult.

Some people think that maps look cool on dashboards. But while they are deceptively familiar (we all look at maps often while driving), they serve quite a different purpose than often needed in a dashboard. We rarely want to show geographical patterns, more often the point is just to show data by country, and a simple bar chart serves this purpose much better.

Some people wait for their chance to try chord, sankey, or other cool data visualizations which they saw in some fancy award-winning data journalism article. However, those charts cover very specific cases, which, sadly, are rare in dashboards. I saw a chord used sensibly in a dashboard only once — that one indicated passenger traffic between stations.

If you wonder how these things appeared in Power BI — they are R visuals.

The point is to choose the most appropriate and most interesting chart for the comparison you want to make. Data first — chart later. If you are picking a chart first and then looking for data, you’re doing data art (or [design driven data visualization](https://www.amazon.com/Questions-Dataviz-Design-Driven-Visualisation-Visualization/dp/1032139447) as coined by Neil Richards). Which is fine, but maybe not for a dashboard.

If you have trouble with choosing charts — [try recommendations by Nick Desbarats](https://www.linkedin.com/pulse/choosing-chart-type-harder-than-you-think-nick-desbarats/) — they will make your life simpler (_evil laugh_).

But if you insist on a nice image — add an image of a cat instead of another chart. Cats have won the internet, they are universally more loved than charts.

## 2. Use background images

So you want to make a dashboard look cool and you start thinking — what if I added a beautiful image in the background? — STAHP!

It’s simple — background images might interfere with texts and charts making them harder to read. Some experts will say that it will distract the attention — but if you consider the beautification of your dashboard — you’re already fine with some distractions. The more serious problem is that the background image might not align with your layout very well and in combination with other objects, it will **not** look as beautiful as expected.

An AI-generated busy city reflects the busy schedule of someone looking at a dashboard, it will look so relatable.

What to do instead — add a plain colour background and that’s it. Some experts would even argue against that.

But if you insist on having spectacular scenery — then add extra effort to integrate your charts into that scenery, not just throw them on top. In the example below the sky is reserved for dashboard title and BANs, while the charts reside on the crop field. Would be great if there were no tracks in the field because they are distracting and interfere with legend, but AI was too stubborn — “ _But you need tractors to look after the crops, don’t you?_ _So they are going to leave tracks!_“

## 3. Use images of people

So you want to make a dashboard look cool and you start thinking — if I would just add stock photos of office people the dashboard would look more attractive and relatable? — STAHP!

Eye tracking studies constantly reveal again and again that people are attracted to look at people, faces are the number one thing they pay attention to. What would you choose yourself — a smiling face or a bar chart?

So, putting faces or images of random, stock people introduces **massive** distraction. If you include a photo that represents the “persona” the dashboard is about — you might still introduce unnecessary biases by representing a typical office worker as a middle-aged white man dressed in a suit while this might or might not be true. In my company, it’s not.

The prompt was: “a very generic smiling office man with suit”. Stop looking at him, look at charts.

But what to do if there is some empty space left? Leave it empty! Utilize it to move other charts a bit more apart, or maybe resize them a bit.

If you insist on filling space with a relevant image representing the topic on the page, then add a more abstract image or even better — an icon representing that topic. If you’re doing a dashboard for a pet shop about cat food sales — maybe that is your chance to add an image of a cat.

Now you know what is the dashboard about — it’s about stars.

## 4. Smoothing things where inappropriate

So you want to make a dashboard look cool and you start thinking — let me just round all the corners, users will be so satisfied with its look and feel! — STAHP!

While I suggest rounded corners of graphical elements, data representing elements should still be edgy. There is a great debate whether smoothing a line chart [is a good idea or not](https://www.linkedin.com/pulse/smoothed-line-charts-ok-nick-desbarats-iagvc/), but it boils down how to much distortion this smoothing adds. Power BI and Excel users can smooth charts out of the box using splines — and those behave weirdly! Another problem — when the line is smooth it might be difficult to understand what is the time-frequency of the chart — do we have a data point for every month or every day? When that chart is jagged — frequency becomes obvious!

How many data points are there in the line chart?

Making rounder bars is even more difficult in probably all the BI tools ([while it’s relatively easy in Excel — youtube link](https://www.youtube.com/watch?v=8g9DK5noi1s)). However, I’ve seen financial presentations where bars had perfectly rounded ends in all cases. Distortions are obvious and comparison is impossible.

Source: Lithuanian Railways Annual Report 2020

It might be a good idea to add all this smoothing when you want to demonstrate that some values are not exact, rounded, or uncertain. So, to make the chart look better might not be the only use case for smoothing.

Interestingly, Tableau users do not have any smoothing out-of-the-box so they do it themselves with a bit of hacking. You might see a lot of examples on Tableau Public with beautiful curves and most of them are not those naughty splines, they use sigmoid curves instead — these add less distortion and in my personal opinion look more beautiful. So, if you insist on some smoothing — use sigmoid! To do this in Tableau — learn about [data densification](https://www.flerlagetwins.com/2019/05/intro-to-data-densification.html), to do this on Power BI — you will have to invent your own way to include those intermediary data points.

Line chart is still a Power BI core visual.

## 5. Fancy fonts for data

So you want to make a dashboard look cool and you start thinking — now I will find a cool-looking font and use it everywhere! — STAHP!

The problem with text in data visualization is that it is all around the place in varying sizes and colours. There is a title, then a subtitle, then axis titles, which are often rotated, then axis values, which are often light grey, then data labels and finally tooltips. To make this mess as readable as possible we have no freedom to choose whatever font we like — we must stick to fonts which are easy to read even in uncomfortable positions.

Fancy handwritten fonts can be only OK in limited places — as in maybe page titles, logos and probably that’s it.

If you insist on using Comic Sans — you can try. This one is [readable to even people with dyslexia](https://www.nothingcomicaboutdyslexia.com/), just have a bad reputation within some communities.

## 6. Use animations

So you want to make a dashboard look cool and you start thinking — animation is so trendy in dataviz right now, I should use it to grab the reader’s attention! — STAHP!

I’ve seen a Power BI dashboard with animated visuals created with HTML. The first time I opened it there was this WOW effect — something is moving! HOW DID THEY DO THIS? Moving elements is not something we often see in dashboards — so definitely this is impressive and attention-catching. Even more — those were the main KPIs animated, so I was immediately looking at the right place.

But the funny thing was that every other time I opened the same page — the animation restarted and my eyes were drawn to the same KPIs which I had already seen. Very quickly this became quite an annoying thing. So, animation in the dashboard will create a WOW effect, but the second time you see it you start looking for the button to turn this off.

There is still one case where animation can be OK, it’s when there is an operational dashboard which indicates a critical process. For example, when a bar chart showing the heating of a nuclear reactor reaches a certain threshold I believe it would make sense to add blinking, flashing, other visual or even sound effects to make sure that someone notices this critical event and no one dies.

I’m sure this thing has animations and sound effects. ( link )

If you think _“But it’s not possible to make animations on Power BI and other BI tools, why do you even write about it?”_ — yes it is ([youtube link](https://www.youtube.com/watch?v=MbPmCr4tfvk)).

## 7. Use all the colours

So you want to make a dashboard look cool and you need to pick a colour for another chart and you start thinking — which colour should I add next? — STAHP!

Limited colour palettes allow for a more beautiful and elegant visual experience ([more about elegance in dataviz here](https://medium.com/nightingale/what-makes-a-data-visualisation-elegant-fb032c3a259e)). A colour palette with only 2 or 3 or 4 colours will always look better than a rainbow all over the place. So trying to make the dashboard more beautiful by just adding more colour will have the **opposite** effect.

Unless you are a fan of Lisa Frank or create a dashboard for her, then all rainbow is yours — you can buy the [iPad case below at her eshop here](https://lisafrank.com/products/lisa-frank%C2%AE-rainbow-leopard-folio-ipad-case).

But if you still insist on having more colours than only gray — there are good news for you. You can add them if they encode something. For example, having every KPI assigned a special colour will not only make your dashboard more colourful — it will also make it more readable because now colours have meanings which a reader can decode! Some people say it is not OK to have every bar in a bar chart coloured differently, but here a bar chart serves also as another legend!

## 8. Considering beauty without cleaning the look of your dashboard first

So you want to make a dashboard look cool and you start thinking — I’m using all the default settings, but I need to make the dashboard cool right away! — STAHP!

The wrong thing to do is to make a dashboard beautiful first, and only then declutter — remove those tiny redundant details like gridlines, axis titles, redundant labels and other things.

The right thing to do is to declutter first. It’s like having a shower before putting on your best clothes for a ball. In medieval times they did not have a shower so used perfume to cover the bad smell. So, failing to declutter first will require more effort to make something beautiful, like more perfume is needed if you don’t take a shower.

But what if you do not have time to declutter first and only then make the dashboard beautiful? Then declutter only. A decluttered dashboard will have this tidy professional look which is something authors like Stephen Few or Edvard Tufte preach.

I’d insist, that plain, but well-prepared dashboards look better and are easier to use than the default, but beautified dashboards.

## +9. Sacrifice User Experience

This point is not counted in the title because it’s not a technique to avoid, but rather a limitation to consider.

Whenever some beautiful design decision is added to a dashboard, consider: _did I sacrifice something for that_? Did colour choices reduce readability? Did chart placement make it harder to compare? Maybe hiding ugly slicers made it more difficult to filter relevant information?

I’ve seen hyperminimalistic (beautiful?) reports where it is simply difficult to find the information you need. I’ve seen reports where all things are perfectly aligned in a nicely looking grid although the position of charts made no sense at all and just made it more confusing. It is like seeing beautiful Vietnamese calligraphy without having a clue what those words written in Latin letters mean.

Someone tried to make this look tidy.

Any design decision which makes the dashboard harder to use and to read will have a negative effect in the longer run because the WOW effect which sometimes we try to achieve only works **once**. Great user experience, however, works every time. And if it doesn’t work — it frustrates. Every time.

Making beautiful dashboards is a legit and useful endeavour, time spent on design is a time well spent, but only if it enhances readability and experience. So, if you just keep the techniques mentioned in this article for emergencies only — you should be able to create not only beautiful dashboards like the ones you can find by googling but also way more useful than those. And definitely, you will do a better job in dashboard design than most AI. At least until machines finally take over.

## P.S.

Worth noting that some of the suggestions in this article do not count if you do a data visualization project other than a dashboard. For example, images of people or animations would work well in data journalism projects, smoothing things is OK in infographics, and chart and colour choices are unrestricted in data art. Dashboard is a very specific media with unique considerations!

_Charts were created with Power BI, sometimes using R visuals._

The article were first published on Chart Planet: [https://chartplanet.net/when-cool-design-breaks-a-dashboard-8-techniques-to-avoid/](https://chartplanet.net/when-cool-design-breaks-a-dashboard-8-techniques-to-avoid/)

## Related
[Add wiki-links manually or run update_wikilinks.py]