"""Deck slides 13-18: MVP & PMF (2), product development, pricing, GTM (2)."""
from pptx.chart.data import CategoryChartData
from pptx.enum.chart import XL_CHART_TYPE, XL_LABEL_POSITION
from pptx.enum.shapes import MSO_SHAPE
from pptx.util import Inches, Pt
from deck_lib import *
import sdata as N


def s_mvp(prs):
    s = blank(prs)
    header(s, "7  MVP & PMF", "Build a focused 12-week MVP, not a full platform")
    why = [("!", "Dev risk moderate-high", "UI changes break adapters; detection needs tuning", AMBER),
           ("?", "PMF unproven", "n = 3 tests; willingness to pay needs real money", BLUE),
           ("$", "Opportunity cost", "MVP = 1 squad x 12 weeks vs. 3 squads x 12 months", GREEN)]
    for i, (b, t, d, c) in enumerate(why):
        y = 1.75 + i * 1.05
        badge(s, 0.6, y + 0.1, 0.55, b, fill=c, size=18)
        text(s, 1.3, y, 3.9, 0.4, t, size=15, color=NAVY, bold=True)
        text(s, 1.3, y + 0.38, 3.9, 0.6, d, size=12)
    rows = [["Capability", "MVP scope (P0)"],
            ["Apps", "ChatGPT + Gemini web; Chrome & Edge; status badge"],
            ["Protect", "Local secrets / PII checks; 'Redact & send'; warn / block"],
            ["Govern", "Duo / Entra SSO, groups, monitor -> enforce, signed policies"],
            ["Optimize", "On-demand Copilot, 3 modes, diff, accept / revert"],
            ["Console", "Policies, users, metadata-only event export"],
            ["Out", "Desktop apps, API traffic, every AI site, certification"]]
    table(s, 5.6, 1.75, 7.1, rows, [1.3, 5.8], size=12, row_h=0.42)
    text(s, 0.6, 5.0, 12, 0.35, "EARLY-SUCCESS FACTORS (PILOT EXIT CRITERIA)", size=12, color=BLUE, bold=True)
    kpis = [("≥ 60%", "session-1 activation"), ("≤ 100 ms", "p95 local latency"),
            ("≥ 95%", "detection precision"), ("≥ 40%", "suggestion acceptance"),
            ("≥ 35%", "week-4 retention"), ("≥ 30%", "pilot-to-paid")]
    for i, (b, t) in enumerate(kpis):
        x = 0.6 + i * 2.03
        rect(s, x, 5.4, 1.88, 1.35, fill=ICE)
        text(s, x + 0.12, 5.5, 1.7, 0.6, b, size=22, color=BLUE, bold=True)
        text(s, x + 0.12, 6.1, 1.7, 0.55, t, size=12)


def s_roadmap(prs):
    s = blank(prs)
    header(s, "7  Roadmap, PMF & growth", "From discovery to commercial launch in six months")
    ph = [("Wk 1-2", "Discovery", "Interviews, threat model, pricing tests"),
          ("Wk 3-6", "Prototype", "2 apps, local checks, preview UX"),
          ("Wk 7-9", "Alpha", "RBAC, console, metering, red team"),
          ("Wk 10-12", "Pilot", "5 design partners + 500 beta users"),
          ("Mo 4-6", "Launch", "Cisco Live EMEA; Business GA"),
          ("Mo 7-12", "Scale", "Secure Access, Splunk, more apps")]
    for i, (when, t, d) in enumerate(ph):
        x = 0.6 + i * 2.03
        ch = rect(s, x, 1.75, 2.1, 0.6, fill=[SKY, SKY, BLUE, BLUE, NAVY, NAVY][i],
                  shape=MSO_SHAPE.CHEVRON if i else MSO_SHAPE.PENTAGON)
        shape_text(ch, when, size=13, bold=True, color=NAVY if i < 2 else WHITE)
        text(s, x + 0.08, 2.45, 1.85, 0.35, t, size=14, color=NAVY, bold=True)
        text(s, x + 0.08, 2.8, 1.85, 0.8, d, size=12)
    text(s, 0.6, 3.85, 5.0, 0.35, "HOW WE REACH PMF", size=12, color=BLUE, bold=True)
    text(s, 0.6, 4.25, 5.0, 2.6, bullets([
        "Beachhead: mid-market Duo / Meraki firms + developers",
        "Sean Ellis test ≥ 40% 'very disappointed'",
        "Retention curves flatten by cohort",
        "Weekly review of false positives and overrides",
        "5 design partners as co-builders"], size=13, after=5))
    rows = [["AARRR", "Growth experiment", "Success metric"],
            ["Acquire", "Store listing A/B: 'safer' vs. 'better prompts'", "+20% installs"],
            ["Activate", "Guided first run with a sample risky prompt", "45% -> 60%"],
            ["Engage", "Shortcut + subtle Copilot button", "+25% uses / WAU"],
            ["Retain", "Weekly 'you were protected' digest", "+5 pts W4"],
            ["Refer", "Invite a teammate: +100 ops each", "K ≥ 0.2"],
            ["Revenue", "Annual plan: 2 months free", "≥ 40% annual"]]
    table(s, 5.9, 3.85, 6.8, rows, [1.2, 3.85, 1.75], size=12, row_h=0.42)


