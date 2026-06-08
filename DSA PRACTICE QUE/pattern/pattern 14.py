n = 7
mid = (n+1)//2
for row in range(1, n+1):
    for col in range(1, n+1):
        condition = row+col==8 or col==row
        if condition:
            print('*',end=" ")
        else:
            print(" ", end=" ")
    print() 
print()
