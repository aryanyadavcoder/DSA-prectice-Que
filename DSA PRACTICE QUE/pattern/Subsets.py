items = [1, 2, 3]
subsets = [[]]

for item in items:
    new_subsets = []
    for subset in subsets:
        new_subset = subset + [item]
        new_subsets.append(new_subset)
    subsets = subsets + new_subsets
for subset in subsets:
    print(subset)