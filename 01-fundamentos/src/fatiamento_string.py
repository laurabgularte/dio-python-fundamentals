nome = "Laura Beatriz de Matos Gularte"

# Obter o primeiro carater
print(f"Primeiro carater: {nome[0]}")

# Obter os primeiros carateres (do início até ao índice 5)
print(f"Fatia inicial [0:5]: {nome[:5]}")

# A partir de um índice específico até ao fim
print(f"A partir do índice 6: {nome[6:]}")

# Intervalo específico [inicio:fim]
print(f"Nome do meio [6:13]: {nome[6:13]}")

# Com passo (saltos) [inicio:fim:passo]
print(f"De 2 em 2 carateres: {nome[::2]}")

# Inverter a string inteira utilizando passo negativo
print(f"String invertida: {nome[::-1]}")
