curso = "Curso de Python"
frutas = ["laranja", "uva", "limão"]
saques = [1500, 100]

# Verificar se string faz parte de outra string
print(f"'Python' está em '{curso}'? {'Python' in curso}")  # True
print(f"'Java' não está em '{curso}'? {'Java' not in curso}")  # True

# Verificar se elemento faz parte de uma lista
print(f"'maçã' está na lista de frutas? {'maçã' in frutas}")  # False
print(f"'uva' está na lista de frutas? {'uva' in frutas}")  # True
print(f"O valor 200 está na lista de saques? {200 in saques}")  # False
