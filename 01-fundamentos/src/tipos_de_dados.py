"""
Módulo 01: Tipos de Dados Built-in em Python
Demonstração prática dos tipos apresentados nas aulas fundamentais da DIO.
"""

# 1. Texto (String)
nome = "DIO Python"
print(f"Valor: {nome} | Tipo: {type(nome)}")

# 2. Numérico (int, float, complex)
idade = 25  # int (Inteiro)
altura = 1.75  # float (Ponto flutuante)
numero_complexo = 1 + 2j  # complex (Número complexo)
print(f"Valor: {idade} | Tipo: {type(idade)}")
print(f"Valor: {altura} | Tipo: {type(altura)}")
print(f"Valor: {numero_complexo} | Tipo: {type(numero_complexo)}")

# 3. Sequência (list, tuple, range)
lista = [10, 20, 30]  # list (Lista mutável)
tupla = (10, 20, 30)  # tuple (Tupla imutável)
intervalo = range(5)  # range (Sequência numérica)
print(f"Valor: {lista} | Tipo: {type(lista)}")
print(f"Valor: {tupla} | Tipo: {type(tupla)}")
print(f"Valor: {list(intervalo)} | Tipo: {type(intervalo)}")

# 4. Mapa (dict)
usuario = {"nome": "Laura", "nivel": "Junior/Pleno"}
print(f"Valor: {usuario} | Tipo: {type(usuario)}")

# 5. Coleção / Conjunto (set, frozenset)
conjunto = {1, 2, 3, 3, 2}  # set (Remove duplicados automaticamente)
conjunto_imutavel = frozenset([1, 2, 3])
print(f"Valor: {conjunto} | Tipo: {type(conjunto)}")
print(f"Valor: {conjunto_imutavel} | Tipo: {type(conjunto_imutavel)}")

# 6. Booleano (bool)
estudando = True
trabalhando = False
print(f"Valor: {estudando} | Tipo: {type(estudando)}")

# 7. Binário (bytes, bytearray, memoryview)
dados_bytes = b"Python"
dados_bytearray = bytearray(5)
dados_memoryview = memoryview(b"ABC")
print(f"Valor: {dados_bytes} | Tipo: {type(dados_bytes)}")
print(f"Valor: {dados_bytearray} | Tipo: {type(dados_bytearray)}")
print(f"Valor: {dados_memoryview} | Tipo: {type(dados_memoryview)}")
