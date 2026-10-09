"""Lo-fi (sketch-style) wireframes of the AI Sentinel concept for concept testing."""
import os
import warnings
import logging
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

warnings.filterwarnings("ignore")
logging.getLogger("matplotlib.font_manager").setLevel(logging.ERROR)
OUT = os.path.join(os.path.dirname(__file__), "img")
INK, MID, LITE, HI = "#2B2B2B", "#8C8C8C", "#E6E6E6", "#049FD9"


def box(ax, x, y, w, h, fc="white", ec=INK, lw=1.4, r=0.01):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad=0,rounding_size={r}",
                                fc=fc, ec=ec, lw=lw))


def t(ax, x, y, s, size=9, color=INK, weight="normal", ha="left"):
    ax.text(x, y, s, fontsize=size, color=color, fontweight=weight, ha=ha, va="center")


def btn(ax, x, y, w, label, primary=False):
    box(ax, x, y, w, 0.055, fc="#BFE6F7" if primary else "white", ec=HI if primary else INK, lw=1.8 if primary else 1.4, r=0.012)
    t(ax, x + w / 2, y + 0.028, label, 8, INK, "bold", "center")


def frame(title):
    fig, ax = plt.subplots(figsize=(7.2, 4.4))
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
    box(ax, 0.01, 0.01, 0.98, 0.98, lw=2)
    box(ax, 0.01, 0.91, 0.98, 0.08, fc=LITE, lw=2)
    for i in range(3):
        ax.add_patch(plt.Circle((0.04 + i * 0.025, 0.95), 0.008, color=MID))
    box(ax, 0.14, 0.925, 0.6, 0.05, r=0.02)
    t(ax, 0.16, 0.95, title, 8, MID)
    return fig, ax


