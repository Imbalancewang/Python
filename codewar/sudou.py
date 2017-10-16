__metatype__=type
class shudou:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.value=range(1,10)
def assign(puzzle):
    final=[[],[],[],[],[],[],[],[],[]]
    for i in range(9):
        for j in range(9):
            temp=shudou(i,j)
            if puzzle[i][j]!=0:
                temp.value=[puzzle[i][j]]
            else:
                for k in range(9):
                    if puzzle[k][j]!=0 and puzzle[k][j] in temp.value:
                        temp.value.remove(puzzle[k][j])#horizon line
                    if puzzle[i][k]!=0 and puzzle[i][k] in temp.value:
                        temp.value.remove(puzzle[i][k])#vertical line
                for m in range(3):
                    for n in range(3):
                        if puzzle[3*(i//3)+m][3*(j//3)+n]!=0 and puzzle[3*(i//3)+m][3*(j//3)+n] in temp.value:
                            temp.value.remove(puzzle[3*(i//3)+m][3*(j//3)+n])#9-gongge
            final[i].append(temp)
    return final
def cal(final):
    flag=0
    """for i in range(9):
        for j in range(9):
            if len(final[i][j].value)>1:
                for k in range(9):
                    if len(final[k][j].value)==1 and final[k][j].value[0] in final[i][j].value and k!=i:
                        final[i][j].value.remove(final[k][j].value[0])
                        flag=1
                    if len(final[i][k].value)==1 and final[i][k].value[0] in final[i][j].value and k!=j:
                        final[i][j].value.remove(final[i][k].value[0])
                        flag=1"""
    """  for m in range(3):
                    for n in range(3):
                        if len(final[3*(i//3)+m][3*(j//3)+n].value)==1 and final[3*(i//3)+m][3*(j//3)+n].value[0]
                            in final[i][j].value and not(3*(i//3)+m==i and 3*(j//3)+n==j):
                            final[i][j].value.remove(final[3*(i//3)+m][3*(j//3)+n].value[0])
                            flag=1"""
    if flag==0:
        return final
    else:cal(final)
def sudoku(puzzle):
    """return the solved puzzle as a 2d array of 9 x 9"""

    return puzzle
puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]
final=assign(puzzle)
qq=cal(final)
print qq
solution = [[5,3,4,6,7,8,9,1,2],
            [6,7,2,1,9,5,3,4,8],
            [1,9,8,3,4,2,5,6,7],
            [8,5,9,7,6,1,4,2,3],
            [4,2,6,8,5,3,7,9,1],
            [7,1,3,9,2,4,8,5,6],
            [9,6,1,5,3,7,2,8,4],
            [2,8,7,4,1,9,6,3,5],
            [3,4,5,2,8,6,1,7,9]]
