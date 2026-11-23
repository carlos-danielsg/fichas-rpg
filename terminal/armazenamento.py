import json
from pathlib import Path

ARQUIVO = Path(__file__).parent / "fichas.json"

def carregar_fichas():
    try:
        with open(ARQUIVO, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def salvar_fichas(fichas):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(fichas, f, ensure_ascii= False, indent= 2)

def adicionar_ficha(ficha):
    fichas = carregar_fichas()
    nome = ficha["nome"].strip().lower()
    if nome in fichas:
        raise ValueError(f"A ficha com o nome '{nome}' já existe.")
    fichas[nome] = ficha
    salvar_fichas(fichas)