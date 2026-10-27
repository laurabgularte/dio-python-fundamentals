def sacar(valor: float) -> None:
    saldo = 500.0

    # Início do bloco do 'if' (indentado com 4 espaços)
    if saldo >= valor:
        saldo -= valor
        print(f"Saque de R$ {valor:.2f} efetuado com sucesso!")
        print("Retire o seu dinheiro na boca do caixa.")
    # Fim do bloco do 'if'

    print(f"Obrigado por ser nosso cliente. Saldo atual: R$ {saldo:.2f}")


# Chamada da função
sacar(100.0)
