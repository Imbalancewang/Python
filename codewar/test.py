#coding=utf-8
class sol(object):
    def __init__(self,board):
        self.b = board
    def check(self,x,y,value):
        for row_item in self.b[x]:
            if row_item == value:
                return False
        for row_all in self.b:
            if row_all[y] == value:
                return False
        row,col=x/3*3,y/3*3
        row3col3=self.b[row][col:col+3]+self.b[row+1][col:col+3]+self.b[row+2][col:col+3]
        for row3col3_item in row3col3:
            if row3col3_item == value:
                return False
        return True#conflict function

    def get_next(self,x,y):
        for next_soulu in range(y+1,9):
            if self.b[x][next_soulu] == 0:
                return x,next_soulu
        for row_n in range(x+1,9):
            for col_n in range(0,9):
                if self.b[row_n][col_n] == 0:
                    return row_n,col_n
        return -1,-1

    def try_it(self,x,y):
        if self.b[x][y] == 0:
            for i in range(1,10):
                if self.check(x,y,i):
                    self.b[x][y]=i
                    next_x,next_y=self.get_next(x,y)
                    if next_x == -1:
                        return True
                    else:
                        end=self.try_it(next_x,next_y)
                        if not end:
                            self.b[x][y] = 0
                        else:
                            return True

    def start(self):
        if self.b[0][0] == 0:
            self.try_it(0,0)
        else:
            x,y=self.get_next(0,0)
            self.try_it(x,y)
        return
def sudoku(puzzle):
    s=sol(puzzle)
    s.start()
    return s.b
puzzle = [[0, 0, 6, 1, 0, 0, 0, 0, 8],
          [0, 8, 0, 0, 9, 0, 0, 3, 0],
          [2, 0, 0, 0, 0, 5, 4, 0, 0],
          [4, 0, 0, 0, 0, 1, 8, 0, 0],
          [0, 3, 0, 0, 7, 0, 0, 4, 0],
          [0, 0, 7, 9, 0, 0, 0, 0, 3],
          [0, 0, 8, 4, 0, 0, 0, 0, 6],
          [0, 2, 0, 0, 5, 0, 0, 8, 0],
          [1, 0, 0, 0, 0, 2, 5, 0, 0]]
s=sudoku_solver(puzzle)
print s