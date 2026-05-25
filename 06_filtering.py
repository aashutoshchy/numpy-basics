import numpy as np

ages = np.array([[21, 43, 12, 34, 17, 52],
                 [56, 15, 22, 16, 20, 67]])

teenagers = ages[ages <= 18]
adults = ages[(ages > 18) & (ages < 65)]
evens = ages[ages % 2 == 0]
odds = ages[ages % 2 != 0]

print(teenagers)
print(adults)
print("Evens: ", evens)
print("Odds: ", odds)