a = [3, 4,1, 9, -6, -3]
n = len(a)
print("Start",a)
for i in range(n-1):
    for j in range(n-1):
        if a[j]<a[j+1]:
            a[j] , a[j+1] = a[j+1] , a[j] 
print("Final descending",a)

for i in range(n-1):
    for j in range(n-1):
        if a[j]>a[j+1]:
            a[j] , a[j+1] = a[j+1] , a[j]             

print("Final ascending",a)
