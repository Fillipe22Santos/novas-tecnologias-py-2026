valida = False 

while valida == False:
    
    tem_numero = False
    tem_maiuscula = False
    tem_especial = False
    
    senha = str(input("Digite sua senha:"))
    if len(senha) < 8:
         print("senha muito curta!")     
         continue
     
    for caractere in senha:
        if caractere.isdigit():
            tem_numero = True
            
    if not tem_numero:
        print("A senha precisa ter pelo menos um numero!")
        continue
        
    for caractere in senha:
        if caractere.isupper():
            tem_maiuscula = True
            
    if not tem_maiuscula:
        print("A senha precisa ter pelo menos um caractere em maiusuclo!")
        continue
       
    for caractere in senha:
        if not caractere.isalnum():
            tem_especial = True
            
    if not tem_especial:
            print("Sua senha precisa ter pelo menos um caractere especial!")
            continue
        
    valida = True
    print("Senha valida!")
    
qtd_numeros = 0
qtd_maiusculas = 0
qtd_especiais = 0

for caractere in senha:
    
    if caractere.isdigit():
        qtd_numeros += 1
    
    if caractere.isupper():
        qtd_maiusculas += 1
    
    if not caractere.isalnum():
        qtd_especiais += 1
        
print("\nRELATORIO DA SENHA")
print("Tamanho da senha:", len(senha))
print("Quantidade de numeros:", qtd_numeros)
print("Quantidade de letras maiusculas:", qtd_maiusculas)
print("Quantidade de caracteres especiais:", qtd_especiais)

if len(senha) <= 9:
    print("Senha fraca!")

elif len(senha) >= 10 and len(senha) <= 12:
    print("Senha mediana!")

elif len(senha) >= 13:
    print("Senha forte!")           
            
            
  