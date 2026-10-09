"""Word content: Sections 9-10 and sources."""
import sdata as N

_dq, _dp, _ped, _rev_a, _rev_b = N.elasticity()

S9 = [
    ("h", "9.1 Pricing strategy: freemium + value-based tiers + metered advanced usage"),
    ("p", "We combine three logics, each matched to a cost or value driver:"),
    ("b", [
        "**Freemium for individuals (penetration):** basic local checks cost us almost nothing to run, so "
        "we give them away. This builds trust, installs and bottom-up enterprise leads. Charging for basic "
        "safety would discourage safe behaviour.",
        "**Value-based seats for organisations:** the reference value is risk avoided. IBM's 2025 report "
        "puts the average breach at US$4.44M globally (US$10.22M in the US), and shadow AI adds about "
        "US$670K. For a 500-seat company at US$8/user/month (US$48K/year), preventing a single incident "
        "pays for the product many times over. We price below enterprise-browser suites to win the "
        "mid-market.",
        "**Usage-based for expensive inference:** advanced remote classification and model-assisted "
        "optimisation cost real compute, so a pooled allowance is included and overage is metered. "
        "Revenue then scales with cost, protecting gross margin.",
    ]),
    ("h", "9.2 Launch price points to test"),
    ("t", ["Tier", "Launch price", "Includes", "Rationale"], [
        ["Personal Free", "Rs 0 / US$0", "Local PII and secret checks, basic prompt clean-up, 50 advanced "
                                        "ops/month", "Acquisition and trust"],
        ["Personal Plus", "**Rs 399/month** (Rs 3,999/yr); US$6.99 international",
         "1,000 advanced ops, all Copilot modes, personal usage view", "Inside the Rs 249-499 range from "
                                                                       "concept tests"],
        ["Business (25-2,000 seats)", "**US$8/user/month** (Rs 499 in India)",
         "RBAC, console, event export, Duo/Entra SSO, 500 pooled ops/user", "Below Prisma/Island; "
                                                                             "matches CISO's US$5-8"],
        ["Enterprise", "US$6-7/user at volume; EA bundle", "Splunk/XDR, extended retention, premium "
                                                           "support, custom policies", "Volume and bundle "
                                                                                       "pricing"],
        ["Overage", "US$2 per 1,000 advanced ops", "Spending caps and alerts by default",
         "~60% margin on inference"],
    ], [1.2, 1.6, 2.0, 1.4], 8.5),
    ("h2", "Unit economics check"),
    ("p", "A Business seat (US$96/year) uses about 300 advanced operations a month at about US$0.0008 each, "
          "or roughly US$2.90/year in inference. Hosting, adapters and support add about US$12/seat/year, "
          "and the partner margin is 20%. That leaves a **contribution margin of about 65% of list price (about 80% of net revenue after "
          "partner margin)**, which improves as local checks handle more of the traffic."),
    ("h", "9.3 Managing price over time based on elasticity"),
    ("p", "We will measure price elasticity of demand (PED = % change in quantity / % change in price) "
          "through randomised price cells on new Personal Plus sign-ups and through win/loss and discount "
          "data for Business deals."),
    ("t", ["Illustrative test (per 1,000 trial users)", "Cell A: Rs 399", "Cell B: Rs 549"], [
        ["Trial-to-paid conversion", f"{N.CONV_A:.1%}", f"{N.CONV_B:.1%}"],
        ["Monthly revenue", f"Rs {_rev_a:,.0f}", f"Rs {_rev_b:,.0f}"],
        ["Change", "-", f"Price +{_dp:.1%}, quantity {_dq:.1%}"],
        ["PED", "-", f"{_ped:.2f} (inelastic)"],
    ], [2.6, 1.8, 1.8], 8.5),
    ("h2", "When to increase price"),
    ("b", [
        f"If |PED| < 1, as in the illustration ({_ped:.2f}), revenue rises with price (+"
        f"{(_rev_b / _rev_a - 1):.0%}). We would move Personal Plus toward Rs 499-549 for new users and "
        "keep earlier users on their original price for 12 months.",
        "Raise enterprise list prices when new value ships (Secure Access integration, AI Defense "
        "classifiers, compliance reports), using good / better / best packaging rather than flat increases.",
        "Use value metrics: as customers expand AI use, pooled operations grow and revenue grows with them.",
    ]),
    ("h2", "When to decrease price"),
    ("b", [
        "If |PED| > 1 (conversion falls faster than price rises), test Rs 299 and annual-only discounts. "
        "Offer a student plan at Rs 149 and purchasing-power pricing in emerging markets.",
        "Use volume discounts and EA bundles for large deals; competitive displacement offers when a rival "
        "SSE bundle is the alternative.",
        "Use temporary promotions (Cisco Live launch, Diwali / year-end) rather than permanent cuts, so "
        "the reference price is preserved.",
        "Guardrails: never price critical safety checks out of reach; keep them in the free tier even "
        "when a quota is exhausted.",
    ]),
]

