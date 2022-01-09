# python3
import math

def linear_search(keys, query):
    for i in range(len(keys)):
        if keys[i] == query:
            return i

    return -1

    left, right = 0, len(keys)
    while left + 1 < right:
        ave = (left + right) // 2
        if keys[ave] <= query:
            left = ave
        else:
            right = ave
    if keys[left] != query:
        return -1
    else:
        return left

def binary_search(keys, query, low=0, high=None):
    """
    #
    :param keys:
    :param query:
    :param low:
    :param high:
    :return:
    """
    assert all(keys[i] < keys[i + 1] for i in range(len(keys) - 1))
    assert 1 <= len(keys) <= 3 * 10 ** 4
    if high is None:
        high = len(keys) - 1
    if high < low:
        return -1
    elif keys[low] == query:
        return low
    elif keys[high] == query:
        return high

    mid = (low + high)//2
    if query == keys[mid]:
        return mid
    elif query < keys[mid]:
        return binary_search(keys, query, low, mid - 1)
    else:
        return binary_search(keys, query, mid + 1, high)


if __name__ == '__main__':
    input_keys = list(map(int, input().split()))[1:]
    input_queries = list(map(int, input().split()))[1:]

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
