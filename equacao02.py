'''A diferença entre um número e sua terça parte é 20.'''

# x - x / 3 = 20
# 2x / 3 = 20
# 2x = 60
# x = 30

x = 30
terca_parte = x / 3
resultado = x - terca_parte

print(f"Número: {x}")
print(f"Terça parte: {terca_parte}")
print(f"Diferença: {resultado}")
print(f"A resposta está correta? {resultado == 20}")

