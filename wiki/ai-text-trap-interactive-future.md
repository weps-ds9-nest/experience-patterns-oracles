# AI's Text Trap: Moving Towards a More Interactive Future

AI assistants trapped in text-based interfaces create commoditization risk for SaaS products. Conversational-only UX limits complex workflows to information retrieval and basic CRUD operations. The solution: integrate design systems into AI assistants so they render rich, differentiated interfaces instead of generic text blocks. Three design modes enable richer AI experiences: rich output (data visualization replacing text), UI as input (structured forms replacing prompts), and co-creation (workspaces supporting multi-step workflows with fluid modality switching, proactive suggestions, task delegation, and contextual refinement).

## Key Patterns & Concepts

- **Closed vs Open Approaches**: Closed (embedded in single product like Zoom AI, Salesforce Einstein, Copilot); Open (external assistants like Claude, ChatGPT, Gemini enhanced via MCP protocol)
- **Text-Trap Risk**: Text-only interfaces reduce UX to commodity; commoditized products lose differentiation; commoditized SaaS reduces companies to "just an API"
- **Generative UI Risk**: AI autonomously creating interfaces from training data defaults to generic average; every product looks same; no differentiation; reinforces mediocrity
- **Rich Output Mode**: Data visualization instead of text; display contact cards side-by-side not essays; maximizes scannability, helps user grasp situations instantly
- **UI as Input Mode**: Structured input components (query builders) replacing text prompts; removes ambiguity; reduces back-and-forth; faster, more precise interaction
- **Co-Creation Mode**: AI becomes workspace not responder; supports multi-step workflows (marketing campaigns, complex reports, integrations); transforms turn-by-turn conversation
- **Fluid Modality Switching**: Users toggle between text and direct manipulation without forced prompts; adjust UI elements directly (change wait time vs prompt)
- **Proactive Cross-Tool Suggestions**: AI pulls data from connected tools into workflow; surfaces insights without being prompted; knows when silence better choice
- **Delegation of Subtasks**: User hands off contained work; AI executes while user continues; co-creation as division of labor
- **Contextual Text Refinement**: Text prompts anchored to UI elements not generic prompt box; AI understands position in workflow not just what user saying
- **Design System Integration**: AI assistants have knowledge of product's unique design system, components, patterns, guidelines; enables rich interface rendering

## Full Article

LLMs made AI assistants standard SaaS feature. AI assistants allow instant information retrieval and text-based system interaction. However, both Closed and Open approaches offer flexibility while reducing carefully crafted UX to purely text-based interface. Text-only interfaces detached from product mean UX no longer differentiator—product risks becoming commodity.

### Risk of Commoditization

Text-only interfaces also limit interactions to simple information retrieval and basic CRUD operations, making complex workflows difficult. Andrej Karpathy noted: text favored by computers/LLMs but not humans. Humans prefer visual information. Chat often poor fit for complex interaction patterns.

### Temptation of Generative UI

One answer gaining traction: generative UI where AI autonomously creates interfaces from user prompts. While capability improving, also presents risk delivering generic experiences. Without designer input, AI-generated UX defaults to generic training data average. Every product starts looking same. No differentiation. AI reinforces mediocrity via training data from common design platforms optimized for visual appeal.

### Case for Design System Integration

Need alternate approach: AI assistants have knowledge of product's unique design system—components, patterns, guidelines. When user prompts, instead of text blocks/paragraphs, assistant renders rich interfaces from product's design system. Chat transforms from static text box into dynamic viewport with rich interactive elements. Latest MCP protocol developments making this possible.

### Three Modes for Richer AI Experiences

To create richer, differentiated experiences, three design modes help move beyond text-trap.

**Mode 1: Rich Output**
In complex business apps, users consume data, not answers. Large text blocks create cognitive load. Move beyond text toward richer UI output. Example: user prompts "Merge two John Smith records flagged yesterday." AI doesn't ask "Which should be primary?" Instead displays two contact cards side-by-side with metadata, enabling user decision-making through UI. Maximizes scannability; lets user grasp situation instantly and prioritize follow-up.

**Mode 2: UI as Input**
Differentiated experience starts at input point, not just output. Rather than forcing users to craft precise text prompts knowing exact parameters, AI assistant replaces text box with structured input. Example: retrieving record, instead of typing "Show me California leads with high activity" and re-prompting for parameter changes, AI displays query builder.

Shift from text to high-fidelity input removes ambiguity, reduces back-and-forth, makes interaction faster and more precise.

**Mode 3: Co-Creation**
Modes 1-2 represent single interactions. Real-world scenarios rarely simple. In SaaS, high-value tasks are multi-step workflows (creating marketing automation campaign, building complex report, configuring integration). Not one-prompt accomplishments; they unfold over conversation where user and AI refine work together.

Support this by making AI assistant more than responder—it needs to become workspace.

Four capabilities transform back-and-forth conversation into co-creation:

**Fluid Modality Switching**: When user updates block, shouldn't force back to text prompt. AI should allow users moving fluidly between text and direct manipulation. Rather than "change wait time to 5 days," user adjusts component directly; AI validates and updates dependents automatically.

**Proactive Cross-Tool Suggestions**: Complex workflows often span multiple tools. Rather than forcing new conversation or tab opening, AI brings connected tool data directly into workflow. Can surface insights proactively. Example: once flow created, AI notices most unactivated users mobile while email templates desktop-focused. Without prompting, pulls usage analytics data and surfaces insight: "68% unactivated users on mobile, but templates not mobile-optimized."

**Delegation of Discrete Subtasks**: At workflow points, user may hand off contained piece entirely. Based on mobile optimization insight, user prompts AI to update template. AI takes content work while user refines campaign structure. When ready, AI surfaces updated template for review. **Co-creation as division of labor.**

**Contextually Refine with Text**: Text-based input doesn't live in prompt box—it can be contextual to UI elements. User hovers over connector, prompts "Send survey asking biggest challenge, route to different content tracks based on answer." AI inserts survey block, creates conditional branches, shows multi-path workflow.

Because prompt anchored to component not generic prompt box, AI understands position in workflow, not just what user saying.

## Related

[[genai-ux-patterns]]
[[ai-ux-patterns-2026]]
[[beyond-chat-user-intents]]
