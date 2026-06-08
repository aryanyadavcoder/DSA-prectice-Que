h = 23
m = 50
addm = 25
one_h = 60
one_day = one_h*24
one_h = 60
total_min = h*one_h+m+addm
print(total_min)
d = total_min%one_day
print(d)
ah = total_min//one_h
am = total_min%one_h
print(ah,am)



