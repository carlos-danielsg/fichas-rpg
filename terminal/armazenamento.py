import json
from pathlib import Path
from web.db import conectar
import sqlite3

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

def criar_ficha(nome, dono_id, campanha_id, pv_max, atributos):
    conexao = conectar()
    cursor = conexao.execute(
        "INSERT INTO fichas (nome, pv_atual, pv_max, dados, dono_id, campanha_id) "
        "VALUES (?, ?, ?, ?, ?, ?)",
        (nome, 0, pv_max, json.dumps(atributos), dono_id, campanha_id),
    )
    conexao.commit()
    novo_id = cursor.lastrowid
    conexao.close()
    return novo_id

def buscar_ficha(ficha_id):
    conexao = conectar()
    conexao.row_factory = sqlite3.Row
    linha = conexao.execute(
        "SELECT * FROM fichas WHERE id = ?",
        (ficha_id,),
    ).fetchone()
    conexao.close()

    if linha is None:
        return None

    ficha = dict(linha)
    ficha["dados"] = json.loads(ficha["dados"])
    return ficha