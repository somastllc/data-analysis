#!/usr/bin/env python3
"""Build a lesson's slide deck: 16:9 HTML, then PDF via WeasyPrint. DESIGN.md §7.

The deck is one slide per chip in that lesson's `**Shots:**` line in PRODUCTION.md,
with the diagram chip expanded to one slide per node (standing rule 7). The HTML is
self-contained — stylesheet and diagram SVGs are inlined — so it can be opened or
handed over on its own, the same way `samples/01-01-what-is-data.html` is.

    python3 tools/build_slides.py            # writes samples/01-01-what-is-data-slides.{html,pdf}
    python3 tools/build_slides.py --no-pdf   # HTML only, no .venv needed
"""
import html, pathlib, re, subprocess, sys, tempfile

import gen_diagram as gd

ROOT = pathlib.Path(__file__).resolve().parent.parent
TOOLS = ROOT / "tools"
OUT = ROOT / "samples"
WEASY = ROOT / ".venv" / "bin" / "weasyprint"


# ── slide helpers ───────────────────────────────────────────────────────────
def slide(body, ink=False, mid=False):
    cls = "slide" + (" ink" if ink else "") + (" mid" if mid else "")
    return f'<section class="{cls}">\n{body}\n</section>'


def table(headers, rows, term_col=True):
    th = "".join(f"<th>{html.escape(h)}</th>" for h in headers)
    out = [f'  <table>\n    <thead><tr>{th}</tr></thead>\n    <tbody>']
    for r in rows:
        cells = "".join(
            f'<td class="term">{c}</td>' if (term_col and i == 0) else f"<td>{c}</td>"
            for i, c in enumerate(r)
        )
        out.append(f"      <tr>{cells}</tr>")
    out.append("    </tbody>\n  </table>")
    return "\n".join(out)


def plate(title, inner, cap=None):
    tail = f'\n    <p class="plate-cap">{cap}</p>' if cap else ""
    return (f'  <div class="plate">\n'
            f'    <p class="plate-title">{html.escape(title)}</p>\n'
            f'    <div class="plate-body">{inner}</div>{tail}\n'
            f'  </div>')


def marks(items, two=False):
    """`literal — gloss` rows, the form the handout uses for the example list."""
    li = "\n".join(
        f'    <li>{lit}' + (f' <span class="what">— {g}</span>' if g else "") + "</li>"
        for lit, g in items)
    return f'  <ul class="marks{" two" if two else ""}">\n{li}\n  </ul>'


def build_frames(nodes, tmpdir, name, under=None, per_row=None):
    """One background-less SVG per beat, all on the same canvas so nothing shifts."""
    frames = []
    for n in range(1, len(nodes) + 1):
        p = tmpdir / f"{name}-build-{n}.svg"
        gd.svg(nodes, p, under=under, background=False, reveal=n, per_row=per_row)
        frames.append(p.read_text(encoding="utf-8"))
    return frames