S10 = [
    ("h", "10.1 GTM strategy overview"),
    ("p", "**Two motions on one platform:** (1) a **sales-led and partner-led enterprise motion** into "
          "Cisco's installed base, and (2) a **product-led individual motion** that builds awareness and "
          "creates bottom-up demand inside companies. Launch: private preview at **Cisco Live EMEA "
          "(Feb 2027)**, Business-tier GA in **April 2027**, showcase at **Cisco Live US (June 2027)**."),
    ("h", "10.2 Sales funnel plan"),
    ("t", ["Funnel stage", "Enterprise (CISO / IT manager)", "Individual (power user)", "Stage KPI"], [
        ["Awareness", "Talos 'State of Shadow AI' report; Cisco Live keynote demo; LinkedIn; partner "
                      "newsletters; security podcasts", "Developer communities, YouTube/Instagram "
                                                        "creators, Product Hunt, Chrome Web Store SEO",
         "Reach, report downloads, store impressions"],
        ["Interest", "Webinars with design-partner CISOs; free 'Shadow AI Risk Check' in monitor mode",
         "Short demo videos of 'Redact & send' and Copilot; free tier", "Sign-ups, risk checks started"],
        ["Consideration", "Comparison guides vs. enterprise browsers/SSE; ROI calculator; reference calls",
         "Ratings and reviews, transparent privacy page, in-product wins", "Demo requests; WAU"],
        ["Intent", "4-week paid pilot (credit applied on purchase); security review pack; pilot "
                   "report", "Usage nudges at quota limits; trial of Plus", "Pilots started; trial starts"],
        ["Purchase", "Partner quote, EA add-on, Cisco/AWS marketplace; seat-based contract",
         "In-app upgrade via UPI/cards; annual plan offer", "Pilot-to-paid %, paid conversion"],
    ], [1.0, 2.2, 1.8, 1.2], 8.5),
    ("h", "10.3 From zero to the first 10 paying customers"),
    ("b", [
        "**Customer zero:** Cisco IT runs AI Sentinel internally first. This gives a credible case study "
        "and real telemetry.",
        "**Design partners:** account teams nominate 15 mid-market Duo/Meraki customers (India and US). "
        "We recruit 5 for pilots and aim to convert 3-4.",
        "**Founder-led selling:** the VP Product and PM join every early call. Pilot reports are tailored "
        "to each customer's data.",
        "**Pilot economics:** 4-week paid pilot at US$2,500, credited against an annual contract. Goal: "
        "10 paying logos by the end of month 6.",
    ]),
    ("h", "10.4 From 10 to 100s of customers"),
    ("b", [
        "**Partner channel:** enable 50 Gold/Premier partners and MSSPs with a packaged 'AI Safe "
        "Adoption' service, deal registration and margin incentives.",
        "**Installed-base campaigns:** in-console offers to Duo and Meraki admins; Secure Access bundle "
        "for EA renewals.",
        "**Product-led signals:** when 10 or more free users share a company domain, alert the account "
        "team and offer the admin a free org trial (PQLs).",
        "**Content flywheel:** quarterly Talos AI-leak research, case studies and Cisco Live sessions.",
        "**Scale targets:** 100 business customers and 50,000 individual users by month 12; 1,000 "
        "customers and US$20M ARR by month 24, on the path to the US$77M SOM by FY2029.",
    ]),
    ("h", "10.5 Launch metrics and governance"),
    ("t", ["Metric", "Month 6", "Month 12"], [
        ["Paying business customers", "10", "100"],
        ["Individual users (free / paid)", "15,000 / 600", "50,000 / 2,500"],
        ["Pilot-to-paid conversion", ">= 30%", ">= 40%"],
        ["Blended CAC payback", "< 18 months", "< 12 months"],
        ["Net revenue retention", "-", ">= 115%"],
    ], [2.6, 1.8, 1.8], 8.5),
    ("p", "**Decision requested:** approve the 12-week MVP squad (~US$1.2M) with a launch / no-launch "
          "review at week 12 against the exit criteria in Section 7."),
]

SOURCES = [
    "Cisco newsroom, 'Cisco Unveils AI Defense to Secure the AI Transformation of Enterprises', 15 Jan 2025.",
    "Cisco, Q4 and FY2026 earnings release, Aug 2026 (FY2026 revenue US$63.3B).",
    "Cisco 2024 Data Privacy Benchmark Study, press release, 25 Jan 2024.",
    "Microsoft & LinkedIn, 2024 Work Trend Index: 'AI at Work Is Here. Now Comes the Hard Part'.",
    "IBM / Ponemon, Cost of a Data Breach Report 2025, press release, 30 Jul 2025.",
    "MarketsandMarkets, Shadow AI Risk & Governance Market (Sept 2026); AI TRiSM Market (Aug 2026); "
    "Generative AI Cybersecurity Market.",
    "SentinelOne press release, 'SentinelOne to Acquire Prompt Security', 5 Aug 2025.",
    "Check Point press release, 'Check Point Acquires Lakera', 16 Sep 2025.",
    "Palo Alto Networks, Prisma Browser product page (accessed Oct 2026).",
    "Urban, G., Carter, T., Gaskin, S. & Mucha, Z. (1986). Market Share Rewards to Pioneering Brands. "
    "Management Science, 32(6).",
    "Product_Idea.md (AI Sentinel product concept), author's working document.",
    "Bottom-up market sizing, competitor scoring, interview and concept-test data are the author's "
    "estimates / illustrative and are labelled as such.",
]
