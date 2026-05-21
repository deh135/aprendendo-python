peso = float(input("qual o seu peso?"))
altura = float(input("qual a sua altura?"))

imc = peso / altura ** 2

print("seu IMC è:")

if imc < 18.5:
    print("baixo peso")
elif imc < 25:
    print("peso normal")
else:
    print("sobrepeso")