# ── the deck: lesson 1.1, from its PRODUCTION.md shot list ──────────────────
# Shots: cold open -> title -> objective -> Data: raw facts -> table ->
#        diagram build (3) -> Where you see data every day -> end card
#
# Every word below is the lesson's own, copied from 01-what-is-data/01-what-is-data.md.
# Where a sentence appears here that is not in the Markdown, it is one the handout
# already added (samples/01-01-what-is-data.html) and it is marked as such.
def deck_01_01(frames):
    s = []

    # 1 - cold open. Standing rule 1: `## Overview` opens the video, said verbatim
    # before the title card. It is on screen because the deck is the thing being
    # screen-recorded; there is no separate camera to cut to. The whole paragraph
    # goes here, down to the question it ends on — which is the one the title card
    # answers, so no heading may be stacked on top of it.
    #
    # No eyebrow. "COLD OPEN" is a shot name — it belongs to PRODUCTION.md, not to
    # the frame the viewer sees. Rule 1 is that the video opens cold; labelling the
    # slide "cold open" is the on-screen equivalent of saying "hi, welcome back".
    s.append(slide(
        '  <p class="lead" style="max-width:50ch">You check your phone and see a mobile money\n'
        '     transfer of <code>$25</code>, a weather app showing <code>32&deg;C</code>, and a\n'
        '     message from school about your attendance. Each of those is a piece of data —\n'
        '     a small fact about something that happened. Before you analyze data, build\n'
        '     dashboards, or choose a career in data, you need a clear answer to a simple\n'
        '     question: <strong>what is data?</strong></p>',
        mid=True))

    # 2 - title card. Standing rule 3: the metadata block goes on screen, never read.
    s.append(slide(
        '  <p class="eyebrow">Chapter 1 — What Is Data?</p>\n'
        '  <h1>What Is Data?</h1>\n'
        '  <p class="mono" style="font-size:var(--t-data);color:var(--muted)">Lesson 1 of 5</p>',
        mid=True))

    # 3 - objective. Standing rule 2: the `**By the end:**` line, said at ~0:15.
    s.append(slide(
        '  <p class="eyebrow">By the end</p>\n'
        '  <div class="rule"></div>\n'
        '  <h2 style="max-width:30ch">You can explain what data is, and tell\n'
        '      <span class="accent">data</span>, <span class="accent">information</span> and\n'
        '      <span class="accent">insight</span> apart.</h2>'))

    # 4 - section 1, the definition
    s.append(slide(
        '  <p class="eyebrow">1 — Raw facts</p>\n'
        '  <h2>Data: raw facts about the world</h2>\n'
        '  <p class="lead wide"><strong>Data</strong> is a collection of facts, measurements,\n'
        '     or observations about the world. On its own, data usually does not tell a full\n'
        '     story. It is the raw material we use to understand what is happening.</p>'))

    # 5 - the five examples, in the handout's `literal — gloss` form
    s.append(slide(
        '  <p class="eyebrow">1 — Raw facts</p>\n'
        '  <h2>Examples of data</h2>\n'
        + marks([("$25", "a mobile money transfer amount"),
                 ("$2.50 per kg", "the market price of rice"),
                 ("present", "a student&rsquo;s attendance record"),
                 ("$49.99", "a product price"),
                 ("32&deg;C", "a temperature reading")])
        + '\n  <p style="margin-top:32rem;max-width:56ch">Each example is a single fact. By itself,\n'
          '     it may not mean much. But when we collect many facts together, patterns start\n'
          '     to appear.</p>'))

    # 6 - section 2, heading and table together. Standing rule 6: on screen as
    # written; read a row, then explain it. The heading and its one-line lead do
    # not earn a slide of their own — they are how you introduce the table.
    s.append(slide(
        '  <p class="eyebrow">2 — Not the same thing</p>\n'
        '  <h2 style="margin-bottom:16rem">Data vs information vs insight</h2>\n'
        '  <p style="max-width:56ch">These three terms are related, but they are not\n'
        '     the same.</p>\n'
        + table(["Term", "Meaning", "Example"], [
            ("Data", "Raw facts",
             "Sales were <code>$1,200</code>, <code>$980</code> and <code>$1,450</code> "
             "on three days"),
            ("Information", "Data organized to answer a basic question",
             "Sales increased from Monday to Wednesday"),
            ("Insight", "A useful conclusion that can guide action",
             "Promotions on Wednesday may be driving higher sales"),
        ])))

    # 7-9 - the diagram build. Standing rule 7: one node per beat, spoken as it lands.
    # PRODUCTION.md: build it straight out of the table above. So each beat carries that
    # row's own Meaning cell, word for word — same three words, same order.
    beats = ["Raw facts",
             "Data organized to answer a basic question",
             "A useful conclusion that can guide action"]
    # the closing caption is the handout's, held on the completed diagram
    cap = ("Each step throws information away and adds meaning. You cannot skip one: "
           "an insight with no data underneath it is just an opinion.")
    for i, (frame, beat) in enumerate(zip(frames, beats)):
        last = i == len(beats) - 1
        s.append(slide(
            '  <p class="eyebrow">2 — Not the same thing</p>\n'
            + plate("Plate I — from facts to a decision", frame, cap=cap if last else None)
            + f'\n  <p class="lead" style="margin-top:40rem">{beat}</p>'))

    # 10 - the cooking analogy. PRODUCTION.md: lands better spoken — give it a beat.
    s.append(slide(
        '  <p class="eyebrow">2 — Not the same thing</p>\n'
        '  <h2>Think of it like cooking</h2>\n'
        '  <div class="analogy">\n'
        '    <div><p class="k">Data</p><p class="v">The ingredients, before anyone has\n'
        '         decided what to make.</p></div>\n'
        '    <div><p class="k">Information</p><p class="v">A prepared meal you can actually\n'
        '         understand.</p></div>\n'
        '    <div><p class="k">Insight</p><p class="v">Knowing what to cook next time, based\n'
        '         on what people liked.</p></div>\n'
        '  </div>\n'
        '  <p class="lead" style="margin-top:48rem">In data work, your goal is to move from raw\n'
        '     data toward meaningful insight.</p>'))

    # 11 - section 3, whole. The list and the sentence that draws the conclusion
    # from it are one thought; splitting them puts a beat where the lesson has none.
    s.append(slide(
        '  <p class="eyebrow">3 — Every day</p>\n'
        '  <h2 style="margin-bottom:16rem">Where you see data every day</h2>\n'
        '  <p style="max-width:56ch">Data is not only found in spreadsheets or databases.\n'
        '     You create and use data constantly:</p>\n'
        + marks([("Mobile money transactions and bank transfers", None),
                 ("School grades and attendance records", None),
                 ("Market prices at a local shop", None),
                 ("Likes and comments on social media", None),
                 ("Steps tracked by a fitness app", None),
                 ("Weather forecasts", None)], two=True)
        + '\n  <p style="margin-top:24rem;max-width:64ch">Businesses, schools, hospitals and\n'
          '     governments all rely on data to make decisions. That is why data skills are\n'
          '     valuable across many industries.</p>'))

    # 12 - end card. Standing rule 4: held on screen, never narrated.
    s.append(slide(
        '  <p class="eyebrow">Key terms</p>\n'
        + table(["Term", "Definition"], [
            ("Data", "Raw facts, measurements, or observations"),
            ("Information", "Data that has been organized to convey meaning"),
            ("Insight", "A meaningful conclusion, supported by data, "
                        "that helps guide a decision"),
        ])))

    return s


