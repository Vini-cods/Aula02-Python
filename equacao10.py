# Problema: "Cinco vezes um número somado com 2 é igual ao número multiplicado por 7."
#
# Representando o problema em uma equação:
# Seja 'x' o número desconhecido.
# "Cinco vezes um número" -> 5 * x
# "somado com 2" -> + 2
# "é igual ao número multiplicado por 7" -> = 7 * x
#
# Equação: 5 * x + 2 = 7 * x

# Resolvendo a equação:
# 5x + 2 = 7x
# 2 = 7x - 5x
# 2 = 2x
# x = 2 / 2
# x = 1

# Solução:
x = 2 / 2

# Verificação:
# 5 * 1 + 2 = 5 + 2 = 7
# 7 * 1 = 7
# 7 = 7 (A solução está correta)

lado_esquerdo = 5 * x + 2
lado_direito = 7 * x

print(f"Número: {x}")
print(f"Lado esquerdo: {lado_esquerdo}")
print(f"Lado direito: {lado_direito}")
print(f"A resposta está correta? {lado_esquerdo == lado_direito}")