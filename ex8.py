qtd = int(input("Quantos números você deseja digitar: "))
num = int(input("Digite um número: "))
menor_numero = num
maior_numero = num

contador = qtd - 1
while contador > 0:
    num = int(input("Digite um número: "))
    if num > maior_numero:
        maior_numero = num
    if num < menor_numero:
        menor_numero = num
    contador -= 1

print(f"O maior número é {maior_numero}\nO menor número é {menor_numero}")
