palavra = input("Jogador 1, escolha uma palavra: ").lower()

tentativas_maximas = 6

letras_adivinhadas = []

letras_erradas = []

while tentativas_maximas > 0:
    palavra_mascarada = ""
    for letra in palavra:
        if letra in letras_adivinhadas:
            palavra_mascarada += letra
        else:
            palavra_mascarada += "_"

    print("\nPalavra: " + palavra_mascarada)
    print("Letras erradas: " + ", ".join(letras_erradas))
    print(f"Tentativas restantes: {tentativas_maximas}")

    letra_adivinhada = input("Jogador 2, adivinhe uma letra: ").lower()

    if letra_adivinhada in letras_adivinhadas or letra_adivinhada in letras_erradas:
        print("Você já adivinhou essa letra.")
    elif letra_adivinhada in palavra:
        letras_adivinhadas.append(letra_adivinhada)

        if all(letra in letras_adivinhadas for letra in palavra):
            print("\nParabéns! Você adivinhou a palavra: " + palavra)
            break
    else:
        letras_erradas.append(letra_adivinhada)
        tentativas_maximas -= 1
else:
    print("\nVocê perdeu! A palavra era: " + palavra)
