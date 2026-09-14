"""Versão interativa do exercício 7."""

print("A metade de um número mais um valor é igual a um resultado.")
valor_somado = float(input("Digite o valor somado: "))
resultado_esperado = float(input("Digite o resultado esperado: "))

# x/2 + valor_somado = resultado_esperado.
numero = (resultado_esperado - valor_somado) * 2
resultado = numero / 2 + valor_somado

print(f"Número encontrado: {numero}")
print(f"Conferência: {resultado}")
