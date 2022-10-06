from manim import *


class VMobjectDemo(Scene):

    def set_background(self):
        plane = NumberPlane()
        self.play(
            Create(plane, run_time=1, lag_ratio=0.1),
        )
        my_vmobject = VMobject(color=GREEN)
        handles = [
            Dot(point, color=RED) for point in
            [[-2, -2, 0], [2, -2, 0], [-2, 2, 0]]
        ]
        handles += [
            Dot(point, color=GREEN) for point in
            [[2, 2, 0]]
        ]
        handle_line = [
            Line(np.array([-2, -2, 0]), np.array([2, -2, 0]), color=RED, stroke_width=0),
            Line(np.array([-2, -2, 0]), np.array([-2, 2, 0]), color=GREEN, stroke_width=0),
            Line(np.array([2, 2, 0]), np.array([2.1, 2.1, 0]), color=GREEN, stroke_width=0)
        ]
        arrow = Arrow(ORIGIN, [4, 2, 0], buff=0)
        b1 = Brace(handle_line[0])
        b1text = b1.get_text("False")
        b2 = Brace(handle_line[1], direction=handle_line[1].copy().rotate(PI / 2).get_unit_vector())
        b2text = b2.get_text("False")
        b3 = Brace(handle_line[2], direction=handle_line[2].copy().rotate(PI / 4).get_unit_vector(),stroke_width=0)
        b3text = b3.get_text("True")

        return *handles, *handle_line,b1,b1text,b2,b2text,b3,b3text


    def scene_1(self):
        background = self.set_background()
        self.play(FadeIn(*background))
        self.play(FadeOut(background[-1],background[-2],background[-3],background[-4],background[-5],background[-6]))

    def initial_question(self):
        text = Text("Que linea puede dividir\n a los puntos verdes de los rojos?")
        self.play(Write(text))
        self.play(FadeOut(text))
        self.remove(text)


    def try_line(self,line, does_it_work):
        #expect at line:lambda x: 2x + 1

        axes = Axes(
            x_range = [-1, 1, 1],
            y_range = [-1, 1, 1],
            axis_config={"include_tip": False}
        )

        lower_bound = axes.plot(lambda x: -5)
        upper_bound = axes.plot(lambda x: 5)

        if(does_it_work):
            line_graph = axes.plot(line, color=GREEN)
            line_label = axes.get_graph_label(line_graph,"YES!",color=GREEN,x_val=TAU, direction=UR)
            area2 = axes.get_area(line_graph, [-6, 6], bounded_graph=upper_bound, color=GREEN, opacity=0.2)
            area1 = axes.get_area(line_graph, [-6, 6], bounded_graph=lower_bound, color=RED, opacity=0.2)
        else:
            line_graph = axes.plot(line, color=RED)
            line_label = axes.get_graph_label(line_graph,"No :(",color=RED,x_val=TAU, direction=UR)
            area2 = axes.get_area(line_graph, [-6, 6], bounded_graph=upper_bound, color=RED, opacity=0.2)
            area1 = axes.get_area(line_graph, [-6, 6], bounded_graph=lower_bound, color=RED, opacity=0.2)

        plot = VGroup(axes, line_graph)
        labels = VGroup(line_label)
        self.play(FadeIn(plot,labels))

        self.play(FadeIn(area1))
        self.play(FadeOut(area1), FadeIn(area2,run_time= 2,lag_ratio=0.1))
        self.play(FadeOut(area2))
        self.play(FadeOut(plot,labels))

    def construct(self):
        self.scene_1()
        self.try_line(lambda x: (-0.9084891138140043*x + -0.037298527903231814)*2, False)
        self.try_line(lambda x: (-1.1439673098655678*x + 0.08148402335402664)*2, False)
        self.try_line(lambda x: (-0.9084891138140043*x + 0.18236731771670792)*2, True)