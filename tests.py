import random
import time

from linear_selection import linear_selection
from sort_selection import sort_selection


n = 1000
step = 1000
max = 10000

vets = []
for i in range(10):
    while n <= max:
        vet = []
        while len(vet) < n:
            num = random.randint(1, 100000)
            if num not in vet:
                vet.append(num)
        vets.append(vet)
        n += step

l_times = []
s_times = []
for vet in vets:
    start_time = time.time()
    linear = linear_selection(vet, len(vet) // 2)
    l_times.append((time.time() - start_time))
    start_time = time.time()
    sort = sort_selection(vet, len(vet) // 2)
    s_times.append((time.time() - start_time))
    if linear != sort:
        # raise Exception("ERRÔ!", len(vet), vet)
        print("ERRÔ!", len(vet), vet)
    print("linear == sort ?", linear, sort, linear == sort)
