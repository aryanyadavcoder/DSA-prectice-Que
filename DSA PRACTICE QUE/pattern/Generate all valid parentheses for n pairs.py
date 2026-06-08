n = 3

for a in ["(", ")"]:
    for b in ["(", ")"]:
        for c in ["(", ")"]:
            for d in ["(", ")"]:
                for e in ["(", ")"]:
                    for f in ["(", ")"]:
                        s = a + b + c + d + e + f

                        count = 0
                        valid = True

                        for ch in s:

                            if ch == "(":
                                count = count + 1
                            else:
                                count = count - 1

                            if count < 0:
                                valid = False

                        if count != 0:
                            valid = False

                        if valid:
                            print(s)
