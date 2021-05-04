import random
import time

from linear_selection import linear_selection
from sort_selection import sort_selection

n = 1000
step = 1000
_max = 10000
vets = []
n_vets = 10
j = 0
linear_selection_times = []
sort_selection_times = []

print("Iniciando execução...\n")

while n <= _max:
    for i in range(n_vets):
        vet = []
        while len(vet) < n:
            num = random.randint(1, 100000)
            vet.append(num)
        k = len(vet) // 2
        start_time = time.time()
        linear = linear_selection(vet, k)
        linear_selection_times.append((time.time() - start_time))
        start_time = time.time()
        sort = sort_selection(vet, k)
        sort_selection_times.append((time.time() - start_time))
        vet.sort()
        if linear != sort:
            print(f"Erro! Resultados do vetor {i + 1} de tamanho {len(vet)} com k = {k} -> "
                  f"Linear Selection: {linear} - Sort Selection: {sort} - Manual: {vet[k - 1]}")
        else:
            print(f"OK! Resultados do vetor {i + 1} de tamanho {len(vet)} com k = {k} -> "
                  f"Linear Selection: {linear} - Sort Selection: {sort} - Manual: {vet[k - 1]}")
    n += step

for i in range(n_vets):
    linear_selection_average = sum(linear_selection_times[j:j + n_vets]) / n_vets
    sort_selection_average = sum(sort_selection_times[j:j + n_vets]) / n_vets
    print(f"\nMédias de tempo de execução entre {n_vets} vetores de tamanho {(i + 1) * step}: "
          f"\n  - Linear Selection: {linear_selection_average} segundos"
          f"\n  - Sort Selection: {sort_selection_average} segundos"
          f"\n  - Tempo economizado ao utilizar Linear Selection ao invés do Sort selection: "
          f"{sort_selection_average - linear_selection_average} segundos")
    j += n_vets

print("\nFim da execução!")
