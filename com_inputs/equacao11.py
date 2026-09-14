"""Versão interativa do exercício 11."""

print("Um número somado ao triplo de seu sucessor resulta em um total.")
total = float(input("Digite o total: "))

# x + 3(x + 1) = total, então 4x + 3 = total.
numero = (total - 3) / 4
sucessor = numero + 1
resultado = numero + 3 * sucessor

print(f"Número encontrado: {numero}")
print(f"Sucessor: {sucessor}")
print(f"Conferência: {resultado}")
