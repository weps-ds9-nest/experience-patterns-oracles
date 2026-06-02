# 21 GenAI UX Patterns: A Shared Language for Building Usable, Intelligent, Safe AI

Generative AI introduces intent-based outcome specification and novel challenges: probabilistic outputs, variability, hallucinations, memory, and safety concerns. These 21 design patterns provide a shared language for product managers, data scientists, and designers to create human-centered, trustworthy, and safe GenAI experiences.

## Key Patterns & Concepts

- **GenAI or No GenAI**: Evaluate whether GenAI improves UX or adds complexity; heuristic solutions sometimes better
- **Convert User Needs to Data Needs**: Translate goals into structured, model-ready inputs; use triangulated research and frameworks (JTBD, empathy maps)
- **Augment vs Automate**: Full automation for tedious tasks; augmentation for tasks users want to remain involved in
- **Define Level of Automation**: No automation (AI assists), partial (co-pilot), or full (agentic)—based on risk and user expectations
- **Progressive GenAI Adoption**: Onboard gradually; communicate benefits first; simplify early access; define automation levels; explain errors
- **Leverage Mental Models**: Build on existing user expectations; Adobe Photoshop's generative fill extends familiar rectangular controls
- **Convey Product Limits**: State model limitations, knowledge cutoffs, capabilities explicitly; provide fallback options
- **Display Chain of Thought (CoT)**: Show step-by-step reasoning; communicate progress ("researching," "reasoning"); allow expansion of details
- **Leverage Multiple Outputs**: Generate alternatives; let users compare and select best options
- **Provide Data Sources**: Show which sources informed the response; enable verification and fact-checking
- **Convey Model Confidence**: Indicate certainty levels; highlight low-confidence outputs for user scrutiny
- **Design for Memory and Recall**: Manage conversation context; clarify what system remembers; support multi-turn interactions
- **Provide Contextual Input Parameters**: Offer suggested filters or constraints upfront to improve output relevance
- **Co-Pilot, Co-Editor, or Partial Automation**: Let users review, modify, or override AI suggestions; maintain human agency
- **Define User Controls for Automation**: Give users ability to pause, override, or adjust automation levels mid-session
- **Design for User Input Error States**: Guide users toward better prompts; show examples; validate intent before execution
- **Design for AI System Error States**: Handle hallucinations, failures gracefully; offer rollback or retry; apologize when appropriate
- **Design to Capture User Feedback**: Thumbs up/down, corrections, annotations; use feedback for model evaluation and improvement
- **Design for Model Evaluation**: A/B test outputs; measure user satisfaction; track error rates; iterate on prompts and training
- **Design for AI Safety Guardrails**: Implement content filtering, PII detection, rate limiting; prevent misuse without crippling usability
- **Communicate Data Privacy and Controls**: Explain data collection, storage, processing, protection clearly; give users control

## Full Article

Generative AI introduces a new way for humans to interact with systems through intent-based outcome specification. GenAI brings essential challenges requiring principles and design patterns because outputs are probabilistic, requiring understanding of variability, memory, errors, hallucinations, and malicious use.

AI products are layered systems where LLM is just one ingredient—memory, orchestration, tool extensions, UX, and agentic user-flows build the real magic.

### Pattern 1: GenAI or No GenAI

Evaluate whether GenAI improves UX or introduces unnecessary complexity. Often, heuristic-based (IF/Else) solutions are easier to build and maintain.

GenAI is beneficial for: open-ended and creative tasks augmenting users (writing, summarizing, drafting); creating or transforming complex outputs (images, video, code); where structured UX fails to capture intent.

GenAI should be avoided for: outcomes requiring precision, auditability, or determinism (tax forms, legal contracts); where users expect clear and consistent information (open-source documentation).

To use this pattern: (1) Determine friction points in customer journey. (2) Assess technology feasibility—can AI address friction? Evaluate scale, dataset availability, error risk, ROI. (3) Validate user expectations—does AI solution erode expectations by replacing vs augmenting? Does it erode mental models?

### [Additional 20 Patterns continue with implementation strategies, examples, and cross-pattern relationships...]

## Related

[[ai-driven-ux-patterns-by-2026]]
