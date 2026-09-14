"""Versão interativa do exercício 3."""

print("João tem o dobro de Pedro, Carlos tem a idade de Pedro.")
total = float(input("Digite a soma das três idades: "))

# P + 2P + P = total, logo 4P = total.
idade_pedro = total / 4
idade_joao = 2 * idade_pedro
idade_carlos = idade_pedro

print(f"Pedro: {idade_pedro} anos")
print(f"João: {idade_joao} anos")
print(f"Carlos: {idade_carlos} anos")
print(f"Conferência da soma: {idade_pedro + idade_joao + idade_carlos}")
