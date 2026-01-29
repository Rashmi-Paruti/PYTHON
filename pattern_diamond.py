# h = int(input("Enter diamond's height: "))
# for x in range(h):
#      print(" " * (h - x), "*" * (2*x + 1))
# for x in range(h - 2, -1, -1):
#      print(" " * (h - x), "*" * (2*x + 1))



a=int(input("enter size"))
for i in range(a):
    for j in range(a-i-1):
        print(" ",end=" ")
    for k in range(2*i+1):
        print("*",end=" ")
    print(" ")
for i in range(a-2,-1,-1):
    for j in range(a-i-1):
        print(" ",end=" ")
    for k in range(2*i+1):
        print("*",end=" ")
    print(" ")