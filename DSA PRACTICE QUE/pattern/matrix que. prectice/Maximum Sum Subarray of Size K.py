a = [2,1,5,1,3,2]
k = 3
n = len(a)
part = []
for i in range(k):
    part.append(a[i])
s = sum(part)
max_sum = s

print(f"{part}, sum = {s}, max_sum = {max_sum}")

for i in range(k,n):
    part.pop(0)
    part.append(a[i])

    s = sum(part)

    if s > max_sum:
        max_sum = s

    print(f"{part}, sum = {s}, max_sum = {max_sum}")

print("Max Sum =", max_sum)