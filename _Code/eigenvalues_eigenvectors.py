from manim import *
import numpy as np


class BaseEigenScene(Scene):
    """Shared subtitle and typography helpers across all 6 scenes."""

    def setup(self):
        super().setup()
        self.current_sub = None

    def show_subtitle(self, text_str, wait_time=4.5):
        new_sub = Text(text_str, font_size=22, color=WHITE).to_edge(DOWN, buff=0.22)
        bg = BackgroundRectangle(new_sub, color=BLACK, fill_opacity=0.88, buff=0.12)
        sub_group = VGroup(bg, new_sub)

        if self.current_sub is not None:
            self.play(FadeOut(self.current_sub, run_time=0.18), FadeIn(sub_group, run_time=0.18))
        else:
            self.play(FadeIn(sub_group, run_time=0.18))

        self.current_sub = sub_group
        self.wait(wait_time)

    def clear_subtitle(self):
        if self.current_sub is not None:
            self.play(FadeOut(self.current_sub, run_time=0.2))
            self.current_sub = None


# ==============================================================================
# SCENE 1: HOOK (0:00 – 0:40 | 40 seconds)
# ==============================================================================
class Scene1Hook(BaseEigenScene):
    def construct(self):
        self.play_scene()

    def play_scene(self):
        title = Text("Eigenvalues & Eigenvectors", font_size=46, color=BLUE)
        sub = Text("Understanding Matrix Transformations Visually", font_size=26, color=GRAY_B)
        meta = Text("M3 Internal Assessment | Dhruvil Kamlesh Shah | URN No.: E25B070661", font_size=20, color=YELLOW)
        header_group = VGroup(title, sub, meta).arrange(DOWN, buff=0.32)

        self.play(Write(title, run_time=0.9), FadeIn(sub, run_time=0.6))
        self.play(FadeIn(meta, run_time=0.5))
        self.show_subtitle("Welcome! Today we uncover the hidden geometry of eigenvalues and eigenvectors.", wait_time=3.5)
        self.play(FadeOut(header_group, run_time=0.5))

        plane = NumberPlane(
            x_range=[-7, 7, 1], y_range=[-4, 4, 1],
            background_line_style={"stroke_color": BLUE_D, "stroke_width": 1.3, "stroke_opacity": 0.65}
        )
        A = [[2, 1], [1, 2]]

        v_off1 = Vector([2, 0], color=GRAY_A, stroke_width=4)
        v_off2 = Vector([0, 2], color=TEAL, stroke_width=4)
        v_off3 = Vector([-2, 1], color=ORANGE, stroke_width=4)
        v_eigen = Vector([1.5, 1.5], color=YELLOW, stroke_width=6)

        span_line = DashedLine([-4.5, -4.5, 0], [4.5, 4.5, 0], color=YELLOW, stroke_opacity=0.6)
        eigen_tag = Text("Special Vector (Eigenvector)", font_size=22, color=YELLOW).next_to(v_eigen.get_end(), UR, buff=0.15)
        eigen_tag.add_background_rectangle()

        self.play(Create(plane, run_time=0.8))
        self.play(
            GrowArrow(v_off1), GrowArrow(v_off2), GrowArrow(v_off3),
            GrowArrow(v_eigen), Create(span_line), FadeIn(eigen_tag),
            run_time=1.0
        )
        self.show_subtitle("Watch these four vectors when we apply a 2x2 matrix transformation to the plane.", wait_time=4.5)

        self.play(FadeOut(eigen_tag, run_time=0.3))
        self.play(
            ApplyMatrix(A, plane),
            ApplyMatrix(A, v_off1),
            ApplyMatrix(A, v_off2),
            ApplyMatrix(A, v_off3),
            ApplyMatrix(A, v_eigen),
            run_time=2.2
        )

        question_box = Text(
            "Why does this yellow vector keep pointing in the exact same direction\n"
            "even after the transformation?",
            font_size=23, color=YELLOW
        ).to_edge(UP, buff=0.45)
        question_box.add_background_rectangle()

        self.play(FadeIn(question_box, run_time=0.6))
        self.show_subtitle("Most vectors get knocked off their original lines — yet the yellow vector only stretched!", wait_time=5.5)
        self.show_subtitle("These special invariant directions are called eigenvectors, and they unlock matrix behavior.", wait_time=5.5)

        self.clear_subtitle()
        self.play(FadeOut(VGroup(plane, v_off1, v_off2, v_off3, v_eigen, span_line, question_box), run_time=0.6))


