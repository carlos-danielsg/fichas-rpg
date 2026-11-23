from dados import rolar_dados
from fichas import criar_ficha, resumo, ATRIBUTOS, DADOS_VALIDOS
from armazenamento import adicionar_ficha, carregar_fichas


# --- Entrada de dados ---

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
    # Lê os defeitos separados por vírgula e devolve uma lista de textos.
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


# --- Conversa genérica com o usuário ---

def confirmar(pergunta):
    # Pergunta s/n até receber uma resposta válida. Devolve True para sim e False para não.
    while True:
        resposta = input(f"{pergunta} (s/n): ").strip().lower()
        if resposta in ("s", "sim"):
            return True
        if resposta in ("n", "nao", "não"):
            return False
        print("Digite s ou n.")


def escolher_algo(titulo, itens):
    print(f"\n{titulo}")
    for numero, item in enumerate(itens, start=1):
        print(f"{numero} - {item}")
    try:
        escolha = int(input("Número: "))
    except ValueError:
        print("Digite um número válido.")
        return None
    if not 1 <= escolha <= len(itens):
        print("Essa opção não existe!")
        return None
    return itens[escolha - 1]


# --- Exibição ---

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


# --- Telas do menu ---

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


def menu_mestre():
    fichas = carregar_fichas()
    if not fichas:
        print("Não há fichas cadastradas.")
        return
    for ficha in fichas.values():
        print(resumo(ficha))


def menu_rolar_atributo():
    fichas = carregar_fichas()
    if not fichas:
        print("Nenhuma ficha cadastrada!")
        return
    nomes = [ficha["nome"] for ficha in fichas.values()]
    nome = escolher_algo("Qual personagem?", nomes)
    if nome is None:
        return
    ficha = fichas[nome.strip().lower()]

    atributo = escolher_algo("Qual atributo?", ATRIBUTOS)
    if atributo is None:
        return

    dado = ficha["atributos"][atributo]
    total, rolagens, _ = rolar_dados(dado)
    print(f"{nome} testa {atributo} ({dado.upper()}): {total}")


# --- Menu principal ---

def menu_principal():
    while True:
        print("\n--- Fichas RPG ---")
        print("1 - Criar ficha")
        print("2 - Resumo do mestre")
        print("3 - Rolar atributos")
        print("0 - Sair")

        opcao = input("Qual deseja usar: ").strip()

        if opcao == "0":
            print("Até a próxima!")
            break
        elif opcao == "1":
            menu_criar_ficha()
        elif opcao == "2":
            menu_mestre()
        elif opcao == "3":
            menu_rolar_atributo()
        else:
            print("\nOpção inválida.")


if __name__ == "__main__":
    menu_principal()