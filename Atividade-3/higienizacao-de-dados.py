def limpar_dados(lista):

    usuarios_ativos = list(filter(lambda u: u.get("status_ativo") == True, lista))
    
    for usuario in usuarios_ativos:
        if "nome" in usuario and isinstance(usuario["nome"], str):
            usuario["nome"] = usuario["nome"].upper()
        if "email" in usuario and isinstance(usuario["email"], str):
            usuario["email"] = usuario["email"].lower()
    
    return usuarios_ativos


dados = [
    {"nome": "Fillipe Andrade", "email": "FILLIPE@EMAIL.COM", "status_ativo": True},
    {"nome": "Maria Silva", "email": "Maria@Email.com", "status_ativo": False},
    {"nome": "João Souza", "email": "JOAO@EMAIL.COM", "status_ativo": True},
    {"nome": "Ana Costa", "email": "ANA@EMAIL.COM", "status_ativo": False}
]

resultado = limpar_dados(dados)

print("DADOS LIMPOS:\n")
for usuario in resultado:
    print(usuario)