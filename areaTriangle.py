import math
import sys

def areaTriangle(a,b,c):
    s=(a+b+c)/2
    return math.sqrt(s*(s-a)*(s-b)*(s-c))

print(sys.argv[0],sys.argv[1],sys.argv[2],sys.argv[3])

a=int(sys.argv[1])
b=int(sys.argv[2])
c=int(sys.argv[3])

if ( a+b>c and b+c>a and c+a>b ):
    area = areaTriangle(a,b,c)
    print(area)

else :
    print("Invalid Combination! Triangle cannot be formed")
