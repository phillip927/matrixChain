# -*- coding:utf-8 -*-
"""
-- Author:phil
-- Time: 2024/12/30 17:50
-- Title: matrixChain.py
-- Software: PyCharm
"""
import numpy as np
from ttkbootstrap import Style
from showMatrix import show_matrix
import ttkbootstrap as ttk

class matrix_chain():
    def __init__(self,width=900,row_num=3,width_resizable=False,height_resizable=True,
                 text_fill="#813f09",text_title_fill="#813f09",arrow_fill="black"):
        self.window = Style(theme="pulse").master
        self.window.title("矩阵链路展示")
        self.width = width
        self.num = row_num
        self.window.geometry(f'{self.width}x400+400+200')
        self.window.resizable(width=width_resizable, height=height_resizable)  # 阻止Python GUI的大小调整 False
        self.max_num = 0
        self.order_dict = {}
        self.text_fill = text_fill
        self.text_title_fill = text_title_fill
        self.arrow_fill = arrow_fill

    # 主函数
    def machain_run(self):
        for item in self.order_dict:
            matrix_dict = self.order_dict[item]
            matrix = matrix_dict["matrix"]
            matrix_title = matrix_dict["matrix_title"]
            order_num = matrix_dict["order_num"]
            self.matrix_print(matrix,matrix_title,order_num)
        self.window.mainloop()

    def marix_dict(self,matrix=None,matrix_title="",order_num=0):
        name = "order_num_" + str(order_num)
        m,n = matrix.shape
        matrix_title = matrix_title+"("+str(m)+"x"+str(n)+")"
        self.order_dict[name] = {"matrix": matrix, "matrix_title": matrix_title, "order_num": order_num}
        self.max_num = order_num

    def matrix_print(self,matrix,matrix_title,order_num):
        num = self.num
        width = self.width / num        # 900/2 = 450
        row = int((order_num-1) / num)  # 450 /2 225
        column = int(((order_num-1) % num) * 2)

        canvas = ttk.Canvas(self.window, width=width*(9/10), height=130)
        canvas.grid(row=row, column=column, padx=2, pady=2)
        # 创建文本 make a text and text title
        canvas.create_text(width/2,60,text=show_matrix(matrix), fill=self.text_fill)
        canvas.create_text(width/2,120,text=matrix_title, fill=self.text_title_fill)
        # 画箭头 draw an arrow
        if order_num != self.max_num:
            self.arrow_print(row, column + 1)

    def arrow_print(self, row,column):
        canvas = ttk.Canvas(self.window, width=15, height=130)
        canvas.grid(row=row, column=column, padx=0, pady=0)
        # 绘制一个箭头 draw an arrow
        canvas.create_line(15, 60, 0, 60, fill=self.arrow_fill, width=3, arrow=ttk.FIRST, arrowshape=(10, 10, 5))

if __name__ == '__main__':
    app = matrix_chain()
    app.marix_dict(np.ones((9, 9)),"原始矩阵",1)
    app.marix_dict(np.ones((9, 9))*2, "变化矩阵1", 2)
    app.marix_dict(np.ones((9, 9))*3, "变化矩阵2", 3)
    app.marix_dict(np.ones((9, 9))*4, "变化矩阵3", 4)
    app.marix_dict(np.zeros((587, 5)), "变化矩阵4", 5)
    app.machain_run()

