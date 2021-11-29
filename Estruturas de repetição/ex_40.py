"""Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos
os seguintes dados:
Código da cidade;
Número de veículos de passeio (em 1999);
Número de acidentes de trânsito com vítimas (em 1999).
Deseja-se saber:
Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
Qual a média de veículos nas cinco cidades juntas;
Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio."""

cod_cidade = maior_indice_acidentes = menor_indice_acidentes = cidade_menor_indice = cidade_maior_indice = 0
acidentes_cidades_menos_dois_mil_veiculos = []

for i in range(5):
    cod_cidade = int(input('Código da cidade: '))
    numero_veiculos_de_passeio = int(input('Número de veículos de passeio (em 1999): '))
    numero_acidentes_com_vitimas = int(input('Número de acidentes de trânsito com vítimas (em 1999): '))
    if i == 0:
        maior_indice_acidentes = menor_indice_acidentes = numero_acidentes_com_vitimas
        cidade_maior_indice = cidade_menor_indice = cod_cidade

    if numero_acidentes_com_vitimas > maior_indice_acidentes:
        maior_indice_acidentes = numero_acidentes_com_vitimas
        cidade_maior_indice = cod_cidade

    if numero_acidentes_com_vitimas < menor_indice_acidentes:
        menor_indice_acidentes = numero_acidentes_com_vitimas
        cidade_menor_indice = cod_cidade

    if numero_veiculos_de_passeio < 2000:
        acidentes_cidades_menos_dois_mil_veiculos.append(numero_acidentes_com_vitimas)

media = sum(acidentes_cidades_menos_dois_mil_veiculos) / len(acidentes_cidades_menos_dois_mil_veiculos)

print(f'Menor indice de acidentes: {menor_indice_acidentes} pertence a cidade {cidade_menor_indice}')
print(f'Maior indice de acidentes: {maior_indice_acidentes} pertence a cidade {cidade_maior_indice}')
print(f'Média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio {media}')
