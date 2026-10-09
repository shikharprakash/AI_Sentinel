"""Word content: Sections 6-8."""

S6 = [
    ("note", "Note: concept-test results are ILLUSTRATIVE placeholders. Replace them with the outcomes of "
             "real sessions with 3 of the 5 interviewees before submission."),
    ("h", "6.1 Low-fidelity prototype"),
    ("p", "We built three clickable low-fi screens (sketch-style wireframes, Figma/Balsamiq equivalent) "
          "covering the three pillars. Participants completed realistic tasks on each screen."),
    ("img", "wf_protect.png", 5.0, "Screen 1 - Protect: inline detection with one-click 'Redact & send'"),
    ("img", "wf_optimize.png", 5.0, "Screen 2 - Optimize: Prompt Copilot with before/after, accept / reject / revert"),
    ("img", "wf_admin.png", 5.0, "Screen 3 - Govern: admin console with group policies, monitor/enforce modes and events"),
    ("h", "6.2 Method: qualitative 1-on-1 sessions + a short quantitative survey"),
    ("p", "**Participants:** Ananya (individual developer), Vikram (CISO) and Meera (HR knowledge worker), "
          "one per persona. Each 45-minute moderated session used a think-aloud protocol: (1) paste a "
          "prompt containing a PAN number and an API key; (2) improve a vague prompt with Prompt Copilot; "
          "(3) Vikram only: create an HR policy in the admin console. Each session ended with a "
          "10-question survey."),
    ("h2", "Survey questions (Likert 1-5 unless noted)"),
    ("n", [
        "The warning clearly explained what was wrong and why.",
        "I would trust 'Redact & send' to remove the sensitive data correctly.",
        "The suggested prompt is better than what I wrote.",
        "The tool interrupted my flow (reverse-scored).",
        "I understood that basic checks run on my device.",
        "How likely are you to keep this installed after a week? (1-5)",
        "How would you feel if you could no longer use it? (very / somewhat / not disappointed)",
        "At what monthly price would this be too cheap to trust / a bargain / getting expensive / too "
        "expensive? (Van Westendorp)",
        "Which ONE feature would you remove?",
        "What is missing for you (or your company) to adopt this?",
    ]),
    ("h", "6.3 Results"),
    ("t", ["Measure", "Ananya", "Vikram", "Meera", "Avg / result"], [
        ["Task 1 completed unaided (redact)", "Yes", "Yes", "Yes, after 1 hesitation", "3/3"],
        ["Task 2 accepted suggestion", "Yes (wanted 'concise')", "Partly", "Yes", "2.5/3"],
        ["Q1 warning clarity", "5", "4", "5", "4.7"],
        ["Q2 trust in redaction", "4", "4", "4", "4.0"],
        ["Q3 suggested prompt better", "5", "3", "5", "4.3"],
        ["Q4 interrupted my flow (lower = better)", "3", "2", "2", "2.3"],
        ["Q5 understood local checks", "4", "5", "2", "3.7"],
        ["Q7 'very disappointed' without it", "Yes", "Yes", "No (somewhat)", "67%"],
        ["Q8 acceptable price", "Rs 249-499/mo", "US$5-8/user/mo", "Employer should pay", "Rs 399; US$6-8"],
    ], [2.2, 1.0, 1.0, 1.1, 0.9], 8.5),
    ("h", "6.4 Key learnings and how we will use them"),
    ("t", ["Learning", "Evidence", "Change to the product"], [
        ["Fix, don't just block", "Meera hesitated at 'Send anyway'; all three preferred 'Redact & send'",
         "Make 'Redact & send' the default primary action; 'Send anyway' requires a reason and is logged"],
        ["The optimiser must be on demand", "Ananya disliked auto pop-ups; wanted a 'concise' mode",
         "Copilot appears as a button / shortcut only; add Concise, Structured and Detailed modes; no "
         "auto-suggest"],
        ["Monitor before enforce", "Vikram will not block on day one without data",
         "Monitor mode is the default pilot mode; one-click policy promotion to Enforce"],
        ["Evidence for auditors", "Vikram asked for exportable, metadata-only events",
         "Event export (CSV / Splunk) in the MVP; prompt content excluded by default"],
        ["Explain privacy visually", "Meera did not notice the on-device message (3.7)",
         "Persistent 'Checked on device' badge with a hover explanation"],
        ["Token savings are not the hook", "Nobody mentioned token savings unprompted",
         "Lead with quality and safety; move the savings dashboard to P1"],
    ], [1.4, 2.2, 2.6], 8.5),
    ("p", "**Conclusion:** the concept is validated well enough to justify an MVP. All three completed the "
          "core task, two of three would be 'very disappointed' without it (above the 40% PMF bar, though "
          "with a tiny sample), and price ranges match our hypotheses. Friction and privacy communication "
          "are the main design risks to carry into the MVP."),
]

