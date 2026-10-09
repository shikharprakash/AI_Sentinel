"""Word content: Sections 4-5."""
import sdata as N

_rt = N.rating_table()
_rating_rows = [[str(d["rank"]), d["feature"]] + [str(x) for x in d["scores"]] + [f"{d['mean']:.1f}"]
                for d in _rt]

S4 = [
    ("note", "Note: the interview responses and ratings below are ILLUSTRATIVE placeholders built from the "
             "personas. They must be replaced with the student's real conversations before submission."),
    ("h", "4.1 Customer personas"),
    ("t", ["", "Persona A: Ananya, the AI power user", "Persona B: Vikram, the security leader",
           "Persona C: Meera, the everyday knowledge worker"], [
        ["Demographics", "27, software developer at a Bengaluru SaaS start-up; B.Tech; earns Rs 18-25 LPA; "
                         "uses ChatGPT, Claude and Copilot daily",
         "44, CISO at a 1,200-employee IT-services firm in Pune; 20 years in security; reports to the CIO; "
         "owns a US$2M security budget",
         "33, HR business partner at a 600-employee fintech in Mumbai; MBA (HR); non-technical; uses AI "
         "for JDs, policies and summaries"],
        ["Psychographics", "Early adopter, efficiency-obsessed, privacy-aware, dislikes 'corporate' tools "
                           "that slow her down",
         "Risk-averse but pragmatic; does not want to be the 'department of no'; values evidence and audit "
         "trails",
         "Conscientious, time-poor, anxious about doing something wrong with employee data"],
        ["Goals", "Ship code faster; get precise answers first time; stay within her token limits",
         "Enable safe AI adoption; pass audits (ISO 27001, DPDP Act); prove ROI of controls",
         "Finish routine writing faster; look competent with AI; never leak employee PII"],
        ["Pain points", "Vague prompts give vague answers; repeats context; once pasted an API key into a "
                        "chat", "No visibility into which AI tools are used; blanket bans backfire; existing "
                                 "DLP is noisy and blind to chat boxes", "Does not know what counts as "
                                                                          "'sensitive'; warnings she has seen "
                                                                          "are cryptic and block her work"],
        ["Buying role", "User and buyer (Rs 299-599/month)", "Economic buyer & decision-maker",
         "End user and influencer"],
    ], [1.0, 1.75, 1.75, 1.7], 8.5),
    ("h", "4.2 Customer journey map (enterprise, with the individual path noted)"),
    ("t", ["Stage", "Touchpoints", "Customer thinking / feeling", "Our action / metric"], [
        ["1. Unaware", "News of AI data leaks, peer CISOs, LinkedIn, Talos blogs",
         "\"Are my people pasting data into ChatGPT?\" (worried)", "Thought leadership; free 'Shadow AI "
                                                                  "Risk Check'"],
        ["2. Aware", "Cisco account team, partner webinar, Chrome Web Store (individuals)",
         "\"Cisco has something for this?\" (curious)", "Reach and click-through to landing page"],
        ["3. Consider", "Demo, comparison sheet, free individual tier, peer reviews",
         "\"Will it slow people down? False positives?\" (sceptical)", "Interactive demo; latency and "
                                                                       "precision proof"],
        ["4. Trial / pilot", "4-week paid pilot in monitor mode, then enforce",
         "\"Show me data from my own environment\" (testing)", "Pilot report: exposures prevented, "
                                                               "overrides, latency"],
        ["5. Purchase", "Partner quote, EA add-on, Cisco marketplace; in-app upgrade (individual)",
         "\"Is the price justified vs. a breach?\" (rational)", "ROI calculator; pilot credit"],
        ["6. Onboard & use", "Managed deployment via MDM/Duo, admin console, inline tips",
         "\"It actually helps people\" (relieved)", "Weekly active users, suggestion acceptance"],
        ["7. Advocate", "Case study, Cisco Live session, referral credits",
         "\"I'd recommend this to peers\" (proud)", "NPS, references, expansion revenue"],
    ], [0.95, 1.85, 1.75, 1.65], 8.5),
    ("h", "4.3 Primary research: conversations with 5 potential customers"),
    ("p", "Each participant took part in a 30-minute semi-structured conversation covering current AI usage, "
          "past near-misses with sensitive data, tolerance for security friction, trust in an optimiser, "
          "and who would pay. They then completed an **importance rating scale** (1 = not important, "
          "5 = critical) across ten candidate features."),
    ("t", ["#", "Participant", "Profile", "Key quote (illustrative)"], [
        ["1", "Ananya", "Developer, SaaS start-up, Bengaluru (Persona A)",
         "\"If it adds even a second to every prompt, I'll uninstall it.\""],
        ["2", "Vikram", "CISO, IT services, 1,200 staff (Persona B)",
         "\"I need monitor mode first, then evidence I can show the auditors.\""],
        ["3", "Meera", "HR business partner, fintech (Persona C)",
         "\"Just tell me what is wrong and fix it for me. Don't just block me.\""],
        ["4", "Rahul", "IT & security manager, 350-staff manufacturer, Meraki customer",
         "\"We can't afford an SSE rollout. A browser extension I can push via MDM is perfect.\""],
        ["5", "Priya", "MBA student and freelance content consultant",
         "\"Better prompts matter more to me than security, but I don't want my clients' data leaking.\""],
    ], [0.3, 0.8, 2.1, 3.0], 8.5),
    ("h2", "Importance rating results (1-5)"),
    ("t", ["Rank", "Feature", "Ananya", "Vikram", "Meera", "Rahul", "Priya", "Mean"], _rating_rows,
     [0.45, 2.35, 0.55, 0.55, 0.55, 0.55, 0.55, 0.55], 8.5, False),
    ("img", "importance.png", 5.6, "Figure 4.1 - Mean importance with enterprise vs. individual splits"),
    ("h2", "Findings"),
    ("b", [
        "**Data redaction (4.6) and low friction (4.6) tie for first place.** Protection is the reason to "
        "buy, and friction is the reason to uninstall. Latency and false positives are product-critical.",
        "**Local-first checks (4.4)** matter to every segment. 'Your data never leaves your device for "
        "basic checks' is a key message.",
        "**There is a sharp segment split.** RBAC (5.0) and audit/reports (5.0) are must-haves for "
        "enterprise buyers but near-irrelevant for individuals (1.5 and 1.0). The prompt optimiser shows "
        "the reverse pattern (5.0 vs. 3.0). This confirms a shared core with separate packaging.",
        "**The savings dashboard (3.4) is a 'nice to have'.** We move it to P1 and lead with quality, "
        "not token savings.",
        "**Multi-tool coverage (4.2)** matters because people use 2-3 AI tools. The MVP must cover at "
        "least the two most-used tools.",
    ]),
]

