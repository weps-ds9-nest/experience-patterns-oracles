# > In this article, I’m going to talk about my learnings about designing a complex dashboard.

> In this article, I’m going to talk about my learnings about designing a complex dashboard.

## About the Project

As the first product designer to join Unscript as an intern, I played a pivotal role in building the company’s product from the ground up to a large-scale platform within a year. Throughout my internship, I engaged in numerous and diverse projects. This case study focuses on one of the most significant and cherished projects I led. I was the sole designer responsible for this project from inception to completion while collaborating with various key team members.

### Key Collaborations:

*   **Co-founder:** Collaborated to understand the full scope of the project and its requirements. We introduced several innovative features such as text-to-video, a video editor, email and landing page templates, and revamped existing workflows like the campaign and avatar training.
*   **Senior Design Consultant(Mentor) and Stakeholders:** Sought timely feedback on my designs and overall design direction.
*   **Engineers:** Worked closely to ensure the final output precisely matched the design specifications.

## About the Company

Unscript leverages cutting-edge AI technology to revolutionize video production with realistic human avatars. Our platform creates unique, personalized videos for each customer, fostering increased loyalty and driving higher conversion rates over time. /company link/

> Experience the future of video production with Unscript.

## The Product Dashboard

With the expansion of Research and Development within our company, the potential for new functionalities within our product became evident. Our journey began with data collection for training AI-based human avatars, followed by the creation of landing pages and email templates for marketing campaigns. Subsequently, we ventured into running custom marketing campaigns, implementing text-to-video capabilities using AI-trained avatars, and developing a comprehensive video editor with versatile functionality catering to both B2B and B2C use cases.

Given the scope of these enhancements, we opted to meticulously design the entire product, tackling each phase and feature methodically. Building the product from the ground up necessitated the introduction of a new design language for the platform.

So let’s get started🚀

## Product Structure

The co-founder provided me with the requirements of various features that the product should have. Here’s how the product flow looked.

Product flow

So let’s discuss the initial design decisions:

*   On the left-hand side, we have 7 tabs that take us to respective functionality or pages.

*   Each functionality has 4–5 steps involved on average, so we decided to handle all the functionalities in full-screen modals with a dedicated stepper on the left-hand side, educating the user on the progress and how many more steps are left to be completed.

*   Each functionality is going to have an empty state with a prompt and a CTA to encourage the user to start using that functionality.

Empty states

## Model/Avatar

### Context

The cornerstone feature of our product is the data collection process for training AI-based human avatars. The fundamental concept involves gathering video data from users and adhering to specific constraints and protocols. Users are required to provide either ten video clips, each one minute in length, or a total of ten minutes of video data. This data is crucial for effectively training the AI models to create realistic and responsive human avatars.

### User Story

> **User Persona:** Aarav, a 32-year-old Marketing Manager, seeks to train an avatar/model for marketing campaigns.
> 
> 
> **Challenge:** He struggles to gather clean video data that meets the specific requirements for training.
> 
> 
> **Solution:** Includes scripts for 10 videos for in-house recording, an in-house teleprompter for assistance, and an option to upload clean video data if available.

### Model/Avatar Screen

### Create New Model/Avatar

### Entry Points for Creating a Model/Avatar

Before starting the model/avatar creation process, it’s crucial to define entry points for first-time and regular users. For first-time users, we provide an engaging illustration with explanatory text and a prominent CTA to prompt avatar creation. Regular users see a CTA on the model/avatar listing screen, allowing them to initiate the creation process easily. These entry points ensure a smooth and intuitive experience for all users.

Now, let’s begin with the steps and discuss them individually.

### Step 1: Introduction — Enter Avatar/Model Details

In this initial step, users are required to name their avatar/model. To guide them through the process of training the avatar/model, we provide essential instructions in both video and written formats. This ensures users are well-informed about the steps involved, facilitating a smoother and more efficient experience.

### Step 2: Train Our AI — Record or Upload Training Videos 📷

This step, which involves collecting training videos, is the most challenging for both the user and us. The complexity arises because this page serves as the entry point for the teleprompter functionality. Users have multiple options: they can download all video scripts and upload videos created using the script without the teleprompter, record videos locally using the teleprompter, or use the teleprompter and then upload an external recording.

This modal helps us narrow down the choices and select the modes through which the user wants to train our AI.

Let’s first try out the Record using our set script!

### Record Using Our Set Script

This option lets the user upload or record videos using the provided scripts.

