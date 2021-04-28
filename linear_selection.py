import math


def linear_selection(a, k):
    if len(a) == 1:
        return a[0]
    M = get_medians_list(a)
    print("M", M, "ceil", math.ceil(len(M) / 2))
    median = linear_selection(M, math.ceil(len(M) / 2))
    print("median", median)
    L = []
    R = []
    for item in a:
        if item < median:
            L.append(item)
        else:
            R.append(item)
    print(L, R)
    if len(L) == k - 1:
        print("Mediana final", median)
        return median
    if len(L) > k - 1:
        print("segundo if", len(L), len(R), L, R, k, median)
        return linear_selection(L, k)
    if len(L) < k - 1:
        print("terceiro if", len(L), len(R), L, R, k, median)
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
        print(lists[i])
        medians_list.append(lists[i][len(lists[i]) // 2])
        print(lists[i][len(lists[i]) // 2])

    print(medians_list)
    return medians_list


# vet = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# print(median_of_medians(vet, len(vet) // 2))
# vet.sort()
# print(vet)

# vet = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# print(temp_median(vet))
# vet.sort()
# print(vet)


vet = [1, 2, 2, 3, 4, 5]
print(linear_selection(vet, math.ceil(len(vet) / 2)))
vet.sort()
print(vet)
