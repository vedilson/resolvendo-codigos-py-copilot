# Solicita uma palavra do usuário
palavra = input("Digite uma palavra: ").strip().lower()

# Verifica se a palavra é um palíndromo
if palavra == palavra[::-1]:
    resultado = "A palavra é um palíndromo."
else:
    resultado = "A palavra não é um palíndromo."

# Exibe o resultado
print(resultado)