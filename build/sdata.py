"""Shared numbers for the AI Sentinel capstone (doc + deck use the same figures)."""

# ---- Palette (Cisco-inspired) ----
NAVY, BLUE, SKY, GREEN, AMBER, GREY, RED, ICE = (
    "0D274D", "049FD9", "BFE6F7", "6CC04A", "FBAB18", "5B6770", "E2231A", "EEF7FC")

# ---- Top-down market (MarketsandMarkets, 2026 reports) ----
SHADOW_AI = {"start": 2026, "v0": 1.39, "end": 2032, "v1": 8.64, "cagr": 0.356}
AI_TRISM = {"start": 2026, "v0": 3.09, "end": 2031, "v1": 11.61, "cagr": 0.303}


def shadow_series():
    yrs = list(range(2026, 2033))
    return yrs, [round(1.39 * (1.356 ** (y - 2026)), 2) for y in yrs]


# ---- Bottom-up sizing (author estimates, FY2029 = year 3 after launch) ----
# Enterprise: knowledge workers using GenAI in orgs with 100+ employees
ENT_TAM_SEATS = 300e6          # ~1bn knowledge workers x 75% AI use x ~40% in 100+ emp orgs
ENT_ARPU_YR = 72               # US$6 / user / month blended
ENT_SAM_SEATS = 25e6           # Cisco-reachable mid-market (100-5,000 emp) in NA, EMEA, India
ENT_SOM_SEATS = 0.75e6         # 3% of SAM seats by FY2029
IND_TAM_USERS = 150e6          # frequent individual GenAI users worldwide willing to install tools
IND_ARPU_YR = 57               # ~Rs 399 / month (~US$4.75) blended incl. intl
IND_SAM_USERS = 20e6           # India + English-speaking power users reachable via PLG
IND_SOM_USERS = 0.4e6          # 2% of SAM paying by FY2029

TAM = (ENT_TAM_SEATS * ENT_ARPU_YR + IND_TAM_USERS * IND_ARPU_YR) / 1e9   # US$ bn
SAM = (ENT_SAM_SEATS * ENT_ARPU_YR + IND_SAM_USERS * IND_ARPU_YR) / 1e9
SOM = (ENT_SOM_SEATS * ENT_ARPU_YR + IND_SOM_USERS * IND_ARPU_YR) / 1e6   # US$ m

# ---- Order of entry (Urban, Carter, Gatignon & Mucha 1986) ----
# share_n / share_1 = entry^-0.49 * pref^1.11 * adv^0.28 * lag^0.07
CONTESTED_SEGMENT_M = 300      # browser-layer AI usage security, mid-market, FY2029, US$ m


def entry_shares(n=3):
    raw = [k ** -0.49 for k in range(1, n + 1)]
    tot = sum(raw)
    return [r / tot for r in raw]


def cisco_adjusted(pref=1.2, adv=1.5, lag=2):
    pioneer, second = 1.0, 2 ** -0.49
    cisco = 3 ** -0.49 * pref ** 1.11 * adv ** 0.28 * lag ** 0.07
    tot = pioneer + second + cisco
    return pioneer / tot, second / tot, cisco / tot, cisco


# ---- Customer research (ILLUSTRATIVE - replace with real interview data) ----
FEATURES = [
    "Sensitive-data detection & redaction",
    "Approved / blocked AI tool controls (RBAC)",
    "Prompt optimizer (rewrite & structure)",
    "Token / cost savings dashboard",
    "Before/after preview with undo",
    "Local-first, on-device checks",
    "Admin audit log & reports",
    "Low latency, no workflow friction",
    "Output checks on AI responses",
    "Works across multiple AI tools",
]
SHORT = ["Data redaction", "Tool access (RBAC)", "Prompt optimizer", "Savings dashboard",
         "Preview & undo", "Local-first checks", "Audit & reports", "Low friction",
         "Output checks", "Multi-tool coverage"]
PEOPLE = ["Ananya (Dev)", "Vikram (CISO)", "Meera (HR)", "Rahul (IT Mgr)", "Priya (Freelancer)"]
RATINGS = [  # rows = features, cols = people (1 = not important, 5 = critical)
    [4, 5, 5, 5, 4], [2, 5, 3, 5, 1], [5, 3, 4, 3, 5], [4, 3, 2, 4, 4], [5, 4, 4, 3, 5],
    [5, 4, 4, 4, 5], [1, 5, 2, 5, 1], [5, 4, 5, 4, 5], [3, 4, 3, 4, 2], [4, 5, 4, 4, 4],
]


def rating_table():
    rows = []
    for f, s, r in zip(FEATURES, SHORT, RATINGS):
        ent = (r[1] + r[3]) / 2
        ind = (r[0] + r[4]) / 2
        rows.append({"feature": f, "short": s, "scores": r, "mean": sum(r) / 5,
                     "ent": ent, "ind": ind})
    rows.sort(key=lambda d: (-d["mean"], -d["ent"]))
    for i, d in enumerate(rows, 1):
        d["rank"] = i
    return rows


# ---- Pricing elasticity illustration ----
PRICE_A, CONV_A = 399, 0.040
PRICE_B, CONV_B = 549, 0.034


def elasticity():
    dq = (CONV_B - CONV_A) / CONV_A
    dp = (PRICE_B - PRICE_A) / PRICE_A
    return dq, dp, dq / dp, PRICE_A * CONV_A * 1000, PRICE_B * CONV_B * 1000


if __name__ == "__main__":
    print(f"TAM ${TAM:.1f}bn  SAM ${SAM:.2f}bn  SOM ${SOM:.0f}m")
    s = entry_shares()
    print("entry shares", [f"{x:.1%}" for x in s])
    print("pioneer $m", s[0] * CONTESTED_SEGMENT_M, "third $m", s[2] * CONTESTED_SEGMENT_M,
          "gap", (s[0] - s[2]) * CONTESTED_SEGMENT_M)
    print("cisco adjusted", [f"{x:.3f}" for x in cisco_adjusted()],
          cisco_adjusted()[2] * CONTESTED_SEGMENT_M)
    for d in rating_table():
        print(d["rank"], d["short"], d["mean"], d["ent"], d["ind"])
    print("elasticity", elasticity())
    print(shadow_series())
