MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

# 1. Condicional Simples, Composta e Encadeada
# Simulando uma idade de entrada
idade_usuario = 20

if idade_usuario >= MAIOR_IDADE:
    print("O utilizador é maior de idade e pode tirar a carta de condução.")
elif idade_usuario == IDADE_ESPECIAL:
    print("O utilizador pode fazer aulas teóricas, mas ainda falta um pouco.")
else:
    print("O utilizador é menor de idade.")


# 2. Condicional Ternária (forma compacta de tomar decisão)
status = "Sucesso" if idade_usuario >= MAIOR_IDADE else "Bloqueado"
print(f"Estado da transação: {status}")
