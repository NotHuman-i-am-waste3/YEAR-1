import itertools
digits = [1, 2, 3]
for L in range(0, len(digits)+1):
    for subset in itertools.combinations(digits, L):
        print(subset)