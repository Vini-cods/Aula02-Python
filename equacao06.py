# Problema: "A soma de dois números consecutivos é 47."
#
# Seja o primeiro número = x
# O número consecutivo a ele = x + 1
#
# Equação:
# x + (x + 1) = 47
# 2x + 1 = 47
# 2x = 47 - 1
# 2x = 46
# x = 46 / 2
# x = 23

# O primeiro número é 23 e o segundo é seu sucessor.
numero1 = (47 - 1) / 2
numero2 = numero1 + 1

# Verificando a soma
soma = numero1 + numero2

print(f"O primeiro número é: {numero1:.0f}")
print(f"O segundo número é: {numero2:.0f}")
print(f"A soma dos dois é: {soma:.0f}")
print(f"A resposta está correta? {soma == 47}")
