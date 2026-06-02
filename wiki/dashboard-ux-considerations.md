# 6 Important UX Considerations in Dashboard Design

Effective dashboard design requires considering personas, data viability, limitations, hierarchies, metric grouping, and contextual elements. Rather than designing for each persona, design for user roles. Before building dashboards, validate that user research data meets three criteria: authentic source type, data veracity, and mission relevance. Acknowledge business and technological constraints upfront; create feasible experiences with available data while planning future enhancements.

## Key Patterns & Concepts

- **Roles Over Personas**: Design one dashboard per role, not per persona; different roles have different dashboard needs despite similar backgrounds
- **Data Viability**: Validate research data—check source authenticity (primary vs secondary), sample size, bias, and relevance to dashboard mission
- **Acknowledge Limitations**: Understand business and technological constraints; design for current capabilities while roadmapping future features
- **Visual Hierarchies**: Rank metric importance by role; head supervisor sees monthly absenteeism rates, junior supervisor sees individual absentees
- **Metric Grouping**: Associate related metrics; allow filtering across groups for seamless exploration (e.g., monthly revenue grouped with monthly expenditure)
- **Contextual Reference**: Support each metric with reference elements showing change or comparison; $10k sales is meaningless without growth context (+50% vs yesterday)
- **Role-Based Metric Priority**: Different roles prioritize differently—warehouse head supervisor prioritizes inventory turnover; junior supervisor prioritizes days-in-hand

## Full Article

As data becomes the new fuel, almost every business is significantly dependent on dashboards. They appear across industries providing real-time data representation in summarized format for easier comprehension. Logistics companies show delivery/inventory metrics; loan providers show customer data for approval decisions.

Since dashboards are used commonly across every industry, creating designs that lead to seamless viewable experiences is imperative.

### Consideration 1: Categorize Personas into Roles

Target persona is based on market research and demographics identifying target audience. Unlike other applications, dashboards don't cater to each persona but to each role.

Filter target audience into personas, create comprehensive persona list, then categorize each into roles. Create one dashboard per role, not per persona. This enables accurate user experience for target audience.

### Consideration 2: Check Data Viability

First phase of creating dashboard is gathering abundance of user data. Collected data must meet three criteria:

1. **Type and Authenticity of Source**: Is source primary or secondary? Primary sources (audience interviews, autobiographies) carry higher weight than secondary (magazine articles).

2. **Veracity of Data**: What's the sample size? Is information biased? Example: including recently-migrated audiences when collecting city navigation data biases results.

3. **Dashboard Mission and Audience**: Is mission to maintain daily schedule for doctors? If yes, do you need prescription history in analysis? Filter relevant data; discard distracting data.

### Consideration 3: Acknowledge Limitations

Dashboards created after understanding limitations—both business and technological. Create most feasible user experience after acknowledging current challenges. Understand product thoroughly; note all problems it can't currently address.

Create design that effectively portrays available data while acknowledging additional features desired in near future.

### Consideration 4: Create Hierarchies

Once data filtered and dashboard roles identified, understand metric importance for each role based on market research. Create visual hierarchies.

Example: Managing warehouse of 1000 people, head supervisor wants absenteeism rates across months; junior supervisor wants individual absentees. For head supervisor, inventory turnover is critical; for junior supervisor, days-in-hand is important.

### Consideration 5: Group Relevant Metrics

Understand importance of each metric. Create group of associated metrics. Grouping enables audience to find relevant metrics easily and makes dashboard logically consistent.

Example: Finance dashboard should group monthly revenue with monthly expenditure. Add filters for these groups to enable seamless dashboard exploration.

### Consideration 6: Give Context to Each Element

How would sales manager know if $10k daily sales is good performance? If shown $10k sales increased 50% versus yesterday, it's clear indicator of great performance.

Each metric supported by contextual elements providing reference to change. Another example: show total sales bar graph across days/months to provide comparison context.

## Related

[[dashboard-design-questions]]
[[dashboard-user-research-questions]]
[[dashboard-design-principles-uxplanet]]
