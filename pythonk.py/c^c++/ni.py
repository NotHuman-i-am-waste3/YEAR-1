def product(x, y):
    result = []
    while x >= 1:
        if x%2 != 0:
            result.append([x, y])
        x //= 2
        y *= 2
    return reversed(result)


x = int(input())
y = int(input())
for i in product(x, y):
        print(*i)
print(x*y)