# ── the deck: lesson 3.1, from its PRODUCTION.md shot list ──────────────────
# Shots: cold open -> title -> objective -> diagram build (7) ->
#        Start with the business problem -> Know your stakeholders ->
#        How to ask good analytical questions -> Example -> end card
def deck_03_01(frames):
    s = []

    # 1 - cold open, whole `## Overview` paragraph. No eyebrow: "cold open" is a
    # shot name, and the video opens cold — DESIGN.md §7.
    s.append(slide(
        '  <p class="lead" style="max-width:50ch">&ldquo;Can you look into the sales\n'
        '     data?&rdquo; is one of the most common requests an analyst receives, and it is\n'
        '     not yet a question. Answering it exactly as written is how a week disappears.</p>',
        mid=True))

    # 2 - title card
    s.append(slide(
        '  <p class="eyebrow">Chapter 3 — The Data Analysis Process</p>\n'
        '  <h1>Defining the Problem<br>and Asking Questions</h1>\n'
        '  <p class="mono" style="font-size:var(--t-data);color:var(--muted)">Lesson 1 of 6</p>',
        mid=True))

    # 3 - objective
    s.append(slide(
        '  <p class="eyebrow">By the end</p>\n'
        '  <div class="rule"></div>\n'
        '  <h2 style="max-width:30ch">You can turn a vague request into a\n'
        '      <span class="accent">specific analytical question</span>.</h2>'))

    # 4-10 - the diagram build, one stage per beat (standing rule 7). PRODUCTION.md:
    # "This is the map for the whole chapter." No per-beat caption — the lesson
    # glosses none of the seven stages, and inventing seven glosses would put words
    # on screen that the narration does not have. The diagram's own caption is baked
    # into the artwork and lands with the last node.
    for frame in frames:
        s.append(slide(
            '  <p class="eyebrow">The process</p>\n'
            + plate("Plate I — the data analysis process", frame)))

    # 11 - the business problem: the three questions to always ask
    s.append(slide(
        '  <p class="eyebrow">1 — The business problem</p>\n'
        '  <h2 style="margin-bottom:16rem">Start with the business problem</h2>\n'
        '  <p style="max-width:56ch">A common mistake is jumping straight into data\n'
        '     without knowing what you are trying to solve. Always begin by asking:</p>\n'
        + marks([("What problem are we trying to solve?", None),
                 ("Who cares about the answer?", None),
                 ("What decision will this analysis support?", None)])))

    # 12 - the two weak/strong pairs, written the way the lesson writes them. The
    # section heading repeats because this is still that section; inventing a second
    # heading ("Weak question, strong question") put words on screen the lesson does
    # not have, and the verbatim check caught it.
    s.append(slide(
        '  <p class="eyebrow">1 — The business problem</p>\n'
        '  <h2 style="margin-bottom:32rem">Start with the business problem</h2>\n'
        '  <div class="cols">\n'
        '    <div><p class="k">Example</p>\n'
        + marks([("Weak question: &ldquo;Let&rsquo;s analyze the sales data.&rdquo;", None),
                 ("Strong question: &ldquo;Why did sales drop in the North region "
                  "last quarter?&rdquo;", None)])
        + '\n    </div>\n'
          '    <div><p class="k">For a local shop, the same idea applies</p>\n'
        + marks([("Weak question: &ldquo;Let&rsquo;s look at the sales spreadsheet.&rdquo;", None),
                 ("Strong question: &ldquo;Why did rice sales drop in the last two weeks "
                  "compared to the month before?&rdquo;", None)])
        + '\n    </div>\n  </div>\n'
          '  <p style="margin-top:40rem;max-width:56ch">The stronger questions give analysis\n'
          '     a clear direction.</p>'))

    # 13 - stakeholders: who they are, and what knowing them buys you
    s.append(slide(
        '  <p class="eyebrow">2 — Stakeholders</p>\n'
        '  <h2 style="margin-bottom:16rem">Know your stakeholders</h2>\n'
        '  <p style="max-width:56ch">A <strong>stakeholder</strong> is anyone who needs the\n'
        '     results of your analysis.</p>\n'
        '  <div class="cols">\n'
        '    <div><p class="k">Examples</p>\n'
        + marks([("A manager deciding on marketing spend", None),
                 ("A product team improving an app feature", None),
                 ("A finance team reviewing budget performance", None)])
        + '\n    </div>\n'
          '    <div><p class="k">Understanding stakeholders helps you</p>\n'
        + marks([("Ask the right questions", None),
                 ("Choose relevant metrics", None),
                 ("Present results in a useful way", None)])
        + '\n    </div>\n  </div>'))

    # 14 - the four qualities, plus the lesson's own three examples
    s.append(slide(
        '  <p class="eyebrow">3 — Good questions</p>\n'
        '  <h2 style="margin-bottom:32rem">How to ask good analytical questions</h2>\n'
        '  <div class="cols">\n'
        '    <div><p class="k">Good questions are</p>\n'
        + marks([("Specific", "focused on one issue"),
                 ("Measurable", "answerable with data"),
                 ("Relevant", "connected to a real decision"),
                 ("Clear", "easy for others to understand")])
        + '\n    </div>\n'
          '    <div><p class="k">Examples</p>\n'
        + marks([("Which product category had the highest return rate last month?", None),
                 ("Are new customers more likely to cancel within 30 days?", None),
                 ("Which marketing channel brings the most qualified leads?", None)])
        + '\n    </div>\n  </div>'))

    # 15 - the worked example
    s.append(slide(
        '  <p class="eyebrow">4 — Worked example</p>\n'
        '  <h2 style="margin-bottom:16rem">An online course platform notices fewer\n'
        '      enrollments.</h2>\n'
        '  <div class="cols">\n'
        '    <div><p class="k">Stakeholders</p>\n'
        '      <p>marketing team and product manager</p>\n'
        '      <p class="k" style="margin-top:40rem">Problem</p>\n'
        '      <p>enrollment decline</p>\n'
        '    </div>\n'
        '    <div><p class="k">Questions</p>\n'
        + marks([("When did enrollments start dropping?", None),
                 ("Did the drop affect all courses or only some?", None),
                 ("Did traffic decrease, or did fewer visitors convert?", None)])
        + '\n    </div>\n  </div>'))

    # 16 - end card. Standing rule 4: held on screen, never narrated.
    s.append(slide(
        '  <p class="eyebrow">Key terms</p>\n'
        + table(["Term", "Definition"], [
            ("Business problem", "The issue or decision the analysis is meant to support"),
            ("Stakeholder", "A person or group affected by, or interested in, "
                            "the results of the analysis"),
            ("Analytical question", "A clear question that data can help answer"),
        ])))

    return s


