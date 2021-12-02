"""
Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores
deverão ser compostos pelos elementos intercalados dos dois outros vetores.
"""

vetor_a = []
vetor_b = []
vetor_c = []

for elem in range(10):
    vetor_a.append(elem)

for elem in range(10, 20):
    vetor_b.append(elem)


for i in range(10):
    vetor_c.append(vetor_a[i])
    vetor_c.append(vetor_b[i])

print(vetor_c)

# resolução com list comprehension
print([x for par in zip(vetor_a, vetor_b) for x in par])
