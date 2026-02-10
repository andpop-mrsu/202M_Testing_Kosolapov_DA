import math

def solve_quadratic(a, b, c):
    if a == 0:
        if b == 0:
            return []
        return [-c / b]

    d = b**2 - 4*a*c

    if d < 0:
        return []

    if d == 0:
        x = -b / (2 * a)
        return [x]

    sqrt_d = math.sqrt(d)
    x1 = (-b - sqrt_d) / (2 * a)
    x2 = (-b + sqrt_d) / (2 * a)

    return sorted([x1, x2])

if __name__ == "__main__":
    test_cases = [
        (1, -5, 6), 
        (1, -4, 4),  
        (1, 2, 5),   
        (-1, 1, 6),
        (0, 2, -4),
        (1, 0, -9),
        (2, -8, 0),
        (0, 0, 0),
        (4, 0, -1)
    ]

    for a, b, c in test_cases:
        print(f"Коэффициенты: a={a}, b={b}, c={c}; корни: {solve_quadratic(a, b, c)}")