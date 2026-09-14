"""Versão interativa do exercício 5."""

print("3 vezes um número menos A é igual a 2 vezes o número mais B.")
valor_a = float(input("Digite A (valor subtraído): "))
valor_b = float(input("Digite B (valor somado): "))

# 3x - A = 2x + B, então x = A + B.
numero = valor_a + valor_b
lado_esquerdo = 3 * numero - valor_a
lado_direito = 2 * numero + valor_b

print(f"Número encontrado: {numero}")
print(f"Lado esquerdo: {lado_esquerdo}")
print(f"Lado direito: {lado_direito}")
print(f"Os dois lados são iguais? {lado_esquerdo == lado_direito}")
