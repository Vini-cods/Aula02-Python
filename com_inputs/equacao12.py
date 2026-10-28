"""Versão interativa do exercício 12."""

import math
print("O quádruplo de um número menos A é igual ao dobro mais B.")
valor_a = float(input("Digite A (valor subtraído): "))
valor_b = float(input("Digite B (valor somado): "))

# 4x - A = 2x + B, então 2x = A + B.
numero = (valor_a + valor_b) / 2
lado_esquerdo = 4 * numero - valor_a
lado_direito = 2 * numero + valor_b

print(f"Número encontrado: {numero}")
print(f"Lado esquerdo: {lado_esquerdo}")
print(f"Lado direito: {lado_direito}")
print(f"Os dois lados são iguais? {math.isclose(lado_esquerdo, lado_direito, abs_tol=1e-9)}")
