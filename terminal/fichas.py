ATRIBUTOS = ["luta", "fuga", "mente", "musculo", "charme", "garra"]
DADOS_VALIDOS = ["d4", "d6", "d8", "d10", "d12", "d20"]

def criar_ficha(nome, jogador, idade, medo, motivacao, defeitos, atributos):
    if not nome.strip():
        raise ValueError("Preencha o nome!")
    
    return {
        "nome": nome,
        "jogador": jogador,
        "sistema": "kids-on-bikes",
        "idade": idade,
        "medo": medo,
        "motivacao": motivacao,
        "defeitos": defeitos,
        "atributos": atributos,
    }