def formatar_valor(valor_str):
    # Troca a vírgula por ponto
    valor_str = valor_str.replace(',', '.')

    # Converte a nova string para valor numérico (float)
    valor_numerico = float(valor_str)

    return valor_numerico

def valor_tostring(valor_float):
    # Converte o valor float para uma string com ponto no lugar da vírgula
    valor_str = "{:.2f}".format(valor_float).replace('.', ',')

    return valor_str