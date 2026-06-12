# Components

Components

Checkboxes allow users to select one or more options from a list.

Passed WCAG 2.1 AA

## [](https://designsystem.digital.gov/components/checkbox/)About the checkbox component

Checkboxes are an easily understandable way to indicate that users can select one or more answers to a question or items from a list. They’re always followed by a label or instructions that clearly indicate what checking the box represents.

Each checkbox has two different states: selected or unselected, which are similar to an on and off switch. If a checkbox label says “Yes, send me an email,” it’s clear what checking that box (or not checking it) will accomplish.

Checkboxes also visibly show users what’s been selected and makes it easy for them to “uncheck” an option, which can be difficult with other selection methods on a form (such as radio buttons or select menus). It’s common to include “check all that apply” instructions with checkboxes to let users know it’s okay to select more than one option at a time.

## [](https://designsystem.digital.gov/components/checkbox/) Guidance

*   **To display multiple answers.** When a user can select any number of choices from a list.
*   **To allow users to toggle answers.** When a user needs to acknowledge acceptance of something (like terms of service) or switch between two opposite states, such as unchecked = “no” and checked = “yes.”

*   **Single-select only.** If a user can only select one option from a list of many, use [radio buttons](https://designsystem.digital.gov/components/radio-buttons) instead.

*   **Make the label selectable.** Users should be able to select either the text label or the checkbox to select or deselect an option.
*   **List options vertically.** Horizontal listings can make it difficult to tell which label pertains to which checkbox.
*   **Use positive statements.** Negative language in labels can be counterintuitive. For example, use “I want to receive a promotional email” instead of “I don’t want to receive a promotional email.”
*   **Use logical labels.** Make sure that the label makes both states — checked and unchecked — clear to the user. If that’s not possible, consider using a [radio button](https://designsystem.digital.gov/components/radio-buttons) with two individual options instead. Then both states can have their own clearly marked label.
*   **Use adequate touch targets.** Make sure selections are adequately spaced for touch screens. Consider using the tile variant for larger touch targets.
*   **Don’t mix default and tile variants.** Pick one implementation and stick with it. When mixed, tiles can appear to indicate a bias or preference toward that option.
*   **Use a logical order.** Make sure the selection options are organized in a meaningful way, like alphabetical or most-frequent to least-frequent. This helps users easily find the option they’re looking for.

Test the checkbox component in your own project.

USWDS tested the checkbox component for accessibility. You should test your implementation, too.

[Use checkbox accessibility tests](https://designsystem.digital.gov/components/checkbox/accessibility-tests)

*   **Customize form controls accessibly.** If you customize this component, ensure that it continues to meet the [accessibility requirements that apply to all form controls](https://designsystem.digital.gov/components/form).
*   **Use a fieldset and legend for a checkbox group.** Surround a related set of checkboxes with a `<fieldset>`. The `<legend>` provides context for the grouping. Don’t use fieldset and legend for a single check.
*   **These custom checkboxes are accessible.** The custom checkboxes here are accessible to screen readers because the default checkboxes are moved off-screen with `position: absolute; left: -999em`.
*   **Use semantic tags.** Each input should have a semantic tag for the `id` attribute, and its corresponding label should have the same value in its `for` attribute.

| Variable | Description |
| --- | --- |
| ``` $theme-checkbox-border-radius ``` | Checkbox border radius for rounded corners. |
| ``` $theme-input-background-color ``` | Background color for radio and checkbox inputs. |
| ``` $theme-input-tile-border-radius ``` | Tile border radius for rounded corners. |
| ``` $theme-input-tile-border-width ``` | Tile border thickness |

_This component has no variants._

## [](https://designsystem.digital.gov/components/checkbox/)Accessibility test status

The USWDS team did 8 tests based on WCAG 2.1 AA success criteria.

 Overview of recent accessibility test results: 
| Total tests | Passed | Passed with exceptions | Conditional | Failed |
| --- | --- | --- | --- | --- |
| 8 | 7 | 0 | 1 | 0 |

Overview of recent accessibility test results:

*   **Passed:** 7

*   **Passed with exceptions:** 0

*   **Conditional:** 1

*   **Failed:** 0

Learn more on the [checkbox accessibility tests page](https://designsystem.digital.gov/components/checkbox/accessibility-tests/).

## [](https://designsystem.digital.gov/components/checkbox/)Package

*   **Package usage:**`@forward "usa-checkbox";`
*   **Dependencies:**`uswds-fonts`, `usa-fieldset`, `usa-legend`, `usa-input-list`

## [](https://designsystem.digital.gov/components/checkbox/)Latest updates

Meaningful code and guidance updates are listed in the following table:

| Date | USWDS version | Affects | Breaking | Description |
| --- | --- | --- | --- | --- |
| 2025-03-07 | [3.12.0](https://github.com/uswds/uswds/releases/tag/v3.12.0) | * Styles | No | **Updated the width of the label’s target area to match the width of the content.** Previously, the interactive area extended the full width of the container. More information: [uswds#6192](https://github.com/uswds/uswds/pull/6192) |
| 2024-11-13 | [3.10.0](https://github.com/uswds/uswds/releases/tag/v3.10.0) | * Assets | No | **Removed style tags from indeterminate checkbox SVGs.** These style tags were unnecessary and caused a conflict with some automated testing tools. More information: [uswds#6162](https://github.com/uswds/uswds/pull/6162) |
| 2024-09-18 | N/A | * Guidance | No | **Added WCAG compliance tag and accessibility test status section.** More information: [uswds-site#2803](https://github.com/uswds/uswds-site/pull/2803) |
| 2024-04-26 | [3.8.0](https://github.com/uswds/uswds/releases/tag/v3.8.0) | * Assets * Styles | No | **Added indeterminate styles for checkboxes.** Checkboxes will now display as indeterminate when you set `input.indeterminate = true` via JavaScript or add the `data-indeterminate` attribute. This is currently only a style addition and does not affect checkbox functionality. More information: [uswds#5713](https://github.com/uswds/uswds/pull/5713) |
| 2023-11-20 | N/A | * Guidance | No | **Added `usa-input-list` to the list of dependencies.** More information: [uswds-site#2149](https://github.com/uswds/uswds-site/pull/2149) |
| 2023-09-29 | [3.6.1](https://github.com/uswds/uswds/releases/tag/v3.6.1) | * Accessibility * Styles | No | **Updated radio and checkbox tiles to have lighter borders, reducing visual noise.** More information: [uswds#5494](https://github.com/uswds/uswds/pull/5494) |
| 2023-06-09 | [3.5.0](https://github.com/uswds/uswds/releases/tag/v3.5.0) | * Accessibility * Styles | No | **Improved legibility in forced colors mode.** Adds a consistent border in forced colors mode. More information: [uswds#5147](https://github.com/uswds/uswds/pull/5147) |
| 2023-06-09 | [3.5.0](https://github.com/uswds/uswds/releases/tag/v3.5.0) | * Accessibility * Styles | No | **Improved consistency and visibility of disabled styles.** Form elements with the `disabled` or `aria-disabled` attribute now get consistent styling and have proper color contrast. More information: [uswds#5063](https://github.com/uswds/uswds/pull/5063) |
| 2023-06-09 | [3.5.0](https://github.com/uswds/uswds/releases/tag/v3.5.0) | * Accessibility * Styles | No | **Improved consistency of disabled styles in forced colors mode.** More information: [uswds#5295](https://github.com/uswds/uswds/pull/5295) |
| 2022-08-05 | [3.1.0](https://github.com/uswds/uswds/releases/tag/v3.1.0) | * Accessibility * Styles | No | **Styled aria-disabled to match disabled.** Now disabled styling is applied whether you use `disabled` (disabled and hidden from screen readers) or `aria-disabled` (disabled and visible to screen readers). More information: [uswds#4783](https://github.com/uswds/uswds/pull/4783) |
| 2022-04-28 | [3.0.0](https://github.com/uswds/uswds/releases/tag/v3.0.0) | * Assets * JavaScript * Styles | Breaking | Breaking**Updated to Sass module syntax and new package structure.** More information: [uswds#4656](https://github.com/uswds/uswds/pull/4656) |
| 2022-04-11 | [2.13.3](https://github.com/uswds/uswds/releases/tag/v2.13.3) | * Accessibility * Styles | No | **Added support for forced colors mode.** All our components now support proper display when users have a forced colors mode set in their operating system. More information: [uswds#4610](https://github.com/uswds/uswds/pull/4610) |
| 2021-08-18 | [2.12.1](https://github.com/uswds/uswds/releases/tag/v2.12.1) | * Styles | No | **Improved whitespace sensitivity of radio and checkbox tiles.** Now radio and checkbox tiles will display consistently whether or not there’s extra whitespace in the markup. More information: [uswds#4286](https://github.com/uswds/uswds/pull/4286) |
| 2021-08-18 | [2.12.1](https://github.com/uswds/uswds/releases/tag/v2.12.1) | * Styles | No | **Improved class order sensitivity for checkbox and radio.** Now checkbox and radio components display properly regardless of the order of the class and modifier names. More information: [uswds#4262](https://github.com/uswds/uswds/pull/4262) |
| 2021-06-16 | [2.12.0](https://github.com/uswds/uswds/releases/tag/v2.12.0) | * Accessibility * Styles | No | **Updated checkbox and radio buttons to include automatic accessible color.** Now checkbox and radio buttons will display in the proper accessible color, and adapt to the text, link, and background colors you set in your projects’s settings. More information: [uswds#4199](https://github.com/uswds/uswds/pull/4199) |
| 2021-03-17 | [2.11.0](https://github.com/uswds/uswds/releases/tag/v2.11.0) | * JavaScript * Styles | No | **Fixed character display in checkboxes and radio buttons.** Allowed checkboxes and radio buttons to display properly regardless of character encoding. More information: [uswds#4080](https://github.com/uswds/uswds/pull/4080) |

## Related
[Add wiki-links manually or run update_wikilinks.py]