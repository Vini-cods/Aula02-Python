'''Três amigos somaram suas idades. João tem o dobro de Pedro,
Carlos tem a mesma idade de Pedro e a soma é 60 anos.'''

# Definição do problema:
# Idade de Pedro = P
# Idade de João = 2 * P
# Idade de Carlos = P
# A soma das idades é 60: P + 2P + P = 60

# Resolvendo a equação:
# 4P = 60
# P = 60 / 4
# P = 15

# Atribuindo as idades com base na solução.
idade_pedro = 60 / 4
idade_joao = 2 * idade_pedro
idade_carlos = idade_pedro

# Verificando a soma das idades
soma_idade = idade_pedro + idade_joao + idade_carlos

print(f"Pedro: {idade_pedro:.0f} anos")
print(f"João: {idade_joao:.0f} anos")
print(f"Carlos: {idade_carlos:.0f} anos")
print(f"Soma: {soma_idade:.0f} anos")
print(f"A resposta está correta? {soma_idade == 60}")

