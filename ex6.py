numero = int(input("Digite um número inteiro para calcular o fatorial: "))

fatorial = 1

while numero > 1:
    fatorial *= numero
    numero -= 1

print("O fatorial do número é:", fatorial)
