"""
Roots of Polynomials: From Quadratics to Quartics, and the Birth of Vieta's Formula
Manim Community Edition — Cinematic Mathematics Series

Run with:
    manim -qh vietas_formula.py FullVideo
Or individual scenes:
    manim -qh vietas_formula.py Scene1Hook
"""

from manim import *
import numpy as np

# ─────────────────────────────────────────────
#  GLOBAL STYLE CONSTANTS
# ─────────────────────────────────────────────
GOLD      = "#FFD700"
BLUE_CLR  = "#5BA4CF"
GREEN_CLR = "#50C878"
RED_CLR   = "#FF6B6B"
WHITE_CLR = WHITE
GRAY_CLR  = "#AAAAAA"
DIM_GRAY  = "#555555"
BG        = BLACK

# ─────────────────────────────────────────────
#  REUSABLE HELPERS
# ─────────────────────────────────────────────

def glow_tex(tex_str, color=WHITE, scale=1.0, **kwargs):
    """Return a MathTex with a subtle glow using a colored backdrop."""
    obj = MathTex(tex_str, color=color, **kwargs).scale(scale)
    return obj


def section_title(text, color=GOLD):
    return Text(text, font="Georgia", color=color).scale(0.65)


def rule_line(width=10, color=DIM_GRAY):
    return Line(LEFT * width / 2, RIGHT * width / 2, color=color, stroke_width=1)


def glowing_underline(mob, color=GOLD):
    ul = Underline(mob, color=color, stroke_width=3)
    return ul


def coefficient_box(mob, color=GOLD):
    return SurroundingRectangle(mob, color=color, buff=0.12, corner_radius=0.08,
                                stroke_width=2)


# ─────────────────────────────────────────────
#  SCENE 1 — CINEMATIC HOOK
# ─────────────────────────────────────────────

class Scene1Hook(Scene):
    def construct(self):
        self.camera.background_color = BG

        # ── Darkness + first equation ──────────────────────
        general_poly = MathTex(
            r"ax^n + bx^{n-1} + \cdots + k = 0",
            color=WHITE
        ).scale(1.1)
        general_poly.move_to(UP * 0.5)

        self.play(FadeIn(general_poly, run_time=2.5, rate_func=slow_into))
        self.wait(1.2)

        # ── Roots appear one by one ────────────────────────
        roots_label = MathTex(r"\alpha,\; \beta,\; \gamma,\; \delta",
                               color=GREEN_CLR).scale(0.95)
        roots_label.next_to(general_poly, DOWN, buff=0.7)

        for i, part in enumerate(roots_label):
            self.play(Write(part), run_time=0.5)
            self.wait(0.15)
        self.wait(0.8)

        # ── Morph to factored form ─────────────────────────
        factored = MathTex(
            r"(x-\alpha)(x-\beta)(x-\gamma)(x-\delta) = 0",
            color=GOLD
        ).scale(1.0)
        factored.move_to(DOWN * 1.2)

        self.play(
            LaggedStart(
                FadeOut(roots_label, shift=UP * 0.3),
                TransformMatchingShapes(general_poly.copy(), factored),
                lag_ratio=0.3
            ),
            run_time=2.0
        )
        self.play(
            general_poly.animate.set_color(GRAY_CLR).scale(0.8).shift(UP * 0.4),
            run_time=1.0
        )
        self.wait(0.5)

        # ── Circumscribe the factored form ─────────────────
        self.play(Circumscribe(factored, color=GOLD, run_time=1.5, fade_out=True))
        self.wait(1.5)

        # ── Narration text ─────────────────────────────────
        line1 = Text("Hidden inside every polynomial is a secret structure (lol).",
                     font="Georgia", color=GRAY_CLR).scale(0.42)
        line2 = Text("A structure connecting roots… coefficients… symmetry… and algebra itself. (Vieta's Formula basically)",
                     font="Georgia", color=GRAY_CLR).scale(0.38)
        line3 = Text("Today, we uncover that structure. (Other word for lecture)",
                     font="Georgia", color=WHITE).scale(0.45)

        narration = VGroup(line1, line2, line3).arrange(DOWN, buff=0.3)
        narration.to_edge(DOWN, buff=0.55)

        self.play(FadeIn(line1, shift=UP * 0.1), run_time=1.2)
        self.wait(0.5)
        self.play(FadeIn(line2, shift=UP * 0.1), run_time=1.2)
        self.wait(0.8)
        self.play(FadeIn(line3, shift=UP * 0.1), run_time=1.2)
        self.wait(2.5)

        self.play(FadeOut(VGroup(general_poly, factored, narration)), run_time=1.5)
        self.wait(0.5)


# ─────────────────────────────────────────────
#  SCENE 2 — WHAT IS A ROOT?
# ─────────────────────────────────────────────

