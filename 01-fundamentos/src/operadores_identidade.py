curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200

# 'is' verifica se apontam para o mesmo objecto na memória
print(f"curso is nome_curso: {curso is nome_curso}")  # True (mesma referência)
print(f"curso is not nome_curso: {curso is not nome_curso}")  # False

# Mesmo com valor numérico, inteiros pequenos no Python podem partilhar memória
# mas o operador de identidade valida a referência de objecto estrita.
print(f"saldo is limite: {saldo is limite}")
