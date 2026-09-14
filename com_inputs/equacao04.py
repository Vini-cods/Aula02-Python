"""Versão interativa do exercício 4."""

print("3 vezes um número, menos um valor, é igual ao próprio número.")
valor_subtraido = float(input("Digite o valor subtraído: "))

# 3x - valor = x, então 2x = valor.
numero = valor_subtraido / 2
resultado = 3 * numero - valor_subtraido

print(f"Número encontrado: {numero}")
print(f"Conferência: 3 x {numero} - {valor_subtraido} = {resultado}")
