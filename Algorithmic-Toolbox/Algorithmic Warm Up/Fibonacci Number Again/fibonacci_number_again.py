# python3


def fibonacci_number_again_naive(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3
    if n <= 1:
        return n
    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m
    return current

def find_pisano(m):
    """ find pisano period

    :param m: modular
    :return: period
    """
    p, c = 0, 1
    seq = [p, c]
    for _ in range(m*m):
        p, c = c, (p + c) % m
        seq.append(c)
        if (p, c) == (0, 1):
            break
    return seq[:-2], len(seq[:-2])

def fibonacci_number_again(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3
    seq, seq_sz = find_pisano(m)
    return seq[n % seq_sz]

if __name__ == '__main__':
    input_n, input_m = map(int, input().split())
    print(fibonacci_number_again(input_n, input_m))
