n = 7
for row in range(1,n+1):
    for col in range(1,n+1):
        condition = (row>=1 and row<=7 and col==n) or (row==n and col>=1 and col<=7) or (row+col==8)
        if condition: 
            print(0,end="")
        else:
            print(" ",end="")
    print()                