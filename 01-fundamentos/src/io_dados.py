# ==============================================================================
# 1. Função de Saída (print)
# ==============================================================================
# A função print() exibe informações no terminal.
nome = "Laura"
idade = 25

print("Exemplo básico de impressão:")
print(nome, idade)

# O argumento 'sep' define o separador entre os elementos (por defeito é um espaço)
print("Python", "é", "uma", "linguagem", "poderosa", sep="-")

# O argumento 'end' define o que é colocado no final da linha (por defeito é '\n',
# que muda de linha)
print("Carregando", end="...")
print(" Concluído!")


# ==============================================================================
# 2. Formatação de Strings (f-strings)
# ==============================================================================
# A forma moderna e recomendada de interpolar variáveis em Python é usando f-strings.
print(f"Olá, meu nome é {nome} e eu tenho {idade} anos.")

# Formatação de números de ponto flutuante (ex: limitar a 2 casas decimais)
saldo = 1500.54321
print(f"Saldo atualizado: R$ {saldo:.2f}")


# ==============================================================================
# 3. Função de Entrada (input)
# ==============================================================================
# O input() captura sempre os dados digitados pelo utilizador no formato de String (str)
# Nota: Comentado para evitar bloqueio automático do script em execuções automatizadas

# nome_digitado = input("Digite o seu nome: ")
# idade_digitada = input("Digite a sua idade: ")

# print(f"Bem-vindo(a) {nome_digitado}, você tem {idade_digitada} anos.")

# Boa prática: Converter imediatamente o valor numérico capturado pelo input
# ano_nascimento = int(input("Digite o seu ano de nascimento: "))
# idade_calculada = 2026 - ano_nascimento
# print(f"Você tem (ou fará) {idade_calculada} anos em 2026.")