The training video cards here took a lot of iterations and brainstorming to finalize. Let’s quickly have a look at few of the iterations.

Iterations

**Final component**

Now, here’s a catch: when you hover any of the icons on the card, they expand and show what that icon is for.

This is what the entire screen looks like:

Training videos pending

Training videos uploaded or recorded successfully

### Teleprompter

To understand the need for a teleprompter, consider the difficulty of repeating a script word for word. Memorizing a script and saying it exactly as written is challenging, highlighting the need for a preview of the script during video recording. Recognizing this need, we developed our in-house teleprompter, which not only displays the script but also allows users to record videos simultaneously.

### Upload Video Data of 10 Minutes

With advancements in our R&D, the product has evolved to train models/avatars with just 10 minutes of video data. This can be a single continuous clip or multiple clips, each with a minimum length of 10 seconds. This flexibility allows users to provide the necessary training data in a manner that best suits their convenience.

The structure of this page is straightforward. The middle section is the upload area for video files, while the corner section provides instructions outlining the requirements to ensure a high success rate.

### Step 3: Provide Consent — Record Consent Video 🧑⚖️

Given the increasing concerns about crimes involving AI, ensuring that users provide explicit consent for Unscript to use their video data for training models/avatars is crucial. We made this crucial product decision and iterated upon its implementation. Initially, we considered using a checkbox for users to mark their consent, a common practice. However, we determined that a consent video would be more viable, genuine, and legitimate, especially in the context of video data.

To verify that the person in the training videos consents to use their video data, users must record a consent video using a predefined script displayed via the teleprompter. This video must be recorded in-house; external video uploads are not permitted. This measure guarantees that users clearly acknowledge and authorize the use of their data to create models/avatars.

### Step 4: Congratulations! Your Model/Avatar is in Training 🎉

Once the model/avatar creation process is initiated, it will take approximately 48 hours to complete the training. At this point, users are provided with a clear exit from this functionality. They will receive notifications both via email and in-app once the training is finished.

In the meantime, users are encouraged to explore other functionalities, such as text-to-video or campaign video creation, or they can return to the models/avatars page. This ensures users remain engaged and productive while their model/avatar is being trained.

Success modal

Let’s have a clear look on the card component and it’s various states.

It was not easy to finalize the card, had to iterate a lot, here are some discarded iterations:

> Let’s move forward to other functionality of the product i.e., _Templates_!

## Templates

### Context

Email and landing page templates are indispensable assets for any sales and marketing campaign. They offer numerous benefits, from ensuring brand consistency and saving time, to enabling personalization, scalability, and data-driven optimization. By leveraging these templates, businesses can enhance their marketing efforts, engage their audience more effectively, and ultimately drive greater sales and growth.

If Unscript enables in-house marketing campaigns, it should also allow users to create templates in just a few clicks.

### User Story

> **Persona**: Abhinav, a 25-year-old marketing manager at a mid-sized tech company. He is tech-savvy and values tools that streamline his workflow.
> 
> 
> **Challenges**: He faces time constraints managing multiple campaigns and finds creating new templates from scratch time-consuming. Ensuring brand consistency and personalizing content efficiently are also significant challenges.
> 
> 
> **Solution**: Create email and landing page templates in just a few clicks to quickly design consistent, and run campaigns within a single platform.

### Template Screen

### Create New Template

The process for creating landing page templates and email templates is almost identical. Let’s examine both flows.

When creating a template, it’s crucial for the user to see how the template looks as they add information and other relevant fields. To facilitate this, we designed the full-screen modal to be divided into three sections:

*   **Stepper:** This is consistent throughout the product.
*   **Form Section:** User can enter or upload relevant information and materials for the template.
*   **Live Preview:** This section provides a real-time preview of the template, allowing users to see their changes instantly.

While creating these templates, we realized some users might need even more flexibility. Although our platform offers a lot of customization options, there could be cases where users want to directly edit the HTML of the template to create a custom design. To accommodate this need, we provide the option for users to edit the HTML of the template as well directly.

Email template on left & Landing page template on right

### Step 1: Branding Info — Add Branding Details 🎨

In this step, the user provides essential branding details for the template. They enter the name of the template, upload the company or brand logo, and choose a brand color. The selected brand color is used for the primary CTA, and a light, minimalistic shade of the brand color is applied to the background of the template. This ensures the template aligns with the company’s branding and maintains a cohesive visual identity.

### Step 2: Video Thumbnail — Upload/Create a Thumbnail 🌁

