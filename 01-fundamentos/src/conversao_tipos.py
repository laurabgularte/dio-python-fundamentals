# ==============================================================================
# 1. int para float
# ==============================================================================
preco = 10
preco_em_float = float(preco)

print(f"Original: {preco} | Tipo: {type(preco)}")
print(f"Convertido: {preco_em_float} | Tipo: {type(preco_em_float)}")


# ==============================================================================
# 2. float para int
# ==============================================================================
# Nota: A conversão de float para int descarta a parte decimal
pi = 3.14159
pi_em_inteiro = int(pi)

print(f"Original: {pi} | Tipo: {type(pi)}")
print(f"Convertido: {pi_em_inteiro} | Tipo: {type(pi_em_inteiro)}")


# ==============================================================================
# 3. int/float para str
# ==============================================================================
idade = 25
idade_em_str = str(idade)

print(f"Original: {idade} | Tipo: {type(idade)}")
print(f"Convertido: '{idade_em_str}' | Tipo: {type(idade_em_str)}")

# Utilidade prática: Concatenar números em mensagens de texto
mensagem = "A minha idade é " + idade_em_str + " anos."
print(mensagem)


# ==============================================================================
# 4. str para int/float
# ==============================================================================
preco_str = "10.50"
idade_str = "30"

preco_convertido = float(preco_str)
idade_convertida = int(idade_str)

print(
    f"String '{preco_str}' convertida para float: {preco_convertido} "
    f"({type(preco_convertido)})"
)
print(
    f"String '{idade_str}' convertida para int: {idade_convertida} "
    f"({type(idade_convertida)})"
)


# ==============================================================================
# 5. Função nativa type() e divisão especial
# ==============================================================================
# Divisão com '/' retorna sempre float
divisao_normal = 10 / 2
print(f"10 / 2 = {divisao_normal} | Tipo: {type(divisao_normal)}")

# Divisão inteira com '//' preserva o tipo inteiro se ambos forem inteiros
divisao_inteira = 10 // 2
print(f"10 // 2 = {divisao_inteira} | Tipo: {type(divisao_inteira)}")
