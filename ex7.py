num_inicial = int(input("Digite um número inicial: "))
num_final = int(input("Digite um número final: "))

for n in range(num_inicial, num_final):
    if n % 2 == 0:
        print(n)
