import sys
while 1:
    tri = list(map(int, sys.stdin.readline().split()))
    if tri == [0,0,0]:
        break
    tri.sort()
    
    if tri[2] >= tri[0] + tri[1]:
        print("Invalid")
    else:
        if len(set(tri)) == 1:
            print("Equilateral")
        elif len(set(tri)) == 2:
            print("Isosceles")
        else:
            print("Scalene")