def s_dev(prs):
    s = blank(prs)
    header(s, "8  Product development", "Design Thinking decides what to build; Agile delivers it safely")
    dt = [("Empathise", "Interviews, shadow AI sessions"), ("Define", "POV + 'How might we'"),
          ("Ideate", "Workshops, Crazy 8s"), ("Prototype", "Lo-fi -> Figma -> spike"),
          ("Test", "Usability, pilots, A/B")]
    for i, (t, d) in enumerate(dt):
        x = 0.6 + i * 2.45
        c = rect(s, x + 0.65, 1.7, 1.0, 1.0, fill=[GREEN, BLUE, "0A6EA8", NAVY, BLUE][i], shape=MSO_SHAPE.OVAL)
        shape_text(c, str(i + 1), size=20, bold=True, color=WHITE)
        text(s, x, 2.8, 2.3, 0.35, t, size=15, color=NAVY, bold=True, align="c")
        text(s, x, 3.15, 2.3, 0.5, d, size=12, align="c")
    lanes = [("DISCOVERY TRACK  (Design Thinking)", ["Empathise", "Ideate + lo-fi", "Hi-fi Copilot",
                                                    "Console tests", "Pricing tests", "Pilot synthesis"], ICE, INK),
             ("DELIVERY TRACK  (Scrum, 2-week sprints)", ["Spike, CI/CD", "Extension, adapters", "Redaction, "
                                                         "policy", "Console, RBAC", "Hardening", "Launch ready"],
              NAVY, WHITE)]
    for li, (lab, items, fill, col) in enumerate(lanes):
        y = 3.95 + li * 1.15
        text(s, 0.6, y, 3.1, 1.0, lab, size=12, color=BLUE, bold=True, anchor="m")
        for k, it in enumerate(items):
            r = rect(s, 3.75 + k * 1.5, y + 0.1, 1.4, 0.8, fill=fill)
            shape_text(r, [(f"S{2 * k + 1}-{2 * k + 2}", {"size": 10, "bold": True,
                                                          "color": BLUE if li == 0 else SKY}),
                           (it, {"size": 11, "color": col})])
    text(s, 0.6, 6.3, 12.1, 0.6, "**Squad of ~10:** PM, designer, 5 engineers, ML engineer, security "
                                 "researcher, QA.  **Definition of Done:** no precision/recall regression, "
                                 "privacy review passed, adapter health checks green.", size=13)


def s_pricing(prs):
    s = blank(prs)
    header(s, "9  Pricing", "Free where safety is cheap; charge for value and for costly inference")
    tiers = [("Personal Free", "Rs 0", "Local checks, basic clean-up, 50 advanced ops", ICE, NAVY),
             ("Personal Plus", "Rs 399/mo", "1,000 ops, all Copilot modes; US$6.99 intl", SKY, NAVY),
             ("Business", "US$8/user/mo", "RBAC, console, SSO, export; 500 pooled ops/user", BLUE, WHITE),
             ("Enterprise", "US$6-7 at volume", "EA bundle, Splunk/XDR, retention, support", NAVY, WHITE)]
    for i, (t, p, d, f, c) in enumerate(tiers):
        x = 0.6 + i * 3.05
        rect(s, x, 1.7, 2.9, 2.1, fill=f)
        text(s, x + 0.2, 1.82, 2.5, 0.35, t, size=14, color=c, bold=True)
        text(s, x + 0.2, 2.2, 2.6, 0.6, p, size=24, color=c, bold=True)
        text(s, x + 0.2, 2.85, 2.55, 0.9, d, size=12, color=c)
    text(s, 0.6, 3.9, 12, 0.35, "Overage: US$2 per 1,000 advanced ops with default spend caps. Seat contribution "
                                "margin ~65% of list, rising as local checks absorb more traffic.", size=12,
         color=GREY)
    dq, dp, ped, ra, rb = N.elasticity()
    cd = CategoryChartData(); cd.categories = ["Rs 399 (4.0% convert)", "Rs 549 (3.4% convert)"]
    cd.add_series("Revenue per 1,000 trials (Rs)", [ra, rb])
    gf = s.shapes.add_chart(XL_CHART_TYPE.COLUMN_CLUSTERED, Inches(0.6), Inches(4.35), Inches(4.6),
                            Inches(2.55), cd)
    ch = gf.chart; chart_style(ch); ch.has_legend = False
    ch.has_title = True; ch.chart_title.text_frame.text = f"Illustrative price test: PED = {ped:.2f}"
    r0 = ch.chart_title.text_frame.paragraphs[0].runs[0]; r0.font.size = Pt(13); r0.font.bold = True
    r0.font.color.rgb = RGB(NAVY)
    pl = ch.plots[0]; pl.gap_width = 90; pl.has_data_labels = True
    pl.data_labels.number_format = '"Rs "#,##0'; pl.data_labels.number_format_is_linked = False
    pl.data_labels.position = XL_LABEL_POSITION.OUTSIDE_END; pl.data_labels.font.size = Pt(12)
    ser = pl.series[0]; ser.format.fill.solid(); ser.format.fill.fore_color.rgb = RGB(BLUE)
    ch.value_axis.visible = False; ch.value_axis.has_major_gridlines = False
    ch.value_axis.minimum_scale = 0; ch.value_axis.maximum_scale = 22000
    ch.category_axis.format.line.color.rgb = RGB(LINE)
    for i, (t, items, c) in enumerate([
        ("Raise price when |PED| < 1", ["Move Plus toward Rs 499-549 for new users", "Grandfather early users "
                                        "12 months", "Raise enterprise price as new value ships"], GREEN),
        ("Lower price when |PED| > 1", ["Test Rs 299, student plan Rs 149", "Volume / EA bundle discounts",
                                        "Time-boxed launch promotions"], AMBER)]):
        x = 5.6 + i * 3.6
        badge(s, x, 4.4, 0.45, "↑" if i == 0 else "↓", fill=c, size=16)
        text(s, x + 0.55, 4.38, 2.95, 0.5, t, size=14, color=NAVY, bold=True, anchor="m")
        text(s, x, 5.0, 3.4, 1.9, bullets(items, size=13, after=4))


