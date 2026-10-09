# Cisco AI Sentinel: ISB PCPM Capstone

Product proposal for **Cisco AI Sentinel**, a browser-native layer that **governs, protects and optimises** how people use third-party AI tools (ChatGPT, Gemini, Claude, Copilot). Written as the capstone for the ISB Professional Certificate in Product Management, from the point of view of a VP of Product at Cisco.

**Author:** Shikhar Prakash

## Deliverables

| File | What it is |
|------|------------|
| `AI_Sentinel_Capstone_Report.docx` | Detailed write-up of all 10 capstone sections (about 26 pages), with charts, tables and sources |
| `AI_Sentinel_Capstone_Deck.pptx` | 18-slide executive deck for upper management (1–2 slides per section) |
| `Product_Idea.md` | Original product concept and strategy notes |
| `CapstoneWordTemplate (2).docx`, `ISB-PCPM-CapstonePowerpointTemplate.pptx` | Course templates the deliverables are built on |
| `build/` | Python scripts that generate the charts, wireframes, report and deck |

## The 10 sections

1. **Introduction:** Cisco overview, the AI Sentinel elevator pitch, the Govern / Protect / Optimize pillars
2. **Target market:** TAM $30B / SAM $2.9B / SOM $77M ARR (FY2029), competitor landscape, perceptual map, Ansoff matrix
3. **Timing:** Cisco as the third entrant; order-of-entry model (Urban et al., 1986) and how Cisco can offset the late-entry penalty
4. **Customers:** three personas, customer journey map, 5 interviews with an importance rating scale
5. **Product:** opportunity cost and development risk, product/company fit and product/market fit, 4Ps, three product levels, positioning, business model
6. **Concept testing:** lo-fi wireframes, 1-on-1 sessions with 3 participants, survey results and learnings
7. **MVP & PMF:** MVP scope, exit criteria, roadmap, PMF approach, AARRR growth experiments
8. **Product development:** Design Thinking combined with Agile (dual-track)
9. **Pricing:** freemium + value-based seats + metered usage; elasticity-based price changes
10. **GTM:** sales funnel by stage, the first 10 customers, scaling to hundreds

> **Note:** the interview and concept-test data in Sections 4 and 6 are illustrative placeholders, and the bottom-up market figures are the author's estimates. Market data, company figures and competitor facts come from public sources listed at the end of the report.

## Regenerating the files

Requires Python 3.9+.

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install python-docx python-pptx matplotlib pillow lxml
cd build
python charts.py        # charts -> build/img/
python wireframes.py    # lo-fi wireframes -> build/img/
python build_docx.py    # -> ../AI_Sentinel_Capstone_Report.docx
python build_deck.py    # -> ../AI_Sentinel_Capstone_Deck.pptx
```

Shared numbers such as market sizes, ratings and elasticity live in `build/sdata.py`. Report text is in `build/content_*.py` and slide layouts are in `build/deck_*.py`.

## Publishing to GitHub

Run `./push_to_github.sh`. It asks for a GitHub personal access token, creates the repository on your account (private by default) and pushes the project. The token is never saved to disk or to the git config.
