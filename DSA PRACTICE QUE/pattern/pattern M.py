n = 7
for row in range(1,n+1):
    for col in range(1,n+1):
        condition = (row>=1 and col==1) or (row == col and row>1 and row<=4 )or(row+col ==n+1 and row>=1 and row<=4 ) or (col==n and row>=1 and row<=7)
        if condition: 
            print(0,end="")
        else:
            print(" ",end="")
    print()                