# ==============================================================================
# SCENE 2: CONCEPT INTRODUCTION & DETERMINANT BRIDGE
# ==============================================================================
class Scene2Concept(BaseEigenScene):
    def construct(self):
        self.play_scene()

    def play_scene(self):
        header = Text("The Fundamental Eigenvalue Equation", font_size=36, color=BLUE).to_edge(UP, buff=0.45)
        self.play(Write(header, run_time=0.8))

        eq = MathTex(r"A", r"\vec{v}", r"=", r"\lambda", r"\vec{v}", font_size=64).next_to(header, DOWN, buff=0.45)
        eq[0].set_color(BLUE)
        eq[1].set_color(YELLOW)
        eq[3].set_color(GREEN)
        eq[4].set_color(YELLOW)

        self.play(Write(eq, run_time=1.0))
        self.show_subtitle("Everything in this topic revolves around one compact equation: A times v equals lambda times v.", wait_time=5.5)

        defs = VGroup(
            MathTex(r"A \in \mathbb{R}^{n \times n} \text{ : Square transformation matrix}", font_size=28, color=BLUE),
            MathTex(r"\vec{v} \neq \vec{0} \text{ : Non-zero eigenvector (invariant direction)}", font_size=28, color=YELLOW),
            MathTex(r"\lambda \in \mathbb{R} \text{ : Corresponding eigenvalue (scalar stretching factor)}", font_size=28, color=GREEN)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.28).next_to(eq, DOWN, buff=0.45)

        for d in defs:
            self.play(FadeIn(d, run_time=0.5))
            self.wait(0.8)

        self.show_subtitle("Notice what the left and right sides say: multiplying v by matrix A does the same job as scaling v by number lambda.", wait_time=6.5)

        note_box = VGroup(
            Text("Key Geometric Rules:", font_size=24, color=ORANGE),
            Text("• v must be non-zero (since A·0 = 0 is trivially true for every matrix).", font_size=21),
            Text("• v stays on its own span line through the origin (stretches if λ > 1, shrinks if 0 < λ < 1, flips if λ < 0).", font_size=21)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.20).next_to(defs, DOWN, buff=0.38)

        self.play(FadeIn(note_box, run_time=0.7))
        self.show_subtitle("Whether lambda stretches, shrinks, or reverses v by 180 degrees, v never leaves its line through the origin.", wait_time=7.0)

        bridge_eq = MathTex(
            r"A\vec{v} = \lambda\vec{v} \implies (A - \lambda I)\vec{v} = \vec{0} \implies \det(A - \lambda I) = 0",
            font_size=26, color=TEAL
        ).next_to(note_box, DOWN, buff=0.32)
        bridge_eq.add_background_rectangle()

        self.play(Write(bridge_eq, run_time=1.0))
        self.show_subtitle("To find these special vectors, we rewrite Av = λv as (A - λI)v = 0, which requires det(A - λI) = 0.", wait_time=7.5)
        self.show_subtitle("When the determinant vanishes, A - λI squashes space onto a lower dimension, allowing non-zero solutions!", wait_time=7.5)
        self.play(FadeOut(bridge_eq, run_time=0.4))

        self.show_subtitle("Let's see this visually on clean diagonal matrices first.", wait_time=4.5)

        self.clear_subtitle()
        self.play(FadeOut(VGroup(header, eq, defs, note_box), run_time=0.6))


