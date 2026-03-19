def limpar_dados(lista):

    
    
    lista_limpa = []

    for pessoa in lista:
        nome = pessoa["nome"].strip().title()
        email = pessoa["email"].strip().lower()
        status = pessoa["status_ativo"]  # já é booleano

        usuario_limpo = {
            "nome": nome,
            "email": email,
            "status_ativo": status
        }

        lista_limpa.append(usuario_limpo)

    return lista_limpa