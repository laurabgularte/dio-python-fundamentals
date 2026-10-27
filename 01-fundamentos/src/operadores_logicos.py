saldo = 1000
saque = 200
limite = 100
conta_especial = True

# Operador AND (Todas as condições devem ser True)
print("--- Operador AND ---")
print(saldo >= saque and saque <= limite)  # True and False -> False
print(saldo >= saque and limite >= saque)  # True and True -> True

# Operador OR (Pelo menos uma condição deve ser True)
print("\n--- Operador OR ---")
print(saldo >= saque or saque <= limite)  # True or False -> True

# Operador NOT (Inverte o valor booleano)
print("\n--- Operador NOT ---")
print(not 1000 > 1500)  # Inverte False para True
print(not conta_especial)

# Expressão complexa com parênteses
expressao_complexa = (saldo >= saque and saque <= limite) or (
    conta_especial and saldo >= saque
)
print(f"\nExpressão Complexa: {expressao_complexa}")
