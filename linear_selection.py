def linear_selection(a, k):
    if len(a) == 1:
        return a[0]
    M = get_medians_list(a)
    median = linear_selection(M, len(M) // 2)
    L = []
    R = []
    for item in a:
        if item < median:
            L.append(item)
        elif item == median and len(L) <= len(R):
            L.append(item)
        elif item == median and len(R) < len(L):
            R.append(item)
        else:
            R.append(item)

    if len(L) == k - 1:
        return median
    if len(L) > k - 1:
        return linear_selection(L, k)
    if len(L) < k - 1:
        return linear_selection(R, k - len(L))


def get_medians_list(a):
    if len(a) < 5:
        a.sort()
        return [a[len(a) // 2]]
    lists = []
    j = 0
    for i in range(0, len(a) // 5):
        lists.append(a[j:j + 5])
        j += 5

    medians_list = []

    for i in range(0, len(lists)):
        lists[i].sort()
        medians_list.append(lists[i][len(lists[i]) // 2])

    return medians_list
