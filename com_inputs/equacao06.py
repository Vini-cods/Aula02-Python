"""Versão interativa do exercício 6."""

print("A soma de dois números consecutivos é um total informado.")
total = float(input("Digite a soma: "))

# x + (x + 1) = total, então x = (total - 1) / 2.
primeiro_numero = (total - 1) / 2
segundo_numero = primeiro_numero + 1

print(f"Primeiro número: {primeiro_numero}")
print(f"Segundo número: {segundo_numero}")
print(f"Conferência: {primeiro_numero + segundo_numero}")
