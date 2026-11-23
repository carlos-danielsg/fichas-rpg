from dados import rolar_dados
from fichas import criar_ficha, ATRIBUTOS, DADOS_VALIDOS
from armazenamento import adicionar_ficha


def pedir_texto(pergunta):
    # Pergunta até a pessoa digitar algo
    while True:
        resposta = input(pergunta).strip()
        if resposta:
            return resposta
        print("Esse campo é obrigatório. Digite alguma coisa.")


def pedir_idade():
    while True:
        texto = input("Idade: ").strip()
        try:
            return int(texto)
        except ValueError:
            print("Sua idade deve ser em números.")


def pedir_defeitos():
    #Lê os defeitos separados por vírgula e devolve uma lista de textos.
    texto = input("Defeitos do seu personagem (separados por vírgula): ")
    defeitos = []
    for item in texto.split(","):
        item = item.strip()
        if item:
            defeitos.append(item)
    return defeitos


def pedir_atributos():
    atributos = {}
    for atributo in ATRIBUTOS:
        while True:
            resposta = input(f"Dado de {atributo}: ").strip().lower()
            if resposta not in DADOS_VALIDOS:
                print(f"Escolha um destes dados: {', '.join(DADOS_VALIDOS).upper()}")
            elif resposta in atributos.values():
                print(f"O {resposta.upper()} já foi usado. Escolha outro.")
            else:
                atributos[atributo] = resposta
                break
    return atributos


def confirmar(pergunta):
    #Pergunta s/n até receber uma resposta válida. Devolve True para sim e False para não.
    while True:
        resposta = input(f"{pergunta} (s/n): ").strip().lower()
        if resposta in ("s", "sim"):
            return True
        if resposta in ("n", "nao", "não"):
            return False
        print("Digite s ou n.")


def mostrar_ficha(nome, jogador, idade, medo, motivacao, defeitos, atributos):
    print("\n--- Confira a ficha ---")
    print(f"Nome: {nome}")
    print(f"Jogador: {jogador}")
    print(f"Idade: {idade}")
    print(f"Medo: {medo}")
    print(f"Motivação: {motivacao}")
    print(f"Defeitos: {', '.join(defeitos)}")
    print("Atributos:")
    for atributo, dado in atributos.items():
        print(f"  {atributo}: {dado.upper()}")


def menu_criar_ficha():
    nome = pedir_texto("Nome do personagem: ")
    jogador = pedir_texto("Nome do jogador: ")
    idade = pedir_idade()
    medo = input("Medo do seu personagem: ").strip()
    motivacao = input("Motivação do seu personagem: ").strip()
    defeitos = pedir_defeitos()
    atributos = pedir_atributos()

    mostrar_ficha(nome, jogador, idade, medo, motivacao, defeitos, atributos)
    if not confirmar("Confirma?"):
        print("Ficha cancelada.")
        return

    try:
        ficha = criar_ficha(nome, jogador, idade, medo, motivacao, defeitos, atributos)
        adicionar_ficha(ficha)
        print(f"Ficha de nome '{nome}' criada!")
    except ValueError as erro:
        print(f"Erro: {erro}")
        
if __name__ == "__main__":
    menu_criar_ficha()