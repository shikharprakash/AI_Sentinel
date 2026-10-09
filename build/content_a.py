"""Word content: Sections 1-3."""
import sdata as N

_s = N.entry_shares()
_adj = N.cisco_adjusted()
SEG = N.CONTESTED_SEGMENT_M

S1 = [
    ("h", "1.1 The company: Cisco Systems, Inc."),
    ("p", "Cisco (NASDAQ: CSCO), founded in 1984 and headquartered in San Jose, California, is a global "
          "leader in networking and security. In fiscal year 2026 Cisco reported record revenue of **US$63.3 "
          "billion (+12% YoY)**, with networking orders growing for eight straight quarters as enterprises "
          "rebuild infrastructure for AI. Cisco serves large enterprises, mid-market and small businesses, "
          "service providers and the public sector in more than 180 countries, mostly through a global "
          "partner ecosystem."),
    ("h2", "Current product portfolio"),
    ("t", ["Business", "Representative products", "Relevance to the new product"], [
        ["Networking", "Catalyst, Meraki, Nexus, Silicon One, AI infrastructure",
         "Huge installed base and partner channel, especially Meraki in the mid-market"],
        ["Security", "Secure Access (SSE), Duo (identity / MFA), XDR, Hypershield, Secure Firewall, "
                     "AI Defense (2025)", "Identity, enforcement points, AI-security models from the "
                                          "Robust Intelligence acquisition (2024), Talos threat intel"],
        ["Observability", "Splunk, ThousandEyes, AppDynamics", "Security analytics and audit-event sink"],
        ["Collaboration", "Webex suite", "Browser and knowledge-worker experience; AI assistant know-how"],
    ], [1.1, 2.6, 2.5]),
    ("h2", "Target market and customers today"),
    ("p", "Cisco's customers are mainly organisations, not individuals. Buyers are CIOs, CISOs, network and "
          "security architects and IT managers. Mid-market companies (100 to 2,000 employees) are an "
          "important and growing segment, served largely through Meraki, Duo and partners. Cisco has little "
          "direct relationship with individual end users. This proposal changes that, carefully."),
    ("h", "1.2 Why a new product now"),
    ("b", [
        "**AI use has outpaced governance.** 75% of knowledge workers use generative AI at work and 78% of "
        "them bring their own AI tools (Microsoft & LinkedIn Work Trend Index 2024).",
        "**Data is already leaking.** In Cisco's own 2024 Data Privacy Benchmark, 48% of respondents admitted "
        "entering non-public company information into GenAI tools, and 27% of organisations had banned "
        "GenAI at least temporarily.",
        "**It is costly.** IBM's 2025 Cost of a Data Breach report found that one in five organisations "
        "suffered a breach because of shadow AI, which added about US$670,000 to the average breach cost. "
        "97% of organisations with AI-related breaches lacked AI access controls.",
        "**Cisco has started, but at the top of the market.** Cisco AI Defense (January 2025) secures AI "
        "applications and AI access for large enterprises through Secure Access and the network. "
        "Mid-market firms without a full SSE stack, and the individual employees who actually type the "
        "prompts, are under-served.",
    ]),
    ("h", "1.3 The proposed product: Cisco AI Sentinel"),
    ("p", "**AI Sentinel** is a browser-native security and productivity layer for third-party AI tools such "
          "as ChatGPT, Gemini, Claude and Copilot. It is delivered as a lightweight Chromium/Edge extension "
          "with a cloud policy and validation service, and it joins the AI Defense family. It brings three "
          "capabilities into one workflow:"),
    ("b", [
        "**Govern:** role-based access to AI tools by user, group and application, with allow, warn and "
        "block actions driven by centrally signed policy bundles.",
        "**Protect:** real-time input and output checks for PII, secrets, confidential data, "
        "prompt-injection indicators and toxic content, with local redaction first.",
        "**Optimize:** an opt-in Prompt Copilot that rewrites vague prompts and compresses redundant context. "
        "It always shows a before/after preview and never overrides a security decision.",
    ]),
    ("h2", "Elevator pitch"),
    ("p", "\"Every company wants its people to use AI, but nobody wants the next data leak to start in a "
          "chat box. Cisco AI Sentinel sits quietly inside the browser, catches the API key or customer list "
          "before it leaves, enforces the company's AI policy across every AI tool, and helps people write "
          "better prompts while doing it. Security teams get control and evidence. Employees get better "
          "answers with fewer interruptions. It takes about a minute to install.\""),
    ("h2", "Who it is for"),
    ("b", [
        "**Primary buyer:** security and IT leaders at mid-market and enterprise organisations (100 to "
        "5,000 employees) that use several AI tools, starting with Cisco's existing Duo, Meraki and Secure "
        "Access customers.",
        "**Primary users:** knowledge workers in engineering, HR, sales, finance and operations.",
        "**Secondary segment:** individual AI power users (developers, researchers, freelancers, students), "
        "served through a freemium, product-led tier. It also acts as a bottom-up acquisition channel "
        "into their employers.",
    ]),
    ("p", "**Vision:** enable everyone to use AI confidently, securely and efficiently, across the tools they "
          "already prefer. **Ask of management:** approve a 12-week MVP (one squad, about US$1.2M fully "
          "loaded) and a 4-week paid pilot, with a launch / no-launch gate at week 12."),
]

