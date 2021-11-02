def imprimir_triangulo_de_numeros (n: int):
  for i in range(1, n+1):
    lista = [0] * i
    print('   '.join([str(i) for _ in lista]))


imprimir_triangulo_de_numeros(10)
