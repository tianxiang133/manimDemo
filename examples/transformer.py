import copy

from manim import *
class AllReduce(Scene):
    def construct(self):
        # 创建三条虚线,
        line1 = DashedLine(start=[-6, -2, 0], end=[-6, 2, 0], color=BLUE)
        line2 = DashedLine(start=[-4, -2, 0], end=[-4, 2, 0], color=BLUE)
        line3 = DashedLine(start=[-2, -2, 0], end=[-2, 2, 0], color=BLUE)
        # 创建两个长方形
        rectangle1 = Rectangle(width=1, height=2, color=GREEN).shift(LEFT * 5)
        rectangle2 = Rectangle(width=1, height=2, color=GREEN).shift(LEFT * 3)

        #创建两个矩阵
        matrix1 = Matrix([[1, 2], [3, 4]])
        matrix2 = Matrix([[5, 6], [7, 8]])

        #matrix 缩小
        matrix1.scale(0.35)
        matrix2.scale(0.35)
        #创建两个文字
        txt1 = Text("rank01", color=BLUE, font_size=30)
        txt2 = Text("rank02",color=BLUE,font_size=30)

        #文字移动到长方形上方
        txt1.next_to(rectangle1,UP)
        txt2.next_to(rectangle2,UP)
        #举证移动到长方形内部
        matrix1.move_to(rectangle1.get_center())
        matrix2.move_to(rectangle2.get_center())

        # 将虚线和长方形添加到场景中
        self.add(line1,txt1,matrix1,line2,txt2,matrix2, line3, rectangle1,rectangle2)
        self.wait(1)

        #创建一个箭头
        arrow1 = Arrow([-1.5, 0, 0], [1.5, 0, 0])


        #添加文字，并至于箭头上方
        arrow1_txt1 = Text("all-reduce",color=BLUE,font_size=30)
        arrow1_txt1.next_to(arrow1, UP)

        #添加将两个矩阵的加法过程至于箭头下方
        # matrix5 = Matrix([[1, 2], [3, 4]])
        # matrix6 = Matrix([[5, 6], [7, 8]])
        matrix5 = copy.deepcopy(matrix1)
        matrix6 = copy.deepcopy(matrix2)
        matrix5.set_color(BLUE)
        matrix6.set_color(BLUE)
        txt_plus = Text("+", color=BLUE, font_size=30)
        txt_equal = Text("=", color=BLUE, font_size=30)
        result_matrix = Matrix([[1 + 5, 2 + 6], [3 + 7, 4 + 8]])
        txt_plus.scale(0.5)
        txt_equal.scale(0.5)
        result_matrix.scale(0.3)
        result_matrix.set_color(BLUE)
        matrix_group = VGroup(matrix5,txt_plus, matrix6,  txt_equal, result_matrix)
        matrix_group.arrange(RIGHT,buff=0.1)
        arrow1_center = arrow1.get_center()
        matrix_group.move_to(arrow1_center).shift(DOWN/2)
        self.play(Write(matrix_group))

        #创建3条虚线
        self.play(Create(arrow1),Create(arrow1_txt1),run_time=0.5)
        line4 = DashedLine(start=[2, -2, 0], end=[2, 2, 0], color=BLUE)
        line5 = DashedLine(start=[4, -2, 0], end=[4, 2, 0], color=BLUE)
        line6 = DashedLine(start=[6, -2, 0], end=[6, 2, 0], color=BLUE)


        # 创建两个长方形，并将result_matrix 放在里面
        matrix7 = copy.deepcopy(result_matrix)
        matrix8 = copy.deepcopy(result_matrix)
        rectangle3 = Rectangle(width=1, height=2, color=GREEN).shift(RIGHT * 5)
        rectangle4 = Rectangle(width=1, height=2, color=GREEN).shift(RIGHT * 3)
        txt3 = Text("rank01", color=BLUE, font_size=30)
        txt4 = Text("rank02", color=BLUE, font_size=30)
        txt3.next_to(rectangle3,UP)
        txt4.next_to(rectangle4, UP)
        matrix7.move_to(rectangle3.get_center())
        matrix8.move_to(rectangle4.get_center())

        # 将虚线和长方形添加到场景中
        self.add(line4, line5, line6, rectangle3,txt3, rectangle4,txt4,
                 matrix7,matrix8)
        self.wait(1)

