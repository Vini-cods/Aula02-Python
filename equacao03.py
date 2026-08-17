'''
Docstring para equacao03
Três amigos somaram suas idades. 
João tem o dobro da idade de Pedro. 
Carlos tem a mesma idade de Pedro. 
A soma das idades é 60 anos. Qual é a idade de cada um?
'''

# Definição do problema:
# Idade de Pedro = P
# Idade de João = 2 * P
# Idade de Carlos = P
# A soma das idades é 60: P + 2P + P = 60

# Resolvendo a equação:
# 4P = 60
# P = 60 / 4
# P = 15

# Atribuindo as idades com base na solução

idade_pedro = 15
idade_joao = 2 * idade_pedro
idade_carlos = idade_pedro

# Verificando a soma das idades
soma_idade = idade_pedro + idade_joao + idade_carlos

print(f"Idade de Pedro: {idade_pedro} anos.")
print(f"Idade de Joao: {idade_joao} anos.")
print(f"Idade de Carlos: {idade_carlos} anos.")
print(f"Soma das idades: {soma_idade} anos.")

# O resultado indica que Pedro tem 15 anos, João tem 30 anos e Carlos tem 15 anos.
# Isso decorre da equação montada: P + 2P + P = 60 → 4P = 60 → P = 15.
# Portanto João = 2 * 15 = 30 e a soma 15 + 30 + 15 = 60 confirma a solução.

