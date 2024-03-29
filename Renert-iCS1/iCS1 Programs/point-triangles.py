import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def area(x1, y1, x2, y2, x3, y3):
    return abs((x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))/2)
 
def isInside(x1,y1,x2,y2,x3,y3,x,y):
    A = area (x1,y1,x2,y2,x3,y3)
    A1 = area (x,y,x2,y2,x3,y3)
    A2 = area (x1,y1,x,y,x3,y3)
    A3 = area (x1,y1,x2,y2,x,y)
    if(A==A1+A2+A3):
        return True
    else:
        return False

x,y=[int(i) for i in input().split()]
n=int(input())
for i in range(n):
    x1,y1,x2,y2,x3,y3=[int(j) for j in input().split()]
    if (isInside(x1,y1,x2,y2,x3,y3,x,y)):
        print('inside')
    else:
        print('outside')