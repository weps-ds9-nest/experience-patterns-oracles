# 26 Steps of Product Dashboard Design: From Pre-Process to Testing

Dashboard design requires structured methodology spanning five phases: pre-process research and planning, low-fidelity exploration, design and iteration, asset delivery and specifications, and post-launch testing. This 26-step framework, developed over four years of enterprise dashboard design, ensures decisions are validated against real user needs and product goals.

## Key Patterns & Concepts

- **Pre-Process Research**: Collect inspiration; learn user personas; define exact goals and metrics to track
- **Low-Fidelity Whiteboarding**: Collaborative ideation; map all screens and data flows; document all possible states
- **Data and States Documentation**: List user inputs, stories, and desired goals; prepare state diagrams; define edge cases early
- **Information Architecture**: Use tools like Camunda Modeler for scalable interaction diagrams
- **Moodboarding**: Establish visual tone before pixel-perfect design; communicate thinking to team
- **Iterative Design**: Mix real components; gather early feedback; prototype on Marvelapp/Invision; test with internal users
- **Copy and Tone**: Define voice and language; ensure clarity in dialogs and next-step guidance
- **Consistent Component System**: Build design systems with resizable shapes; enable teams to create hi-fidelity from wireframes
- **Specifications and Documentation**: Write detailed specs in Google Docs or directly in design files; reduce developer difficulty
- **Prototyping and Animation**: Create 3–5 prototypes; document all states in single artboards; use video screenshares explaining designs
- **Style Guide Development**: Document component behaviors—error states, disabled states, spinners; build symbols for developers
- **Post-Launch Testing**: Use Inspectlet/Hotjar for session recording and heatmaps; implement Mixpanel for funnel and goal tracking
- **Click Tracking**: Set up Google Analytics click tracking to understand user behavior patterns
- **Continuous Feedback**: Monitor engagement; gather user feedback; iterate on layouts, fonts, KPI positioning

## Full Article

I have learned over four years designing dashboards and applications, dealing with different departments, and utilizing their knowledge to make designs better and more efficient. These 26 steps have become my daily routine.

### Phase 1: Pre-Process

**Get Information**: Ask clients for three inspirational examples. Real working examples provide clarity for both parties and help understand expectations. Spend equal time with developers and designers—developers often have solutions to design problems.

**Learn About Personas**: Create 4–5 personas based on actual users. This helps identify issues and understand who you're really designing for, especially when solutions have many edge cases.

**Setup Exact Goals**: Define what you want to track—new sign-ups, payment methods, feature usage. You'll need these for setting up funnels in Mixpanel later.

**Set Up Project Structure**: Create folders for Source Files, Screens & Export, Inspiration & Resources. Save everything you find online to use later for moodboards.

### Phase 2: Going Low Fidelity

**Whiteboard Collaboratively**: Sit down with team and sketch ideas on whiteboard, paper, or iPad. Everyone becomes a designer. Compare 2+ options; discuss edge cases now rather than during development.

**Map Out Screens**: List user inputs, stories, and desired goals for each screen. Document what data users need to input and how they achieve goals.

**Write Down All Possible States**: Address empty states, loading states, error states, and success states. Most users see the "unshiny" side—be prepared. Design for opposite of perfect conditions.

**Prepare Interaction Diagram**: Summarize outcomes into scalable diagrams using tools like Camunda Modeler. Helps avoid repetitive rework when changes arise mid-project.

### Phase 3: Work & Design

**Create Moodboard**: Gather images from inspiration folder to discuss visual thinking before pixel work.

**First Draft**: Mix real components to gather early feedback from teammates, clients, or potential users. Don't wait for pixel perfection.

**Write Copy and Tone**: Establish voice clarity in dialogs. Nothing worse than nice design with confusing instructions.

**First Internal Test**: Create prototype in Marvelapp/Invision with non-involved team members. Test particular flows and questioning skills. Avoid testers who've already seen the prototype.

**Maintain File Organization**: Keep Sketch/PSD files tidy. If folder has 8+ layers, create new subfolder. Design like creating for someone else.

**Put Content in Canvas First**: Lay out content before polishing details. Easier to design nice headers with content in place than with white canvas.

**Use Component Systems**: Build resizable design system elements. Enable any team member to create hi-fidelity drafts via drag-and-drop.

### Phase 4: Assets & Delivery

**Create Specifications**: Document interactions and features. Write specs in Google Docs or below screens in Sketch. Explain all features for future reference.

**Prepare Final Prototype**: Have 3–5 prototypes ready. Prepare all states in single Sketch artboard; duplicate artboards for each state.

**Record Video Walkthroughs**: Create screenshare video walking through prototype, explaining everything designed. Works well for remote teams. Everyone can replay interaction thinking anytime.

**Add Microinteractions**: Use After Effects or Principle to explain motion and hover states.

**Build Style Guide**: Document component behaviors—error states of inputs, disabled buttons, spinners. Create symbols artboard for developers to reference component library.

### Phase 5: Final & Test

**Implement Session Recording**: Use Inspectlet/Hotjar to capture user sessions. Watch how users navigate and interact. Inspectlet great for larger projects with page filtering.

**Set Up Mixpanel**: Validate goals defined at project start. Track funnel completion, drop-off points, flow metrics. Understand user behavior patterns.

**Set Up Click Tracking**: Implement Google Analytics click tracking to see where users click. Attach different labels to each anchor point. Map user behavior patterns and identify misuse.

**Monitor Post-Launch**: Watch engagement data; gather feedback regularly; iterate on layouts, fonts, and KPI card positioning based on real usage patterns.

## Related

[[dashboard-design-principles-uxplanet]]
[[dashboard-design-questions]]
