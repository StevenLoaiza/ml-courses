# python3


def last_digit_of_the_sum_of_squares_of_fibonacci_numbers_naive(n):
    assert 0 <= n <= 10 ** 18

    if n <= 1:
        return n

    fibonacci_numbers = [0] * (n + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, n + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum([f ** 2 for f in fibonacci_numbers]) % 10

def check_repeat(n):
    """Check if sequence repeats
    Hint: Try n=119, repeats after 60.
    """
    assert (n+1) % 2 == 0
    return_ls = list(range(n+1))
    for i in range(n+1):
        return_ls[i] = last_digit_of_the_sum_of_squares_of_fibonacci_numbers_naive(i)

    idx = int((n+1)/2)
    if return_ls[:idx] != return_ls[idx:]:
        print('Sequence does not repeat')
    else:
        print('Sequence repeats at n = %s' % (n+1/2))

def last_digit_of_the_sum_of_squares_of_fibonacci_numbers(n):
    assert 0 <= n <= 10 ** 18

    if n <= 1:
        return n

    n = n % 60
    prev, curr = 0, 1

    for i in range(2, n+2):
        prev, curr = curr, prev + curr

    return (prev * curr) % 10


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_the_sum_of_squares_of_fibonacci_numbers(input_n))