class Scene2WhatIsARoot(Scene):
    def construct(self):
        self.camera.background_color = BG

        # ── Title ──────────────────────────────────────────
        title = section_title("What Is a Root?")
        title.to_edge(UP, buff=0.4)
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=1.0)
        self.wait(0.3)
        self.play(Create(rule_line().next_to(title, DOWN, buff=0.15)), run_time=0.8)
        self.wait(0.5)

        # ── Graph ──────────────────────────────────────────
        axes = Axes(
            x_range=[-3.5, 3.5, 1],
            y_range=[-4, 6, 2],
            x_length=7,
            y_length=4.5,
            axis_config={"color": GRAY_CLR, "stroke_width": 1.5,
                         "include_tip": True, "tip_length": 0.15},
        ).shift(DOWN * 0.3)

        def poly(x):
            return (x + 2) * (x - 0.5) * (x - 2.5) * 0.5 + 0.3

        curve = axes.plot(poly, color=BLUE_CLR, stroke_width=2.5)

        self.play(Create(axes), run_time=1.2)
        self.play(Create(curve), run_time=1.5)
        self.wait(0.5)

        # ── f(x) = 0 ──────────────────────────────────────
        fx0 = MathTex(r"f(x) = 0", color=WHITE).scale(0.85)
        fx0.to_edge(RIGHT, buff=1.2).shift(UP * 1.5)
        self.play(Write(fx0), run_time=1.0)

        # ── Roots light up ─────────────────────────────────
        root_xs = [-2.0, 0.5, 2.5]
        root_labels = [r"\alpha", r"\beta", r"\gamma"]
        root_colors = [GREEN_CLR, GREEN_CLR, GREEN_CLR]
        dots = VGroup()
        dot_labels = VGroup()

        for rx, rl, rc in zip(root_xs, root_labels, root_colors):
            pt = axes.c2p(rx, 0)
            dot = Dot(pt, color=rc, radius=0.1)
            lbl = MathTex(rl, color=rc).scale(0.7).next_to(dot, DOWN, buff=0.2)
            dots.add(dot)
            dot_labels.add(lbl)

            self.play(
                Flash(pt, color=rc, flash_radius=0.25, line_stroke_width=2, run_time=0.4),
                FadeIn(dot, scale=0.5),
                Write(lbl),
                run_time=0.7
            )
            self.wait(0.2)

        self.wait(0.8)

        # ── f(alpha) = 0 ───────────────────────────────────
        fa0 = MathTex(r"f(\alpha) = 0", color=GREEN_CLR).scale(0.85)
        fa0.next_to(fx0, DOWN, buff=0.4)
        self.play(TransformMatchingShapes(fx0.copy(), fa0), run_time=1.2)
        self.wait(0.5)

        # ── Factor theorem ─────────────────────────────────
        factor_thm = MathTex(
            r"(x - \alpha)", r"\text{ divides }", r"f(x)",
            color=WHITE
        ).scale(0.8)
        factor_thm.next_to(fa0, DOWN, buff=0.5)
        self.play(Write(factor_thm), run_time=1.2)

        box = coefficient_box(factor_thm[0], color=GREEN_CLR)
        self.play(Create(box), run_time=0.8)
        self.wait(1.0)

        # ── Show factored form below ───────────────────────
        factored = MathTex(
            r"f(x) = (x-\alpha)(x-\beta)(x-\gamma)\cdots",
            color=GOLD
        ).scale(0.85)
        factored.to_edge(DOWN, buff=0.7)
        self.play(
            FadeOut(VGroup(box, factor_thm)),
            Write(factored),
            run_time=1.5
        )
        self.wait(2.0)

        self.play(FadeOut(VGroup(axes, curve, dots, dot_labels, fx0, fa0, factored, title)),
                  run_time=1.2)


# ─────────────────────────────────────────────
#  SCENE 3 — QUADRATIC EQUATIONS
# ─────────────────────────────────────────────

