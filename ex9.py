numero = int(input("Digite um número inteiro: "))
numero_original = numero
soma = 0

for numero_original in range(1, numero + 1):
    digito = numero % 10
    soma += digito
    numero //= 10

print(f"A soma dos dígitos de {numero_original} é igual a {soma}")
