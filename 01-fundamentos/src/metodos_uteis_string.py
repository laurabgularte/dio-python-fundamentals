curso = "   python e ng  "

# Transformação de maiúsculas e minúsculas
print(f"Maiúsculas: {curso.upper()}")
print(f"Minúsculas: {curso.lower()}")
print(f"Título (Title): {curso.title()}")

# Remoção de espaços em branco
print(f"Strip (remove em redor): '{curso.strip()}'")
print(f"Lstrip (remove à esquerda): '{curso.lstrip()}'")
print(f"Rstrip (remove à direita): '{curso.rstrip()}'")

# Junção e centralização
linguagem = "Python"
print(f"Centralizado: {linguagem.center(10, '#')}")
print(f"Junção com hífen: '{'-'.join(linguagem)}'")
