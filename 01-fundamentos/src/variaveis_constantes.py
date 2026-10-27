# ==============================================================================
# 1. Variáveis
# ==============================================================================
# Variáveis são mutáveis e seus valores podem ser alterados ao longo da execução.

nome_usuario = "Laura"
idade_usuario = 25
saldo_conta = 1500.50

print(f"Nome: {nome_usuario} | Idade: {idade_usuario} | Saldo: R$ {saldo_conta}")

# Alterando os valores da variável
idade_usuario = 26
saldo_conta = saldo_conta - 200.00

print(f"Nova Idade: {idade_usuario} | Novo Saldo: R$ {saldo_conta}")


# ==============================================================================
# 2. Atribuição Múltipla
# ==============================================================================
# Python permite atribuir valores a múltiplas variáveis em uma única linha.

cidade, estado, pais = "Ibirubá", "RS", "Brasil"
print(f"Localização: {cidade}/{estado} - {pais}")


# ==============================================================================
# 3. Constantes
# ==============================================================================
# Por convenção (PEP 8), constantes são escritas em MAIÚSCULAS.
# Embora o Python permita alterar o valor fisicamente, o desenvolvedor NÃO deve
# alterar o valor de uma constante.

PI = 3.14159
TAXA_DE_JUROS_ANUAL = 0.05
ESTADOS_SUDESTE = ["SP", "RJ", "MG", "ES"]
NOME_SISTEMA = "Sistema Bancário DIO"

print(f"Sistema: {NOME_SISTEMA}")
print(f"Valor de PI: {PI}")
print(f"Taxa de Juros: {TAXA_DE_JUROS_ANUAL * 100}%")
