# -*- coding:utf-8 -*-
"""
-- Author:phil
-- Time: 2024/12/31 14:59  
-- Title: showMatrix.py
-- Software: PyCharm
"""
import numpy as np

def show_m1(one_matrix):
    show_str = f""
    m, n = one_matrix.shape
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                show_str += "[["
                show_str += getStr(one_matrix[i, j])
                show_str += " "
            elif j != 0 and j != (n - 1):
                show_str += getStr(one_matrix[i, j])
                show_str += " "
            elif j == (n - 1) and i != (m - 1):
                show_str += getStr(one_matrix[i, j])
                show_str += "]"
                show_str += "\n"
            elif j == (n - 1) and i == (m - 1):
                show_str += getStr(one_matrix[i, j])
                show_str += f"]]"
            else:
                show_str += " ["
                show_str += getStr(one_matrix[i, j])
                show_str += " "
    return show_str

def show_m2(one_matrix):
    show_str = f""
    m, n = one_matrix.shape
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                show_str += "[["
                show_str += getStr(one_matrix[i, j])
                show_str += " "
            elif j == 0:
                show_str += " ["
                show_str += getStr(one_matrix[i, j])
                show_str += " "
            elif j == 1:
                show_str += getStr(one_matrix[i, j])
            elif j != 0 and j == n - 2:
                show_str += " ... "
                show_str += getStr(one_matrix[i, j])
                show_str += " "
            elif j == (n - 1) and i != (m - 1):
                show_str += getStr(one_matrix[i, j])
                show_str += "]"
                show_str += "\n"
            elif j == (n - 1) and i == (m - 1):
                show_str += getStr(one_matrix[i, j])
                show_str += f"]]"
    return show_str

def show_m3(one_matrix):
    show_str = f""
    m, n = one_matrix.shape
    for i in range(2):
        for j in range(n):
            if i == 0 and j == 0:
                show_str += "[["
                show_str += getStr(one_matrix[i, j])
                show_str += " "
            elif j != 0 and j != (n - 1):
                show_str += getStr(one_matrix[i, j])
                show_str += " "
            elif j == (n - 1) and i != (m - 1):
                show_str += getStr(one_matrix[i, j])
                show_str += "]"
                show_str += "\n"
            elif j == 0:
                show_str += " ["
                show_str += getStr(one_matrix[i, j])
                show_str += " "
    show_str += "     ...  ... " + "\n"
    for i in range(m - 2, m):
        for j in range(n):
            if j != 0 and j != (n - 1):
                show_str += getStr(one_matrix[i, j])
                show_str += " "
            elif j == (n - 1) and i != (m - 1):
                show_str += getStr(one_matrix[i, j])
                show_str += "]"
                show_str += "\n"
            elif j == 0:
                show_str += " ["
                show_str += getStr(one_matrix[i, j])
                show_str += " "
            elif j == (n - 1) and i == (m - 1):
                show_str += getStr(one_matrix[i, j])
                show_str += f"]]"
    return show_str

def show_m4(one_matrix):
    show_str = f""
    m, n = one_matrix.shape
    show_str += "[[" + getStr(one_matrix[0, 0]) + " " + getStr(one_matrix[0, 1]) + " ... " + getStr(one_matrix[0, n - 2]) + " " + getStr(one_matrix[0, n - 1]) + "]" + "\n"
    show_str += " [" + getStr(one_matrix[1, 0]) + " " + getStr(one_matrix[1, 1]) + " ... " + getStr(one_matrix[1, n - 2]) + " " + getStr(one_matrix[1, n - 1]) + "]" + "\n"
    show_str += "     ...   ...   ... " + "\n"
    show_str += " [" + getStr(one_matrix[m - 2, 0]) + " " + getStr(one_matrix[m - 2, 1]) + " ... " + getStr(one_matrix[m - 2, n - 2]) + " " + getStr(one_matrix[m - 2, n - 1]) + "]" + "\n"
    show_str += " [" + getStr(one_matrix[m - 1, 0]) + " " + getStr(one_matrix[m - 1, 1]) + " ... " + getStr(one_matrix[m - 1, n - 2]) + " " + getStr(one_matrix[m - 1, n - 1]) + f"]]"
    return show_str


def getStr(data,length=10):
    # 处理矩阵中元素显示格式
    if type(data) == np.float64:
        strText = round(data,2)
        return str(strText)
    elif type(data) == np.int32:
        strText = str(data)
        return str(strText)
    else:
        strText = str(data)[0:length]
        return strText

def show_matrix(one_matrix):
    if one_matrix.ndim==2:
        show_str = f""
        m, n = one_matrix.shape
        if m <= 4 and n <= 4:
            show_str = show_m1(one_matrix)
        elif m == 4 and n > 4:
            show_str = show_m2(one_matrix)
        elif m > 4 and n == 4:
            show_str = show_m3(one_matrix)
        elif m > 4 and n > 4:
            show_str = show_m4(one_matrix)
        return show_str
    else:
        print("sorry,your matrix's dim not equal two in the matrixChain!")

if __name__ == '__main__':
    one_matrix = np.ones((4,4))
    # one_matrix = np.array([0,2,3,4,5])
    show_str = show_matrix(one_matrix)
    print(show_str)
