import json
from web.db import conectar
import sqlite3

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

def listar_fichas_campanha(campanha_id):
    conexao = conectar()
    conexao.row_factory = sqlite3.Row
    linhas = conexao.execute(
        "SELECT fichas.id, fichas.nome, fichas.pv_atual, fichas.pv_max, fichas.dados, "
        "usuarios.nome AS nome_jogador "
        "FROM fichas "
        "JOIN usuarios ON fichas.dono_id = usuarios.id "
        "WHERE fichas.campanha_id = ?",
        (campanha_id,),
    ).fetchall()
    conexao.close()

    resultado = []
    for linha in linhas:
        ficha = dict(linha)
        ficha["dados"] = json.loads(ficha["dados"])
        resultado.append(ficha)
    return resultado

def registrar_rolagem(ficha_id, expressao, dados_sorteados, total):
    ficha = buscar_ficha(ficha_id)
    if ficha is None:
        raise ValueError(f"Ficha {ficha_id} não existe!")
    resultado = ",".join(str(dado) for dado in dados_sorteados)

    conexao = conectar()
    cursor = conexao.execute(
        "INSERT INTO rolagens (ficha_id, campanha_id, expressao, resultado, total) "
        "VALUES (?, ?, ?, ?, ?)",
        (ficha_id, ficha["campanha_id"], expressao, resultado, total),
    )
    conexao.commit()
    novo_id = cursor.lastrowid
    conexao.close()
    return novo_id