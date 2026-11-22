import random
import re

MAX_DADOS = 30
MAX_LADOS = 100

# quantidade (opcional), a letra d, lados e, se houver, sinal e valor do modificador
PADRAO = re.compile(r"(\d*)d(\d+)(?:\s*([+-])\s*(\d+))?", re.IGNORECASE)

def interpretar(expressao):
    m = PADRAO.fullmatch(expressao.strip())
    if m is None:
        raise ValueError("Sua entrada é invalida. (Ex: 2d6, 10d20, 1d8+3)")

    quantidade = int(m.group(1) or 1)
    lados = int(m.group(2))
    if m.group(3) is None:
        modificador = 0
    else:
        modificador = int(m.group(3) + m.group(4))
    return quantidade, lados, modificador

def rolar_dados(expressao):

    quantidade, lados, modificador = interpretar(expressao)

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
    
    return sum(resultados) + modificador, resultados

if __name__ == "__main__":
    try:
        total, rolagens = rolar_dados("ad20")
        print(f"Rolagens: {rolagens} | Total: {total}")
    except ValueError as erro:
        print(f"Erro: {erro}") 