S2 = [
    ("h", "2.1 Target market"),
    ("p", "AI Sentinel serves the intersection of three fast-growing categories: (a) shadow-AI risk and "
          "governance, (b) browser and data-loss security for generative AI, and (c) AI productivity "
          "tooling. The core segment is **mid-market and lower-enterprise organisations (100 to 5,000 "
          "employees)** in North America, EMEA and India that use several third-party AI tools and have a "
          "named security or IT owner. A second segment is **individual AI power users**, starting in "
          "India and English-speaking markets."),
    ("h", "2.2 Estimated market size"),
    ("h2", "Top-down (third-party research)"),
    ("b", [
        "Shadow AI risk & governance: **US$1.39B (2026) to US$8.64B (2032), 35.6% CAGR** (MarketsandMarkets, "
        "Sept 2026).",
        "AI Trust, Risk & Security Management (AI TRiSM): **US$3.09B (2026) to US$11.61B (2031), 30.3% "
        "CAGR** (MarketsandMarkets, Aug 2026).",
        "Generative-AI cybersecurity overall: **US$8.65B (2025) to US$35.5B (2031), 26.5% CAGR**.",
    ]),
    ("img", "market_growth.png", 5.6, "Figure 2.1 - Shadow AI risk & governance market (MarketsandMarkets)"),
    ("h2", "Bottom-up (author estimates, steady state FY2029)"),
    ("t", ["Layer", "Logic", "Value (US$/yr)"], [
        ["TAM", "~1B knowledge workers x 75% using GenAI x ~40% in 100+ employee firms = ~300M seats x "
                "US$72/yr; plus ~150M frequent individual users x US$57/yr", f"~${N.TAM:.0f}B potential"],
        ["SAM", "Cisco-reachable mid-market seats in NA, EMEA and India (~25M) x US$72; plus ~20M India and "
                "English-speaking power users reachable via PLG x US$57", f"~${N.SAM:.1f}B"],
        ["SOM", "Year 3: 3% of SAM seats (0.75M) through Duo/Meraki/Secure Access cross-sell and partners; "
                "2% of SAM individuals paying (0.4M)", f"~${N.SOM:.0f}M ARR"],
    ], [0.6, 4.2, 1.4]),
    ("img", "tam_sam_som.png", 5.6, "Figure 2.2 - TAM / SAM / SOM"),
    ("note", "The bottom-up TAM measures potential spend, which is why it exceeds today's realised spend in "
             "the analyst reports. SOM is the planning number used throughout this document."),
    ("h", "2.3 Competitive landscape"),
    ("p", "The market consolidated quickly in 2025 as platform vendors bought AI-security start-ups: "
          "SentinelOne acquired Prompt Security (Aug 2025), Check Point acquired Lakera (Sept 2025), and Palo "
          "Alto Networks turned its Talon acquisition into Prisma Browser. Competitors fall into four groups:"),
    ("t", ["Competitor", "Approach", "Strength", "Gap AI Sentinel targets"], [
        ["Palo Alto Prisma Browser", "Enterprise browser + extension; AI governance, DLP",
         "Deep security, SASE bundle", "Heavy rollout; little productivity value; enterprise-only"],
        ["Island", "Dedicated enterprise browser", "Full browser control", "Users must switch browser"],
        ["Prompt Security (SentinelOne)", "Browser ext, desktop, API runtime for GenAI",
         "Early mover, broad coverage", "Security-only; no individual tier"],
        ["Check Point GenAI Protect + Lakera", "Network/SSE + runtime guardrails",
         "Strong detection research", "Not user-centric; enterprise sales motion"],
        ["Harmonic, LayerX", "Browser extensions for AI data protection", "Lightweight, fast to deploy",
         "Start-up scale; limited identity and network integration"],
        ["Microsoft Purview + Edge for Business", "DLP for AI inside the M365 ecosystem",
         "Bundled with E5", "Weaker outside Microsoft tools and browsers"],
        ["Zscaler / Netskope SSE", "Inline GenAI DLP at proxy", "Network-level visibility",
         "Needs full SSE; no in-context user guidance"],
        ["PromptPerfect, AIPRM", "Prompt optimisation tools", "Productivity", "No security or governance"],
    ], [1.35, 1.65, 1.35, 1.85], 8.5),
    ("img", "perceptual_map.png", 5.2, "Figure 2.3 - Perceptual map: security depth vs. user productivity value"),
    ("p", "**Insight:** competitors treat the user as a risk to be controlled. Nobody owns the upper-right "
          "quadrant, where governance and productivity reinforce each other. That is AI Sentinel's "
          "positioning wedge: security that employees *want* installed."),
    ("h", "2.4 Ansoff matrix analysis"),
    ("t", ["", "Existing products", "New products"], [
        ["Existing markets (Cisco enterprise & mid-market security customers)",
         "**Market penetration:** cross-sell AI Defense and Secure Access AI controls into the installed "
         "base (current strategy)",
         "**Product development (primary strategy):** AI Sentinel for existing Duo, Meraki and Secure "
         "Access customers. Same buyer, new browser-native product"],
        ["New markets (individual users, SMB via PLG, India mid-market)",
         "**Market development:** take Duo / Secure Access into new regions and segments",
         "**Related diversification (secondary):** AI Sentinel Personal for prosumers. New buyer and new "
         "motion for Cisco, kept to a limited bet"],
    ], [1.6, 2.2, 2.4], 8.5),
    ("p", "**Conclusion:** AI Sentinel is mainly a **product-development** move. It builds on Cisco's "
          "brand, identity (Duo), threat intelligence (Talos) and AI Defense models, so risk is moderate. "
          "The individual tier is a **related diversification**. It stays a small, contained bet (freemium, "
          "low CAC) and its main job is to feed enterprise demand."),
]

