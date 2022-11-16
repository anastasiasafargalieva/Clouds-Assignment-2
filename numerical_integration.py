from math import sin

def trapezoid(a, b, n):
    

    res = 0

    h = (b - a) / n

    x = a

    for _ in range(1, n):
        x += h
        res += abs(sin(x))
    res *= 2

    # evaluate function at a and b and add to final result
    res += abs(sin(a))
    res += abs(sin(b))

    # divide h by 2 and multiply by bracketed term
    return (h / 2) * res

n = [5, 10, 100, 1000, 10000, 100000, 1000000]

for i in n:
    print(trapezoid(0, 3.14159, i))