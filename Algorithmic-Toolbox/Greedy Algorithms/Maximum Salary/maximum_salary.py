# python3

from itertools import permutations


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest


def largest_number(numbers):
    numbers = list(map(str, numbers))
    # naive sort
    numbers.sort(reverse=True)

    # else check element wise moving largest number to the front.
    for _ in numbers:
        for i in range(len(numbers) - 1):
            if numbers[i] + numbers[i + 1] < numbers[i + 1] + numbers[i]:
                curr_ = numbers[i]
                numbers[i] = numbers[i + 1]
                numbers[i + 1] = curr_

    return int("".join(numbers))


if __name__ == '__main__':
    n = int(input())
    input_numbers = input().split()
    assert len(input_numbers) == n
    print(largest_number(input_numbers))
