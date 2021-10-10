# python3


def fibonacci_number_naive(n):
    assert 0 <= n <= 45

    if n <= 1:
        return n

    return fibonacci_number_naive(n - 1) + fibonacci_number_naive(n - 2)


def fibonacci_number(n):
    assert 0 <= n <= 45

    f_array = list(range(n+1))
    for i in range(2, n+1):
        f_array[i] = f_array[i-1] + f_array[i-2]
    return f_array[-1]


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
