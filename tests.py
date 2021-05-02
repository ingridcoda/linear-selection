import random
import time

from linear_selection import linear_selection
from sort_selection import sort_selection

n = 1000
step = 1000
_max = 10000
vets = []

print("Populando vetores...")
while n <= _max:
    for i in range(10):
        vet = []
        while len(vet) < n:
            num = random.randint(1, 100000)
            if num not in vet:
                vet.append(num)
        vets.append(vet)
    n += step
print("Vetores populados.")

l_times = []
s_times = []
count = 0
countByLen = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
countLinearErrorsByLen = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
countSortErrorsByLen = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for vet in vets:
    start_time = time.time()
    linear = linear_selection(vet, len(vet) // 2)
    l_times.append((time.time() - start_time))
    start_time = time.time()
    sort = sort_selection(vet, len(vet) // 2)
    s_times.append((time.time() - start_time))

    if linear != sort:
        vet.sort()
        print("ERRÔ!", len(vet), "linear == sort ?", linear, sort, linear == sort,
              vet[len(vet) // 2], linear == vet[len(vet) // 2], sort == vet[len(vet) // 2])
        count += 1
        countByLen[(len(vet) // 1000) - 1] += 1
        if linear != vet[len(vet) // 2]:
            countLinearErrorsByLen[(len(vet) // 1000) - 1] += 1
        if sort != vet[len(vet) // 2]:
            countSortErrorsByLen[(len(vet) // 1000) - 1] += 1
    else:
        print(len(vet), "linear == sort ?", linear, sort, linear == sort)

averagesLinearByLen = []
averagesSortByLen = []
j = 0
for i in range(10):
    averagesLinearByLen.append(sum(l_times[j:j + 10]) / 10)
    averagesSortByLen.append(sum(s_times[j:j + 10]) / 10)
    j += 10

print("Total diferentes:", count)
print("Total diferentes por tam:", countByLen)
print("Total diferentes linear por tam:", countLinearErrorsByLen)
print("Total diferentes sort por tam:", countSortErrorsByLen)
print("Medias linear por tam:", averagesLinearByLen)
print("Medias sort por tam:", averagesSortByLen)
