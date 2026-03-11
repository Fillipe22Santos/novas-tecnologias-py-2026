max_tentativas = 6  
numero_secreto = 42
tentativas = 1  
acertou = False

while tentativas < max_tentativas:
    print(f"tentativa numero ({tentativas})")
    chute = int(input("Qual o seu chute?"))
    if chute <= 39:
        print("muito abaixo!")
        
    elif chute == 42:
            print("Parabens, voce acertou!")
        
    elif chute >= 50:
        print("muito acima!")
        
    elif chute >= 40 and chute <= 49:
        print("chegando perto!")
        
    if chute == numero_secreto:
        
        acertou = True
        break
    
    tentativas +=1
    
    if tentativas == max_tentativas:
        acertou = False
        print("voce perdeu!")
        break 