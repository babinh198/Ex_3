
result = []
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            if a * c + b == 10 * c:
                result.append([a, b, c])
print(result)

## [[1, 9, 1], [2, 8, 1], [3, 7, 1], [4, 6, 1], [5, 5, 1], [6, 4, 1], [6, 8, 2], [7, 3, 1], [7, 6, 2], [7, 9, 3], [8, 2, 1], [8, 4, 2], [8, 6, 3], [8, 8, 4], [9, 1, 1], [9, 2, 2], [9, 3, 3], [9, 4, 4], [9, 5, 5], [9, 6, 6], [9, 7, 7], [9, 8, 8], [9, 9, 9]]
