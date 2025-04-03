# Solicita dois números do usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Solicita a operação desejada
operacao = input("Escolha a operação (+, -, *, /): ")

# Realiza a operação escolhida
if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = abs(num1 - num2)
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    resultado = num1 / num2 if num2 != 0 else "Erro: Divisão por zero"
else:
    resultado = "Operação inválida"

# Exibe o resultado
print("Resultado:", resultado)