def numbered(slides):
    """Stamp each slide with its frame number so it can be called during the shoot."""
    out = []
    for i, sl in enumerate(slides, 1):
        marker = f'  <p class="num">{i:02d} / {len(slides):02d}</p>\n'
        out.append(sl.replace("\n</section>", f"\n{marker}</section>"))
    return out


def verbatim_report(deck_html, sources):
    """Every text element on a slide must be the lesson's own words.

    The deck is what gets screen-recorded while the lesson is narrated, so a slide
    that paraphrases puts different words on screen and in the presenter's mouth.
    Only the eyebrows are ours — they are running heads, not content."""
    def norm(t):
        t = html.unescape(re.sub(r"<[^>]+>", " ", t))
        t = t.translate(str.maketrans({"’": "'", "‘": "'", "“": '"', "”": '"'}))
        t = re.sub(r"[*`]", "", t)          # Markdown emphasis and code ticks
        t = re.sub(r"\s+([,.;:?!])", r"\1", t)   # a stripped inline tag leaves a gap
        return re.sub(r"\s+", " ", t).strip()

    corpus = [norm(p.read_text(encoding="utf-8")) for p in sources]
    body = deck_html.split("</style>", 1)[1]
    chrome = re.compile(r"^(\d+ / \d+|Lesson \d+ of \d+)$")
    # Furniture, not content: the running head and the plate's own label. Both name
    # the frame rather than say anything, the same way a figure number does.
    furniture = ("eyebrow", "plate-title", 'class="k"', "num")

    checked, strays = 0, []
    for tag, attrs, inner in re.findall(r"<(h1|h2|p|li|td)\b([^>]*)>(.*?)</\1>", body, re.S):
        txt = norm(inner)
        if (not txt or chrome.match(txt) or len(txt.split()) < 2
                or any(f in attrs for f in furniture)):
            continue
        checked += 1
        if not any(txt in c for c in corpus):
            strays.append((tag, txt))
    return checked, strays