# ==============================================================================
# SCENE 3: VISUAL INTUITION — POSITIVE & NEGATIVE EIGENVALUES
# ==============================================================================
class Scene3VisualIntuition(BaseEigenScene):
    def construct(self):
        self.play_scene()

    def play_scene(self):
        # Part 1: Positive Eigenvalues A = [[2, 0], [0, 3]]
        plane = NumberPlane(
            x_range=[-7, 7, 1], y_range=[-4, 4, 1],
            background_line_style={"stroke_color": BLUE_D, "stroke_width": 1.3, "stroke_opacity": 0.65}
        )
        mat_label = MathTex(
            r"A = \begin{bmatrix} 2 & 0 \\ 0 & 3 \end{bmatrix}",
            font_size=34, color=BLUE
        ).to_corner(UL, buff=0.4)
        mat_label.add_background_rectangle()

        i_hat = Vector([1, 0], color=GREEN, stroke_width=6)
        j_hat = Vector([0, 1], color=RED, stroke_width=6)
        w_vec = Vector([1, 1], color=ORANGE, stroke_width=5)

        i_txt = MathTex(r"\hat{\imath} = \begin{bmatrix} 1 \\ 0 \end{bmatrix}", color=GREEN, font_size=25).next_to(i_hat.get_end(), DOWN, buff=0.15)
        i_txt.add_background_rectangle()
        j_txt = MathTex(r"\hat{\jmath} = \begin{bmatrix} 0 \\ 1 \end{bmatrix}", color=RED, font_size=25).next_to(j_hat.get_end(), LEFT, buff=0.15)
        j_txt.add_background_rectangle()
        w_txt = MathTex(r"\vec{w} = \begin{bmatrix} 1 \\ 1 \end{bmatrix}", color=ORANGE, font_size=25).next_to(w_vec.get_end(), UR, buff=0.12)
        w_txt.add_background_rectangle()

        self.play(Create(plane, run_time=0.8), FadeIn(mat_label, run_time=0.5))
        self.play(
            GrowArrow(i_hat), FadeIn(i_txt),
            GrowArrow(j_hat), FadeIn(j_txt),
            GrowArrow(w_vec), FadeIn(w_txt),
            run_time=1.0
        )
        self.show_subtitle("Consider the diagonal matrix A = [[2, 0], [0, 3]], along with basis vectors i-hat, j-hat, and vector w = [1, 1].", wait_time=6.0)

        A_diag = [[2, 0], [0, 3]]
        self.play(FadeOut(i_txt, run_time=0.25), FadeOut(j_txt, run_time=0.25), FadeOut(w_txt, run_time=0.25))
        self.play(
            ApplyMatrix(A_diag, plane),
            ApplyMatrix(A_diag, i_hat),
            ApplyMatrix(A_diag, j_hat),
            ApplyMatrix(A_diag, w_vec),
            run_time=2.2
        )

        res_panel = VGroup(
            MathTex(r"A\begin{bmatrix} 1 \\ 0 \end{bmatrix} = \begin{bmatrix} 2 \\ 0 \end{bmatrix} = 2\begin{bmatrix} 1 \\ 0 \end{bmatrix} \implies \lambda_1 = 2", font_size=26, color=GREEN),
            MathTex(r"A\begin{bmatrix} 0 \\ 1 \end{bmatrix} = \begin{bmatrix} 0 \\ 3 \end{bmatrix} = 3\begin{bmatrix} 0 \\ 1 \end{bmatrix} \implies \lambda_2 = 3", font_size=26, color=RED),
            MathTex(r"A\begin{bmatrix} 1 \\ 1 \end{bmatrix} = \begin{bmatrix} 2 \\ 3 \end{bmatrix} \neq \lambda\begin{bmatrix} 1 \\ 1 \end{bmatrix} \text{ (Direction changed!)}", font_size=25, color=ORANGE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).to_corner(UR, buff=0.35)
        res_panel.add_background_rectangle()

        self.play(FadeIn(res_panel, run_time=0.7))
        self.show_subtitle("Horizontally, i-hat stretched by a factor of 2 along the x-axis — so [1, 0] is an eigenvector with eigenvalue 2.", wait_time=6.5)
        self.show_subtitle("Vertically, j-hat stretched by 3 along the y-axis — giving eigenvalue 3.", wait_time=5.5)
        self.show_subtitle("Meanwhile, the orange vector [1, 1] moved to [2, 3] — changing its angle, so it is NOT an eigenvector!", wait_time=6.5)

        self.play(FadeOut(VGroup(plane, mat_label, i_hat, j_hat, w_vec, res_panel), run_time=0.5))

        # Part 2: Negative Eigenvalue Demonstration (180-degree reversal along span)
        plane2 = NumberPlane(
            x_range=[-7, 7, 1], y_range=[-4, 4, 1],
            background_line_style={"stroke_color": TEAL, "stroke_width": 1.3, "stroke_opacity": 0.6}
        )
        mat_b_lbl = MathTex(
            r"B = \begin{bmatrix} 2 & 0 \\ 0 & -1.5 \end{bmatrix} \quad (\text{Negative Eigenvalue})",
            font_size=30, color=TEAL
        ).to_corner(UL, buff=0.4)
        mat_b_lbl.add_background_rectangle()

        y_span = DashedLine([0, -4, 0], [0, 4, 0], color=RED, stroke_opacity=0.6)
        bi = Vector([1, 0], color=GREEN, stroke_width=6)
        bj = Vector([0, 1], color=RED, stroke_width=6)

        self.play(Create(plane2, run_time=0.7), Create(y_span), FadeIn(mat_b_lbl), GrowArrow(bi), GrowArrow(bj))
        self.show_subtitle("Now look at what happens when an eigenvalue is negative, as in matrix B = [[2, 0], [0, -1.5]].", wait_time=6.0)

        B_diag = [[2, 0], [0, -1.5]]
        self.play(
            ApplyMatrix(B_diag, plane2),
            ApplyMatrix(B_diag, bi),
            ApplyMatrix(B_diag, bj),
            run_time=2.2
        )

        neg_box = MathTex(
            r"B\begin{bmatrix} 0 \\ 1 \end{bmatrix} = \begin{bmatrix} 0 \\ -1.5 \end{bmatrix} = -1.5\begin{bmatrix} 0 \\ 1 \end{bmatrix} \implies \lambda_2 = -1.5",
            font_size=26, color=RED
        ).to_corner(UR, buff=0.35)
        neg_box.add_background_rectangle()

        self.play(FadeIn(neg_box, run_time=0.6))
        self.show_subtitle("The red vector j-hat flipped 180 degrees to [0, -1.5], yet it STILL lies on the exact same vertical line!", wait_time=6.8)
        self.show_subtitle("That is why negative eigenvalues represent orientation reversal along an invariant eigen-line.", wait_time=6.0)

        self.clear_subtitle()
        self.play(FadeOut(VGroup(plane2, y_span, mat_b_lbl, bi, bj, neg_box), run_time=0.6))


# ==============================================================================
# SCENE 4: WORKED MATHEMATICAL EXAMPLE, VERIFICATION & INVERTIBILITY CHECK
# ==============================================================================
class Scene4WorkedExample(BaseEigenScene):
    def construct(self):
        self.play_scene()

    def play_scene(self):
        header = Text("Worked Example: Finding Eigenvalues & Eigenvectors", font_size=32, color=BLUE).to_edge(UP, buff=0.4)
        self.play(Write(header, run_time=0.7))

        # Part A: Characteristic Equation
        part1_title = Text("Part A: Characteristic Equation", font_size=25, color=YELLOW).next_to(header, DOWN, buff=0.35).to_edge(LEFT, buff=0.7)
        mat_A = MathTex(r"A = \begin{bmatrix} 4 & 1 \\ 2 & 3 \end{bmatrix}", font_size=34).next_to(part1_title, DOWN, buff=0.3, aligned_edge=LEFT)

        self.play(Write(part1_title, run_time=0.5), Write(mat_A, run_time=0.6))
        self.show_subtitle("Now let's compute eigenvalues and eigenvectors algebraically for a non-diagonal matrix A = [[4, 1], [2, 3]].", wait_time=6.2)

        step1 = MathTex(r"\text{Step 1: } \det(A - \lambda I) = 0", font_size=30).next_to(mat_A, DOWN, buff=0.35, aligned_edge=LEFT)
        self.play(Write(step1, run_time=0.7))
        self.show_subtitle("We rewrite Av = λv as (A - λI)v = 0. For a non-zero solution v, the determinant must equal zero.", wait_time=6.5)

        step2 = MathTex(
            r"\text{Step 2: } \begin{vmatrix} 4 - \lambda & 1 \\ 2 & 3 - \lambda \end{vmatrix} = 0",
            font_size=30
        ).next_to(step1, DOWN, buff=0.3, aligned_edge=LEFT)
        self.play(Write(step2, run_time=0.8))
        self.show_subtitle("Subtract lambda from the main diagonal entries 4 and 3.", wait_time=5.5)

        step3 = MathTex(r"\text{Step 3: } (4 - \lambda)(3 - \lambda) - (1)(2) = 0", font_size=30).next_to(step2, DOWN, buff=0.3, aligned_edge=LEFT)
        self.play(Write(step3, run_time=0.8))
        self.show_subtitle("Expand the 2x2 determinant using ad minus bc.", wait_time=5.5)

        step4 = MathTex(r"\text{Step 4: } \lambda^2 - 7\lambda + 10 = 0", font_size=30, color=TEAL).next_to(step3, DOWN, buff=0.3, aligned_edge=LEFT)
        self.play(Write(step4, run_time=0.8))
        self.show_subtitle("Expanding gives the quadratic characteristic polynomial: lambda squared minus 7 lambda plus 10 equals 0.", wait_time=6.5)

        step5 = MathTex(
            r"\text{Step 5: } (\lambda - 5)(\lambda - 2) = 0 \implies \lambda_1 = 5,\ \lambda_2 = 2",
            font_size=30, color=GREEN
        ).next_to(step4, DOWN, buff=0.3, aligned_edge=LEFT)
        self.play(Write(step5, run_time=0.9))
        self.show_subtitle("Factoring gives our two eigenvalues: lambda-1 equals 5 and lambda-2 equals 2.", wait_time=6.5)

        self.play(FadeOut(VGroup(part1_title, mat_A, step1, step2, step3, step4, step5), run_time=0.5))

        # Part B: Eigenvectors side-by-side
        left_col_title = MathTex(r"\text{Case 1: } \lambda_1 = 5", font_size=32, color=GREEN).next_to(header, DOWN, buff=0.45).shift(LEFT * 3.3)
        c1_s1 = MathTex(r"(A - 5I)\vec{v}_1 = \vec{0}", font_size=28).next_to(left_col_title, DOWN, buff=0.35)
        c1_s2 = MathTex(r"\begin{bmatrix} 4-5 & 1 \\ 2 & 3-5 \end{bmatrix}\begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}", font_size=27).next_to(c1_s1, DOWN, buff=0.3)
        c1_s3 = MathTex(r"\begin{bmatrix} -1 & 1 \\ 2 & -2 \end{bmatrix}\begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}", font_size=27).next_to(c1_s2, DOWN, buff=0.3)
        c1_s4 = MathTex(r"-x + y = 0 \implies y = x", font_size=28, color=YELLOW).next_to(c1_s3, DOWN, buff=0.3)
        c1_s5 = MathTex(r"\text{Set } x = 1 \implies \vec{v}_1 = \begin{bmatrix} 1 \\ 1 \end{bmatrix}", font_size=30, color=GREEN).next_to(c1_s4, DOWN, buff=0.3)

        self.play(Write(left_col_title, run_time=0.6))
        self.play(Write(c1_s1, run_time=0.6))
        self.show_subtitle("First, substitute lambda-1 = 5 into (A - 5I)v = 0.", wait_time=5.2)
        self.play(Write(c1_s2, run_time=0.7))
        self.play(Write(c1_s3, run_time=0.7))
        self.show_subtitle("Both rows simplify to the single equation minus x plus y equals 0, meaning y equals x.", wait_time=6.2)
        self.play(Write(c1_s4, run_time=0.6), Write(c1_s5, run_time=0.7))
        self.show_subtitle("Setting x = 1 gives our first eigenvector: v1 = [1, 1].", wait_time=5.8)

        divider = DashedLine(UP * 1.8, DOWN * 2.5, color=GRAY).next_to(header, DOWN, buff=0.4)
        right_col_title = MathTex(r"\text{Case 2: } \lambda_2 = 2", font_size=32, color=ORANGE).next_to(header, DOWN, buff=0.45).shift(RIGHT * 3.3)
        c2_s1 = MathTex(r"(A - 2I)\vec{v}_2 = \vec{0}", font_size=28).next_to(right_col_title, DOWN, buff=0.35)
        c2_s2 = MathTex(r"\begin{bmatrix} 4-2 & 1 \\ 2 & 3-2 \end{bmatrix}\begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}", font_size=27).next_to(c2_s1, DOWN, buff=0.3)
        c2_s3 = MathTex(r"\begin{bmatrix} 2 & 1 \\ 2 & 1 \end{bmatrix}\begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}", font_size=27).next_to(c2_s2, DOWN, buff=0.3)
        c2_s4 = MathTex(r"2x + y = 0 \implies y = -2x", font_size=28, color=YELLOW).next_to(c2_s3, DOWN, buff=0.3)
        c2_s5 = MathTex(r"\text{Set } x = 1 \implies \vec{v}_2 = \begin{bmatrix} 1 \\ -2 \end{bmatrix}", font_size=30, color=ORANGE).next_to(c2_s4, DOWN, buff=0.3)

        self.play(Create(divider, run_time=0.4), Write(right_col_title, run_time=0.6))
        self.play(Write(c2_s1, run_time=0.6))
        self.show_subtitle("Next, substitute lambda-2 = 2 into (A - 2I)v = 0.", wait_time=5.2)
        self.play(Write(c2_s2, run_time=0.7))
        self.play(Write(c2_s3, run_time=0.7))
        self.show_subtitle("Here, both rows yield 2x + y = 0, so y equals minus 2x.", wait_time=6.2)
        self.play(Write(c2_s4, run_time=0.6), Write(c2_s5, run_time=0.7))
        self.show_subtitle("Setting x = 1 gives our second eigenvector: v2 = [1, -2].", wait_time=5.8)

        self.play(FadeOut(VGroup(
            divider,
            left_col_title, c1_s1, c1_s2, c1_s3, c1_s4, c1_s5,
            right_col_title, c2_s1, c2_s2, c2_s3, c2_s4, c2_s5
        ), run_time=0.5))

        # Part C: Explicit Verification using Av = lambda * v + Trace/Det & Invertibility Check
        ver_title = Text("Part C: Verifying Our Solution with Av = λv", font_size=26, color=YELLOW).next_to(header, DOWN, buff=0.35)
        self.play(Write(ver_title, run_time=0.6))
        self.show_subtitle("Before celebrating, let's verify both eigenpairs directly in the equation Av = λv.", wait_time=5.5)

        v1_check = MathTex(
            r"A\vec{v}_1 = \begin{bmatrix} 4 & 1 \\ 2 & 3 \end{bmatrix}\begin{bmatrix} 1 \\ 1 \end{bmatrix} = \begin{bmatrix} 4(1)+1(1) \\ 2(1)+3(1) \end{bmatrix} = \begin{bmatrix} 5 \\ 5 \end{bmatrix} = 5\begin{bmatrix} 1 \\ 1 \end{bmatrix} \ \checkmark",
            font_size=27, color=GREEN
        ).next_to(ver_title, DOWN, buff=0.35)

        v2_check = MathTex(
            r"A\vec{v}_2 = \begin{bmatrix} 4 & 1 \\ 2 & 3 \end{bmatrix}\begin{bmatrix} 1 \\ -2 \end{bmatrix} = \begin{bmatrix} 4(1)+1(-2) \\ 2(1)+3(-2) \end{bmatrix} = \begin{bmatrix} 2 \\ -4 \end{bmatrix} = 2\begin{bmatrix} 1 \\ -2 \end{bmatrix} \ \checkmark",
            font_size=27, color=ORANGE
        ).next_to(v1_check, DOWN, buff=0.35)

        self.play(Write(v1_check, run_time=1.0))
        self.show_subtitle("For v1 = [1, 1], matrix multiplication produces [5, 5], which is indeed 5 times v1.", wait_time=6.2)

        self.play(Write(v2_check, run_time=1.0))
        self.show_subtitle("And for v2 = [1, -2], matrix multiplication produces [2, -4], which is exact 2 times v2!", wait_time=6.2)

        shortcut_box = MathTex(
            r"\text{Quick Check: } \text{tr}(A) = 4 + 3 = 7 = \lambda_1 + \lambda_2 \quad \text{and} \quad \det(A) = 12 - 2 = 10 = \lambda_1 \cdot \lambda_2",
            font_size=24, color=TEAL
        ).next_to(v2_check, DOWN, buff=0.35)
        shortcut_box.add_background_rectangle()

        self.play(Write(shortcut_box, run_time=1.0))
        self.show_subtitle("Pro tip: For any 2x2 matrix, eigenvalues always sum to the trace and multiply to the determinant!", wait_time=6.8)
        self.show_subtitle("Here 5 + 2 equals 7, and 5 times 2 equals 10 — confirming our roots instantly.", wait_time=6.0)

        det_note = MathTex(
            r"\text{Notice: } \det(A) = 10 \neq 0 \implies \text{Neither eigenvalue is } 0 \text{ (Matrix } A \text{ is invertible)}",
            font_size=24, color=YELLOW
        ).next_to(shortcut_box, DOWN, buff=0.3)
        det_note.add_background_rectangle()

        self.play(FadeIn(det_note, run_time=0.6))
        self.show_subtitle("Because the determinant is non-zero, neither eigenvalue is zero — confirming A is invertible with no null-space collapse.", wait_time=7.5)

        self.clear_subtitle()
        self.play(FadeOut(VGroup(header, ver_title, v1_check, v2_check, shortcut_box, det_note), run_time=0.6))


# ==============================================================================
# SCENE 5: GEOMETRIC INTERPRETATION & EIGEN-DECOMPOSITION
# ==============================================================================
class Scene5GeometricInterpretation(BaseEigenScene):
    def construct(self):
        self.play_scene()

    def play_scene(self):
        plane = NumberPlane(
            x_range=[-8, 8, 1], y_range=[-6, 6, 1],
            background_line_style={"stroke_color": BLUE_D, "stroke_width": 1.2, "stroke_opacity": 0.6}
        )
        A = [[4, 1], [2, 3]]

        span1 = DashedLine([-5, -5, 0], [5, 5, 0], color=GREEN, stroke_opacity=0.65)
        span2 = DashedLine([-3, 6, 0], [3, -6, 0], color=ORANGE, stroke_opacity=0.65)

        v1 = Vector([1, 1], color=GREEN, stroke_width=6)
        v2 = Vector([1, -2], color=ORANGE, stroke_width=6)

        v1_lbl = MathTex(r"\vec{v}_1 = \begin{bmatrix} 1 \\ 1 \end{bmatrix}", color=GREEN, font_size=26).next_to(v1.get_end(), UR, buff=0.12)
        v1_lbl.add_background_rectangle()
        v2_lbl = MathTex(r"\vec{v}_2 = \begin{bmatrix} 1 \\ -2 \end{bmatrix}", color=ORANGE, font_size=26).next_to(v2.get_end(), DR, buff=0.12)
        v2_lbl.add_background_rectangle()

        self.play(Create(plane, run_time=0.8), Create(span1), Create(span2))
        self.play(GrowArrow(v1), FadeIn(v1_lbl), GrowArrow(v2), FadeIn(v2_lbl), run_time=1.0)
        self.show_subtitle("Now let's return to the coordinate grid with A = [[4, 1], [2, 3]] and plot v1 = [1, 1] and v2 = [1, -2].", wait_time=6.2)

        self.play(FadeOut(v1_lbl, run_time=0.25), FadeOut(v2_lbl, run_time=0.25))
        self.play(
            ApplyMatrix(A, plane),
            ApplyMatrix(A, v1),
            ApplyMatrix(A, v2),
            run_time=2.5
        )

        verify_box = VGroup(
            MathTex(r"A\vec{v}_1 = \begin{bmatrix} 5 \\ 5 \end{bmatrix} = 5\vec{v}_1 \quad (\text{Stretched } 5\times)", font_size=26, color=GREEN),
            MathTex(r"A\vec{v}_2 = \begin{bmatrix} 2 \\ -4 \end{bmatrix} = 2\vec{v}_2 \quad (\text{Stretched } 2\times)", font_size=26, color=ORANGE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).to_corner(UL, buff=0.35)
        verify_box.add_background_rectangle()

        self.play(FadeIn(verify_box, run_time=0.7))
        self.show_subtitle("Look at the green vector: v1 stretched by a factor of 5 to [5, 5], staying right on its dashed green line!", wait_time=6.5)
        self.show_subtitle("And the orange vector v2 stretched by a factor of 2 to [2, -4], staying locked on its orange line!", wait_time=6.5)

        u_vec = Vector([7, 1], color=YELLOW, stroke_width=5)
        u_lbl = MathTex(
            r"\text{Any vector } \vec{u} = \vec{v}_1 + \vec{v}_2 = \begin{bmatrix} 2 \\ -1 \end{bmatrix} \implies A\vec{u} = 5\vec{v}_1 + 2\vec{v}_2 = \begin{bmatrix} 7 \\ 1 \end{bmatrix}",
            font_size=24, color=YELLOW
        ).to_corner(UR, buff=0.35)
        u_lbl.add_background_rectangle()

        self.play(GrowArrow(u_vec, run_time=0.8), FadeIn(u_lbl, run_time=0.6))
        self.show_subtitle("Better yet, any vector u = v1 + v2 transforms simply by scaling its v1 part by 5 and its v2 part by 2!", wait_time=7.0)
        self.show_subtitle("Eigenvectors turn complicated 2D shears into effortless 1D stretches along invariant axes.", wait_time=6.2)

        power_box = MathTex(
            r"\text{Why It Matters: } A^k\vec{u} = 5^k\vec{v}_1 + 2^k\vec{v}_2 \implies A^2\vec{u} = 25\begin{bmatrix} 1 \\ 1 \end{bmatrix} + 4\begin{bmatrix} 1 \\ -2 \end{bmatrix} = \begin{bmatrix} 29 \\ 17 \end{bmatrix}",
            font_size=24, color=BLUE_B
        ).to_edge(DOWN, buff=1.15)
        power_box.add_background_rectangle()

        self.play(FadeIn(power_box, run_time=0.7))
        self.show_subtitle("In engineering and physics, this lets us compute high powers like A-squared or A-to-the-100th without multiplying matrices!", wait_time=7.0)
        self.show_subtitle("We simply raise each scalar eigenvalue to the k-th power along its invariant eigen-direction.", wait_time=6.5)

        self.clear_subtitle()
        self.play(FadeOut(VGroup(plane, span1, span2, v1, v2, verify_box, u_vec, u_lbl, power_box), run_time=0.6))


# ==============================================================================
# SCENE 6: SUMMARY & CREDITS (5:30 – 6:00)
# ==============================================================================
class Scene6SummaryCredits(BaseEigenScene):
    def construct(self):
        self.play_scene()

    def play_scene(self):
        header = Text("Summary & Key Takeaways", font_size=38, color=BLUE).to_edge(UP, buff=0.45)
        self.play(Write(header, run_time=0.7))

        takeaways = VGroup(
            Text("1. Eigenvectors are non-zero vectors whose span line is preserved under A.", font_size=23),
            Text("2. Eigenvalues (λ) measure the exact scaling factor along each eigenvector.", font_size=23),
            Text("3. Solving det(A - λI) = 0 bridges matrix algebra with geometric invariance.", font_size=23)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.28).next_to(header, DOWN, buff=0.4)

        final_eq = MathTex(r"A\vec{v} = \lambda\vec{v}", font_size=52, color=YELLOW).next_to(takeaways, DOWN, buff=0.45)
        box = SurroundingRectangle(final_eq, color=YELLOW, buff=0.2)

        credits = VGroup(
            Text("Project: Eigenvalues & Eigenvectors | Dhruvil Kamlesh Shah | URN No.: E25B070661", font_size=18, color=WHITE),
            Text("References: Gilbert Strang, Introduction to Linear Algebra; 3Blue1Brown (Essence of Linear Algebra)", font_size=17, color=GRAY_B),
            Text("AI Disclosure: Manim Python code, storyboard, and narration script structured with AI assistance.", font_size=17, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.16).to_edge(DOWN, buff=0.95)

        for item in takeaways:
            self.play(FadeIn(item, run_time=0.5))
            self.wait(3.2)

        self.play(Write(final_eq, run_time=0.8), Create(box, run_time=0.6))
        self.show_subtitle("Every eigenvalue-eigenvector pair satisfies Av = λv — connecting matrix algebra to pure geometry.", wait_time=6.5)

        self.play(FadeIn(credits, run_time=0.7))
        self.show_subtitle("Thank you for watching!", wait_time=6.5)
        self.clear_subtitle()
        self.wait(2.5)


# ==============================================================================
# MASTER SCENE: RENDERS ALL 6 SCENES IN ONE 6-MINUTE VIDEO
# ==============================================================================
class FullEigenvaluesProject(BaseEigenScene):
    def construct(self):
        for scene_cls in (
            Scene1Hook,
            Scene2Concept,
            Scene3VisualIntuition,
            Scene4WorkedExample,
            Scene5GeometricInterpretation,
            Scene6SummaryCredits,
        ):
            scene_cls.play_scene(self)
            self.clear()