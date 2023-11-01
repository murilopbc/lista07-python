n = int(input("Digite a posição do número na sequência de fibonacci: "))

fibonacci = [0, 1]

for i in range(2, n):
    next_term = fibonacci[i - 1] + fibonacci[i - 2]
    fibonacci.append(next_term)

print("Sequência de Fibonacci até o", n, "º termo:")
print(fibonacci)