def save(fig, name):
    fig.savefig(os.path.join(OUT, name), dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def wf_protect():
    with plt.xkcd(scale=0.6, length=120, randomness=2):
        fig, ax = frame("chat.ai-tool.com  (supported app)")
        box(ax, 0.80, 0.927, 0.17, 0.046, fc="#BFE6F7", ec=HI, r=0.02)
        t(ax, 0.885, 0.95, "Sentinel: Protected", 7, INK, "bold", "center")
        for i, w in enumerate([0.55, 0.45, 0.6]):
            box(ax, 0.06, 0.80 - i * 0.07, w, 0.04, fc=LITE, ec=LITE)
        box(ax, 0.06, 0.40, 0.88, 0.17)
        t(ax, 0.08, 0.53, "Summarise this vendor contract for Acme Pvt Ltd. Contact: Ravi,", 8.5)
        t(ax, 0.08, 0.49, "PAN [ABCDE1234F]  and use API key [sk-live-8f3...]  to fetch invoices", 8.5)
        t(ax, 0.08, 0.44, "...", 8.5, MID)
        box(ax, 0.06, 0.06, 0.88, 0.30, fc="#FFF6E0", ec="#E0A100", lw=1.8)
        t(ax, 0.08, 0.32, "(!)  2 sensitive items found before sending", 10, INK, "bold")
        t(ax, 0.08, 0.27, "- PAN number (Personal ID)   - API key (Secret)   Policy: Finance team", 8.5)
        t(ax, 0.08, 0.225, "Why? Your org blocks secrets and PII from leaving in AI prompts.", 8, MID)
        btn(ax, 0.08, 0.10, 0.22, "Redact & send", True)
        btn(ax, 0.32, 0.10, 0.16, "Edit prompt")
        btn(ax, 0.50, 0.10, 0.26, "Send anyway (logged)")
        t(ax, 0.79, 0.127, "Checked on device\n  in 38 ms", 7, MID)
        save(fig, "wf_protect.png")


def wf_optimize():
    with plt.xkcd(scale=0.6, length=120, randomness=2):
        fig, ax = frame("chat.ai-tool.com  -  Prompt Copilot panel")
        box(ax, 0.04, 0.06, 0.40, 0.82, fc=LITE, ec=LITE)
        t(ax, 0.06, 0.84, "(AI tool conversation)", 8, MID)
        box(ax, 0.47, 0.06, 0.49, 0.82)
        t(ax, 0.49, 0.84, "Prompt Copilot", 10, INK, "bold")
        t(ax, 0.49, 0.79, "Mode:  ( ) Concise   (o) Structured   ( ) Detailed", 7.5)
        t(ax, 0.49, 0.735, "ORIGINAL", 7, MID, "bold")
        box(ax, 0.49, 0.60, 0.45, 0.11, fc="white", ec=MID)
        t(ax, 0.50, 0.68, "can u write something about our Q3 sales for", 7.5)
        t(ax, 0.50, 0.64, "the leadership, make it good and not too long...", 7.5)
        t(ax, 0.49, 0.565, "SUGGESTED", 7, HI, "bold")
        box(ax, 0.49, 0.32, 0.45, 0.22, fc="#EAF6FC", ec=HI)
        for i, s in enumerate(["Role: You are a sales analyst.", "Task: Write a 150-word Q3 sales summary",
                               "  for the leadership team.", "Include: revenue vs target, top 3 wins,",
                               "  1 risk. Format: 3 bullets + 1 line ask."]):
            t(ax, 0.50, 0.51 - i * 0.04, s, 7.5)
        t(ax, 0.49, 0.28, "Preserved: names, numbers, constraints  [OK]", 7.5)
        t(ax, 0.49, 0.24, "Tokens: 41 -> 52 (+11)  |  clarity score 2/5 -> 4/5", 7.5)
        btn(ax, 0.49, 0.10, 0.13, "Accept", True)
        btn(ax, 0.64, 0.10, 0.13, "Reject")
        btn(ax, 0.79, 0.10, 0.13, "Revert")
        save(fig, "wf_optimize.png")


def wf_admin():
    with plt.xkcd(scale=0.6, length=120, randomness=2):
        fig, ax = frame("sentinel.cisco.com/admin  -  Policies")
        box(ax, 0.02, 0.02, 0.17, 0.89, fc=LITE, ec=LITE)
        for i, s in enumerate(["Overview", "Policies", "Groups", "Apps", "Events", "Usage & billing"]):
            t(ax, 0.04, 0.85 - i * 0.07, s, 8, INK, "bold" if s == "Policies" else "normal")
        for i, (k, v) in enumerate([("Compliance", "97.8%"), ("Prompts protected", "12,480"),
                                    ("Blocked", "214"), ("p95 latency", "62 ms")]):
            box(ax, 0.22 + i * 0.19, 0.74, 0.17, 0.13)
            t(ax, 0.235 + i * 0.19, 0.835, k, 7, MID)
            t(ax, 0.235 + i * 0.19, 0.775, v, 11, INK, "bold")
        box(ax, 0.22, 0.30, 0.74, 0.40)
        hdr = ["Group", "AI app", "Data rule", "Action", "Mode"]
        xs = [0.235, 0.36, 0.49, 0.67, 0.81]
        for x, h in zip(xs, hdr):
            t(ax, x, 0.665, h, 7.5, MID, "bold")
        rows = [["Engineering", "ChatGPT", "Secrets", "Block", "Enforce"],
                ["HR", "Gemini", "PII (Aadhaar, PAN)", "Redact", "Enforce"],
                ["Sales", "Any approved", "Customer data", "Warn", "Monitor"],
                ["All", "Unapproved", "Any", "Block", "Enforce"]]
        for r, row in enumerate(rows):
            for x, v in zip(xs, row):
                t(ax, x, 0.61 - r * 0.06, v, 7.5)
        btn(ax, 0.77, 0.32, 0.17, "+ New policy", True)
        t(ax, 0.235, 0.345, "Policy bundle v14 - signed - expires offline in 72 h", 7, MID)
        box(ax, 0.22, 0.04, 0.74, 0.22)
        t(ax, 0.235, 0.22, "Recent events (no prompt content stored)", 8, INK, "bold")
        t(ax, 0.235, 0.165, "10:42  meera@  HR  Gemini  PII redacted   [view metadata]", 7.5)
        t(ax, 0.235, 0.115, "10:31  dev12@  Eng  ChatGPT  API key blocked  [export]", 7.5)
        t(ax, 0.235, 0.065, "10:05  sales3@ Sales  Claude  warning overridden (reason given)", 7.5)
        save(fig, "wf_admin.png")


if __name__ == "__main__":
    wf_protect(); wf_optimize(); wf_admin()
    print("ok")
