frase = input("Digite uma frase: ")

palavras = frase.split()

contagem = {}

for palavra in palavras:
    if palavra in contagem:
        contagem[palavra] += 1
    else:
        contagem[palavra] = 1

total_palavras = len(palavras)

total_unicas = len(contagem)

repetidas = [p for p in contagem if contagem[p] > 1]

mais_frequente = max(contagem, key=contagem.get)

print("\nRELATÓRIO")
print("Total de palavras:", total_palavras)
print("Total de palavras únicas:", total_unicas)
print("Palavras repetidas:", repetidas)
print("Palavra mais frequente:", mais_frequente)