S3 = [
    ("h", "3.1 Are we the first mover? No. Cisco would be a late (third-wave) entrant"),
    ("p", "Browser-layer AI data protection was pioneered in 2023 by start-ups (Prompt Security, Harmonic, "
          "LayerX, Lakera). Platform vendors followed in 2024-25 (Palo Alto Prisma Browser, Microsoft "
          "Purview for AI, Zscaler/Netskope GenAI DLP, then the SentinelOne and Check Point acquisitions). "
          "Following the brief, we model Cisco as the **third entrant** into the contested segment: "
          "browser-layer AI usage security for the mid-market, worth an estimated **US$300M a year by "
          "FY2029** in Cisco's regions."),
    ("h", "3.2 Cost of being a late entrant: order-of-entry model"),
    ("p", "Urban, Carter, Gaskin & Mucha (1986) found that, holding other factors equal, an entrant's "
          "long-run share relative to the pioneer is (order of entry)^-0.49. The full model also adjusts for "
          "relative product preference (^1.11), relative advertising/marketing spend (^0.28) and entry lag "
          "(^0.07)."),
    ("t", ["Entrant", "Relative share (n^-0.49)", "Normalised share", f"Revenue on US${SEG}M segment"], [
        ["Pioneer (1st)", "1.000", f"{_s[0]:.1%}", f"US${_s[0] * SEG:.0f}M"],
        ["2nd entrant", f"{2 ** -0.49:.3f}", f"{_s[1]:.1%}", f"US${_s[1] * SEG:.0f}M"],
        ["Cisco (3rd)", f"{3 ** -0.49:.3f}", f"{_s[2]:.1%}", f"US${_s[2] * SEG:.0f}M"],
    ], [1.4, 1.6, 1.4, 1.8]),
    ("p", f"**Cost of entering third:** about **{(_s[0] - _s[2]) * 100:.1f} share points** below the "
          f"pioneer. That is roughly **US${(_s[0] - _s[2]) * SEG:.0f}M of annual revenue** forgone by FY2029, "
          f"or about US${(_s[0] - _s[2]) * SEG * 3:.0f}M over three years. Cisco cannot win on timing."),
    ("h", "3.3 How Cisco closes the gap: late-mover advantages"),
    ("p", f"The same model shows how the penalty can be offset. If AI Sentinel achieves a **1.2x relative "
          f"preference** (Govern + Protect + Optimize in one product, no browser switch) and Cisco invests "
          f"**1.5x the marketing and channel weight** of the average rival, with a two-year lag, then "
          f"Cisco's relative share becomes 0.584 x 1.2^1.11 x 1.5^0.28 x 2^0.07 = **{_adj[3]:.2f}**. "
          f"That gives a normalised share of **{_adj[2]:.1%}** (about US${_adj[2] * SEG:.0f}M), better than "
          f"the second entrant and close to the pioneer."),
    ("img", "entry_share.png", 5.4, "Figure 3.1 - Long-run share by order of entry, base vs. Cisco-adjusted"),
    ("b", [
        "**Lower market-education cost:** pioneers already convinced CISOs that GenAI data leakage is "
        "real. Cisco sells into existing budgets.",
        "**Learn from pioneers' mistakes:** competitor reviews show heavy rollouts, noisy false positives "
        "and alert fatigue. We design for low friction from day one.",
        "**Distribution advantage:** Duo, Meraki and Secure Access customers, plus thousands of channel "
        "partners, cut CAC well below a start-up's.",
        "**Bundling and trust:** Enterprise Agreements, Talos threat intelligence and a trusted brand make "
        "Cisco the 'safe choice' for risk-averse buyers.",
        "**Technology maturity:** AI Defense classifiers and smaller, cheaper models make local and remote "
        "checks faster and cheaper than they were in 2023.",
    ]),
    ("p", "**Timing recommendation:** the window is still open (35.6% CAGR, no dominant mid-market "
          "standard), but it is closing as SSE vendors bundle GenAI controls. Each six months of delay "
          "lets rivals lock in enterprise renewals. We should therefore **ship a focused MVP in 12 weeks**, "
          "not a full platform in 12 months."),
]