Videos are a crucial element of email and landing page templates, significantly impacting click-through and conversion rates. In this step, users upload or create a thumbnail for the campaign video, which they select during the campaign creation process. To create the thumbnail, users can choose a model/avatar they want to feature and then select a preset thumbnail design. The chosen model/avatar is seamlessly integrated into the preset thumbnail, ensuring a professional and appealing visual that enhances the likelihood of user interaction and conversion.

For the time being, we only have the option to upload the video thumbnail.

Email template on left & Landing page template on right

### Step 3: Template Details — Enter Template Details

In this step, the user adds all necessary text hierarchies, including greeting text, the main message, and button text required for the template. Users can customize the number of CTAs, ranging from 0 to 2, and provide the links for redirection from each CTA. This flexibility allows for a tailored approach to meet specific campaign goals and enhance user engagement.

Email template on left & Landing page template on right

### Template Created Successfully

After the flow is completed, we acknowledge with a success modal.

> Let’s move forward explore, _Campaigns_!

## Campaign

### Context

Campaigns are designed to deliver personalized and engaging content to target audiences, maximizing the impact of marketing efforts. One powerful example of this personalization is through campaign video scripts and emails/landing pages.

**Example Campaign Video Script:**

> “Dear Mayank,
> 
> 
> Congratulations and welcome to the Raymond family! You’ve made a great choice with the Raymond 10X project. Our first tower is progressing well ahead of schedule, and we’re two years ahead of our original timeline. I look forward to delivering your home soon so you can enjoy the 10X lifestyle and over 50 amenities.
> 
> 
> Thanks!”

In this script, “Mayank” and “Raymond family” are considered **variables**. Unscript can replace these variables with any names, allowing the creation of numerous personalized videos.

**Example Campaign Email:**

> Subject: Welcome to the [Company Name] Family, [First Name]!
> 
> 
> Dear [First Name],
> 
> 
> We are thrilled to welcome you to the [Company Name] family! Your decision to invest in the Raymond 10X project is a fantastic choice. Our first tower is progressing well ahead of schedule, and we are now two years ahead of our original timeline. We can’t wait to deliver your new home so you can start enjoying the 10X lifestyle and over 50 amenities.
> 
> 
> If you have any questions, please feel free to reach out. We look forward to seeing you soon.
> 
> 
> Best regards,
> 
>  [Company Name]

In this email, “[First Name]” and “[Company Name]” are variables that Unscript can replace with the recipient’s name and the company name, creating a personalized experience for each user.

By leveraging Unscript’s capabilities, campaigns can deliver a personalized experience at scale, ensuring each recipient feels uniquely addressed and valued.

### User Story

> **Persona**: Anchal, 24 years old, is a marketing intern at a real estate development firm, specializing in email marketing and online engagement.
> 
> 
> **Challenges**: Anchal struggles to create personalized content for a large audience efficiently.
> 
> 
> **Solution:** Unscript automates personalized messages in video scripts and emails, offers customizable templates for consistent branding.

### Campaign Screen

### Create New Campaign

### Step 1: Select a campaign video — Use or Create a Model/Avatar Based Video for your Campaign

In this step, the user can choose to either use an existing campaign video, which could have been created for a previous campaign or immediately after creating a model/avatar, or create a new campaign video. This flexibility allows the user to leverage existing content or produce fresh, personalized videos for their campaign.

Alongside the the play icon, we decided to give an option for viewing the script of the video so, the user can be sure that the chosen is the correct one.

### Create New Campaign Video

When creating a new campaign video, the user can include variables in the script to personalize each video. The variables will be seamlessly stitched into the base video, allowing for the creation of numerous personalized videos as needed. The user specifies any variables in the script by selecting options from a dropdown below the script text box. Unscript’s text-to-video capabilities then generate the videos with these variables, integrating them into the base video for a cohesive and customized campaign.

Let’s have a look at how the Insert variable thing works:

If the user chooses to record a new campaign video, teleprompter opens. The variables in the script are replaced by AI generated values.

### Step 2: Campaign Data — Upload CSV File for your Campaign

In this step, the user uploads a CSV file that includes all the variables and the list of email addresses or phone numbers, depending on the campaign medium. To assist the user, a sample CSV file is provided for reference, ensuring they can easily format their data correctly for the campaign. This step is crucial for personalizing the content and targeting the right audience effectively.

### Step 3: Campaign Details — Select Delivery Channel for Your Campaign

