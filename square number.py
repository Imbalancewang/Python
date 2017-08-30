from math import sqrt
#x,y=input('please input two numbers : x,y')
for n in range(80,90):
    root=sqrt(n)
    if root==int(root):
        flag=1
        break
    else:
        flag=0;
