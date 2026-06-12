# Links Vs Buttons A Perennial Problem Digitala11Y

# Links VS Buttons: A Perennial Problem • DigitalA11Y

[Skip to content](https://www.digitala11y.com/links-vs-buttons-a-perennial-problem/#main)

[DigitalA11Y Your Accessibility Partner](https://www.digitala11y.com/)

*   [Home](https://www.digitala11y.com/)
*   [Services](https://www.digitala11y.com/services/)
    *   [Accessibility Audits](https://www.digitala11y.com/services/audits/)
    *   [VPAT & ACR](https://www.digitala11y.com/services/vpat/)
    *   [Accessibility Consulting](https://www.digitala11y.com/services/consulting/)
    *   [Mobile Accessibility Audit](https://www.digitala11y.com/services/audits/mobile/)
    *   [Design Reviews](https://www.digitala11y.com/services/design/)
    *   [Document Remediation](https://www.digitala11y.com/services/pdf/)
    *   [Accessibility Training](https://www.digitala11y.com/trainings/)
    *   [Ongoing Accessibility Support](https://www.digitala11y.com/services/remediation/)

*   [Solutions](https://www.digitala11y.com/solutions/)
*   [Resources](https://www.digitala11y.com/web-accessibility-resources/)
    *   [A11Y Articles](https://www.digitala11y.com/acccessibility-archives/)
    *   [Frequently Asked Accessibility Questions](https://www.digitala11y.com/faqs/)
    *   [WCAG Primer](https://www.digitala11y.com/wcag2-0/ "Understanding WCAG 2.2 success criterions")
    *   [ARIA Cheatsheet](https://www.digitala11y.com/wai-aria-1-1-cheat-sheet/ "WAI-ARIA 1.2 Cheat sheet")
    *   [A11Y Tools](https://www.digitala11y.com/accessibility-tools/)
    *   [A11Y Patterns](https://www.digitala11y.com/demos/)
    *   [A11Y Cheatsheets](https://www.digitala11y.com/accessibility-cheat-sheets/ "Curated list of accessibility cheatsheets")
    *   [Free Tools](https://www.digitala11y.com/products/)
        *   [Accessibility Checker](https://www.digitala11y.com/products/scan/)
        *   [A11Y Cost Calculator](https://www.digitala11y.com/cost/)
        *   [A11Y Bookmarklets](https://www.digitala11y.com/products/tublets/)
        *   [Color Contrast Extension](https://www.digitala11y.com/products/color/)
        *   [WCAG Contrast Checker](https://www.digitala11y.com/color-blind/)

*   [Contact](https://www.digitala11y.com/contact/)

Search for: 

[DigitalA11Y Your Accessibility Partner](https://www.digitala11y.com/)

Search for: 

[Design](https://www.digitala11y.com/category/design/)

# Links VS Buttons: A Perennial Problem

[![Image 3: Avatar for Sathish Kumar](https://static.digitala11y.com/wp-content/litespeed/avatar/f5633f99acc2843af57d440f86611913.jpg?ver=1780457117)](https://www.digitala11y.com/author/sathishkumar/)Authored By :[Sathish Kumar](https://www.digitala11y.com/author/sathishkumar/)Last Updated :February 20, 2023[Design](https://www.digitala11y.com/category/design/)

![Image 4: Links VS Buttons: A Perennial Problem](https://static.digitala11y.com/wp-content/uploads/2018/04/112.png)

Links VS Buttons: A Perennial Problem

Once a friend told me about a site and asked me to sign up to do some course. He told me that “Sign up” was a link that I needed to click to register myself on the site and do the course. I pulled the links list in my screen reader and searched for some time. Alas! I found nothing. Out of frustration and desperation, I tried for buttons and there it was – “Register button”.

Now, was my friend wrong in guiding me? Or was the screen reader wrong? Or was I wrong in understanding his instruction? Well, it could be either one of them; all of them or none of them at all.

My friend is visually right as he sees the element that looks like a link. The screen reader is technically right as somewhere the code says that it is a button. The only problem is that a button is styled as a link but coded as a button.

## A link or a button: Does it really matter?

When an element is operable, it doesn’t matter in a normal circumstance. But certainly it matters to assistive technologies and the people who use them.

## When and where do we use a link or a button?

Usability experts offer the following explanation in this regard:

*    Use buttons when the user- action causes a change in either back-end or the front-end of the website. For example, submitting a form, opening a pop-up or a modal or a pannel on the same page.
*    Use links when the user-action doesn’t affect the website at all. In this, the users are just readers or spectators of the site. For example, to navigate to the next page or an external source after viewing the content of the page.

This is just usability. When it comes to accessibility, when an element looks like a button or link, use the respective markup to mark its role. That would help the assistive technologies like screen readers and speech recognition software like “Naturally Dragon” to expose appropriate roles to the users.

## Use native markup

An anchor <a> gives the following advantages:

*    Navigates to new pages
*    Allows browser refresh
*    Supports opening in new tab/window
*    Provides with default tab focus with (href) attribute
*    Supports in-page skips with internal href attributes
*    Provides with implicit role (link role) to sscreen readers
*    Shows active, visited, hover and focus.

Buttons <button>:

*    Have default keyboard focus
*    Are activatable by space key
*    Provide with implicit role (button) to screen readers
*    Can be disabled
*    Submit and reset forms, open modals and expand/collapse panels.

At any point, native markups have much more to offer to the developers and the users than the custom controls.

## Points to remember:

*    Design with best usability and accessibility practices
*    Complement the style with the appropriate and semantically correct code
*    Ensure whatever element you use, the implicit role matches with the element’s look
*    Use ARIA roles like (role=button” or (role=”link” to maintain the semantic role when all efforts to maintain native markup fail.

Link or button, let that be inclusive and convey the same meaning to everyone.

This is just an attempt to put things to perspective. If you have comments, suggestions and/or opinions, we welcome with open hands!

### Explore more on DigitalA11Y Insights

*   [![Image 5: Accessibility Communities Roundup](https://static.digitala11y.com/wp-content/uploads/2014/10/71-150x150.png)](https://www.digitala11y.com/accessibility-meetups-communities/) [Accessibility Communities Roundup](https://www.digitala11y.com/accessibility-meetups-communities/)
Here are list of meet-up communities that are focused on accessibility & inclusive design, this… 
*   [![Image 6: Creating Inclusive Web Designs: Unveiling User Habits and Accessibility Needs](https://static.digitala11y.com/wp-content/uploads/2023/05/Creating-Inclusive-Web-Designs-150x150.png)](https://www.digitala11y.com/creating-inclusive-web-designs-unveiling-user-habits-and-accessibility-needs/) [Creating Inclusive Web Design: Unveiling User Habits and Accessibility Needs](https://www.digitala11y.com/creating-inclusive-web-designs-unveiling-user-habits-and-accessibility-needs/)
The internet has revolutionized the way we access information, connect with others, and conduct business.… 
*   [![Image 7](https://static.digitala11y.com/wp-content/uploads/2024/02/The-Home-Link-Dilemma-2-150x150.png)](https://www.digitala11y.com/the-home-link-dilemma-who-wins-design-or-accessibility/) [The Home Link Dilemma: Who Wins? Design or Accessibility!](https://www.digitala11y.com/the-home-link-dilemma-who-wins-design-or-accessibility/)
The idea for this article came when I was trying to figure out how to… 
*   [![Image 8: Shift Left Accessibility Testing](https://static.digitala11y.com/wp-content/uploads/2023/03/Shift-Left-Accessibility-Testing-150x150.png)](https://www.digitala11y.com/connecting-dots-of-an-accessibility-audit/) [Shift Left Accessibility in Design, Development and Testing](https://www.digitala11y.com/connecting-dots-of-an-accessibility-audit/)
You need to make sure your digital products and services meets level AA of the… 
*   [![Image 9: The Image showing a man who is confused between SEO and Accessibility](https://static.digitala11y.com/wp-content/uploads/2023/03/seoVSaccessibility-150x150.png)](https://www.digitala11y.com/the-alt-text-war-seo-vs-accessibility/) [The Alt Text War! SEO VS Accessibility](https://www.digitala11y.com/the-alt-text-war-seo-vs-accessibility/)
There is always a cold war between different compartments of digital world and accessibility. One… 

Share A11y Love

[](https://www.linkedin.com/shareArticle?mini=true&url=https://www.digitala11y.com/links-vs-buttons-a-perennial-problem/)[](https://twitter.com/intent/tweet?url=https://www.digitala11y.com/links-vs-buttons-a-perennial-problem/&text=Links+VS+Buttons%3A+A+Perennial+Problem)[](https://www.facebook.com/sharer.php?u=https://www.digitala11y.com/links-vs-buttons-a-perennial-problem/)[](https://reddit.com/submit?url=https://www.digitala11y.com/links-vs-buttons-a-perennial-problem/&title=Links%20VS%20Buttons:%20A%20Perennial%20Problem)[](javascript:void((function()%7Bvar%20e=document.createElement('script');e.setAttribute('type','text/javascript');e.setAttribute('charset','UTF-8');e.setAttribute('src','//assets.pinterest.com/js/pinmarklet.js?r='+Math.random()*99999999);document.body.appendChild(e)%7D)());)[](https://wa.me/?text=https://www.digitala11y.com/links-vs-buttons-a-perennial-problem/)

![Image 10: Avatar for Sathish Kumar](https://static.digitala11y.com/wp-content/litespeed/avatar/0a5e03ee5b25d7aaf9d9c730d4342aa0.jpg?ver=1780461625)

**[Sathish Kumar](https://www.digitala11y.com/author/sathishkumar/)**

Digital accessibility is my passion. Working with as many industry leaders, striving to achieve digital inclusiveness and spread #a11y awareness in every

 nuke and corner of the digital world!

## Post navigation

[Previous Screen Readers and Browsers! Which is the Best Combination for Accessibility Testing?](https://www.digitala11y.com/screen-readers-browsers-which-is-the-best-combination-for-accessibility-testing/)

[Next Understanding WCAG SC 2.1.2 No Keyboard Trap](https://www.digitala11y.com/understanding-sc-2-1-2-no-keyboard-trap/)

## Similar Posts

*   [![Image 11: Designing For Neurodiversity Resources Roundup](https://static.digitala11y.com/wp-content/uploads/2024/06/Designing-For-Neurodiversity-Resources-Roundup-768x432.png)](https://www.digitala11y.com/designing-for-neurodiversity-resources-roundup/)[Cognitive Disability](https://www.digitala11y.com/category/disability/cognitive-disability/) | [Design](https://www.digitala11y.com/category/design/) | [Web Accessibility](https://www.digitala11y.com/category/web-accessibility/) 
### [Designing For Neurodiversity Resources Roundup](https://www.digitala11y.com/designing-for-neurodiversity-resources-roundup/)

[![Image 12: Avatar for Raghavendra Satish Peri](https://static.digitala11y.com/wp-content/litespeed/avatar/9a78a14f858582de6d1d330c9e9c9ca7.jpg?ver=1780456735)](https://www.digitala11y.com/about/)Authored By :[Raghavendra Satish Peri](https://www.digitala11y.com/about/)Last Updated On :August 20, 2024[0 Comments](https://www.digitala11y.com/designing-for-neurodiversity-resources-roundup/#comments)  Recently, while going through my LinkedIn feed, I came across a list of resources for designing for neurodiversity and decided to share it here with a wider group. As someone who posts on social media, I realized that whatever we share or create on social platforms has a short lifespan and is also hard to… [Read More Designing For Neurodiversity Resources Roundup](https://www.digitala11y.com/designing-for-neurodiversity-resources-roundup/)  
*   [![Image 13: Accessibility Best Practices for Creating Form Designs](https://static.digitala11y.com/wp-content/uploads/2014/10/70-768x432.png)](https://www.digitala11y.com/anatomy-of-creating-accessible-forms-practice-the-best/)[Design](https://www.digitala11y.com/category/design/) 
### [Accessibility Best Practices for Creating Form Designs](https://www.digitala11y.com/anatomy-of-creating-accessible-forms-practice-the-best/)

[![Image 14: Avatar for Raghavendra Satish Peri](https://static.digitala11y.com/wp-content/litespeed/avatar/9a78a14f858582de6d1d330c9e9c9ca7.jpg?ver=1780456735)](https://www.digitala11y.com/about/)Authored By :[Raghavendra Satish Peri](https://www.digitala11y.com/about/)Last Updated On :September 25, 2024[0 Comments](https://www.digitala11y.com/anatomy-of-creating-accessible-forms-practice-the-best/#comments)  This is a series of four articles that discusses all aspects off creating accessible forms: When we complete a task independently and successfully, the exhilaration is boundless. Filling forms on websites and apps for people with disabilities and even for the non-disabled is such a task and the independence in that is exciting, even if… [Read More Accessibility Best Practices for Creating Form Designs](https://www.digitala11y.com/anatomy-of-creating-accessible-forms-practice-the-best/)  
*   [![Image 15: Anatomy of Accessible Forms: The Accessibility Of Placeholder](https://static.digitala11y.com/wp-content/uploads/2018/04/AccessibleUIComponentLibrariesRoundup-768x432.png)](https://www.digitala11y.com/anatomy-of-accessible-forms-placeholder-is-a-mirage/)[Design](https://www.digitala11y.com/category/design/) | [HTML](https://www.digitala11y.com/category/html/) 
### [Placeholders and Accessibility: Problems with the Placeholder Attribute](https://www.digitala11y.com/anatomy-of-accessible-forms-placeholder-is-a-mirage/)

[![Image 16: Avatar for Raghavendra Satish Peri](https://static.digitala11y.com/wp-content/litespeed/avatar/9a78a14f858582de6d1d330c9e9c9ca7.jpg?ver=1780456735)](https://www.digitala11y.com/about/)Authored By :[Raghavendra Satish Peri](https://www.digitala11y.com/about/)Last Updated On :September 25, 2024[5 Comments](https://www.digitala11y.com/anatomy-of-accessible-forms-placeholder-is-a-mirage/#comments)  This is a series of four articles that discusses all aspects off creating accessible forms: Oh! I am alright! No, wait! I forget things very easily. What do they call that? Short term memory loss? The other day, I was filling an online exam registration form. They asked me to write my office address, home… [Read More Placeholders and Accessibility: Problems with the Placeholder Attribute](https://www.digitala11y.com/anatomy-of-accessible-forms-placeholder-is-a-mirage/)  
*   [![Image 17: Best Accessible Fonts For Readability and ADA Compliance](https://static.digitala11y.com/wp-content/uploads/2024/10/Choosing-Accessible-Fonts--768x432.png)](https://www.digitala11y.com/choosing-accessible-fonts-enhancing-readability-and-inclusivity/)[Web Accessibility](https://www.digitala11y.com/category/web-accessibility/) | [Design](https://www.digitala11y.com/category/design/) 
### [Best Accessible Fonts For Readability and ADA Compliance](https://www.digitala11y.com/choosing-accessible-fonts-enhancing-readability-and-inclusivity/)

[![Image 18: Avatar for Monika Prasad](https://static.digitala11y.com/wp-content/litespeed/avatar/90f184fc299fb7f124f17ccf8a7f34cb.jpg?ver=1780458245)](https://holistica11y.com/)Authored By :[Monika Prasad](https://holistica11y.com/)Last Updated On :April 2, 2026[2 Comments](https://www.digitala11y.com/choosing-accessible-fonts-enhancing-readability-and-inclusivity/#comments)  When I was revamping DigitalA11Y, we ensured the website was accessible in many ways. But there was one thing that stood out as missing: Accessible fonts. Through my research, I realized that not all fonts are designed with web accessibility in mind. Now, we all understand the importance of accessibility, so I looked into the… [Read More Best Accessible Fonts For Readability and ADA Compliance](https://www.digitala11y.com/choosing-accessible-fonts-enhancing-readability-and-inclusivity/)  
*   [![Image 19: Inclusive Design 24 #ID24: An Open Platform for Inclusivity](https://static.digitala11y.com/wp-content/uploads/2018/04/108-768x432.png)](https://www.digitala11y.com/inclusive-design-24-id24-an-open-platform-for-inclusivity/)[Design](https://www.digitala11y.com/category/design/) | [Events](https://www.digitala11y.com/category/events/) 
### [Inclusive Design 24 #ID24: An Open Platform for Inclusivity](https://www.digitala11y.com/inclusive-design-24-id24-an-open-platform-for-inclusivity/)

[![Image 20: Avatar for Raghavendra Satish Peri](https://static.digitala11y.com/wp-content/litespeed/avatar/9a78a14f858582de6d1d330c9e9c9ca7.jpg?ver=1780456735)](https://www.digitala11y.com/about/)Authored By :[Raghavendra Satish Peri](https://www.digitala11y.com/about/)Last Updated On :August 29, 2024[0 Comments](https://www.digitala11y.com/inclusive-design-24-id24-an-open-platform-for-inclusivity/#comments)  Born was accessibility once upon a time. From usability, it has moved to a stage that is known as ‘Inclusivity’ – for all; by all.It is the people who have carried this forward here. But we need more and more platforms to discuss, collaborate and innovate with new ideas, designs and orchestrate solutions that are… [Read More Inclusive Design 24 #ID24: An Open Platform for Inclusivity](https://www.digitala11y.com/inclusive-design-24-id24-an-open-platform-for-inclusivity/)  
*   [![Image 21: Best Practices for Form Validation and Error Messages](https://static.digitala11y.com/wp-content/uploads/2015/06/87-768x432.png)](https://www.digitala11y.com/anatomy-of-accessible-forms-errors-of-the-ways/)[Design](https://www.digitala11y.com/category/design/) 
### [Best Practices for Form Validation and Error Messages](https://www.digitala11y.com/anatomy-of-accessible-forms-errors-of-the-ways/)

[![Image 22: Avatar for Raghavendra Satish Peri](https://static.digitala11y.com/wp-content/litespeed/avatar/9a78a14f858582de6d1d330c9e9c9ca7.jpg?ver=1780456735)](https://www.digitala11y.com/about/)Authored By :[Raghavendra Satish Peri](https://www.digitala11y.com/about/)Last Updated On :September 30, 2024[2 Comments](https://www.digitala11y.com/anatomy-of-accessible-forms-errors-of-the-ways/#comments)  This is a series of four articles that discusses all aspects off creating accessible forms: “To err is human.” “To prevent, suggest and correct are divine.” When we submit user data as in financial transactions, travel and entertainment bookings, or in filling surveys, it is quite common that we make mistakes. Let’s imagine we submit… [Read More Best Practices for Form Validation and Error Messages](https://www.digitala11y.com/anatomy-of-accessible-forms-errors-of-the-ways/)  
*   [![Image 23: Designing For Neurodiversity Resources Roundup](https://static.digitala11y.com/wp-content/uploads/2024/06/Designing-For-Neurodiversity-Resources-Roundup-768x432.png)](https://www.digitala11y.com/designing-for-neurodiversity-resources-roundup/)[Cognitive Disability](https://www.digitala11y.com/category/disability/cognitive-disability/) | [Design](https://www.digitala11y.com/category/design/) | [Web Accessibility](https://www.digitala11y.com/category/web-accessibility/) 
### [Designing For Neurodiversity Resources Roundup](https://www.digitala11y.com/designing-for-neurodiversity-resources-roundup/)

[![Image 24: Avatar for Raghavendra Satish Peri](https://static.digitala11y.com/wp-content/litespeed/avatar/9a78a14f858582de6d1d330c9e9c9ca7.jpg?ver=1780456735)](https://www.digitala11y.com/about/)Authored By :[Raghavendra Satish Peri](https://www.digitala11y.com/about/)Last Updated On :August 20, 2024[0 Comments](https://www.digitala11y.com/designing-for-neurodiversity-resources-roundup/#comments)  Recently, while going through my LinkedIn feed, I came across a list of resources for designing for neurodiversity and decided to share it here with a wider group. As someone who posts on social media, I realized that whatever we share or create on social platforms has a short lifespan and is also hard to… [Read More Designing For Neurodiversity Resources Roundup](https://www.digitala11y.com/designing-for-neurodiversity-resources-roundup/)  
*   [![Image 25: Accessibility Best Practices for Creating Form Designs](https://static.digitala11y.com/wp-content/uploads/2014/10/70-768x432.png)](https://www.digitala11y.com/anatomy-of-creating-accessible-forms-practice-the-best/)[Design](https://www.digitala11y.com/category/design/) 
### [Accessibility Best Practices for Creating Form Designs](https://www.digitala11y.com/anatomy-of-creating-accessible-forms-practice-the-best/)

[![Image 26: Avatar for Raghavendra Satish Peri](https://static.digitala11y.com/wp-content/litespeed/avatar/9a78a14f858582de6d1d330c9e9c9ca7.jpg?ver=1780456735)](https://www.digitala11y.com/about/)Authored By :[Raghavendra Satish Peri](https://www.digitala11y.com/about/)Last Updated On :September 25, 2024[0 Comments](https://www.digitala11y.com/anatomy-of-creating-accessible-forms-practice-the-best/#comments)  This is a series of four articles that discusses all aspects off creating accessible forms: When we complete a task independently and successfully, the exhilaration is boundless. Filling forms on websites and apps for people with disabilities and even for the non-disabled is such a task and the independence in that is exciting, even if… [Read More Accessibility Best Practices for Creating Form Designs](https://www.digitala11y.com/anatomy-of-creating-accessible-forms-practice-the-best/)  
*   [![Image 27: Anatomy of Accessible Forms: The Accessibility Of Placeholder](https://static.digitala11y.com/wp-content/uploads/2018/04/AccessibleUIComponentLibrariesRoundup-768x432.png)](https://www.digitala11y.com/anatomy-of-accessible-forms-placeholder-is-a-mirage/)[Design](https://www.digitala11y.com/category/design/) | [HTML](https://www.digitala11y.com/category/html/) 
### [Placeholders and Accessibility: Problems with the Placeholder Attribute](https://www.digitala11y.com/anatomy-of-accessible-forms-placeholder-is-a-mirage/)

[![Image 28: Avatar for Raghavendra Satish Peri](https://static.digitala11y.com/wp-content/litespeed/avatar/9a78a14f858582de6d1d330c9e9c9ca7.jpg?ver=1780456735)](https://www.digitala11y.com/about/)Authored By :[Raghavendra Satish Peri](https://www.digitala11y.com/about/)Last Updated On :September 25, 2024[5 Comments](https://www.digitala11y.com/anatomy-of-accessible-forms-placeholder-is-a-mirage/#comments)  This is a series of four articles that discusses all aspects off creating accessible forms: Oh! I am alright! No, wait! I forget things very easily. What do they call that? Short term memory loss? The other day, I was filling an online exam registration form. They asked me to write my office address, home… [Read More Placeholders and Accessibility: Problems with the Placeholder Attribute](https://www.digitala11y.com/anatomy-of-accessible-forms-placeholder-is-a-mirage/)  
*   [![Image 29: Best Accessible Fonts For Readability and ADA Compliance](https://static.digitala11y.com/wp-content/uploads/2024/10/Choosing-Accessible-Fonts--768x432.png)](https://www.digitala11y.com/choosing-accessible-fonts-enhancing-readability-and-inclusivity/)[Web Accessibility](https://www.digitala11y.com/category/web-accessibility/) | [Design](https://www.digitala11y.com/category/design/) 
### [Best Accessible Fonts For Readability and ADA Compliance](https://www.digitala11y.com/choosing-accessible-fonts-enhancing-readability-and-inclusivity/)

[![Image 30: Avatar for Monika Prasad](https://static.digitala11y.com/wp-content/litespeed/avatar/90f184fc299fb7f124f17ccf8a7f34cb.jpg?ver=1780458245)](https://holistica11y.com/)Authored By :[Monika Prasad](https://holistica11y.com/)Last Updated On :April 2, 2026[2 Comments](https://www.digitala11y.com/choosing-accessible-fonts-enhancing-readability-and-inclusivity/#comments)  When I was revamping DigitalA11Y, we ensured the website was accessible in many ways. But there was one thing that stood out as missing: Accessible fonts. Through my research, I realized that not all fonts are designed with web accessibility in mind. Now, we all understand the importance of accessibility, so I looked into the… [Read More Best Accessible Fonts For Readability and ADA Compliance](https://www.digitala11y.com/choosing-accessible-fonts-enhancing-readability-and-inclusivity/)  
*   [![Image 31: Inclusive Design 24 #ID24: An Open Platform for Inclusivity](https://static.digitala11y.com/wp-content/uploads/2018/04/108-768x432.png)](https://www.digitala11y.com/inclusive-design-24-id24-an-open-platform-for-inclusivity/)[Design](https://www.digitala11y.com/category/design/) | [Events](https://www.digitala11y.com/category/events/) 
### [Inclusive Design 24 #ID24: An Open Platform for Inclusivity](https://www.digitala11y.com/inclusive-design-24-id24-an-open-platform-for-inclusivity/)

[![Image 32: Avatar for Raghavendra Satish Peri](https://static.digitala11y.com/wp-content/litespeed/avatar/9a78a14f858582de6d1d330c9e9c9ca7.jpg?ver=1780456735)](https://www.digitala11y.com/about/)Authored By :[Raghavendra Satish Peri](https://www.digitala11y.com/about/)Last Updated On :August 29, 2024[0 Comments](https://www.digitala11y.com/inclusive-design-24-id24-an-open-platform-for-inclusivity/#comments)  Born was accessibility once upon a time. From usability, it has moved to a stage that is known as ‘Inclusivity’ – for all; by all.It is the people who have carried this forward here. But we need more and more platforms to discuss, collaborate and innovate with new ideas, designs and orchestrate solutions that are… [Read More Inclusive Design 24 #ID24: An Open Platform for Inclusivity](https://www.digitala11y.com/inclusive-design-24-id24-an-open-platform-for-inclusivity/)  
*   [![Image 33: Best Practices for Form Validation and Error Messages](https://static.digitala11y.com/wp-content/uploads/2015/06/87-768x432.png)](https://www.digitala11y.com/anatomy-of-accessible-forms-errors-of-the-ways/)[Design](https://www.digitala11y.com/category/design/) 
### [Best Practices for Form Validation and Error Messages](https://www.digitala11y.com/anatomy-of-accessible-forms-errors-of-the-ways/)

[![Image 34: Avatar for Raghavendra Satish Peri](https://static.digitala11y.com/wp-content/litespeed/avatar/9a78a14f858582de6d1d330c9e9c9ca7.jpg?ver=1780456735)](https://www.digitala11y.com/about/)Authored By :[Raghavendra Satish Peri](https://www.digitala11y.com/about/)Last Updated On :September 30, 2024[2 Comments](https://www.digitala11y.com/anatomy-of-accessible-forms-errors-of-the-ways/#comments)  This is a series of four articles that discusses all aspects off creating accessible forms: “To err is human.” “To prevent, suggest and correct are divine.” When we submit user data as in financial transactions, travel and entertainment bookings, or in filling surveys, it is quite common that we make mistakes. Let’s imagine we submit… [Read More Best Practices for Form Validation and Error Messages](https://www.digitala11y.com/anatomy-of-accessible-forms-errors-of-the-ways/)  
*   [![Image 35: Designing For Neurodiversity Resources Roundup](https://static.digitala11y.com/wp-content/uploads/2024/06/Designing-For-Neurodiversity-Resources-Roundup-768x432.png)](https://www.digitala11y.com/designing-for-neurodiversity-resources-roundup/)[Cognitive Disability](https://www.digitala11y.com/category/disability/cognitive-disability/) | [Design](https://www.digitala11y.com/category/design/) | [Web Accessibility](https://www.digitala11y.com/category/web-accessibility/) 
### [Designing For Neurodiversity Resources Roundup](https://www.digitala11y.com/designing-for-neurodiversity-resources-roundup/)

[![Image 36: Avatar for Raghavendra Satish Peri](https://static.digitala11y.com/wp-content/litespeed/avatar/9a78a14f858582de6d1d330c9e9c9ca7.jpg?ver=1780456735)](https://www.digitala11y.com/about/)Authored By :[Raghavendra Satish Peri](https://www.digitala11y.com/about/)Last Updated On :August 20, 2024[0 Comments](https://www.digitala11y.com/designing-for-neurodiversity-resources-roundup/#comments)  Recently, while going through my LinkedIn feed, I came across a list of resources for designing for neurodiversity and decided to share it here with a wider group. As someone who posts on social media, I realized that whatever we share or create on social platforms has a short lifespan and is also hard to… [Read More Designing For Neurodiversity Resources Roundup](https://www.digitala11y.com/designing-for-neurodiversity-resources-roundup/)  
*   [![Image 37: Accessibility Best Practices for Creating Form Designs](https://static.digitala11y.com/wp-content/uploads/2014/10/70-768x432.png)](https://www.digitala11y.com/anatomy-of-creating-accessible-forms-practice-the-best/)[Design](https://www.digitala11y.com/category/design/) 
### [Accessibility Best Practices for Creating Form Designs](https://www.digitala11y.com/anatomy-of-creating-accessible-forms-practice-the-best/)

[![Image 38: Avatar for Raghavendra Satish Peri](https://static.digitala11y.com/wp-content/litespeed/avatar/9a78a14f858582de6d1d330c9e9c9ca7.jpg?ver=1780456735)](https://www.digitala11y.com/about/)Authored By :[Raghavendra Satish Peri](https://www.digitala11y.com/about/)Last Updated On :September 25, 2024[0 Comments](https://www.digitala11y.com/anatomy-of-creating-accessible-forms-practice-the-best/#comments)  This is a series of four articles that discusses all aspects off creating accessible forms: When we complete a task independently and successfully, the exhilaration is boundless. Filling forms on websites and apps for people with disabilities and even for the non-disabled is such a task and the independence in that is exciting, even if… [Read More Accessibility Best Practices for Creating Form Designs](https://www.digitala11y.com/anatomy-of-creating-accessible-forms-practice-the-best/)  

## 10 Comments

1.   ![Image 39: Avatar for Roman](https://static.digitala11y.com/wp-content/litespeed/avatar/5fd1faa859e8a638ddd0c6271ee446bd.jpg?ver=1780475284)**Roman**says: [June 6, 2018 at 11:38 am](https://www.digitala11y.com/links-vs-buttons-a-perennial-problem/#comment-73) Hello, Sathish Kumar! I highly familiar with HTML and CSS but sometimes have questions about link and button – How states could i use in mobile screens? Using states :active and :focus for link it’s enough? And :hover using only desktop screen.

 What is your opinion? [Reply](https://www.digitala11y.com/links-vs-buttons-a-perennial-problem/#comment-73) 
    1.   ![Image 40: Avatar for sathish kumar](https://static.digitala11y.com/wp-content/litespeed/avatar/ae5e58d4b35ffcbf174cb0435aba8f53.jpg?ver=1780493284)**sathish kumar**says: [June 22, 2018 at 5:53 pm](https://www.digitala11y.com/links-vs-buttons-a-perennial-problem/#comment-74) Thank you for the question. That’s correct. Hover is used only on desktop screens. [Reply](https://www.digitala11y.com/links-vs-buttons-a-perennial-problem/#comment-74) 

2.   ![Image 41: Avatar for Jamie Herrera](https://static.digitala11y.com/wp-content/litespeed/avatar/eaf43c8415b2cccafa1ab99c2f461062.jpg?ver=1780471684)**[Jamie Herrera](http://www.deque.com/)**says: [December 9, 2021 at 7:43 pm](https://www.digitala11y.com/links-vs-buttons-a-perennial-problem/#comment-33435) Hi! It would be great to provide an updated article that includes native mobile in your example and not just web – the premise is still correct, but should include the caveat that selecting the native app button may navigate the user within the app, but a link takes the user to an external site. Would you agree? [Reply](https://www.digitala11y.com/links-vs-buttons-a-perennial-problem/#comment-33435) 
    1.   ![Image 42: Avatar for Raghavendra Satish Peri](https://static.digitala11y.com/wp-content/litespeed/avatar/f91709da35fb04ccc2d264f06b433a31.jpg?ver=1780458573)**[Raghavendra Satish Peri](https://raghava.in/)**says: [January 5, 2022 at 8:55 am](https://www.digitala11y.com/links-vs-buttons-a-perennial-problem/#comment-36059) Hello Jamie,

 I agree, will get the article updated. Thanks! [Reply](https://www.digitala11y.com/links-vs-buttons-a-perennial-problem/#comment-36059) 

3.   ![Image 43: Avatar for Vaibhav Mishra](https://static.digitala11y.com/wp-content/litespeed/avatar/9cb2a0a83884a78ec2d3aca7c65d94bc.jpg?ver=1780475284)**Vaibhav Mishra**says: [January 6, 2023 at 8:59 pm](https://www.digitala11y.com/links-vs-buttons-a-perennial-problem/#comment-86621) Hi,

 I have one question regarding the tertiary button which appears as a link but operate as a button where button tags are used but visually it seems link. Other than SR user for everyone it seems to be link which sets incorrect expectation, so what can be do in that case. [Reply](https://www.digitala11y.com/links-vs-buttons-a-perennial-problem/#comment-86621) 
    1.   ![Image 44: Avatar for Raghavendra Satish Peri](https://static.digitala11y.com/wp-content/litespeed/avatar/f91709da35fb04ccc2d264f06b433a31.jpg?ver=1780458573)**[Raghavendra Satish Peri](https://www.digitala11y.com/about/)**says: [January 9, 2023 at 9:18 am](https://www.digitala11y.com/links-vs-buttons-a-perennial-problem/#comment-86984) Hi Vaibhav,

 Thanks for the comment. As mentioned in the blog post, we need to prioritize functionality and the design team needs to design buttons and links appropriately.

 If something appears to be a link but functions as a button, it may confuse users who rely on visual assistance from screen readers. I recommend speaking with the design team and educating them on this issue. [Reply](https://www.digitala11y.com/links-vs-buttons-a-perennial-problem/#comment-86984) 
        1.   ![Image 45: Avatar for Jamie Herrera](https://static.digitala11y.com/wp-content/litespeed/avatar/eaf43c8415b2cccafa1ab99c2f461062.jpg?ver=1780471684)**Jamie Herrera**says: [January 14, 2023 at 12:35 am](https://www.digitala11y.com/links-vs-buttons-a-perennial-problem/#comment-87784) As a developer you would code to the function. As an accessibility professional you would have a conversation first with the designer or better, more widely with the design team, about the pattern of using blue text to indicate a button or modal. Other items like a tooltip/more information icon could be used, not just a big button, for example if the action is to open a modal. As a designer you’d think about the various ways someone might access the content that the button goes to, and consider whether blue text is the best indicator. As a PO, there’s the question of why this “linking” of information is needed. What is the requirement? Why is it there? Is it necessary to take the user somewhere else?

Lastly, in a web vs mobile app space, there are times when a webpage makes sense as a functional link whereas in the app for the same function you might link to the same webpage in a browser. But if the action opens a modal or goes to a different section of the same app, many a11y SME’s follow the idea that any navigation action that keeps the user in-app is functionally a button; I’ve seen some variation on this though, which is maybe why this issue comes up regularly in apps. [Reply](https://www.digitala11y.com/links-vs-buttons-a-perennial-problem/#comment-87784) 
            1.   ![Image 46: Avatar for Raghavendra Satish Peri](https://static.digitala11y.com/wp-content/litespeed/avatar/f91709da35fb04ccc2d264f06b433a31.jpg?ver=1780458573)**[Raghavendra Satish Peri](https://www.digitala11y.com/about/)**says: [January 24, 2023 at 8:44 am](https://www.digitala11y.com/links-vs-buttons-a-perennial-problem/#comment-89166) Thank you for bringing up the importance of considering accessibility in the design and development process. It’s crucial to have conversations with the design team, question the requirements, and consider different ways users might access the content. It’s also important to consider the difference between web and mobile app approaches. Your insights are much appreciated. [Reply](https://www.digitala11y.com/links-vs-buttons-a-perennial-problem/#comment-89166) 

4.   ![Image 47: Avatar for Katharine](https://static.digitala11y.com/wp-content/litespeed/avatar/59c09e943788c0a63a62c2f33e80f3a3.jpg?ver=1780471684)**Katharine**says: [July 2, 2023 at 2:25 am](https://www.digitala11y.com/links-vs-buttons-a-perennial-problem/#comment-112003) If i used buttons to take a person to another page on the website instead of the picture links im using on the homepage atm would this be okay

Would changing the picture links to button links speed up the load time of my homepage?

Lastly i need 15 points to get my website speed to 99% mobile would removing the pics and adding buttons do this? [Reply](https://www.digitala11y.com/links-vs-buttons-a-perennial-problem/#comment-112003) 
5.   ![Image 48: Avatar for Harish](https://static.digitala11y.com/wp-content/litespeed/avatar/ba59367dd619e0f1df9bc5c4b623257b.jpg?ver=1780471684)**Harish**says: [July 19, 2023 at 4:21 pm](https://www.digitala11y.com/links-vs-buttons-a-perennial-problem/#comment-115382) I strongly believe that whatever the reason, button must be designed as button and links should be designed as link. Buttons can be triggered by using either enter key or spacebar key, whereas links can be triggered only using enter key. if we style links as buttons there are chances users endup pressing spacebar and user will feel like he/she is been cheated here. [Reply](https://www.digitala11y.com/links-vs-buttons-a-perennial-problem/#comment-115382) 

### Leave a Reply [Cancel reply](https://www.digitala11y.com/links-vs-buttons-a-perennial-problem/#respond)

Your email address will not be published.Required fields are marked *

Comment *

Name *

Email *

Website

- [x] Save my name, email, and website in this browser for the next time I comment.

Δ

## Subscribe To DigitalA11Y Newsletter

![Image 49: loader](https://static.digitala11y.com/wp-includes/images/spinner.gif)

 Email Address*   First Name*   Last Name*  

## Recent A11Y Articles

*   [Introducing the DigitalA11Y Accessibility Checker](https://www.digitala11y.com/introducing-the-digitala11y-accessibility-checker/)
*   [10 Accessibility Questions Every Client Asks Before an Audit](https://www.digitala11y.com/wcag-audits-10-questions-clients-ask-about-accessibility-services/)
*   [Shopify Accessibility Checklist for ADA Compliance](https://www.digitala11y.com/shopify-accessibility-checklist-for-ada-compliance/)
*   [RBI Digital Accessibility Guidelines for Banks: A Complete Implementation Guide](https://www.digitala11y.com/rbi-digital-accessibility-guidelines-for-banks-a-complete-implementation-guide/)

## Recent Comments

1.   ![Image 50: Avatar for Harish](https://static.digitala11y.com/wp-content/litespeed/avatar/d33dbcb83c9847ae20817757233e6b70.jpg?ver=1780489912)[Raghavendra Satish Peri](https://www.digitala11y.com/about/) on [Open Source Accessibility Testing Tools Roundup](https://www.digitala11y.com/open-source-accessibility-tools/#comment-195769)May 28, 2026 Hi Andreas, Looking into the tool, we'll add it. 
2.   ![Image 51: Avatar for Harish](https://static.digitala11y.com/wp-content/litespeed/avatar/54f2f3b495d391ed61b9f78771a62c14.jpg?ver=1780551298)Andreas on [Open Source Accessibility Testing Tools Roundup](https://www.digitala11y.com/open-source-accessibility-tools/#comment-195382)May 22, 2026 Hi Raghavendra, For people in the DACH-Region, I have released a free (german) tool: https://barrieretest.at It is based on axe-core… 
3.   ![Image 52: Avatar for Harish](https://static.digitala11y.com/wp-content/litespeed/avatar/6fe974affee8a99555f2ef47d6c56d9c.jpg?ver=1780456735)Alex Green on [The History of Digital Accessibility: A Timeline of Progress](https://www.digitala11y.com/the-history-of-digital-accessibility-a-timeline-of-progress/#comment-192382)March 31, 2026 This is very clearly AI Generated. I love the message but change it a little. 
4.   ![Image 53: Avatar for Harish](https://static.digitala11y.com/wp-content/litespeed/avatar/7abc0b5801431b4ffcd2318ed378565c.jpg?ver=1780456736)[Lindsay Doyle](https://compliapoint.com/) on [Digital Accessibility Companies Roundup](https://www.digitala11y.com/digital-accessibility-agencies-roundup/#comment-192378)February 24, 2026 Hi Raghavendra, I'd love to be added to this roundup. Compliapoint is a U.S.-based accessibility service company providing WCAG 2.2… 
5.   ![Image 54: Avatar for Harish](https://static.digitala11y.com/wp-content/litespeed/avatar/b6d4beb37bb318be103ebb38012ad812.jpg?ver=1780456736)[Nilan Saha](https://colorframe.net/) on [Free Mobile Accessibility Testing Tools For IOS and Android](https://www.digitala11y.com/free-mobile-accessibility-testing-tools/#comment-192374)February 9, 2026 Hi are you able to add https://colorframe.net/ to the list as well. It is MacOS native and has an inbuilt… 

## A11Y Categories

Categories 

## Company

*   [About](https://www.digitala11y.com/about/)
*   [Blog](https://www.digitala11y.com/blog/)
*   [Careers](https://www.digitala11y.com/careers/)
*   [Contact](https://www.digitala11y.com/contact/)

## Services

*   [Accessibility Audits](https://www.digitala11y.com/services/audits/)
*   [Accessibility Consulting](https://www.digitala11y.com/services/consulting/)
*   [VPAT/ACR](https://www.digitala11y.com/services/vpat/)
*   [Accessibility Trainings](https://www.digitala11y.com/trainings/)

## Compliance

*   [WCAG](https://www.digitala11y.com/compliance/wcag/ "Web Content Accessibility Guidelines")
*   [ADA](https://www.digitala11y.com/compliance/ada/ "Americans with Disabilities Act")
*   [Section 508](https://www.digitala11y.com/compliance/section-508/)
*   [EN 301 549](https://www.digitala11y.com/compliance/en-301-549/)
*   [EAA](https://www.digitala11y.com/compliance/eaa/ "European Accessibility Act")
*   [AODA](https://www.digitala11y.com/compliance/aoda/ "Accessibility for Ontarians with Disabilities Act")
*   [ACA](https://www.digitala11y.com/compliance/aca/ "Accessible Canada Act")

## Resources

*   [A11Y FAQs](https://www.digitala11y.com/faqs/)
*   [Understanding WCAG](https://www.digitala11y.com/wcag2-0/)
*   [WCAG Checklist](https://www.digitala11y.com/wcag-checklist/)
*   [Understanding WAI-ARIA](https://www.digitala11y.com/wai-aria-1-1-cheat-sheet/)

## Legal

*   [Privacy Policy](https://www.digitala11y.com/privacy-policy/)
*   [Terms and Conditions](https://www.digitala11y.com/terms-and-conditions/)
*   [Disclaimer](https://www.digitala11y.com/disclaimer/)
*   [Accessibility Statement](https://www.digitala11y.com/accessibility-statement-2/)
*   [Sitemap](https://www.digitala11y.com/sitemap/)

© 2026 DigitalA11Y

 All Rights Reserved

[](http://www.linkedin.com/company/digitala11y)[](https://www.twitter.com/digitala11y)[](https://www.facebook.com/digitala11y)[](https://www.instagram.com/digitala11yhub/)[](https://www.youtube.com/@digitala11y)

**DigitalA11Y**

Plot No 108, 3rd Cross Rd, Saipuri Colony,

Hastinapuri Colony, Sainikpuri, Secunderabad -500094

Telangana, India.

Tel:(+91)99082 66680,

E-mail: hello@digitala11y.com

[](https://www.digitala11y.com/links-vs-buttons-a-perennial-problem/#wrapper)

*   [Home](https://www.digitala11y.com/)
*   [Services](https://www.digitala11y.com/services/)Toggle child menu 
    *   [Accessibility Audits](https://www.digitala11y.com/services/audits/)
    *   [VPAT & ACR](https://www.digitala11y.com/services/vpat/)
    *   [Accessibility Consulting](https://www.digitala11y.com/services/consulting/)
    *   [Mobile Accessibility Audit](https://www.digitala11y.com/services/audits/mobile/)
    *   [Design Reviews](https://www.digitala11y.com/services/design/)
    *   [Document Remediation](https://www.digitala11y.com/services/pdf/)
    *   [Accessibility Training](https://www.digitala11y.com/trainings/)
    *   [Ongoing Accessibility Support](https://www.digitala11y.com/services/remediation/)

*   [Solutions](https://www.digitala11y.com/solutions/)
*   [Resources](https://www.digitala11y.com/web-accessibility-resources/)Toggle child menu 
    *   [A11Y Articles](https://www.digitala11y.com/acccessibility-archives/)
    *   [Frequently Asked Accessibility Questions](https://www.digitala11y.com/faqs/)
    *   [WCAG Primer](https://www.digitala11y.com/wcag2-0/ "Understanding WCAG 2.2 success criterions")
    *   [ARIA Cheatsheet](https://www.digitala11y.com/wai-aria-1-1-cheat-sheet/ "WAI-ARIA 1.2 Cheat sheet")
    *   [A11Y Tools](https://www.digitala11y.com/accessibility-tools/)
    *   [A11Y Patterns](https://www.digitala11y.com/demos/)
    *   [A11Y Cheatsheets](https://www.digitala11y.com/accessibility-cheat-sheets/ "Curated list of accessibility cheatsheets")
    *   [Free Tools](https://www.digitala11y.com/products/)Toggle child menu 
        *   [Accessibility Checker](https://www.digitala11y.com/products/scan/)
        *   [A11Y Cost Calculator](https://www.digitala11y.com/cost/)
        *   [A11Y Bookmarklets](https://www.digitala11y.com/products/tublets/)
        *   [Color Contrast Extension](https://www.digitala11y.com/products/color/)
        *   [WCAG Contrast Checker](https://www.digitala11y.com/color-blind/)

*   [Contact](https://www.digitala11y.com/contact/)

## Related
[Add wiki-links manually or run update_wikilinks.py]