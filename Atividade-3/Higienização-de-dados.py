def limpar_dados(lista):
    
    lista_limpa = []

    for pessoa in lista:
        nome = pessoa["nome"].strip().title()
        email = pessoa["email"].strip().lower()
        status = pessoa["status_ativo"]  

        usuario_limpo = {
            "nome": nome,
            "email": email,
            "status_ativo": status
        }

        lista_limpa.append(usuario_limpo)

    return lista_limpa

dados = [
    
{"nome": "Yuri Campos", "email": "yuri.campos@email.com", "stuatus_ativo": True},
{"nome": "Aberth Cavalcanti","email": "alberth.cavalcanti@email.com","status_ativo": False},
{"nome": "Matheus Ali","email": "matheus.ali@email.com","status_ativo": True},
    
    ]

resultado = limpar_dados(dados)
print(resultado)