class Scene3Quadratic(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = section_title("The Quadratic")
        title.to_edge(UP, buff=0.4)
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.8)
        self.play(Create(rule_line().next_to(title, DOWN, buff=0.15)), run_time=0.6)

        # ── Start with ax^2 + bx + c = 0 ──────────────────
        eq1 = MathTex(r"ax^2 + bx + c = 0", color=WHITE).scale(1.1)
        eq1.move_to(UP * 1.5)
        self.play(Write(eq1), run_time=1.2)
        self.wait(0.8)

        # ── Normalize ─────────────────────────────────────
        eq2 = MathTex(
            r"x^2 + \frac{b}{a}x + \frac{c}{a} = 0",
            color=WHITE
        ).scale(1.0)
        eq2.move_to(UP * 1.5)

        divide_note = Text("÷ a", font="Georgia", color=BLUE_CLR).scale(0.45)
        divide_note.next_to(eq1, RIGHT, buff=0.5)
        self.play(FadeIn(divide_note, shift=LEFT * 0.2), run_time=0.5)
        self.play(TransformMatchingShapes(eq1, eq2), run_time=1.5)
        self.play(FadeOut(divide_note), run_time=0.4)
        self.wait(0.8)

        # ── Introduce roots ────────────────────────────────
        roots_intro = MathTex(r"\text{Let } \alpha, \beta \text{ be the roots.}",
                               color=GREEN_CLR).scale(0.8)
        roots_intro.move_to(UP * 0.4)
        self.play(FadeIn(roots_intro, shift=UP * 0.1), run_time=1.0)
        self.wait(0.5)

        # ── Factored form ─────────────────────────────────
        factored = MathTex(
            r"(x - \alpha)(x - \beta) = 0",
            color=GREEN_CLR
        ).scale(1.0)
        factored.move_to(DOWN * 0.3)
        self.play(Write(factored), run_time=1.2)
        self.wait(0.8)

        # ── Expand ────────────────────────────────────────
        expanded = MathTex(
            r"x^2",
            r"- (\alpha + \beta)x",
            r"+ \alpha\beta",
            r"= 0",
            color=WHITE
        ).scale(1.0)
        expanded.move_to(DOWN * 1.5)

        self.play(
            TransformMatchingShapes(factored.copy(), expanded),
            run_time=1.8
        )
        self.wait(0.5)

        # ── Color the symmetric parts ──────────────────────
        self.play(
            expanded[1].animate.set_color(BLUE_CLR),
            run_time=0.6
        )
        self.play(
            expanded[2].animate.set_color(RED_CLR),
            run_time=0.6
        )
        self.wait(1.0)

        # ── Side-by-side comparison ────────────────────────
        self.play(
            FadeOut(VGroup(roots_intro, factored)),
            eq2.animate.move_to(UP * 2.3).scale(0.85),
            expanded.animate.move_to(UP * 1.4).scale(0.85),
            run_time=1.2
        )

        arrow = MathTex(r"\Updownarrow", color=GRAY_CLR).scale(0.9)
        arrow.move_to(UP * 1.85)
        self.play(Write(arrow), run_time=0.5)
        self.wait(0.5)

        # ── Vieta's for quadratic ─────────────────────────
        v1 = MathTex(
            r"\alpha + \beta = -\frac{b}{a}",
            color=GOLD
        ).scale(1.05)
        v2 = MathTex(
            r"\alpha\beta = \frac{c}{a}",
            color=GOLD
        ).scale(1.05)

        vieta_group = VGroup(v1, v2).arrange(RIGHT, buff=1.2)
        vieta_group.move_to(DOWN * 1.0)

        self.play(Write(v1), run_time=1.2)
        self.wait(0.3)
        self.play(Write(v2), run_time=1.2)
        self.wait(0.5)

        # ── Glow on vieta ──────────────────────────────────
        for v in [v1, v2]:
            box = coefficient_box(v, GOLD)
            self.play(Create(box), run_time=0.6)
            self.play(Flash(v.get_center(), color=GOLD,
                            flash_radius=0.6, line_stroke_width=2,
                            num_lines=10, run_time=0.5))
            self.wait(0.2)

        self.wait(2.0)
        self.play(FadeOut(Group(*self.mobjects)), run_time=1.2)


# ─────────────────────────────────────────────
#  SCENE 4 — VIETA'S FORMULA (CONCEPTUAL)
# ─────────────────────────────────────────────

