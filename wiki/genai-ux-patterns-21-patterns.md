# GenAI UX Patterns: 21 Design Patterns for Intelligent Products

Generative AI introduces novel challenges requiring understanding of probabilistic outputs, variability, errors, hallucinations, malicious use necessitating essential design principles and patterns as described by IBM research. AI products are layered systems where LLM is one ingredient and memory, orchestration, tool extensions, UX, agentic flows build real magic. Twenty-one GenAI UX patterns provide shared language for product managers, data scientists, interaction designers creating human-centered, trustworthy, safe products. Pattern 1: GenAI or no GenAI evaluating whether GenAI improves UX or introduces complexity; beneficial for open-ended creative tasks, complex output transformation, unstructured intent capture; avoid for precise auditable outcomes or clear information expectations. Pattern 2: convert user needs to data needs ensuring development begins with user intent and data model required achieving that; triangulate research with qualitative, quantitative, emergent methods. Pattern 3: augment vs automate deciding whether fully automating task or augmenting human capability; automation best for tedious time-consuming unsafe tasks, augmentation enhances tasks users remain involved in. Pattern 4: define automation level—no automation (AI assists user decides), partial (AI acts with oversight), full automation (AI acts independently). Pattern 5: progressive GenAI adoption helping user onboard mitigating errors aligning readiness. Pattern 6: leverage mental models building upon existing mental models easing adoption. Pattern 7: convey product limits clearly communicating what AI can cannot do building trust setting expectations. Pattern 8: display chain of thought (CoT) revealing how AI arrived at conclusions fostering trust and interpretability. Pattern 9-21: multiple outputs, data sources, model confidence, memory recall, contextual input parameters, coPilot co-editing, user controls, input error states, system error states, capture feedback, model evaluation, safety guardrails, data privacy controls.

## Key Patterns & Concepts

- **GenAI Decision**: Beneficial for open-ended creative complex transformation unstructured; avoid precise auditable deterministic
- **User to Data Needs**: Triangulate qualitative quantitative emergent research synthesize insights define data model
- **Augment vs Automate**: Automation tedious time-consuming; augmentation enhances user involvement
- **Automation Levels**: No (assist), Partial (co-pilot), Full (independent agentic systems)
- **Progressive Adoption**: Communicate benefits early simplify onboarding define automation level gradually increase autonomy
- **Mental Models**: Build upon existing mental models easing adoption preventing friction
- **Communicate Limits**: Explicit statements about outdated knowledge real-time gaps fallback escalation visible limitations
- **Chain of Thought**: Display step-by-step processing revealing reasoning improving transparency trust
- **Multiple Outputs**: Show diverse options ranked by confidence enabling user choice
- **Data Sources**: Provide references enabling verification building trust
- **Model Confidence**: Display confidence levels percentages visualizations breaking down per component
- **Memory and Recall**: Design for persistent context across sessions surface what AI remembers allow editing
- **Contextual Input Parameters**: Sliders controls specifying context reduce burden on user each prompt
- **Co-Pilot Co-Editing**: User reviews intervenes on AI-initiated actions maintaining oversight
- **User Controls**: Define how much AI can act independently based pain point and risk
- **Input Error States**: Gracefully handle user misinterpretation unclear prompts guide correction
- **System Error States**: Design graceful failure acknowledging limitations offering retry escalation paths
- **Capture Feedback**: Enable thumbs up/down corrections helping model learn and improve
- **Model Evaluation**: Measure impact assess quality continuous improvement
- **Safety Guardrails**: Prevent misuse define boundaries protect users
- **Data Privacy**: Transparent communication data collection storage processing protection

## Related

[[trustworthy-ai-design-patterns]]
[[ai-behaviour-ux-patterns]]
[[genai-ux-patterns]]