In this step, the user names the campaign and selects the delivery medium. Only email campaigns are currently supported, as technical decisions for WhatsApp campaigns are still pending. The user chooses the email address to run the campaign. If no email address has been verified on the platform, the user is prompted to add and verify an email before proceeding.

### Step 4: Template — Select Appropriate Email/Landing Page Template

In this step, the user selects an appropriate email or landing page template for their campaign. The user can preview the template and make any necessary edits to ensure it aligns with their branding and campaign goals. This flexibility ensures that all communications are visually appealing, professional, and tailored to the campaign’s needs.

### Finish — Launch Your Campaign

Once the campaign has been successfully created, the user needs to trigger it by clicking on the appropriate action to start the campaign. This final step initiates the delivery of personalized content to the targeted audience, completing the campaign setup process.

> Now, let’s explore some of the advanced AI-based functionalities that set this product apart and serve as key selling points. These innovative features leverage cutting-edge technology to enhance user experience and campaign effectiveness.

## Video Creation

### Context

The product initially focused on campaign videos by stitching variables into existing footage, enabling video personalization and bulk production. As technology advanced, the Co-founder envisioned revolutionizing video creation further with a Text-to-Video functionality. This feature evolved into a comprehensive AI-based video editor, allowing users to create fully customized videos using AI.

Unlike prompt-based video generation, this feature allows users to provide a script, and the AI will generate audio and lip-sync the avatar to match the script, creating a seamless and realistic video. This innovation eventually evolved into a comprehensive AI-based video editor, empowering users to create fully customized videos with AI.

By streamlining the video production process, this functionality significantly reduces both production time and costs, making it accessible and efficient for businesses of all sizes.

### User Story

> **Persona:** Sonal, 28 years old, Human Resource manager at Mishipay, wants to conduct a training sessions for upskilling.
> 
> 
> **Challenges:** Sonal faces difficulties in conducting live training sessions due to the large size of her company. Recording and editing numerous videos to meet diverse training requirements is tedious and time-consuming.
> 
> 
> **Solution:** Sonal uses Unscript’s video creator with text-to-video capabilities. By inputting training scripts, the AI generates and lip-syncs avatars to create high-quality training videos efficiently, saving Sonal time and effort while ensuring engaging and personalized training content for her employees.

## Create Video Using Simple Text

For events or use cases requiring a quick video message, users can simply enter a script and generate a video. While it might seem that short videos require minimal effort, there’s a significant advantage: many brands train Avatars/Models of celebrities with their full consent and later use these Avatars/Models for immediate video creation. This allows for rapid production of high-quality, personalized videos featuring recognizable figures, enhancing the impact and relevance of the message.

/add flow diagram/

### Step 1: Select a Model — Select/Create a Model/Avatar to Create Videos

In this step, the user selects or creates a model/avatar that will be used to generate the video message. This choice allows the user to leverage pre-trained avatars, including those of celebrities, to quickly produce engaging and personalized videos.

### Step 2: Video Details — Enter Script and Generate Your Video 📷

In this step, the user provides details for the video by entering a name and selecting a script source. With the latest update, there are two options: the user can either upload an audio file to be lip-synced by the avatar/model or type the script, and the AI will generate the audio and lip-sync with the avatar/model. This flexibility ensures that users can quickly create personalized and high-quality video messages.

The user then has the option to save the video or revise the script and generate it again, ensuring satisfaction with the final product.

The CTA in the text box generates audio and the video loads on the right hand side, though the video doesn’t have a lip sync, the lip sync is generated when user clicks on “Save video”.

### Finish — Video Created

Your video has been successfully created. You can now share the video, download it, or embed it in any landing page template for further sharing. This flexibility allows you to utilize the video across various platforms and purposes, ensuring maximum reach and impact.

## Complete AI-Based Video Editor

This video editor goes beyond simple text-to-video functionality, enabling users to create impressive video presentations, product demonstrations, customer onboarding videos, and more. It’s a comprehensive tool designed to meet diverse video production needs. Given its extensive capabilities and ongoing advancements in technology and R&D, I will write a separate case study to thoroughly explore this feature.

> In the meantime, let’s delve into the other crucial screens of the product. While they may not represent the primary features or core functionality, they play a significant role in the overall product development, business strategy, and user experience.

## Support

Given that this product diverges from conventional applications and encompasses numerous features and steps, it’s essential to recognize that it caters to a new market and user base. As the product is still in its early stages of development, users may encounter bugs or issues that require reporting to stakeholders. Hence, the inclusion of a support screen becomes crucial. This screen not only facilitates bug reporting but also provides links to relevant documentation that users may require for assistance.

