numero = float(input("Digite um número: "))

if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")


idade = int(input("Digite a sua idade: "))

if idade >= 16:
    print("Você pode votar.")
else:
    print("Você não pode votar.")

numero = int(input("Digite um número: "))


if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

a = float(input("Digite o comprimento do primeiro lado: "))
b = float(input("Digite o comprimento do segundo lado: "))
c = float(input("Digite o comprimento do terceiro lado: "))


if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("O triângulo é equilátero.")
    elif a == b or a == c or b == c:
        print("O triângulo é isósceles.")
    else:
        print("O triângulo é escaleno.")
else:
    print("Os comprimentos fornecidos não formam um triângulo.")
 
numero = int(input("Digite um número: "))


if numero % 5 == 0 and numero % 7 == 0:
    print("O número é múltiplo de 5 e 7.")
else:
    print("O número não é múltiplo de 5 e 7.")

numero = float(input("Digite um número: "))


if numero > 10:
    print("O número é positivo e maior que 10.")
else:
    print("O número não é positivo e maior que 10.")

numero = int(input("Digite um número: "))
if numero % 3 == 0 or numero % 5 == 0:
    print("O número é divisível por 3 ou 5.")
else:
    print("O número não é divisível por 3 ou 5.")

