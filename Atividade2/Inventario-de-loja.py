estoque = []

produto1 = {
    
    "nome": "memoria_ram",
    "preco": 600,
    "quantidade": 80,
    
    }

produto2 = {
    
    "nome": "SSD",
    "preco": 900,
    "quantidade": 50,
    
    }

produto3 ={
    
    "nome": "processador",
    "preco": 1200,
    "quantidade": 0,
    
    }

estoque.append(produto1)
estoque.append(produto2)
estoque.append(produto3)

for produto in estoque:
    Valor_Total1 = produto1["preco"] * produto1["quantidade"]
    Valor_Total2 = produto2["preco"]* produto2["quantidade"]
    Valor_Total3 = produto3["preco"]*produto3["quantidade"]
    
    print(f"{Valor_Total1}")