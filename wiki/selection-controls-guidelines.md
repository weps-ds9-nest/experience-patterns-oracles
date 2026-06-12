# Selection Controls Guidelines

### Interactive demo

This demo lets you preview selection controls. Each tab displays a different type of selection control.

### Developer documentation

| Component | Platform | Status |
| --- | --- | --- |
| Checkboxes | Android iOS Web Flutter | [Available](https://material.io/develop/android/components/checkbox/) [Platform exception](https://material.io/design/platform-guidance/cross-platform-adaptation.html#when-to-adapt) [Available](https://material.io/develop/web/components/input-controls/checkboxes/) [Available](https://m2.material.io/develop/flutter/components/checkboxes) |
| Radio buttons | Android iOS Web Flutter | [Available](https://material.io/develop/android/components/radiobutton/) [Platform exception](https://material.io/design/platform-guidance/cross-platform-adaptation.html#) [Available](https://material.io/develop/web/components/input-controls/radio-buttons/) [Available](https://m2.material.io/develop/flutter/components/radio-buttons) |
| Switches | Android iOS Web Flutter | [Available](https://material.io/develop/android/components/switch/) [Platform exception](https://material.io/design/platform-guidance/cross-platform-adaptation.html#when-to-adapt) [Available](https://material.io/develop/web/components/input-controls/switches/) [Available](https://api.flutter.dev/flutter/material/Switch-class.html) |

## Usage [](https://m2.material.io/)

Selection controls allow users to complete tasks that involve making choices such as selecting options, or switching settings on or off. Selection controls are found on screens that ask users to make decisions or declare preferences such as settings or dialogs.

### Principles

![Image 1](https://lh3.googleusercontent.com/AluZnXju9EMBSVJpSbSKSHH8Ue0M8a_1jwvHu9KAoHTD3HNH-U0s7ty7AjEc2O6GBM4obY9uWSFaxe5a5ET-rgldoGvl0WOJr-IyQA=w1064-v0)

#### Familiar

Selection controls have been in user interfaces for a long time and should be used as expected.

![Image 2](https://lh3.googleusercontent.com/dFONXu9oySSLQZBjcXrJp2TPVmhcRcv07GjDjfs5GTjf8aJUkekJ7RXT3z46bYDqFgd8paMnrHKbBLid5oG23jn8mJ8SkFSQ_HfAXQ=w1064-v0)

#### Scannable

It should be visible at a glance if a selection control has been selected, and selected items should be more visually prominent than unselected items.

![Image 3](https://lh3.googleusercontent.com/xM-hOYmGuaFgkcDo1SGYUMlwdb9hkh4FJrLL-6LCf42rQDqlkEBpwigzWzhvRt9iXbt_r5MDo9ykBpORe7wtOZajnXbNPpKbV_4QbQ=w1064-v0)

#### Efficient

Selection controls make it easy to compare available options.

* * *

Selection controls are radio buttons, checkboxes, and switches.

![Image 4: Two radio buttons. One is selected and the other is unselected](https://lh3.googleusercontent.com/ROHV_wo1ZnsFHDf05fwQYkVnPHPzFpGEDDjYr2DfVVCwcolvW0X6-nmp4lD-62aCk42VIUhu0XRNhdtoyfQ9Wi9FJHX2LP-SYeGijyM=w1064-v0)

#### Radio buttons

![Image 5: Two checkboxes. One is selected and the other is unselected](https://lh3.googleusercontent.com/t9cpY6rQsr19RqiZtBwKQzwKw9NoKKK-FDO7PJN0xXiskl6GaxKPRwkzlrlzNu478brLIIMVx9-UST8Vbw3FkhLWTgqYSFS9Qkze6hk=w1064-v0)

#### Checkboxes

![Image 6: Two switches. One is on and the other is off](https://lh3.googleusercontent.com/hfIWNN2F2aBPObE2pv2xTy5oPRUteGtr5-h0Fc0cMJzeDu_wZYRLXgpIIpPzmQ89ALOUSFIBbwk6loxDkF4nmAjgeC0e-R0u_muriAE=w1064-v0)

#### Switches

* * *

Selection controls should be used

Use radio buttons to:

*   Select a single option from a list
*   Expose all available options

If available options can be collapsed, consider using a dropdown menu instead, as it uses less space.

![Image 7: List of options to select phone ringtone. Each option has a radio button](https://lh3.googleusercontent.com/c7RktMgE1eqzEX-G_7Mcux-YjvbF_VGUCx_QgFSRsd9kKUzYarHAGAnUTFFHH621CSObn3D9mk1tUM2Fm6wqNX7BBxhahHLpBecVqQ=w1064-v0)

Radio buttons allow for a single option to be selected from a visible list

Radio buttons should be used instead of checkboxes if only one item can be selected from a list.

![Image 8: List of shipping options to home or work. Each option has a checkbox](https://lh3.googleusercontent.com/pwXHXanhFW1agZwzDXs_T0c16jYOfipMTUwzepbatdzfoMQrjvdfNY7W1O9bmi8xZ7s5GxgDoE34eN_A15gZ0jT0cpme66IFASAIZA=w1064-v0)

Don't Don't use checkboxes when only one item can be selected from a list. Use radio buttons instead.

![Image 9: List of shipping options to home or work. Each option has a radio button](https://lh3.googleusercontent.com/-B2N7p8JoHUQE7apVvLE-TcNrTAT8kAnNRavwGRL5LysfKMwSxEsOjnfPX3t4wEiKZm6pCRV5wCO6yajXSu5FC4AkJ9fGTjRI8Yv=w1064-v0)

Do Use radio buttons when only one item can be selected from a list.

* * *

Use switches to: Switches should be used instead of radio buttons if each item in a set can be independently controlled.

Use switches to:

*   Toggle a single item on or off, on mobile and tablet
*   Immediately activate or deactivate something

![Image 10: List of phone settings. Each setting has a switch](https://lh3.googleusercontent.com/QL0d4VhCiaTv_J0ZQfeZln4UGp7n4fmTYfZ6wMDbAOA0j1UxkOB90J-3r7PTfFijVqMZux2RXcU0DPwEsFhejUWWt7DdGbXQBuDoW78=w1064-v0)

Switches

Switches should be used instead of radio buttons if each item in a set can be independently controlled.

![Image 11: List of phone settings. Each item has a radio button](https://lh3.googleusercontent.com/D_TMOiw8-9Cr_HyRBN--djeGULrub4ddEvPNWctZRWHqbqpHnaLtFxD4w3pNwI63p75pnkyE0F9p4lVG-SCtclOgzXVG2AzYU3E0=w1064-v0)

Don't Don't use radio buttons to toggle items on or off. Radio buttons convey that a set of items are options, and that only one can be selected at a time.

![Image 12: List of phone settings. Each item has a switch](https://lh3.googleusercontent.com/_2efsFZHxvF95FzsIVfJQGg3ZjZoLi9CwZ_vyc9sA_Tu_AT0mERYvJlGfPVRfc0ToqgEe6c3URmHgyaJ4YTdvN0r8hPRD5n4IyyaRg=w1064-v0)

Do Use switches to turn an item on or off, especially on mobile instead of a checkbox.

* * *

Use checkboxes to:

Use checkboxes to:

*   Select one or more options from a list
*   Present a list containing sub-selections
*   Turn an item on or off in a desktop environment

![Image 13: List of meal options: pickles, tomato, lettuce, and cheese. Each option has a checkbox](https://lh3.googleusercontent.com/AYL8sj54zSd-rxUBs2IVgDXDzaFvMnwFayX7y7VHMZGQ100DezCX_Ze4t7-d_ZOX-nm_Rxgg6DTEfJ4aN4ditdeJUhutCaOhbjr8=w1064-v0)

Checkboxes

#### When to use checkboxes instead of switches

![Image 14: List of types of emails to receive. Each item has a switch](https://lh3.googleusercontent.com/W9Qu2CURc6uvgYHDBzldrsW6uiKTAyZic7W3weH1anLDRy9rHTVFW5UdD4OE46MRorAvf2---xvpcPDW46DsDDpJkZ3N3ruD-vpB=w1064-v0)

Don't If a list consists of multiple options, use checkboxes instead of switches. Checkboxes imply the items are related, and take up less visual space.

![Image 15: List of types of emails to receive. Each option has a checkbox and the first option is a parent control for receiving emails](https://lh3.googleusercontent.com/k5evzma2gRvUP8mN8i3-pPRxtHzpQvA9mvQ5ikPhMw3Nbzf7K210MbILFgjXhtzGiRVlESkeylx7vIYQi2OryRCOpPqGvnj-8fACSQ=w1064-v0)

Do Checkboxes let users select one or more options from a list. A parent checkbox allows for easy selection or deselection of all items.

* * *

Adapt selection controls to correspond with platform standards.

![Image 16](https://lh3.googleusercontent.com/PWQusdYgcSZkXGvqvEps0gP9g-aqPKaJ1utULmSIX7tbhKUtBm-6vbhFQ63LiSk8T3RuPfFd74RUqGzOM9u8gQK-IWpSH6Mr-_UNzKM=w1064-v0)

**Android**

 Use Material switches, checkboxes, and radio buttons.

![Image 17](https://lh3.googleusercontent.com/771zxWG7CmVmdAEpiLrSCIKZsHa-AyyK59iOK8hTRnG7_k3vVmIoDU439EA-qI2n7qNrL8BkTU0sLAozP5sTln99-qhACvvRtkVN-A=w1064-v0)

**iOS**

 Native platform switches should be used as they have matching functionality and presentation as Material switches.
Use switches instead of checkboxes and check mark lists instead of radio buttons as these are the graphics expected on iOS.

* * *

## Checkboxes [](https://m2.material.io/)

Checkboxes allow the user to select one or more items from a set. Checkboxes can be used to turn an option on or off. Checkboxes...

Checkboxes allow the user to select one or more items from a set. Checkboxes can be used to turn an option on or off.

![Image 18](https://lh3.googleusercontent.com/j-kKHKZ1GpSPIP6A-94OcFOcgJ8fB2oilQrXXfLShXfWxINdrIx2f22E-Jv4sZ3wcNJTLSJJbnXj1RRveYcMw87KPSr3SZQjctfiNQ=w1064-v0)

Selected and unselected checkboxes

Selecting multiple items in a list using checkboxes

Turning an item on or off using a checkbox

#### Parent and child checkboxes

Checkboxes can have a parent-child relationship with other checkboxes.

*   When the parent checkbox is checked, all child checkboxes are checked
*   If a parent checkbox is unchecked, all child checkboxes are unchecked
*   If some, but not all, child checkboxes are checked, the parent checkbox becomes an indeterminate checkbox

Checked, unchecked, and indeterminate states of a parent checkbox

* * *

Checkboxes can be selected, unselected, or indeterminate. Checkboxes have enabled, disabled, hover, focused and pressed states.

Checkboxes can be selected, unselected, or indeterminate. Checkboxes have enabled, disabled, hover, focused and pressed states.

![Image 19: Matrix of all checkbox state combinations](https://lh3.googleusercontent.com/uIZAD8BqdUty_SKq4IqRBcQ5LZEDl_4obrO2eWArEW2FNrP6o1PgRAJrmaGM1nfF9pCI7dQKvftHIJHFBSFpAS_1HbT_3RPSv8DrJjI=w1064-v0)

Interaction states for selected, unselected, and indeterminate checkboxes

* * *

## Radio buttons [](https://m2.material.io/)

Radio buttons allow the user to select one option from a set. Use radio buttons when the user needs to see all available options. If...

Radio buttons allow the user to select one option from a set. Use radio buttons when the user needs to see all available options. If available options can be collapsed, consider using a dropdown menu because it uses less space.

![Image 20: Selected and unselected radio buttons](https://lh3.googleusercontent.com/qnnNzwXtfiaWZjS9bFa2kL3jL5yd93ytx9Ho2MCCMo1lZQ7k_CG9zzqqzrLkdM-7n9jSwURzaiFFwLJnpxSbTUo9uGfdW2rKXALFoA=w1064-v0)

Selected and unselected radio buttons

Using radio buttons to select a single item

* * *

Radio buttons can be selected or unselected. Radio buttons have enabled, disabled, hover, focused and pressed states.

Radio buttons can be selected or unselected. Radio buttons have enabled, disabled, hover, focused and pressed states.

![Image 21: Matrix of all radio button state combinations](https://lh3.googleusercontent.com/xQK41sPgGmQNzcqCAgAiycOZQNh75Ono9cvtrFomKPBAi0CDuaqhn2jTn7Grbr3tMQMTmhMIzN8x0tqmSN4BT5j6Wwf9-e0W4qIbS2k=w1064-v0)

Interaction states for selected and unselected radio buttons

* * *

## Switches [](https://m2.material.io/)

Switches toggle the state of a single item on or off. They are the preferred way to adjust settings on mobile.

Switches toggle the state of a single item on or off. They are the preferred way to adjust settings on mobile.

#### State

A switch is successfully toggled when the switch thumb slides to the other side of the track upon user interaction.

#### Text label

The option that the switch controls, as well as the state it's in, should be made clear from the corresponding inline label.

Avoid creating a switch that includes the text "on" and "off" within the graphic itself. The switch alone should be sufficient.

![Image 22: Unselected and selected switches with numbers identifying its 2 elements and states](https://lh3.googleusercontent.com/r0pCV2CAoi4lCwtJNo4S3UpA4SehUUB48Wpe2QGexCQAWFYfe0j8VRjTrMjFh36weNqbHngUlt6TY770Mk0TnMPIMRbGn-5RTp7pYw=w1064-v0)

1. Thumb 

2. Track

Using a switch to turn an option on and off

* * *

When a user toggles a switch, its corresponding action takes effect immediately.

When a user toggles a switch, its corresponding action takes effect immediately.

#### Display processing status

Because a switch shows the actual status of something, sometimes there is a delay in its change of state. In such cases, a processing status animation can be used.

A processing status is an animation on the thumb of the switch. For example, it can be used when a switch that controls a hardware feature experiences a delay before its final status can be confirmed.

A processing status animation on the thumb of a switch

* * *

Switches can be on or off. Switches have enabled, disabled, hover, focused, and pressed states.

Switches can be on or off. Switches have enabled, disabled, hover, focused, and pressed states.

Display the outer radial reaction only on form factors that use touch, where interaction may otherwise obstruct the switch completely.

For desktop, the radial reaction isn't needed.

![Image 23: Matrix of all switch state combinations](https://lh3.googleusercontent.com/6FtXA5o7Dqb_gn4k_ORUmK59j0ILBEkijtDYIhnQwlOQyMJlMd7wGnRq5_xhMFOgOXEqMcdh-K6PcP7ZKUyyLKWgW0PJxZumLO-WPQ=w1064-v0)

Interaction states for on and off switches

* * *

## Theming [](https://m2.material.io/)

This travel app's selection controls have been customized using Material Theming to use custom color. Crane is a travel app that uses Material Design components...

This travel app's selection controls have been customized using Material Theming to use custom color.

![Image 24: List with checkboxes with custom style to match Crane app’s brand](https://lh3.googleusercontent.com/rxtNZFCSJs_0b-tRrLXTemLk2n2DmXaV5NqjSYkp30cMG-2E1X3uGejvzw9ksUDbDOOBorWhLC3i0Zhhso6b0BNoUbNcMTo-Cw_JWA=w1064-v0)

Crane's customized selection controls

#### Color

Crane's selection controls use a custom color.

![Image 25: Selected checkbox with Crane’s custom color values applied](https://lh3.googleusercontent.com/1Ze1DhY8Jy_jovuGkUl7uckCDoLwIirb0toiMBdkMtX4UNbp30p5NTF8xoCk39A5nHLJpsAY9Z5XCwBREgp9SndP8OTzUs7Waeti4w=w1064-v0)

| Element | Category | Attribute | Value |
| --- | --- | --- | --- |
| Selection controls | Secondary | Color Opacity | #E30425 100% |

* * *

## Specs [](https://m2.material.io/)

#### Checkboxes

*    Measurement 24 

![Image 26](https://storage.googleapis.com/spec-host-backup/mio-components%2Fassets%2F1seffKf9Q3x_zfhAuO8NTGHY86aQj1C5f%2Fselectioncontrols-spec-checkboxes.png)

#### Radio buttons

*    Measurement 20 

![Image 27](https://storage.googleapis.com/spec-host-backup/mio-components%2Fassets%2F1NsvAakg42RV_h0_mz4CKTuSwwprxiYFW%2Fselectioncontrols-spec-radiobuttons.png)

#### Switches

*    Measurement 20 
*    Measurement 36 

![Image 28](https://storage.googleapis.com/spec-host-backup/mio-components%2Fassets%2F1mptGCFjmK-9Vb3yNJe6xGB3_U4f32xe2%2Fselectioncontrols-spec-switches.png)

No Android implementation guidance available

No Web implementation guidance available

No Flutter implementation guidance available

No iOS implementation guidance available

## Related
[Add wiki-links manually or run update_wikilinks.py]