## Settings

The Settings section is divided into three distinct sections, each catering to specific user needs and accessibility based on subscription plans.

### General Settings:

This section encompasses essential profile details, such as name and contact information, along with the option to customize the company subdomain.

For instance, users can utilize their company name when sharing videos and templates, enhancing brand recognition.

Additionally, users can manage their verified email list for campaigns, facilitating efficient communication with target audiences.

Furthermore, there are options to change passwords for users who signed up using email authentication and set passwords for those who opted for Google authentication.

### Subscription (Visible to Subscribed Users):

This section is exclusively accessible to users who have subscribed to the service. It provides vital information regarding the subscription, including the next billing date, monthly allocation of avatars/models, total invoice, and the current active plan. Users can also explore options to upgrade or recharge their subscription plan. Additionally, this page displays the billing history and other relevant details in a tabular format for easy reference.

### API Keys (Exclusive to Enterprise Plan Users):

This section is specifically designed for users on the Enterprise plan. It provides access to API keys, enabling integration with external systems and applications.

First, the user sees an empty state, and then the state is where we add the API key.

These API keys serve as credentials for secure communication between the product and other platforms, facilitating seamless data exchange and workflow automation.

There are various states involved in API key setting process. Let’s have a look.

Now you might see 2 options in the added API key. First is the “Delete key,” which is something self-explanatory; second option is the “Reissue key,” this option can be used in cases where you give access to the key to someone and now want to revoke the access without deleting the key.

Users can atmost of 3 active API keys at a time. Users can create new keys if the old ones expire.

## Pricing

The pricing page is structured to provide a side-by-side comparison of the plans, making it easy for users to understand the differences and choose the plan that best fits their needs. Key features and benefits are highlighted for each plan, ensuring users can quickly grasp the value propositions. Keeping the target audience in mind, we’ve included a toggle to convert the pricing between USD and INR, accommodating users from different regions.

## Notifications

Notifications are indeed crucial for informing users about the completion of any process, especially considering the wait time after every trigger. We adopted a minimalistic and easy-to-understand design to ensure users are promptly and clearly informed, enhancing their overall experience.

## Home Page

The home page was the toughest to crack. For a long time, we couldn’t figure out what to include. After proctoring a few users with consent, we noticed that the most important actions for any user are either generating videos or creating new models, as these are the elementary steps to use the product. Considering the learning curve, we included an introductory video alongside links to documentation. Since the main source of revenue for the company is when users create videos using models/avatars, we also displayed a list of a few generated and library models.

## Product Walkthrough

Given that our product is not conventional and involves a learning curve, so we’ve incorporated a product walkthrough for first-time users. This walkthrough can be re-triggered anytime in the future, helping users familiarize themselves with the product’s functionalities and ensuring a smoother onboarding experience.

## Dev Handovers

Dev handovers were initially challenging as this was my first live project. I started by sharing flow prototype links and screen recordings to help developers understand interactions, but identifying specific frames was difficult. With Figma’s Dev Mode, my process improved. I marked entire sections for developers, included Dev Mode links, and linked component documentation within Figma, enhancing the efficiency and clarity of handovers.

## Learnings

I learned the value of starting with an open-source design system, as building one from scratch is tough without a dedicated team. Collaborating with cross-functional teams — developers, business stakeholders, and product managers — was essential. Iteration proved crucial for good visual design. Testing the product with internal marketing and business teams, whose personas matched our target audience, ensured we kept users at the forefront of our development process.

> I would like to give a special shoutout to [Sejal Jain](https://www.linkedin.com/in/sejaljain2043/), my colleague and college senior, [Apurv Jain](https://www.linkedin.com/in/apurvjain93/), Co-founder of Unscript, Shobhit and Anup from the founding team, and [Prajit Nandeshwar](https://www.linkedin.com/in/prajit-nandeshwar/), our UX consultant, for their constant support and guidance.

## Let’s collaborate

If you’re looking for a product guy who is passionate about creating user-centric solutions, feel free to reach out to me. Let’s build something amazing together!

[LinkedIn](https://www.linkedin.com/in/sahil-mittal07/) | [Portfolio](https://www.sahilmittal.studio/) | [Dribbble](https://dribbble.com/sahil-mittal) | [Medium](https://medium.com/@sahil-mittal) | [Behance](https://www.behance.net/sahil-mittal) | [Email](mailto:sahilm0704@gmail.com)

## Related
[Add wiki-links manually or run update_wikilinks.py]