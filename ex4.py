num_inteiro = int(input("Digite um número inteiro: "))
contador = 0
while num_inteiro > 0:
    contador += 1
    num_inteiro //= 10

print("O número tem", contador, "dígitos")
