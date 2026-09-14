"""Versão interativa do exercício 2."""

print("A diferença entre um número e sua terça parte é um valor informado.")
diferenca = float(input("Digite a diferença: "))

# x - x/3 = diferença, portanto 2x/3 = diferença.
numero = diferenca * 3 / 2
terca_parte = numero / 3

print(f"Número encontrado: {numero}")
print(f"Terça parte: {terca_parte}")
print(f"Conferência: {numero} - {terca_parte} = {numero - terca_parte}")
