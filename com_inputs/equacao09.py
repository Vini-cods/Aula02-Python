"""Versão interativa do exercício 9."""

print("O quádruplo de um número mais A é igual ao triplo mais B.")
valor_a = float(input("Digite A (valor somado ao quádruplo): "))
valor_b = float(input("Digite B (valor somado ao triplo): "))

# 4x + A = 3x + B, então x = B - A.
numero = valor_b - valor_a
lado_esquerdo = 4 * numero + valor_a
lado_direito = 3 * numero + valor_b

print(f"Número encontrado: {numero}")
print(f"Lado esquerdo: {lado_esquerdo}")
print(f"Lado direito: {lado_direito}")
print(f"Os dois lados são iguais? {lado_esquerdo == lado_direito}")
