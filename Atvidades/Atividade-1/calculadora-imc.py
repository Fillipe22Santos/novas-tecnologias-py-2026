nome = str(input('Insira seu nome:'))
peso = float(input('Insira seu peso:'))
altura = float(input('Insira sua altura:'))

imc = peso / (altura ** 2)

print(f"seu imc e {imc}")

if imc < 18.5:
    print("voce esta abaixo do peso")
    
elif imc >= 18.5 and imc <= 24.9:
    print("voce esta no seu peso normal")
    
elif imc >= 25.0 and imc <= 29.9:
    print("voce esta acima do peso")
    
elif imc >= 30.0:
    print("voce esta obeso")
    
    