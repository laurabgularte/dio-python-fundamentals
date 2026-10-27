nome = "Laura"
idade = 25
profissao = "Engenheira de Software"
saldo = 1545.435

# 1. Método antigo %-style (menos utilizado hoje em dia)
print(f"Nome: {nome}, Idade: {idade}")

# 2. Método format()
print(f"Olá, chamo-me {nome}. Tenho {idade} anos e trabalho como {profissao}.")
print(f"Olá, chamo-me {nome}. Tenho {idade} anos.")  # Com índices explícitos

# 3. f-strings (Abordagem moderna, limpa e recomendada)
print(f"Olá, chamo-me {nome}, tenho {idade} anos e o meu saldo é de R$ {saldo:.2f}.")
