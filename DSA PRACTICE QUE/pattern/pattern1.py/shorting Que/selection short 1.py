a = [1,4,7,6,-3,7]
l = len(a)
minpos = 0
for i in range(1,l):
     if a[i]<a[minpos]:
        minpos=i
print(f"Min={a[minpos]}, pos={minpos}")