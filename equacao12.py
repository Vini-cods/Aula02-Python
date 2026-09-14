
# Problema: "Qual é o número cujo quádruplo subtraído de 5 dá o mesmo que seu dobro somado com 11?"
#
# Equação: 4x - 5 = 2x + 11
#
# Resolvendo a equação:
# 4x - 5 = 2x + 11
# 4x - 2x = 5 + 11
# 2x = 5 + 11
# 2x = 16
# x = 8

# Resolvendo com Python

numero = 16 / 2
lado_esquerdo = 4 * numero - 5
lado_direito = 2 * numero + 11

print(f"O número é: {numero}")
print(f"Lado esquerdo: {lado_esquerdo}")
print(f"Lado direito: {lado_direito}")
print(f"A resposta está correta? {lado_esquerdo == lado_direito}")