class AllGather(Scene):
    def construct(self):
        # 创建三条虚线,
        line1 = DashedLine(start=[-6, -2, 0], end=[-6, 2, 0], color=BLUE)
        line2 = DashedLine(start=[-4, -2, 0], end=[-4, 2, 0], color=BLUE)
        line3 = DashedLine(start=[-2, -2, 0], end=[-2, 2, 0], color=BLUE)
        # 创建两个长方形
        rectangle1 = Rectangle(width=1, height=2, color=GREEN).shift(LEFT * 5)
        rectangle2 = Rectangle(width=1, height=2, color=GREEN).shift(LEFT * 3)

        #创建两个矩阵
        matrix1 = Matrix([[1, 2], [3, 4]])
        matrix2 = Matrix([[5, 6], [7, 8]])

        #matrix 缩小
        matrix1.scale(0.35)
        matrix2.scale(0.35)
        #创建两个文字
        txt1 = Text("rank01", color=BLUE, font_size=30)
        txt2 = Text("rank02",color=BLUE,font_size=30)

        #文字移动到长方形上方
        txt1.next_to(rectangle1,UP)
        txt2.next_to(rectangle2,UP)
        #举证移动到长方形内部
        matrix1.move_to(rectangle1.get_center())
        matrix2.move_to(rectangle2.get_center())

        # 将虚线和长方形添加到场景中
        self.add(line1,txt1,matrix1,line2,txt2,matrix2, line3, rectangle1,rectangle2)
        self.wait(1)

        #创建一个箭头
        arrow1 = Arrow([-1.5, 0, 0], [1.5, 0, 0])


        #添加文字，并至于箭头上方
        arrow1_txt1 = Text("all-gather",color=BLUE,font_size=30)
        arrow1_txt1.next_to(arrow1, UP)

        #添加将两个矩阵的加法过程至于箭头下方
        matrix5 = copy.deepcopy(matrix1)
        matrix6 = copy.deepcopy(matrix2)
        matrix5.set_color(BLUE)
        matrix6.set_color(BLUE)
        result_matrix = Matrix([[1 , 2 ,3,4], [5,6,7,8]])
        val_name = Text("out",color=BLUE,font_size=30)
        txt_equal = Text("=",color=BLUE,font_size=30)

        result_matrix.scale(0.3)
        val_name.scale(0.5)
        txt_equal.scale(0.3)
        result_matrix.set_color(BLUE)
        matrix_group = VGroup(val_name,txt_equal,matrix5, matrix6)
        matrix_group.arrange(RIGHT,buff=0.1)
        arrow1_center = arrow1.get_center()
        matrix_group.move_to(arrow1_center).shift(DOWN/2)
        self.play(Write(matrix_group))

        #创建3条虚线
        self.play(Create(arrow1),Create(arrow1_txt1),run_time=0.5)
        line4 = DashedLine(start=[2, -2, 0], end=[2, 2, 0], color=BLUE)
        line5 = DashedLine(start=[4, -2, 0], end=[4, 2, 0], color=BLUE)
        line6 = DashedLine(start=[6, -2, 0], end=[6, 2, 0], color=BLUE)


        # 创建两个长方形，并将result_matrix 放在里面
        matrix7 = copy.deepcopy(result_matrix)
        matrix8 = copy.deepcopy(result_matrix)
        txt_val1 = copy.deepcopy(val_name)
        txt_val2 = copy.deepcopy(val_name)
        rectangle3 = Rectangle(width=1, height=2, color=GREEN).shift(RIGHT * 5)
        rectangle4 = Rectangle(width=1, height=2, color=GREEN).shift(RIGHT * 3)
        txt3 = Text("rank01", color=BLUE, font_size=30)
        txt4 = Text("rank02", color=BLUE, font_size=30)
        txt3.next_to(rectangle3,UP)
        txt4.next_to(rectangle4, UP)
        # matrix7.move_to(rectangle3.get_center())
        # matrix8.move_to(rectangle4.get_center())
        txt_val1.move_to(rectangle3.get_center())
        txt_val2.move_to(rectangle4.get_center())

        # 将虚线和长方形添加到场景中
        self.add(line4, line5, line6, rectangle3,txt_val1, rectangle4,txt_val2)
        self.wait(1)
