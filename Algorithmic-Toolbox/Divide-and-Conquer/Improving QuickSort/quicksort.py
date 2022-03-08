# python3

from random import randint


def partition3(array, left, right):
    """
    Paritions the array into two section, left side is less than the pivot, right side is greater than the pivot.
    It ensures that we avoid a recursive call when there are multiple values for the pivot (no need to sort them).
    :param array: 
    :param left: 
    :param right: 
    :return: 
    """
    x = array[left]  # Pivot
    j = left
    for i in range(left + 1, right + 1):
        if array[i] < x:
            j = j + 1  # increment position j
            array[j], array[i] = array[i], array[j]
    array[j], array[left] = array[left], array[j]

    x = array[j]  # Pivot
    jj = j
    for i in range(jj + 1, right + 1):
        if array[i] == x:
            jj = jj + 1  # increment position j
            array[jj], array[i] = array[i], array[jj]

    return j, jj


def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]
    m1, m2 = partition3(array, left, right)
    randomized_quick_sort(array, left, m1)
    randomized_quick_sort(array, m2 + 1, right)


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
