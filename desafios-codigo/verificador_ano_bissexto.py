def verificador_ano_bissexto():
    ano = int(input())

    # Verifique se o ano é bissexto usando uma estrutura de controle
    # condicional (if/else) e imprima o resultado:
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print("SIM")
    else:
        print("NÃO")


verificador_ano_bissexto()
