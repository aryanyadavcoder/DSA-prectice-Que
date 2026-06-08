a = [1, 3, 7, 9]
b = [2, 5, 8, 10]
c = []
l = 0
m = 0

while l < len(a) and m < len(b):
    if a[l] < b[m]:
        c.append(a[l])
        l += 1
    else:
        c.append(b[m])
        m += 1  
print(c)        
