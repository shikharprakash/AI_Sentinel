"""Matplotlib charts for the Word report (deck uses native PowerPoint charts)."""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import sdata as N

OUT = os.path.join(os.path.dirname(__file__), "img")
os.makedirs(OUT, exist_ok=True)
c = lambda h: "#" + h
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10,
                     "axes.spines.top": False, "axes.spines.right": False,
                     "axes.edgecolor": "#B0B8BF", "axes.labelcolor": "#33414D",
                     "xtick.color": "#33414D", "ytick.color": "#33414D"})


def save(fig, name):
    fig.savefig(os.path.join(OUT, name), dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def market_growth():
    yrs, vals = N.shadow_series()
    fig, ax = plt.subplots(figsize=(6.4, 3.0))
    bars = ax.bar([str(y) for y in yrs], vals, color=c(N.BLUE), width=0.6)
    bars[0].set_color(c(N.NAVY)); bars[-1].set_color(c(N.NAVY))
    for b, v in zip(bars, vals):
        ax.text(b.get_x() + b.get_width() / 2, v + 0.15, f"${v:.2f}B", ha="center", fontsize=9)
    ax.set_ylabel("US$ billion"); ax.set_ylim(0, 10)
    ax.set_title("Shadow AI risk & governance market: 35.6% CAGR (2026-2032)", fontsize=11,
                 loc="left", color=c(N.NAVY), fontweight="bold")
    ax.grid(axis="y", color="#E5E9EC"); ax.set_axisbelow(True)
    save(fig, "market_growth.png")


def tam_sam_som():
    fig, ax = plt.subplots(figsize=(6.4, 3.0))
    ax.set_aspect("equal"); ax.axis("off")
    for r, col in [(1.0, N.SKY), (0.62, N.BLUE), (0.30, N.NAVY)]:
        ax.add_patch(Circle((0, -1 + r), r, color=c(col), ec="white", lw=2))
    rows = [(0.75, f"TAM  ${N.TAM:.1f}B", "Potential annual spend: ~300M enterprise GenAI seats\n+ ~150M individual power users (global)"),
            (0.05, f"SAM  ${N.SAM:.2f}B", "Cisco-reachable: ~25M mid-market seats (NA, EMEA,\nIndia) + ~20M India/English-speaking power users"),
            (-0.62, f"SOM  ${N.SOM:.0f}M ARR", "Year-3 (FY2029) obtainable: 0.75M seats + 0.4M\npaying individuals")]
    for y, head, sub in rows:
        ax.plot([0.15, 1.15], [y, y], color="#8A96A0", lw=0.8)
        ax.text(1.2, y + 0.06, head, fontsize=11, fontweight="bold", color=c(N.NAVY), va="bottom")
        ax.text(1.2, y + 0.02, sub, fontsize=7.5, color="#33414D", va="top")
    ax.set_xlim(-1.05, 3.6); ax.set_ylim(-1.05, 1.05)
    save(fig, "tam_sam_som.png")


def entry_share():
    base = N.entry_shares()
    adj = N.cisco_adjusted()[:3]
    labels = ["Pioneer\n(2023 start-ups)", "2nd entrant\n(platform vendor)", "Cisco\n(3rd entrant)"]
    fig, ax = plt.subplots(figsize=(6.4, 3.0))
    x = range(3)
    b1 = ax.bar([i - 0.18 for i in x], [v * 100 for v in base], 0.36, color=c(N.GREY), label="Order of entry only")
    b2 = ax.bar([i + 0.18 for i in x], [v * 100 for v in adj], 0.36, color=c(N.BLUE),
                label="With Cisco preference 1.2x & marketing 1.5x")
    for bars in (b1, b2):
        for b in bars:
            ax.text(b.get_x() + b.get_width() / 2, b.get_height() + 0.8, f"{b.get_height():.1f}%",
                    ha="center", fontsize=9)
    ax.set_xticks(list(x)); ax.set_xticklabels(labels)
    ax.set_ylabel("Long-run market share"); ax.set_ylim(0, 52)
    ax.legend(frameon=False, fontsize=8, loc="upper right")
    ax.set_title("Order-of-entry model (Urban et al., 1986)", loc="left", fontsize=11,
                 color=c(N.NAVY), fontweight="bold")
    save(fig, "entry_share.png")


def importance():
    rows = sorted(N.rating_table(), key=lambda d: d["mean"])
    fig, ax = plt.subplots(figsize=(6.4, 3.6))
    y = range(len(rows))
    ax.barh(list(y), [d["mean"] for d in rows], color=[c(N.NAVY) if d["mean"] >= 4.2 else c(N.BLUE) for d in rows])
    ax.scatter([d["ent"] for d in rows], list(y), marker="D", color=c(N.AMBER), zorder=3, s=22, label="Enterprise buyers (CISO, IT Mgr)")
    ax.scatter([d["ind"] for d in rows], list(y), marker="o", color=c(N.GREEN), zorder=3, s=22, label="Individuals (Dev, Freelancer)")
    for i, d in enumerate(rows):
        ax.text(0.08, i, f"{d['mean']:.1f}", va="center", color="white", fontsize=8, fontweight="bold")
    ax.set_yticks(list(y)); ax.set_yticklabels([d["short"] for d in rows])
    ax.set_xlim(0, 5.2); ax.set_xlabel("Mean importance (1 = not important, 5 = critical), n = 5")
    ax.legend(frameon=False, fontsize=8, loc="upper center", bbox_to_anchor=(0.45, -0.16), ncol=2)
    ax.set_title("Feature importance rating (illustrative data)", loc="left", fontsize=11,
                 color=c(N.NAVY), fontweight="bold")
    save(fig, "importance.png")


def perceptual_map():
    pts = [("AI Sentinel\n(Cisco)", 8.6, 8.2, N.BLUE, 260), ("Prisma Browser\n(Palo Alto)", 8.9, 3.0, N.GREY, 120),
           ("Island", 7.6, 2.5, N.GREY, 120), ("Prompt Security\n(SentinelOne)", 7.2, 4.0, N.GREY, 120),
           ("Harmonic", 6.2, 3.0, N.GREY, 120), ("MS Purview +\nEdge", 7.0, 5.4, N.GREY, 120),
           ("Zscaler / Netskope\nSSE", 8.1, 1.3, N.GREY, 120), ("PromptPerfect /\nAIPRM", 1.8, 7.6, N.GREY, 120),
           ("Native AI tool\nsettings", 3.0, 4.6, N.GREY, 120)]
    fig, ax = plt.subplots(figsize=(6.4, 4.0))
    ax.axhline(5, color="#C9D1D7", lw=1); ax.axvline(5, color="#C9D1D7", lw=1)
    for name, x, y, col, s in pts:
        ax.scatter(x, y, s=s, color=c(col), zorder=3)
        ax.annotate(name, (x, y), xytext=(7, -3), textcoords="offset points", fontsize=8,
                    color=c(N.NAVY) if col == N.BLUE else "#33414D",
                    fontweight="bold" if col == N.BLUE else "normal")
    ax.set_xlim(0, 11.2); ax.set_ylim(0, 10)
    ax.text(9.9, 9.6, "Target space", fontsize=8, color=c(N.BLUE), style="italic", ha="center")
    ax.set_xticks([]); ax.set_yticks([])
    ax.set_xlabel("Security & governance depth  →"); ax.set_ylabel("Productivity value to the user  →")
    ax.set_title("Perceptual map (author assessment, Oct 2026)", loc="left", fontsize=11,
                 color=c(N.NAVY), fontweight="bold")
    save(fig, "perceptual_map.png")


if __name__ == "__main__":
    market_growth(); tam_sam_som(); entry_share(); importance(); perceptual_map()
    print(sorted(os.listdir(OUT)))
