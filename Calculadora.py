def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero!"

print("Calculadora Simples")
print("Operações disponíveis:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

operacao = input("Escolha a operação (1/2/3/4): ")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if operacao == '1':
    print("Resultado:", soma(num1, num2))
elif operacao == '2':
    print("Resultado:", subtracao(num1, num2))
elif operacao == '3':
    print("Resultado:", multiplicacao(num1, num2))
elif operacao == '4':
    print("Resultado:", divisao(num1, num2))
else:
    print("Operação inválida. Por favor, escolha uma operação válida.")
