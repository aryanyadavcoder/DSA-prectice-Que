A = [[2,3],
     [1,4]]
B = [[5,1],
     [2,6]] 

result = []
for i in range(len(A)):
    row = []
    for j in range(len(A[0])):
        row.append(A[i][j] + B[i][j])     
    result.append(row) 
print("Addition Result :")
for r in result:
    print(r) 


    
   
    
    
           
    