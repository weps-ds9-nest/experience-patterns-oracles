# 20+ GenAI UX Patterns: Examples and Implementation Tactics

GenAI introduces intent-based outcome specification through natural interaction with systems, introducing novel challenges: probabilistic outputs, variability understanding, memory, errors, hallucinations, malicious use. AI products are layered systems where LLM is one ingredient; memory, orchestration, tool extensions, UX and agentic flows build real magic. Twenty-one GenAI UX patterns provide shared language for product managers, data scientists, interaction designers: GenAI or no GenAI, convert user needs to data needs, augment or automate, define automation level, progressive AI adoption, leverage mental models, convey product limits, display chain of thought (CoT), leverage multiple outputs, provide data sources, convey model confidence, design for memory and recall, provide contextual input parameters, design for co-pilot co-editing or partial automation, define user controls for automation, design for user input error states, design for AI system error states, design to capture user feedback, design for model evaluation, design for AI safety guardrails, communicate data privacy and controls.

## Key Patterns & Concepts

- **GenAI Decision**: Evaluate if GenAI improves UX or introduces complexity; heuristic-based solutions sometimes easier
- **When GenAI Beneficial**: Open-ended creative tasks, transforming complex outputs, capturing unstructured user intent
- **When GenAI Avoided**: Precise auditable deterministic outcomes, clear consistent information expectations
- **User Needs to Data**: Translate user needs into structured model-ready inputs via triangulated research and JTBD framework
- **Augment vs Automate**: Augmentation enhances tasks users want involved in; automation delegates tedious time-consuming unsafe tasks
- **Automation Levels**: No automation (AI assists), partial automation (co-pilot), full automation (agentic systems)
- **Risk Assessment**: Low-risk automation beneficial; high-risk tasks require oversight; define user controls for automation
- **Progressive Adoption**: Multi-dimensional strategy helping user onboarding; simplify experience; gradually increase autonomy; design for errors
- **Mental Models**: Build upon existing user mental models; align with developer expectations; explain when breaking patterns
- **Product Limits**: Explicitly state model limitations, knowledge boundaries, capabilities; provide fallbacks/escalation; make visible
- **Chain of Thought**: Display processing steps improving transparency and trust; show status like "researching"; use progressive disclosure
- **Multiple Outputs**: Leverage various outputs supporting different user needs and decision-making
- **Data Sources**: Provide transparency on information used; footnotes and references build trust; enable reproducibility
- **Model Confidence**: Indicate confidence levels; show percentages or visualizations; vary by result parts
- **Memory and Recall**: Design persistent context preservation across sessions; make memory visible/manageable
- **Contextual Input**: Provide input parameters helping users specify needs; sliders, dropdowns, field controls reduce prompt burden
- **Co-Creation**: Design for co-pilot, co-editing, partial automation enabling user involvement and control
- **Automation Control**: User controls for when/how automation initiates; threshold-based triggers; permission requests
- **Input Error States**: Design for user-provided data issues; clear messaging helping users correct
- **System Error States**: Design for AI failures gracefully; acknowledge limitations; offer retry/refine/escalate paths
- **User Feedback**: Capture feedback enabling system improvement; thumbs up/down, detailed comments, usage data
- **Model Evaluation**: Design mechanisms for ongoing model performance assessment and improvement
- **Safety Guardrails**: Implement safeguards preventing misuse and harmful outputs; moderation and filtering
- **Privacy Communication**: Clearly convey data collection, storage, processing, protection; user controls and agency

## Related

[[ai-ux-patterns]]
[[genai-ux-implementation]]
[[beyond-chat-user-intents]]