S5 = [
    ("h", "5.1 Product definition"),
    ("p", "AI Sentinel = a Chromium/Edge browser extension (local detection, inline UX, application "
          "adapters) + a Cisco cloud service (identity and policy, AI Defense-powered advanced validation, "
          "optional prompt optimisation, metering) + an admin console. The MVP supports ChatGPT and Gemini "
          "on the web."),
    ("h", "5.2 Opportunity cost and development risk"),
    ("p", "Investing one squad in AI Sentinel means not investing it elsewhere. We compared three uses of the "
          "same 12-week budget (score 1-5; 5 = most attractive or lowest risk):"),
    ("t", ["Criterion", "A. AI Sentinel (browser layer)", "B. Extend Secure Access AI-DLP only",
           "C. Stand-alone prompt optimiser"], [
        ["Market opportunity / growth", "5", "4", "3"],
        ["Strategic fit with Cisco", "4", "5", "2"],
        ["Differentiation", "5", "2", "2"],
        ["Revenue potential (3 yr)", "4", "3", "2"],
        ["Technical development risk", "3 (DOM brittleness, accuracy)", "4", "4"],
        ["Market / adoption risk", "3 (crowded, new motion)", "4", "2 (commoditised)"],
        ["Weighted total (opportunity avg x 60% + risk avg x 40%)", "**3.9**", "3.7", "2.6"],
    ], [1.8, 1.6, 1.5, 1.3], 8.5),
    ("p", "**Result:** option A scores highest (3.9). B is a close, safer second (3.7) and remains part of the plan, since AI Sentinel integrates with Secure Access later. The opportunity cost of "
          "*not* building it is also high, because rivals would own the user-facing AI layer in Cisco's own "
          "accounts. On the opportunity-cost / development-risk grid, A sits in **'high opportunity, "
          "moderate risk: build, but de-risk through an MVP'**, not a full-scale build."),
    ("h", "5.3 Product/company fit"),
    ("t", ["Cisco strength that fits", "Gap to close"], [
        ["Duo identity and device trust, so policies know who the user is",
         "No consumer / product-led growth (PLG) experience inside Cisco"],
        ["AI Defense and Robust Intelligence models for advanced validation",
         "Browser-extension UX and site-adapter maintenance skills"],
        ["Talos threat intelligence for injection and malicious patterns",
         "Prompt-optimisation quality evaluation (new ML capability)"],
        ["Splunk for audit events; partner channel; Enterprise Agreements",
         "Speed: a start-up-style squad with autonomy is needed"],
    ], [3.1, 3.1], 8.5, False),
    ("h", "5.4 Product/market fit hypotheses to test in concept testing"),
    ("n", [
        "Users understand inline warnings and prefer 'Redact & send' over being blocked.",
        "Added friction stays acceptable (p95 under 100 ms locally; one click to resolve).",
        "Individuals trust an optimiser from a security vendor and accept 40% or more of suggestions.",
        "Mid-market IT buyers will pay about US$6-8 per user per month without buying a full SSE.",
        "The enterprise buyer accepts a browser extension as a sufficient control for an MVP.",
    ]),
    ("h", "5.5 Marketing mix (4Ps)"),
    ("t", ["P", "Decision"], [
        ["Product", "Extension + console; Govern / Protect / Optimize; tiers: Personal Free, Personal Plus, "
                    "Business, Enterprise"],
        ["Price", "Freemium + per-seat subscription + metered advanced operations (see Section 9)"],
        ["Place", "Chrome Web Store and Edge Add-ons (individuals); Cisco account teams, partners, Cisco and "
                  "cloud marketplaces, EA add-on (enterprise)"],
        ["Promotion", "Talos research on AI leaks, Cisco Live launch, partner enablement, developer "
                      "communities, LinkedIn thought leadership, in-product referral"],
    ], [0.9, 5.3], 8.5),
    ("h", "5.6 Three levels of the product"),
    ("b", [
        "**Core benefit:** confidence to use any AI tool without fear of leaking data, and better results "
        "with less effort.",
        "**Actual product:** the AI Sentinel extension, inline warnings and redaction, Prompt Copilot, "
        "admin console, policy templates, Cisco brand and design, and a clear protection-status badge.",
        "**Augmented product:** Duo and Entra ID single sign-on, Splunk and XDR integration, "
        "Talos-updated detection packs, audit-ready reports (DPDP, GDPR, ISO), Cisco support and Customer "
        "Success, and policy best-practice playbooks.",
    ]),
    ("h", "5.7 Positioning"),
    ("p", "*For security leaders and AI-using employees at organisations that rely on third-party AI tools, "
          "Cisco AI Sentinel is the browser-native AI usage layer that combines role-based governance, "
          "real-time data protection and transparent prompt optimisation. Unlike enterprise browsers and "
          "SSE add-ons that only restrict users, AI Sentinel makes the secure way the easiest and most "
          "productive way to use AI, backed by Cisco's identity, threat intelligence and trust.*"),
    ("h", "5.8 Business model and revenue model"),
    ("b", [
        "**Business model:** B2B SaaS with a product-led B2C on-ramp. Individuals adopt for free; usage "
        "signals within a company domain create qualified enterprise leads; partners deploy and manage.",
        "**Revenue streams:** (1) per-seat subscription (Business / Enterprise); (2) metered advanced "
        "validation and optimisation beyond the included pool; (3) Personal Plus subscriptions; "
        "(4) premium add-ons (extended retention, advanced reporting); (5) pull-through of Duo, Secure "
        "Access and Splunk.",
        "**Cost structure:** squad and site-adapter maintenance, inference compute (kept low through local "
        "checks), cloud hosting, partner margin. Target 75%+ gross margin on seats.",
    ]),
]
