import math


def linear_selection(a, k):
    if len(a) == 1:
        return a
    median = temp_median(a)  # TODO Trocar para algoritmo da mediana das medianas
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
        print("segundo if", len(L), len(R), L, R, k)
        return linear_selection(L, k)
    if len(L) < k - 1:
        print("terceiro if", len(L), len(R), L, R, k)
        return linear_selection(R, k - len(L))


def temp_median(a):
    a.sort()
    return a[len(a) // 2]


def mom(a, k):
    if len(a) < 5:
        return a[k]
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
    return mom(medians_list, len(medians_list) // 2)


def median_of_medians(a, k):
    if len(a) <= 5:
        print("A menor igual que 5", a, k)
        return a[k]
    m = mom(a, k)
    print("A", a, "k", k, "mom", m)
    L = []
    R = []
    for item in a:
        if item < m:
            L.append(item)
        else:
            R.append(item)
    if len(L) == k - 1:
        print("Mediana final", m)
        return m
    if len(L) > k - 1:
        print("segundo if", len(L), len(R), L, R, k)
        return median_of_medians(L, k)
    if len(L) < k - 1:
        print("terceiro if", len(L), len(R), L, R, k)
        return median_of_medians(R, k - len(L) - 1)


# vet = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# print(median_of_medians(vet, len(vet) // 2))
# vet.sort()
# print(vet)

# vet = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# print(temp_median(vet))
# vet.sort()
# print(vet)


vet = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(linear_selection(vet, math.ceil(len(vet) / 2)))
vet.sort()
print(vet)
