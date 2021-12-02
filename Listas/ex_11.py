"""
Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
"""

vetor_a = []
vetor_b = []
vetor_c = []
vetor_d = []

for elem in range(10):
    vetor_a.append(elem)

for elem in range(10, 20):
    vetor_b.append(elem)

for elem in range(20, 30):
    vetor_c.append(elem)


for i in range(10):
    vetor_d.append(vetor_a[i])
    vetor_d.append(vetor_b[i])
    vetor_d.append(vetor_c[i])

print(vetor_d)

# resolução com list comprehension
print([x for triplo in zip(vetor_a, vetor_b, vetor_c) for x in triplo])