S7 = [
    ("h", "7.1 MVP or a fully developed product? Build an MVP"),
    ("b", [
        "**Development risk is moderate to high:** site adapters break when AI tools change their UI, "
        "detection accuracy needs real-world tuning, and latency budgets are tight.",
        "**PMF is promising but unproven:** n = 3 concept tests; enterprise willingness to pay must be "
        "validated with real money (paid pilots).",
        "**Opportunity cost:** a full platform would take about 12 months and 3 squads. An MVP takes 12 "
        "weeks and 1 squad, preserving capacity while the market window is still open.",
    ]),
    ("h", "7.2 What the MVP looks like"),
    ("t", ["P0 capability", "MVP scope"], [
        ["App adapters", "ChatGPT and Gemini web on Chrome and Edge; protection-status badge; degraded "
                         "state disclosed"],
        ["Protect", "Local pattern checks for secrets, PAN, Aadhaar, email, phone, card numbers; "
                    "'Redact & send'; warn/block"],
        ["Govern", "Duo / Entra ID SSO; groups; allow/warn/block per app; monitor and enforce modes; "
                   "signed policy bundles with offline expiry"],
        ["Optimize", "On-demand Prompt Copilot (3 modes), before/after diff, accept/reject/revert, token "
                     "estimate"],
        ["Console", "Policy editor, user/group view, metadata-only event log with export"],
        ["Metering", "Idempotent usage events, quotas, Personal Free/Plus entitlements"],
        ["Out of scope", "Native desktop apps, API traffic, all AI sites, autonomous routing, compliance "
                         "certification"],
    ], [1.3, 4.9], 8.5),
    ("h2", "Early-stage success factors (MVP exit criteria)"),
    ("t", ["Factor", "Target at pilot end", "Why it matters"], [
        ["Activation: first safe/optimised prompt in session 1", ">= 60% of installs", "Proves time-to-value"],
        ["p95 added latency (local checks)", "<= 100 ms", "Friction was the #1 uninstall risk"],
        ["Precision, high-confidence detections", ">= 95%", "Keeps false positives and alert fatigue low"],
        ["Recall on critical secrets", ">= 99%", "Core security promise"],
        ["Suggestion acceptance", ">= 40%", "Optimiser value"],
        ["Week-4 retention (individuals)", ">= 35%", "Habit formation"],
        ["Pilot-to-paid conversion (enterprise)", ">= 30% of pilots", "Willingness to pay"],
        ["Unauthorised transmission of test data", "0 cases", "Trust and safety"],
    ], [2.6, 1.4, 2.2], 8.5),
    ("h", "7.3 Product development roadmap"),
    ("t", ["Phase", "Timing", "Key deliverables", "Gate"], [
        ["Discovery & feasibility", "Weeks 1-2 (Oct-Nov 2026)", "20-25 interviews, threat model, adapter "
                                                                "spike, pricing tests", "Segment + buyer "
                                                                                        "confirmed"],
        ["Working prototype", "Weeks 3-6", "Extension for 2 apps, local checks, preview UX, basic policy",
         "Internal dogfood at Cisco IT"],
        ["Alpha & hardening", "Weeks 7-9", "Policy service, RBAC, console, metering, security testing",
         "Red-team findings closed"],
        ["MVP pilot", "Weeks 10-12 (Jan 2027)", "5 design-partner pilots + 500 individual beta users",
         "Launch / no-launch"],
        ["Commercial launch", "Months 4-6 (Feb-Apr 2027)", "Cisco Live EMEA preview; Business tier GA; "
                                                           "+2 AI apps", "Targets in Section 10"],
        ["Scale", "Months 7-12", "Secure Access and Splunk integration, AI Defense classifiers, Firefox/"
                                 "Safari, agentic-browser guardrails", "PMF in two segments"],
    ], [1.3, 1.3, 2.4, 1.2], 8.5),
    ("h", "7.4 How we will achieve product-market fit"),
    ("b", [
        "**Pick the beachhead:** mid-market Duo/Meraki customers in India and the US, plus developers as "
        "the individual beachhead. Do not try to serve everyone.",
        "**Measure PMF with leading and lagging signals:** Sean Ellis test (40% or more 'very "
        "disappointed'), flattening retention curves by cohort, organic installs within pilot companies, "
        "and pilot-to-paid conversion.",
        "**Weekly learning loop:** review false positives, overrides and abandonment every week; ship "
        "adapter and detection fixes within the sprint.",
        "**Design partners as co-builders:** 5 partners with a shared Slack/Webex space, monthly roadmap "
        "reviews and a discount in exchange for references.",
        "**Iterate positioning and packaging per segment** until each shows strong retention on its own.",
    ]),
    ("h", "7.5 Growth experiments (AARRR)"),
    ("t", ["Stage", "Experiment", "Hypothesis / success metric"], [
        ["Acquisition", "Chrome Web Store listing A/B: 'Stop AI data leaks' vs. 'Better, safer prompts'",
         "Productivity framing lifts install rate by 20%+"],
        ["Acquisition", "Free 'Shadow AI Risk Check' for Meraki/Duo admins (one-week monitor mode)",
         "15% of checks convert into pilots"],
        ["Activation", "Guided first-run with a sample risky prompt vs. blank start",
         "Session-1 activation rises from 45% to 60%"],
        ["Engagement", "Keyboard shortcut + subtle Copilot button vs. side-panel only",
         "Copilot uses per WAU +25%"],
        ["Success", "'Fix it for me' redaction default vs. warn-only",
         "Overrides down 30% with no drop in task completion"],
        ["Retention", "Weekly 'You were protected X times' digest email",
         "Week-4 retention +5 points"],
        ["Referral", "Invite a teammate = +100 advanced operations for both", "K-factor >= 0.2"],
        ["Revenue", "Annual-plan discount 2 months free vs. 1 month", "Annual mix >= 40% without ARPU loss"],
    ], [1.0, 2.9, 2.3], 8.5),
]

