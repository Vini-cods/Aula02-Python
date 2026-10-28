"""Versão interativa do exercício 10."""

import math
print("Cinco vezes um número mais A é igual a sete vezes o número.")
valor_somado = float(input("Digite A: "))

# 5x + A = 7x, logo A = 2x e x = A / 2.
numero = valor_somado / 2
lado_esquerdo = 5 * numero + valor_somado
lado_direito = 7 * numero

print(f"Número encontrado: {numero}")
print(f"Lado esquerdo: {lado_esquerdo}")
print(f"Lado direito: {lado_direito}")
print(f"Os dois lados são iguais? {math.isclose(lado_esquerdo, lado_direito, abs_tol=1e-9)}")
