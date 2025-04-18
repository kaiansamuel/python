valor = float(input("Valor total da conta(R$):"))
gorjeta = float(input("Percentual de gorjeta (0-100): "))

valor_gorjeta = valor * gorjeta / 100

print(f"Valor da gorjeta: R$ {valor_gorjeta:.2f}")
print(f"Valor total da conta: R$ {valor + valor_gorjeta:.2f}")
