def formatar_valor(valor_str):
    # Troca a vírgula por ponto
    valor_str = valor_str.replace(',', '.')

    # Converte a nova string para valor numérico (float)
    valor_numerico = float(valor_str)

    return valor_numerico

def valor_tostring(valor):
    # Converte o valor float para uma string com ponto no lugar da vírgula
    if type(valor) == float:
        valor_str = "{:.2f}".format(valor).replace('.', ',')
    elif type(valor) == int:
        valor_str = str(valor)

    return valor_str