def page(title, slides):
    css = (TOOLS / "slides.css").read_text(encoding="utf-8")
    return ("<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n"
            f"<title>{html.escape(title)}</title>\n<style>\n{css}</style>\n</head>\n<body>\n"
            + "\n".join(numbered(slides))
            + "\n</body>\n</html>\n")


# ── the decks that exist, and what each one is checked against ──────────────
# `sources` is the corpus verbatim_report matches every slide's text against: the
# lesson Markdown always, plus the handout where one exists (it carries a few lines
# the Markdown does not, and those are the handout's, not ours).
DECKS = {
    "01-01": dict(
        build=deck_01_01,
        title="What Is Data? — slides",
        out="01-01-what-is-data-slides.html",
        nodes=["Data", "Information", "Insight"],
        diagram="01-01-data-to-insight", caption=None,
        sources=["01-what-is-data/01-what-is-data.md",
                 "samples/01-01-what-is-data.html"],
    ),
    "03-01": dict(
        build=deck_03_01,
        title="Defining the Problem and Asking Questions — slides",
        out="03-01-defining-the-problem-slides.html",
        nodes=["Define\nproblem", "Ask\nquestions", "Collect data", "Clean data",
               "Analyze and\nvisualize", "Communicate\ninsights", "Make\ndecisions"],
        diagram="03-01-analysis-process", per_row=4,
        caption="every stage depends on the question you asked first",
        sources=["03-the-data-analysis-process/"
                 "01-defining-the-problem-and-asking-questions.md"],
    ),
}


def build_deck(key):
    d = DECKS[key]
    # The build frames are inlined into the HTML, so they are intermediate — they
    # do not belong beside the deck in samples/.
    with tempfile.TemporaryDirectory() as tmp:
        frames = build_frames(d["nodes"], pathlib.Path(tmp), d["diagram"],
                              under=d.get("caption"), per_row=d.get("per_row"))

    slides = d["build"](frames)
    dst_html = OUT / d["out"]
    markup = page(d["title"], slides)
    dst_html.write_text(markup, encoding="utf-8")

    words = sum(len(re.findall(r"[A-Za-z0-9$°.,%]+", re.sub(r"<[^>]+>", " ", s)))
                for s in slides)
    print(f"{key}: {len(slides)} slides · 1920×1080 · ~{words // len(slides)} words/slide avg")

    checked, strays = verbatim_report(markup, [ROOT / p for p in d["sources"]])
    print(f"  verbatim: {checked - len(strays)}/{checked} text elements "
          f"are the lesson's own words")
    for tag, txt in strays:
        print(f"    paraphrased <{tag}>: {txt[:84]}")
    print(f"  {dst_html.relative_to(ROOT)}")

    if "--no-pdf" not in sys.argv:
        if not WEASY.exists():
            sys.exit("no .venv — python3 -m venv .venv && .venv/bin/pip install weasyprint")
        dst_pdf = dst_html.with_suffix(".pdf")
        subprocess.run([str(WEASY), str(dst_html), str(dst_pdf)], check=True)
        print(f"  {dst_pdf.relative_to(ROOT)}")


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    keys = [a for a in sys.argv[1:] if a in DECKS] or list(DECKS)
    for k in keys:
        build_deck(k)
