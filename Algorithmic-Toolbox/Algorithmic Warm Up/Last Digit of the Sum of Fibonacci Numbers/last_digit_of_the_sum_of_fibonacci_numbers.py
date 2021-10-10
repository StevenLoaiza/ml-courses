# python3


def last_digit_of_the_sum_of_fibonacci_numbers_naive(n):
    assert 0 <= n <= 10 ** 18

    if n <= 1:
        return n

    fibonacci_numbers = [0] * (n + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, n + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum(fibonacci_numbers) % 10


def last_digit_of_the_sum_of_fibonacci_numbers(n):
    """ Last Digit of sum of the nth fib

    Trick: The last digit of the sum repeats after the 60th round
    :param n:
    :return:
    """
    assert 0 <= n <= 10 ** 18

    if n <= 2:
        return n

    n = n % 60
    f_ = list(range(n+1))
    for i in range(2, len(f_)):
        f_[i] = f_[i-1] + f_[i-2]

    return sum(f_) % 10


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_the_sum_of_fibonacci_numbers(input_n))
