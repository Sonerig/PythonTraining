def is_prime(foo):
    def wrapper(a, b, c):
        for i in range(2, num := foo(a, b, c)):
            if num % i == 0:
                return f"Составное\n{num}"
        return f"Простое\n{num}"
    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)
