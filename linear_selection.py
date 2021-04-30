def linear_selection(a, k):
    if len(a) == 1:
        return a[0]
    M = get_medians_list(a)
    # print("M", M, "ceil", len(M) // 2)
    median = linear_selection(M, len(M) // 2)
    # print("median", median)
    L = []
    R = []
    for item in a:
        # print("ITEM", item, "MEDIAN", median)
        if item < median:
            L.append(item)
            # print("if 1", L, R)
        elif item == median and len(L) <= len(R):
            L.append(item)
            # print("if 2", L, R)
        elif item == median and len(R) < len(L):
            R.append(item)
            # print("if 3", L, R)
        else:
            R.append(item)
            # print("if 4", L, R)
    # print(L, R)
    if len(L) == k - 1:
        # print("Mediana final", median, "k", k, L, R)
        return median
    if len(L) > k - 1:
        # print("segundo if", len(L), len(R), L, R, k, median)
        return linear_selection(L, k)
    if len(L) < k - 1:
        # print("terceiro if", len(L), len(R), L, R, k, median)
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
        # print("LISTA", i, lists[i])
        medians_list.append(lists[i][len(lists[i]) // 2])
        # print("MEDIANA LISTA", i, lists[i][len(lists[i]) // 2])

    # print(medians_list)
    return medians_list


# vet = [8, 7, 6, 5, 4, 3, 2, 2, 2, 1]
# # k = math.ceil(len(vet) / 2)
# k = 5
# print(f"Getting {k}-th item from {vet} using Linear Selection...")
# result = linear_selection(vet, k)
# print(f"Original array: {vet}")
# vet.sort()
# print(f"Sorted array: {vet}")
# print(f"Result: {result}")
