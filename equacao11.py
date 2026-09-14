# Problema: "Um número somado ao triplo de seu sucessor resulta em 74. Qual é esse número?"
#
# Equação: x + 3 * (x + 1) = 74
#
# Resolvendo a equação:
# x + 3x + 3 = 74
# 4x + 3 = 74
# 4x = 74 - 3
# 4x = 71
# x = 71 / 4
# x = 17.75

# Resolvendo com Python: 4x = 71.
x = 71 / 4
sucessor = x + 1
resultado = x + 3 * sucessor

print(f"O número é: {x}")
print(f"Verificação: {x} + 3 x {sucessor} = {resultado}")
print(f"A resposta está correta? {resultado == 74}")