class Scene4VietaQuadratic(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = section_title("Vieta's Formula — Quadratic")
        title.to_edge(UP, buff=0.4)
        self.play(FadeIn(title), run_time=0.8)
        self.play(Create(rule_line().next_to(title, DOWN, buff=0.15)), run_time=0.6)

        # ── Two roots orbiting ─────────────────────────────
        note = Text(
            'The polynomial only "remembers" symmetric combinations of its roots.',
            font="Georgia",
            color=GRAY_CLR
        ).scale(0.38)

        note.move_to(UP * 1.6)

        self.play(FadeIn(note, shift=UP * 0.1), run_time=1.2)
        self.wait(0.8)

        # ── α, β swapping ─────────────────────────────────
        alpha = MathTex(r"\alpha", color=GREEN_CLR).scale(1.3)
        beta  = MathTex(r"\beta",  color=GREEN_CLR).scale(1.3)
        alpha.move_to(LEFT * 2)
        beta.move_to(RIGHT * 2)

        self.play(FadeIn(alpha, scale=0.7), FadeIn(beta, scale=0.7), run_time=0.8)

        plus_sym  = MathTex(r"\alpha + \beta",   color=BLUE_CLR).scale(1.0)
        times_sym = MathTex(r"\alpha\beta",       color=RED_CLR ).scale(1.0)
        plus_sym.move_to(DOWN * 0.5 + LEFT * 2.5)
        times_sym.move_to(DOWN * 0.5 + RIGHT * 2.5)

        self.play(Write(plus_sym), Write(times_sym), run_time=1.0)
        self.wait(0.5)

        # ── Swap α and β ──────────────────────────────────
        swap_arrow = CurvedArrow(alpha.get_top(), beta.get_top(),
                                 color=GRAY_CLR, angle=-PI / 2)
        swap_lbl = Text("swap", font="Georgia", color=GRAY_CLR).scale(0.35)
        swap_lbl.next_to(swap_arrow, UP, buff=0.15)

        self.play(Create(swap_arrow), FadeIn(swap_lbl), run_time=0.8)
        self.play(
            alpha.animate.move_to(RIGHT * 2),
            beta.animate.move_to(LEFT * 2),
            run_time=1.2,
            rate_func=smooth
        )
        self.wait(0.4)

        # ── Symmetric formulas unchanged ───────────────────
        unchanged = Text("…coefficients unchanged ✓",
                         font="Georgia", color=GOLD).scale(0.42)
        unchanged.move_to(DOWN * 1.6)
        self.play(FadeIn(unchanged, shift=UP * 0.1), run_time=0.8)
        self.wait(1.0)

        # ── Symmetry visual ───────────────────────────────
        sym_note = MathTex(
            r"\alpha + \beta = \beta + \alpha, \quad"
            r"\alpha\beta = \beta\alpha",
            color=GRAY_CLR
        ).scale(0.8)
        sym_note.move_to(DOWN * 2.5)
        self.play(Write(sym_note), run_time=1.2)
        self.wait(2.0)

        self.play(FadeOut(Group(*self.mobjects)), run_time=1.2)


# ─────────────────────────────────────────────
#  SCENE 5 — CUBIC POLYNOMIALS
# ─────────────────────────────────────────────

class Scene5Cubic(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = section_title("The Cubic")
        title.to_edge(UP, buff=0.4)
        self.play(FadeIn(title), run_time=0.8)
        self.play(Create(rule_line().next_to(title, DOWN, buff=0.15)), run_time=0.6)

        # ── Cubic equation ─────────────────────────────────
        cubic = MathTex(
            r"ax^3 + bx^2 + cx + d = 0",
            color=WHITE
        ).scale(1.0)
        cubic.move_to(UP * 2.0)
        self.play(Write(cubic), run_time=1.2)
        self.wait(0.6)

        roots_note = MathTex(r"\text{Roots: } \alpha, \beta, \gamma",
                              color=GREEN_CLR).scale(0.85)
        roots_note.next_to(cubic, DOWN, buff=0.5)
        self.play(Write(roots_note), run_time=0.9)
        self.wait(0.5)

        # ── Factored form ─────────────────────────────────
        factored = MathTex(
            r"a(x-\alpha)(x-\beta)(x-\gamma) = 0",
            color=GREEN_CLR
        ).scale(0.95)
        factored.next_to(roots_note, DOWN, buff=0.5)
        self.play(TransformMatchingShapes(roots_note.copy(), factored), run_time=1.5)
        self.wait(0.6)

        # ── Expand step by step ───────────────────────────
        step1 = MathTex(
            r"(x-\alpha)(x-\beta)",
            r"= x^2 - (\alpha+\beta)x + \alpha\beta",
            color=WHITE
        ).scale(0.78)
        step1.next_to(factored, DOWN, buff=0.45)
        self.play(Write(step1), run_time=1.4)
        self.wait(0.5)

        step2 = MathTex(
            r"\Rightarrow\; x^3",
            r"- (\alpha+\beta+\gamma)x^2",
            r"+ (\alpha\beta+\beta\gamma+\gamma\alpha)x",
            r"- \alpha\beta\gamma",
            color=WHITE
        ).scale(0.75)
        step2.next_to(step1, DOWN, buff=0.4)

        self.play(Write(step2[0]), run_time=0.6)
        self.play(step2[1].animate.set_color(BLUE_CLR), Write(step2[1]), run_time=0.9)
        self.play(step2[2].animate.set_color(RED_CLR),  Write(step2[2]), run_time=0.9)
        self.play(step2[3].animate.set_color(GREEN_CLR), Write(step2[3]), run_time=0.9)
        self.wait(1.0)

        # ── Reveal Vieta's for cubic ───────────────────────
        self.play(
            FadeOut(VGroup(roots_note, factored, step1, step2)),
            cubic.animate.move_to(UP * 2.7).scale(0.85),
            run_time=1.0
        )

        v1 = MathTex(r"\alpha+\beta+\gamma = -\dfrac{b}{a}",
                     color=GOLD).scale(0.95)
        v2 = MathTex(r"\alpha\beta+\beta\gamma+\gamma\alpha = \dfrac{c}{a}",
                     color=GOLD).scale(0.95)
        v3 = MathTex(r"\alpha\beta\gamma = -\dfrac{d}{a}",
                     color=GOLD).scale(0.95)

        vgroup = VGroup(v1, v2, v3).arrange(DOWN, buff=0.55)
        vgroup.move_to(DOWN * 0.3)

        for v in vgroup:
            self.play(Write(v), run_time=1.0)
            self.wait(0.25)

        # ── Boxes ─────────────────────────────────────────
        for v in vgroup:
            self.play(Create(coefficient_box(v, GOLD)), run_time=0.5)

        self.wait(2.5)
        self.play(FadeOut(Group(*self.mobjects)), run_time=1.2)


# ─────────────────────────────────────────────
#  SCENE 6 — PATTERN RECOGNITION TABLE
# ─────────────────────────────────────────────

class Scene6PatternTable(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = section_title("The Pattern Emerges")
        title.to_edge(UP, buff=0.4)
        self.play(FadeIn(title), run_time=0.8)
        self.play(Create(rule_line().next_to(title, DOWN, buff=0.15)), run_time=0.6)

        whisper = Text('"The polynomial is hiding a pattern. Notice that:"',
                       font="Georgia", color=GRAY_CLR).scale(0.42)
        whisper.next_to(title, DOWN, buff=0.55)
        self.play(FadeIn(whisper, shift=UP * 0.1), run_time=1.2)
        self.wait(1.0)

        # ── Build comparison table ─────────────────────────
        headers = VGroup(
            Text("", font="Georgia", color=GOLD).scale(0.5),
            Text("Quadratic", font="Georgia", color=BLUE_CLR).scale(0.5),
            Text("Cubic", font="Georgia", color=RED_CLR).scale(0.5),
        ).arrange(RIGHT, buff=1.8)
        headers.move_to(UP * 1.3)
        self.play(Write(headers), run_time=0.9)

        row_labels = ["Sum of roots", "Pairwise products", "Triple product"]
        quad_vals  = [
            r"-\frac{b}{a}",
            r"\frac{c}{a}",
            r"\text{—}",
        ]
        cubic_vals = [
            r"-\frac{b}{a}",
            r"\frac{c}{a}",
            r"-\frac{d}{a}",
        ]

        rows = VGroup()

        for i, (lbl, qv, cv) in enumerate(zip(row_labels, quad_vals, cubic_vals)):
            lbl_t = Text(lbl, font="Georgia", color=GRAY_CLR).scale(0.4)
            q_t   = MathTex(qv, color=BLUE_CLR).scale(0.75)
            c_t   = MathTex(cv, color=RED_CLR).scale(0.75)

            y_pos = 0.3 - i * 0.75

            lbl_t.move_to(LEFT * 3.8 + UP * y_pos)
            q_t.move_to(LEFT * 0.3 + UP * y_pos)
            c_t.move_to(RIGHT * 3.0 + UP * y_pos)

            row = VGroup(lbl_t, q_t, c_t)
            rows.add(row)

        self.play(LaggedStart(*[FadeIn(r) for r in rows], lag_ratio=0.3))
        self.wait(1)

        # ── Highlight matching structures ──────────────────
        arrows = VGroup(
            Arrow(rows[0][1].get_right(), rows[0][2].get_left(),
                  color=GOLD, buff=0.1, stroke_width=2),
            Arrow(rows[1][1].get_right(), rows[1][2].get_left(),
                  color=GOLD, buff=0.1, stroke_width=2),
        )
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.4),
                  run_time=1.0)
        self.wait(0.5)

        # ── Sign alternation note ──────────────────────────
        alt_note = Text("Alternating signs: −, +, −, +, …",
                        font="Georgia", color=GOLD).scale(0.42)
        alt_note.to_edge(DOWN, buff=0.8)
        self.play(FadeIn(alt_note, shift=UP * 0.1), run_time=0.9)
        self.wait(2.0)

        self.play(FadeOut(Group(*self.mobjects)), run_time=1.2)


# ─────────────────────────────────────────────
#  SCENE 7 — QUARTIC POLYNOMIALS
# ─────────────────────────────────────────────

class Scene7Quartic(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = section_title("The Quartic")
        title.to_edge(UP, buff=0.4)
        self.play(FadeIn(title), run_time=0.8)
        self.play(Create(rule_line().next_to(title, DOWN, buff=0.15)), run_time=0.6)

        quartic = MathTex(
            r"ax^4+bx^3+cx^2+dx+e=0", color=WHITE
        ).scale(0.95)
        quartic.move_to(UP * 2.0)
        self.play(Write(quartic), run_time=1.2)

        roots_note = MathTex(r"\text{Roots: } \alpha, \beta, \gamma, \delta",
                              color=GREEN_CLR).scale(0.70)
        roots_note.next_to(quartic, DOWN, buff=0.4)
        self.play(Write(roots_note), run_time=0.8)
        self.wait(0.5)

        factored = MathTex(
            r"a(x-\alpha)(x-\beta)(x-\gamma)(x-\delta)=0",
            color=GREEN_CLR
        ).scale(0.70)
        factored.next_to(roots_note, DOWN, buff=0.4)
        self.play(Write(factored), run_time=1.2)
        self.wait(0.8)

        # ── Layered expansion reveal ───────────────────────
        self.play(FadeOut(VGroup(roots_note, factored)), run_time=0.8)

        combos = [
            (r"\text{Sum:} \quad \alpha+\beta+\gamma+\delta", BLUE_CLR,
             r"= -\dfrac{b}{a}"),
            (r"\text{Pairwise:} \quad \textstyle\sum\alpha\beta", RED_CLR,
             r"= \dfrac{c}{a}"),
            (r"\text{Triple:} \quad \textstyle\sum\alpha\beta\gamma", "#FF9F43",
             r"= -\dfrac{d}{a}"),
            (r"\text{Product:} \quad \alpha\beta\gamma\delta", GOLD,
             r"= \dfrac{e}{a}"),
        ]

        all_lines = VGroup()
        for i, (lhs, col, rhs) in enumerate(combos):
            lhs_t = MathTex(lhs, color=col).scale(0.78)
            rhs_t = MathTex(rhs, color=GOLD).scale(0.78)
            line  = VGroup(lhs_t, rhs_t).arrange(RIGHT, buff=0.3)
            line.move_to(UP * (0.8 - i * 0.72))
            all_lines.add(line)

            self.play(Write(lhs_t), run_time=0.8)
            self.play(Write(rhs_t), run_time=0.6)
            box = coefficient_box(rhs_t, GOLD)
            self.play(Create(box), run_time=0.4)
            self.wait(0.2)

        self.wait(2.0)
        self.play(FadeOut(Group(*self.mobjects)), run_time=1.2)


# ─────────────────────────────────────────────
#  SCENE 8 — GENERAL VIETA'S FORMULA (CLIMAX)
# ─────────────────────────────────────────────

class Scene8GeneralVieta(Scene):
    def construct(self):
        self.camera.background_color = BG

        # ── Build up to climax ─────────────────────────────
        climax_text = Text("The General Form", font="Georgia", color=GOLD).scale(0.75)
        climax_text.move_to(UP * 3.0)
        self.play(FadeIn(climax_text, scale=1.2), run_time=1.5)
        self.wait(0.5)
        self.play(Create(rule_line().next_to(climax_text, DOWN, buff=0.15)), run_time=0.6)

        gen_poly = MathTex(
            r"a_n x^n + a_{n-1}x^{n-1} + \cdots + a_1 x + a_0 = 0",
            color=WHITE
        ).scale(0.9)
        gen_poly.move_to(UP * 1.9)
        self.play(Write(gen_poly), run_time=1.5)
        self.wait(0.5)

        factored = MathTex(
            r"a_n (x-r_1)(x-r_2)\cdots(x-r_n) = 0",
            color=GREEN_CLR
        ).scale(0.9)
        factored.next_to(gen_poly, DOWN, buff=0.5)
        self.play(TransformMatchingShapes(gen_poly.copy(), factored), run_time=1.8)
        self.wait(1.0)

        # ── Vieta's formula formal statement ──────────────
        vieta_title = Text("Vieta's Formulas", font="Georgia", color=GOLD).scale(0.6)
        vieta_title.next_to(factored, DOWN, buff=0.3).shift(UP * 0.2)
        self.play(Write(vieta_title), run_time=0.8)

        vieta1 = MathTex(
            r"\sum_{i=1}^{n} r_i",
            r"= -\frac{a_{n-1}}{a_n}",
            color=GOLD
        ).scale(0.68)

        vieta2 = MathTex(
            r"\sum_{1\le i<j\le n} r_i r_j",
            r"= \frac{a_{n-2}}{a_n}",
            color=GOLD
        ).scale(0.68)

        vieta3 = MathTex(
            r"r_1 r_2 \cdots r_n",
            r"= (-1)^n\frac{a_0}{a_n}",
            color=GOLD
        ).scale(0.68)

        vg = VGroup(vieta1, vieta2, vieta3).arrange(DOWN, buff=0.5)
        vg.next_to(vieta_title, DOWN, buff=0.5).shift(DOWN * 0.2)

        for v in vg:
            self.play(Write(v), run_time=1.0)
            self.wait(0.2)

        # ── Big glow box around all vieta ─────────────────
        big_box = SurroundingRectangle(vg, color=GOLD, buff=0.35,
                                       corner_radius=0.12, stroke_width=2.5)
        self.play(Create(big_box), run_time=1.0)

        for v in vg:
            self.play(Flash(v.get_center(), color=GOLD,
                            flash_radius=0.5, line_stroke_width=2,
                            num_lines=8, run_time=0.4))

        self.wait(3.0)
        self.play(FadeOut(Group(*self.mobjects)), run_time=1.5)


# ─────────────────────────────────────────────
#  SCENE 9 — CONCEPTUAL INTERPRETATION
# ─────────────────────────────────────────────

class Scene9Conceptual(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = section_title("Why Is This Beautiful?")
        title.to_edge(UP, buff=0.4)
        self.play(FadeIn(title), run_time=0.8)
        self.play(Create(rule_line().next_to(title, DOWN, buff=0.15)), run_time=0.6)

        points = [
            ("Symmetrical Properties",
             "Swapping any two roots doesn't change the coefficients.",
             BLUE_CLR),
            ("Information Compression",
             "n roots encoded in just n coefficients.",
             RED_CLR),
            ("Ordering Disappears",
            'The polynomial has no memory of which root is "first".',
            GREEN_CLR),
        ]

        items = VGroup()
        for i, (label, desc, col) in enumerate(points):
            dot_  = Dot(color=col, radius=0.08)
            lbl_t = Text(label, font="Georgia", color=col).scale(0.46)
            dsc_t = Text(desc,  font="Georgia", color=GRAY_CLR).scale(0.36)
            row   = VGroup(dot_, lbl_t, dsc_t).arrange(RIGHT, buff=0.25)
            row.move_to(UP * (1.4 - i * 0.85))
            items.add(row)
            self.play(FadeIn(row, shift=RIGHT * 0.2), run_time=0.8)
            self.wait(0.3)

        # ── Root particles combining into coefficient ──────
        particles = VGroup(*[
            Dot(color=GREEN_CLR, radius=0.12)
            for _ in range(4)
        ])
        positions = [LEFT * 3.5 + DOWN * 2.5,
                     LEFT * 2.5 + DOWN * 2.5,
                     LEFT * 3.0 + DOWN * 3.1,
                     LEFT * 2.0 + DOWN * 3.1]
        for p, pos in zip(particles, positions):
            p.move_to(pos)
        labels = VGroup(*[
            MathTex(l, color=GREEN_CLR).scale(0.5).next_to(p, DOWN, buff=0.1)
            for l, p in zip([r"\alpha", r"\beta", r"\gamma", r"\delta"], particles)
        ])

        self.play(FadeIn(particles), FadeIn(labels), run_time=0.8)

        coeff_dot = Dot(color=GOLD, radius=0.2).move_to(RIGHT * 3.3 + DOWN * 2.8)
        coeff_lbl = MathTex(r"c_k", color=GOLD).scale(0.7).next_to(coeff_dot, DOWN, buff=0.1)

        self.play(
            LaggedStart(*[p.animate.move_to(coeff_dot.get_center())
                          for p in particles],
                        lag_ratio=0.2, run_time=1.5),
            FadeOut(labels),
        )
        self.play(Transform(particles, coeff_dot), FadeIn(coeff_lbl), run_time=0.8)
        self.wait(2.0)

        self.play(FadeOut(Group(*self.mobjects)), run_time=1.2)


# ─────────────────────────────────────────────
#  SCENE 10 — APPLICATIONS
# ─────────────────────────────────────────────

class Scene10Applications(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = section_title("Applications — Vieta in Action")
        title.to_edge(UP, buff=0.4)
        self.play(FadeIn(title), run_time=0.8)
        self.play(Create(rule_line().next_to(title, DOWN, buff=0.15)), run_time=0.6)

        # ── Example 1: alpha^2 + beta^2 ───────────────────
        ex1_title = Text("Example 1", font="Georgia", color=BLUE_CLR).scale(0.5)
        ex1_title.move_to(UP * 1.8 + LEFT * 4.5)
        self.play(Write(ex1_title), run_time=0.6)

        ex1_q = MathTex(
            r"\text{Find } \alpha^2+\beta^2 \text{ for } x^2-5x+6=0",
            color=WHITE
        ).scale(0.78)
        ex1_q.move_to(UP * 1.3)
        self.play(Write(ex1_q), run_time=1.0)

        ex1_step1 = MathTex(
            r"\alpha+\beta = 5, \quad \alpha\beta = 6",
            color=GREEN_CLR
        ).scale(0.78)
        ex1_step2 = MathTex(
            r"\alpha^2+\beta^2 = (\alpha+\beta)^2 - 2\alpha\beta",
            color=WHITE
        ).scale(0.78)
        ex1_step3 = MathTex(
            r"= 25 - 12 = \mathbf{13}",
            color=GOLD
        ).scale(0.85)

        steps1 = VGroup(ex1_step1, ex1_step2, ex1_step3).arrange(DOWN, buff=0.35)
        steps1.move_to(UP * 0.0)

        for s in steps1:
            self.play(Write(s), run_time=0.9)
            self.wait(0.25)

        self.play(Circumscribe(ex1_step3, color=GOLD, run_time=1.0))
        self.wait(1.0)

        self.play(FadeOut(VGroup(ex1_title, ex1_q, steps1)), run_time=0.8)

        # ── Example 2: 1/alpha + 1/beta ───────────────────
        ex2_title = Text("Example 2", font="Georgia", color=RED_CLR).scale(0.5)
        ex2_title.move_to(UP * 1.8 + LEFT * 4.5)
        self.play(Write(ex2_title), run_time=0.6)

        ex2_q = MathTex(
            r"\text{Compute } \frac{1}{\alpha}+\frac{1}{\beta} \text{ for } 2x^2-7x+3=0",
            color=WHITE
        ).scale(0.70)
        ex2_q.move_to(UP * 1.7)
        self.play(Write(ex2_q), run_time=1.0)

        ex2_step1 = MathTex(
            r"\alpha+\beta = \tfrac{7}{2}, \quad \alpha\beta = \tfrac{3}{2}",
            color=GREEN_CLR
        ).scale(0.70)
        ex2_step2 = MathTex(
            r"\frac{1}{\alpha}+\frac{1}{\beta} = \frac{\alpha+\beta}{\alpha\beta}",
            color=WHITE
        ).scale(0.70)
        ex2_step3 = MathTex(
            r"= \frac{7/2}{3/2} = \mathbf{\tfrac{7}{3}}",
            color=GOLD
        ).scale(0.85)

        steps2 = VGroup(ex2_step1, ex2_step2, ex2_step3).arrange(DOWN, buff=0.35)
        steps2.move_to(DOWN * 0.2)

        for s in steps2:
            self.play(Write(s), run_time=0.9)
            self.wait(0.25)

        self.play(Circumscribe(ex2_step3, color=GOLD, run_time=1.0))
        self.wait(1.0)

        self.play(FadeOut(VGroup(ex2_title, ex2_q, steps2)), run_time=0.8)

        # ── Example 3: Cubic symmetric expression ─────────
        ex3_title = Text("Example 3 — Cubic", font="Georgia", color=GOLD).scale(0.5)
        ex3_title.move_to(UP * 1.8 + LEFT * 4.5)
        self.play(Write(ex3_title), run_time=0.6)

        ex3_q = MathTex(
            r"x^3 - 6x^2 + 11x - 6 = 0, \quad \text{find } \alpha^2+\beta^2+\gamma^2",
            color=WHITE
        ).scale(0.72)
        ex3_q.move_to(UP * 1.3)
        self.play(Write(ex3_q), run_time=1.0)

        ex3_step1 = MathTex(
            r"\alpha+\beta+\gamma=6,\; \alpha\beta+\beta\gamma+\gamma\alpha=11,\; \alpha\beta\gamma=6",
            color=GREEN_CLR
        ).scale(0.7)
        ex3_step2 = MathTex(
            r"\alpha^2+\beta^2+\gamma^2 = (\alpha+\beta+\gamma)^2 - 2(\alpha\beta+\beta\gamma+\gamma\alpha)",
            color=WHITE
        ).scale(0.7)
        ex3_step3 = MathTex(
            r"= 36 - 22 = \mathbf{14}",
            color=GOLD
        ).scale(0.85)

        steps3 = VGroup(ex3_step1, ex3_step2, ex3_step3).arrange(DOWN, buff=0.35)
        steps3.move_to(DOWN * 0.3)

        for s in steps3:
            self.play(Write(s), run_time=0.9)
            self.wait(0.25)

        self.play(Circumscribe(ex3_step3, color=GOLD, run_time=1.0))
        self.wait(2.0)

        self.play(FadeOut(Group(*self.mobjects)), run_time=1.2)


# ─────────────────────────────────────────────
#  SCENE 11 — ENDING
# ─────────────────────────────────────────────

class Scene11Ending(Scene):
    def construct(self):
        self.camera.background_color = BG

        # ── Reprise original polynomial ────────────────────
        poly = MathTex(
            r"a_n x^n + a_{n-1}x^{n-1} + \cdots + a_0 = 0",
            color=GRAY_CLR
        ).scale(0.9)
        poly.move_to(UP * 1.8)
        self.play(FadeIn(poly, shift=DOWN * 0.2), run_time=1.5)
        self.wait(0.8)

        # ── Transform to factored form ─────────────────────
        factored = MathTex(
            r"(x-r_1)(x-r_2)\cdots(x-r_n)",
            color=GREEN_CLR
        ).scale(0.95)
        factored.move_to(UP * 0.5)

        self.play(TransformMatchingShapes(poly.copy(), factored), run_time=2.0)
        self.wait(0.5)

        # ── Transform to coefficients ──────────────────────
        coeff_form = MathTex(
            r"\longleftrightarrow\quad"
            r" e_1,\, e_2,\, \ldots,\, e_n",
            color=GOLD
        ).scale(0.95)
        coeff_form.next_to(factored, DOWN, buff=0.6)

        self.play(Write(coeff_form), run_time=1.5)
        self.wait(1.0)

        # ── Narration lines ────────────────────────────────
        line1 = Text(
            "What first looked like chaos (or maybe we're just confused, lol)…",
            font="Georgia", color=GRAY_CLR
        ).scale(0.48)
        line2 = Text(
            "was symmetry all along. (This is why algebra is the GOAT)",
            font="Georgia", color=WHITE
        ).scale(0.52)
        narration = VGroup(line1, line2).arrange(DOWN, buff=0.3)
        narration.move_to(DOWN * 1.3)

        self.play(FadeIn(line1, shift=UP * 0.1), run_time=1.2)
        self.wait(0.6)
        self.play(FadeIn(line2, shift=UP * 0.1), run_time=1.2)
        self.wait(1.5)

        # ── Glow fade ─────────────────────────────────────
        self.play(
            poly.animate.set_color(BLACK),
            factored.animate.set_color(BLACK),
            coeff_form.animate.set_color(BLACK),
            narration.animate.set_color(BLACK),
            run_time=2.0
        )

        # ── Final quote ────────────────────────────────────
        quote = Text(
            '"Algebra is the nice analytical art..." - Isaac Newton',
            font="Georgia", color=GOLD
        ).scale(0.55)
        quote.move_to(ORIGIN)

        self.play(FadeIn(quote, scale=1.05), run_time=2.0)
        self.wait(3.5)
        self.play(FadeOut(quote, run_time=2.0))
        self.wait(1.0)


# ─────────────────────────────────────────────
#  FULL VIDEO — chains all scenes
# ─────────────────────────────────────────────

class FullVideo(Scene):
    def construct(self):
        Scene1Hook.construct(self)
        self.clear()

        Scene2WhatIsARoot.construct(self)
        self.clear()

        Scene3Quadratic.construct(self)
        self.clear()

        Scene4VietaQuadratic.construct(self)
        self.clear()

        Scene5Cubic.construct(self)
        self.clear()

        Scene6PatternTable.construct(self)
        self.clear()

        Scene7Quartic.construct(self)
        self.clear()

        Scene8GeneralVieta.construct(self)
        self.clear()

        Scene9Conceptual.construct(self)
        self.clear()

        Scene10Applications.construct(self)
        self.clear()

        Scene11Ending.construct(self)