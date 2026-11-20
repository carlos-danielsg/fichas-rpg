import random

MAX_DADOS = 30
MAX_LADOS = 100

def rolar_dados(expressao):
   
    try:
        quantidade_str, lados_str = expressao.lower().split('d')
        
        if quantidade_str == "":
            quantidade = 1
        else:
            quantidade = int(quantidade_str)

        lados = int(lados_str)
    except ValueError:
        raise ValueError("Sua entrada é inválida. (Ex: 2d6, 10d20)")

    if quantidade < 1:
        raise ValueError("A quantidade de dados deve ser pelo menos 1.")
    if quantidade > MAX_DADOS:
        raise ValueError(f"A quantidade de dados não deve ser maior que {MAX_DADOS}.")
    if lados < 2:
        raise ValueError("Um dado deve ter pelo menos 2 lados.")
    if lados > MAX_LADOS:
        raise ValueError(f"Um dado deve ter no maximo {MAX_LADOS} lados.")
    
    resultados = []
    for _ in range(quantidade):
        valor = random.randint(1, lados)
        resultados.append(valor)
    
    return sum(resultados), resultados

if __name__ == "__main__":
    try:
        total, rolagens = rolar_dados("ad20")
        print(f"Rolagens: {rolagens} | Total: {total}")
    except ValueError as erro:
        print(f"Erro: {erro}") 