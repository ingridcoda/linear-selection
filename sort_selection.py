import math


def sort_selection(a, k):
    a = bubble_sort(a)
    return a[k-1]  # TODO: talvez deveria ser o k-1, uma vez que os indices de arrays em Python comecam com 0 e não com 1.


def bubble_sort(a):
    # print(f"Original array: {a}")
    for i in range(len(a)):
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    # print(f"Sorted array: {a}")
    return a


# vet = [8, 7, 6, 5, 4, 3, 2, 2, 2, 1]
# k = math.ceil(len(vet) / 2)
# print(f"Getting {k}-th item from {vet} using Sort Selection...")
# result = sort_selection(vet, k)
# print(f"Result: {result}")
