# ==============================================================================
# 1. Estrutura FOR (ideal para percorrer coleções ou intervalos definidos)
# ==============================================================================
texto = "Python"
print("Iterando sobre os carateres de uma string:")
for letra in texto:
    print(letra, end=" ")
print("\n")

# Utilizando a função range(inicio, fim, passo)
print("Gerando números de 0 a 5 com range:")
for numero in range(6):
    print(numero, end=" ")
print("\n")

# Tabuada utilizando o for e range
print("Tabuada do 5:")
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")


# ==============================================================================
# 2. Estrutura WHILE (executa enquanto a expressão booleana for verdadeira)
# ==============================================================================
opcao = -1

print("\nSimulação de menu com while:")
# Apenas a simulação de uma execução para fins didáticos
while opcao != 0:
    print("[1] Sacar")
    print("[2] Extrato")
    print("[0] Sair")

    # Simulando a escolha do utilizador para o loop encerrar
    opcao = 0
    if opcao == 0:
        print("A sair do sistema... Obrigado por utilizar os nossos serviços!")


# ==============================================================================
# 3. Controlo de Fluxo: break e continue
# ==============================================================================
print("\nExemplo com break (interrompe o loop quando o número for 5):")
for numero in range(10):
    if numero == 5:
        break
    print(numero, end=" ")
print("\n")

print("\nExemplo com continue (salta o número 5 e prossegue o loop):")
for numero in range(10):
    if numero == 5:
        continue
    print(numero, end=" ")
print()
