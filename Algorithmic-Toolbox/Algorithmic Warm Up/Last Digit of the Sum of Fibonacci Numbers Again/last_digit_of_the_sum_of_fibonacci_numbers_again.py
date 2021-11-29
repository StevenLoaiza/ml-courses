# python3


def last_digit_of_the_sum_of_fibonacci_numbers_again_naive(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    if to_index == 0:
        return 0

    fibonacci_numbers = [0] * (to_index + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, to_index + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum(fibonacci_numbers[from_index:to_index + 1]) % 10


def last_digit_of_the_sum_of_fibonacci_numbers_again(n):
    assert 0 <= n <= 10 ** 18

    n = n % 60
    prev, curr = 0, 1

    for i in range(2, n+1):
        prev, curr = curr, prev + curr

    return (curr * (prev + curr)) % 10

def reference(from_index, to_index):
    return (20 + fibonacci_sum_last_digit(to_index + 2) - fibonacci_sum_last_digit(from_index + 1)) % 10


if __name__ == '__main__':
    input_from, input_to = map(int, input().split())
    print(last_digit_of_the_sum_of_fibonacci_numbers_again(input_from, input_to))
