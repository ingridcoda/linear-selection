def sort_selection(a, k):
    a = bubble_sort(a)
    return a[k - 1]


def bubble_sort(a):
    for i in range(len(a)):
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp
    return a