def s_gtm(prs):
    s = blank(prs)
    header(s, "10  Go-to-market", "Partner-led enterprise motion, fuelled by a product-led on-ramp")
    text(s, 4.55, 1.65, 4.0, 0.35, "ENTERPRISE (CISO / IT)", size=12, color=BLUE, bold=True)
    text(s, 8.75, 1.65, 4.0, 0.35, "INDIVIDUAL (POWER USER)", size=12, color=BLUE, bold=True)
    fun = [("Awareness", "Talos 'State of Shadow AI' report, Cisco Live demo, partner newsletters",
            "Developer communities, creators, Product Hunt, Web Store SEO"),
           ("Interest", "CISO webinars; free 'Shadow AI Risk Check' (monitor mode)",
            "Short demos of 'Redact & send'; free tier"),
           ("Consideration", "Comparison guides, ROI calculator, reference calls",
            "Reviews, privacy page, in-product wins"),
           ("Intent", "4-week paid pilot (credited); security review pack",
            "Nudges at quota limits; Plus trial"),
           ("Purchase", "Partner quote, EA add-on, Cisco / AWS marketplace",
            "In-app upgrade (UPI / cards); annual offer")]
    for i, (st, ent, ind) in enumerate(fun):
        y = 2.05 + i * 0.95
        w = 3.6 - i * 0.45
        r = rect(s, 0.6 + (3.6 - w) / 2, y, w, 0.82, fill=[SKY, BLUE, "0A6EA8", NAVY, GREEN][i])
        shape_text(r, st, size=14, bold=True, color=NAVY if i == 0 else WHITE)
        text(s, 4.55, y, 4.0, 0.82, ent, size=12, anchor="m")
        text(s, 8.75, y, 4.0, 0.82, ind, size=12, anchor="m")


def s_scale(prs):
    s = blank(prs, dark=True)
    header(s, "10  Scaling & the ask", "From customer zero to hundreds, then the decision we need today",
           dark=True)
    steps = [("0 → 10", "Customer zero: Cisco IT. 15 nominated Duo / Meraki accounts, 5 paid pilots "
                             "(US$2,500, credited). Founder-led selling.", "10 logos by month 6"),
             ("10 → 100", "50 Gold partners and MSSPs, Duo / Meraki in-console offers, Secure Access "
                               "bundle at EA renewal.", "100 customers by month 12"),
             ("100 → 1,000s", "PLG signals (10+ free users per domain -> PQL), Talos research flywheel, "
                                   "Cisco Live case studies.", "US$20M ARR by month 24")]
    for i, (t, d, k) in enumerate(steps):
        x = 0.6 + i * 2.85; y = 3.55 - i * 0.75
        r = rect(s, x, y, 2.7, 6.75 - y, fill=["17406E", "0A6EA8", BLUE][i])
        text(s, x + 0.18, y + 0.15, 2.4, 0.5, t, size=22, color=WHITE, bold=True)
        text(s, x + 0.18, y + 0.7, 2.4, 1.9, d, size=12, color=WHITE)
        text(s, x + 0.18, 6.15, 2.4, 0.5, k, size=12, color=SKY, bold=True)
    r = rect(s, 9.3, 1.85, 3.4, 4.9, fill=WHITE)
    text(s, 9.5, 2.0, 3.0, 0.35, "DECISION REQUESTED", size=12, color=BLUE, bold=True)
    text(s, 9.5, 2.4, 3.0, 1.1, "Approve the 12-week AI Sentinel MVP", size=20, color=NAVY, bold=True)
    text(s, 9.5, 3.55, 3.05, 3.1, bullets([
        "~US$1.2M: one squad",
        "5 paid design-partner pilots",
        "Launch / no-launch gate in Jan 2027 against the exit criteria",
        "Upside: path to US$77M ARR by FY2029"], size=13, after=6))


SLIDES = [s_mvp, s_roadmap, s_dev, s_pricing, s_gtm, s_scale]
