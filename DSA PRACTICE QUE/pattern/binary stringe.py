n = 3

for i in range(2 ** n):

    num = i
    binary = ""

    for j in range(n):

        rem = num % 2
        binary = str(rem) + binary

        num = num // 2

    print(binary)