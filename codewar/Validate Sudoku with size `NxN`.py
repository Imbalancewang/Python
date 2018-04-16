# -*- coding: utf-8 -*-
# @Time    : 2018/1/24 21:08
# @Author  : Matthew
# @Site    : 
# @File    : Validate Sudoku with size `NxN`.py
# @Software: PyCharm
#a little problem has arisen cannot pass the example6 invaild
from math import sqrt
class Sudoku(object):
    #your code here
    def __init__(self,matrix):
        self.matrix=matrix
        self.size=len(matrix)
        self.smallsize=int(sqrt(self.size))
    def is_valid(self):
        if(self.size!=len(self.matrix[0])):return False
        correct=range(1,self.size+1)
        for x in self.matrix:
            if(correct!=sorted(x)):return False
        for x in zip(*self.matrix):
            if (correct != sorted(x)): return False
        for i in range(0,self.size,self.smallsize):
            for j in range(0, self.size, self.smallsize):
                res=[]
                for p in range(0,self.smallsize):
                    for q in range(0,self.smallsize):
                        res.append(self.matrix[i+p][j+q])
                if(correct!=sorted(res)):return False
        return True
goodSudoku1 = Sudoku([
    [7, 8, 4, 1, 5, 9, 3, 2, 6],
    [5, 3, 9, 6, 7, 2, 8, 4, 1],
    [6, 1, 2, 4, 3, 8, 7, 5, 9],

    [9, 2, 8, 7, 1, 5, 4, 6, 3],
    [3, 5, 7, 8, 4, 6, 1, 9, 2],
    [4, 6, 1, 9, 2, 3, 5, 8, 7],

    [8, 7, 6, 3, 9, 4, 2, 1, 5],
    [2, 4, 3, 5, 6, 1, 9, 7, 8],
    [1, 9, 5, 2, 8, 7, 6, 3, 4]
])

goodSudoku2 = Sudoku([
    [1, 4, 2, 3],
    [3, 2, 4, 1],

    [4, 1, 3, 2],
    [2, 3, 1, 4]
])

# Invalid Sudoku
badSudoku1 = Sudoku([
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],

    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],

    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
])

badSudoku2 = Sudoku([
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1]
])
goodSudoku3=Sudoku([[1]])
print badSudoku1.is_valid()
print badSudoku2.is_valid()
print goodSudoku1.is_valid()
print goodSudoku2.is_valid()
print goodSudoku3.is_valid()



