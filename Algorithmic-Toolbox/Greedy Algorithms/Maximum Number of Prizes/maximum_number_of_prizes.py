# python3


def compute_optimal_summands(n):
    assert 1 <= n <= 10 ** 9
    summands = []

    i = 1
    # Check if the next two sequence satisfy condition, else return [n]
    while i + i + 1 <= n:
        summands.append(i)
        n -= i
        i += 1
    summands.append(n)

    return summands


if __name__ == '__main__':
    input_n = int(input())
    output_summands = compute_optimal_summands(input_n)
    print(len(output_summands))
    print(*output_summands)
