def repeat(xs, n):
    if (n < 0):
        return ValueError

    result = []
    for _ in range(n):
        for i in range(len(xs)):
            result.append(xs[i])

    return result

xs = [1, 2, 3]
print(repeat(xs, 0))