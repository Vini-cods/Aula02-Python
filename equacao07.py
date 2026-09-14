'''

Qual número atende ao seguinte critério? “Sua metade mais 7 é igual a 19.”

'''



# Problema: "Sua metade mais 7 é igual a 19."
#
# Equação:
# (x / 2) + 7 = 19
#
# Resolvendo:
# x / 2 = 19 - 7
# x / 2 = 12
# x = 12 * 2
# x = 24

numero = (19 - 7) * 2

# Verificando a condição
resultado = (numero / 2) + 7

print(f"Número: {numero}")
print(f"Verificação: metade de {numero} + 7 = {resultado}")
print(f"A resposta está correta? {resultado == 19}")