class ReduceScatter(Scene):
    def construct(self):
        # 创建三条虚线,
        line1 = DashedLine(start=[-6, -2, 0], end=[-6, 2, 0], color=BLUE)
        line2 = DashedLine(start=[-4, -2, 0], end=[-4, 2, 0], color=BLUE)
        line3 = DashedLine(start=[-2, -2, 0], end=[-2, 2, 0], color=BLUE)
        # 创建两个长方形
        rectangle1 = Rectangle(width=1, height=2, color=GREEN).shift(LEFT * 5)
        rectangle2 = Rectangle(width=1, height=2, color=GREEN).shift(LEFT * 3)

        #创建两个矩阵
        matrix1 = Matrix([[1, 2], [3, 4]])
        matrix2 = Matrix([[5, 6], [7, 8]])

        #matrix 缩小
        matrix1.scale(0.35)
        matrix2.scale(0.35)
        #创建两个文字
        txt1 = Text("rank01", color=BLUE, font_size=30)
        txt2 = Text("rank02",color=BLUE,font_size=30)

        #文字移动到长方形上方
        txt1.next_to(rectangle1,UP)
        txt2.next_to(rectangle2,UP)
        #举证移动到长方形内部
        matrix1.move_to(rectangle1.get_center())
        matrix2.move_to(rectangle2.get_center())

        # 将虚线和长方形添加到场景中
        self.add(line1,txt1,matrix1,line2,txt2,matrix2, line3, rectangle1,rectangle2)
        self.wait(1)

        #创建一个箭头
        arrow1 = Arrow([-1.5, 0, 0], [1.5, 0, 0])


        #添加文字，并至于箭头上方
        arrow1_txt1 = Text("reduce-scatter",color=BLUE,font_size=30)
        arrow1_txt1.next_to(arrow1, UP)

        #添加将两个矩阵的加法过程至于箭头下方
        # matrix5 = Matrix([[1, 2], [3, 4]])
        # matrix6 = Matrix([[5, 6], [7, 8]])
        matrix5 = copy.deepcopy(matrix1)
        matrix6 = copy.deepcopy(matrix2)
        matrix5.set_color(BLUE)
        matrix6.set_color(BLUE)
        txt_plus = Text("+", color=BLUE, font_size=30)
        txt_equal = Text("=", color=BLUE, font_size=30)
        result_matrix = Matrix([[1 + 5, 2 + 6], [3 + 7, 4 + 8]])
        txt_plus.scale(0.5)
        txt_equal.scale(0.5)
        result_matrix.scale(0.3)
        result_matrix.set_color(BLUE)
        matrix_group = VGroup(matrix5,txt_plus, matrix6,  txt_equal, result_matrix)
        matrix_group.arrange(RIGHT,buff=0.1)
        arrow1_center = arrow1.get_center()
        matrix_group.move_to(arrow1_center).shift(DOWN/2)
        self.play(Write(matrix_group))

        #创建3条虚线
        self.play(Create(arrow1),Create(arrow1_txt1),run_time=0.5)
        line4 = DashedLine(start=[2, -2, 0], end=[2, 2, 0], color=BLUE)
        line5 = DashedLine(start=[4, -2, 0], end=[4, 2, 0], color=BLUE)
        line6 = DashedLine(start=[6, -2, 0], end=[6, 2, 0], color=BLUE)


        # 创建两个长方形，并将result_matri拆分成两份 放在里面

        rectangle3 = Rectangle(width=1, height=2, color=GREEN).shift(RIGHT * 5)
        rectangle4 = Rectangle(width=1, height=2, color=GREEN).shift(RIGHT * 3)
        txt3 = Text("rank01", color=BLUE, font_size=30)
        txt4 = Text("rank02", color=BLUE, font_size=30)
        txt3.next_to(rectangle3,UP)
        txt4.next_to(rectangle4, UP)
        matrix7 = Matrix([[6, 8]])
        matrix8 = Matrix([[10, 12]])
        matrix7.scale(0.3)
        matrix8.scale(0.3)
        matrix7.move_to(rectangle3.get_center())
        matrix8.move_to(rectangle4.get_center())

        # 将虚线和长方形添加到场景中
        self.add(line4, line5, line6, rectangle3,txt3, rectangle4,txt4,
                 matrix7,matrix8)
        self.wait(1)