S8 = [
    ("h", "8.1 Approach: user-centred, evidence-led, incremental"),
    ("p", "Management wants user-centric development, so we combine **Design Thinking** (deciding *what* to "
          "build and *why*) with **Agile** (delivering it *fast and safely*). In practice this is a "
          "**dual-track** model: a discovery track runs one to two sprints ahead of a delivery track, and "
          "both share one backlog and one set of outcome metrics."),
    ("h", "8.2 Design thinking applied to AI Sentinel"),
    ("t", ["Stage", "Activities for AI Sentinel", "Output"], [
        ["Empathise", "Interviews with CISOs, IT managers, employees and power users; shadowing real AI "
                      "sessions; reviewing support tickets and competitor reviews", "Empathy maps; journey "
                                                                                    "map; pain-point "
                                                                                    "inventory"],
        ["Define", "Synthesise insights into problem statements, e.g. 'Meera needs to use AI on HR "
                   "documents without knowing data rules, because warnings confuse and block her'",
         "3 POV statements; 'How might we...' questions; success metrics"],
        ["Ideate", "Cross-functional workshops (PM, design, engineering, security research, sales); "
                   "Crazy 8s; prioritise with impact/effort and the importance ratings",
         "Concept options (inline fix, side panel, admin templates)"],
        ["Prototype", "Lo-fi wireframes, then clickable Figma, then a coded spike on one AI app",
         "Testable prototypes at increasing fidelity"],
        ["Test", "Moderated usability tests, concept surveys, pilot telemetry, A/B tests",
         "Validated or killed hypotheses that feed the backlog"],
    ], [1.0, 3.6, 1.6], 8.5),
    ("h", "8.3 Agile delivery"),
    ("b", [
        "**Team (one squad, about 10 people):** PM (product owner), product designer, 5 engineers "
        "(extension, backend, console), 1 ML engineer, 1 security researcher, 1 QA/automation. Shared "
        "SRE and privacy counsel.",
        "**Cadence:** Scrum with 2-week sprints: planning, daily stand-ups, sprint review with design "
        "partners, retrospective. Kanban lane for adapter breakages (24-hour SLA).",
        "**Backlog:** user stories written from POV statements, with acceptance criteria taken from MVP "
        "targets (e.g. 'as Meera, I can redact and send in one click, p95 under 100 ms').",
        "**Definition of Done** includes passing the detection evaluation set (no precision/recall "
        "regression), privacy review (no prompt content in logs), accessibility, and adapter health "
        "checks.",
        "**Release:** continuous delivery to an internal ring (Cisco IT), then design partners, then "
        "general availability, behind feature flags.",
    ]),
    ("h", "8.4 How the two combine"),
    ("t", ["Sprint", "Discovery track (Design Thinking)", "Delivery track (Agile)"], [
        ["1-2", "Empathise + define with 20-25 interviews", "Architecture spike, CI/CD, threat model"],
        ["3-4", "Ideate + lo-fi test of inline UX", "Extension shell, adapters, local detection"],
        ["5-6", "Hi-fi test of Copilot modes", "Redaction UX, policy service v1"],
        ["7-8", "Admin console usability tests with CISOs", "Console, RBAC, metering"],
        ["9-10", "Pricing tests and pilot onboarding research", "Hardening, red-team fixes, pilot release"],
        ["11-12", "Pilot interviews and synthesis", "Fixes, analytics, launch readiness"],
    ], [0.6, 2.8, 2.8], 8.5),
    ("p", "Continuous feedback tools (in-product feedback widget, session heat-maps on the console, "
          "Hotjar-style surveys) close the loop between the tracks. Every sprint review asks two "
          "questions: *did we build it right?* (Agile) and *did we build the right thing?* (Design "
          "Thinking)."),
    ("h", "8.5 Governance and risk controls during development"),
    ("b", [
        "Security-before-optimisation principle enforced in code: optimisation runs only after policy "
        "checks pass.",
        "Least-privilege extension permissions, reviewed by the Cisco PSIRT process before each release.",
        "Monthly steering review with the Security BU GM: metrics, risks and scope changes.",
    ]),
]
