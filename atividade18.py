# Crie um programa que utilize uma estrutura de repetição para imprimir os números de 1 a 10.

valores = list()

for cont in range(1,11):
    valores.append(float(input("Digite um valor: ")))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')

print('Cheguei ao final da lista.')


