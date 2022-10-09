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
            [[-2, -2, 0],[2, 2, 0]]
        ]
        handles += [
            Dot(point, color=GREEN) for point in
            [[2, -2, 0], [-2, 2, 0]]
        ]

        return handles


    def scene_1(self):
        background = self.set_background()
        self.play(FadeIn(*background))

    def try_line(self,line, does_it_work,line_str):
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
            line_label = axes.get_graph_label(line_graph,line_str,color=GREEN,x_val=TAU, direction=UR)
        else:
            line_graph = axes.plot(line, color=RED)
            line_label = axes.get_graph_label(line_graph, line_str,color=RED,x_val=TAU, direction=UR)

        plot = VGroup(axes, line_graph)
        labels = VGroup(line_label)
        self.play(FadeIn(plot,labels,run_time= 0.5))

        if not does_it_work:
            self.play(FadeOut(plot,labels,run_time= 0.5))
        # self.play(FadeIn(area1,run_time= 0.5))
        # self.play(FadeOut(area1,run_time= 0.5), FadeIn(area2,run_time= 0.5,lag_ratio=0.1))
        # self.play(FadeOut(area2,run_time= 0.5))


    def construct(self):
        self.scene_1()
        self.try_line(lambda x: (-0.8473181210896323*x + 0.11474950816116072)*2, False,'Epoch: 0')
        self.try_line(lambda x: (-0.6476034609343251*x + 0.21817018604292596)*2, False,'Epoch: 1')
        self.try_line(lambda x: (-0.795141708611767*x + 0.26787413125933224)*2, False,'Epoch: 2')
        self.try_line(lambda x: (-1.0259156836947039*x + -0.08335359863603771)*2, False,'Epoch: 3')
        self.try_line(lambda x: (-1.0348849298468281*x + -0.11220172599548582)*2, False,'Epoch: 4')