taxa_reproducao = float(input("Digite a taxa de reprodução: "))
taxa_mortalidade = float(input("Digite a taxa de mortalidade: "))
populacao_inicial = int(input("Digite o número inicial de coelhos: "))
geracao = int(input("Digite o número de gerações a simular: "))

populacao = populacao_inicial

for geracao in range(geracao):
    nascimentos = int(populacao * taxa_reproducao)
    mortes = int(populacao * taxa_mortalidade)

    populacao += nascimentos - mortes
    print(f"Geração {geracao + 1}: {populacao} coelhos")
