estoque = [
    {"nome": "Notebook", "preco": 3500, "quantidade": 3},
    {"nome": "Mouse", "preco": 50, "quantidade": 10},
    {"nome": "Monitor", "preco": 900, "quantidade": 2},
    {"nome": "Teclado", "preco": 120, "quantidade": 0},
    {"nome": "Headset", "preco": 300, "quantidade": 1}
]

valor_total = 0

print("Produtos com valor em estoque acima de R$500:\n")

for item in estoque:
    valor = item["preco"] * item["quantidade"]
    valor_total += valor

    if valor > 500:
        print(item["nome"], "- Valor em estoque: R$", valor)

print("\nValor total do estoque: R$", valor_total)


produtos_em_falta = [item["nome"] for item in estoque if item["quantidade"] == 0]

print("\nProdutos em falta:")
print(produtos_em_falta)