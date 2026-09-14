"""Versão interativa do exercício 1."""

print("Um número somado ao seu dobro resulta em um total informado.")
total = float(input("Digite o total: "))

# x + 2x = total, então 3x = total.
numero = total / 3
dobro = 2 * numero

print(f"Número encontrado: {numero}")
print(f"Conferência: {numero} + {dobro} = {numero + dobro}")
