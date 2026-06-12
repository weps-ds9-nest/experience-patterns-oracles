# Master Ios Mobile Ui Design Segmented Control Bootcamp Medium

## Master iOS Mobile UI Design: Segmented Control

Anumod Ajith·3 min read·Nov 9, 2024

Clean article found smry-fast Reading stack medium.com · 366 words

The article is ready without leaving the reader. Source: Direct extraction.

In previous blogs, I covered [iOS header](https://medium.com/@anumodajith293/master-mobile-ui-design-for-ios-components-pt1-the-header-bar-6d179c8853b0) and [tab bar](https://medium.com/design-bootcamp/master-ios-mobile-ui-design-pt-2-tab-bars-b8dd9a96f7cc), and now I want to talk about another commonly used element — segmented control. If you are hearing it for the first time, the term can be confusing, so let me explain. It seems to me that Apple wanted to create distinct components based on use case:

1.   **Segmented control**: component that contains contents/controls that are related to each other. For example, tabs that segregate ‘All photos’ and ‘Favorite photos’ or tabs that provide text editor controls. The segmented control use case for editing controls can be used as single-select or multi-select.
2.   **Tab bar**: used to switch between distinct content section offering different actions, features and information.

In this blog I will cover the following topics — the common uses cases, my tips on using tabs, the best practises from Apple, and accessibility.

## Use cases

The segmented control looks like this. The default look includes grey background, a vertical divider (when there is more than 2 controls) and finally a light or colored background to highlight the currently active control. The segmented control can also be used to provide editable content control like in the Apple Notes app. The primary uses cases can be categorised in to two:

1.   **Navigation or filtering between related content**: iOS Phone app (Recents page) iOS Photos app (Library page), iOS Music app (search tab when search bar is active) and so on.
2.   **Content editing**: iOS Notes app and iOS Mail app (when editing text formatting).

Examples of segmented controls in iOS: (left) for filtering between missed and all calls in the Phone app, and (right) for selecting text formatting options in the Notes app.

## Personal Experience

### Tip 1: Don’t use the default component for main features/page.

In my experience, the default Apple segmented control often looks out of place in modern designs, especially if you’re aiming for a sleek or minimalistic look. The bulkiness and grey background often don’t integrate well with other UI elements. While it’s tempting to customize, Apple’s components usually don’t perform well under heavy customization. You can adjust aspects like color, size, padding, and margins, but be cautious with changes, particularly regarding accessibility. Improper color choices…

## Related
[Add wiki-links manually or run update_wikilinks.py]