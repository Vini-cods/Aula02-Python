"""Versão interativa do exercício 8."""

print("Quatro vezes um número menos um valor é igual a um resultado.")
valor_subtraido = float(input("Digite o valor subtraído: "))
resultado_esperado = float(input("Digite o resultado esperado: "))

# 4x - valor_subtraido = resultado_esperado.
numero = (resultado_esperado + valor_subtraido) / 4
resultado = 4 * numero - valor_subtraido

print(f"Número encontrado: {numero}")
print(f"Conferência: {resultado}")
