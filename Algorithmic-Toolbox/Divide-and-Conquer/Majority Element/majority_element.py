# python3


def majority_element_naive(elements):
    assert len(elements) <= 10 ** 5
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0


def majority_element(elements):
    assert len(elements) <= 10 ** 5
    mid = len(elements)//2
    L = elements[:mid]
    H = elements[mid:]

    majority = 0
    for half in [L, H]:
        for e in half:
            if half.count(e) > len(half) / 2:
                candidate = e
                if elements.count(candidate) > len(elements) / 2:
                    majority = 1
                    break

    return majority


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element(input_elements))
