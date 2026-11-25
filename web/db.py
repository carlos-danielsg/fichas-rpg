import sqlite3
from pathlib import Path

PASTA = Path(__file__).parent

def conectar(caminho=PASTA /"fichas.db"):
    conexao = sqlite3.connect(caminho)
    conexao.execute("PRAGMA foreign_keys = ON")
    return conexao

def criar_banco(caminho=PASTA / "fichas.db"):
    conexao = conectar(caminho)
    with open(PASTA / "schema.sql", encoding="utf-8") as arquivo:
        conexao.executescript(arquivo.read())
    conexao.commit()
    conexao.close()

if __name__ == "__main__":
    criar_banco()
    print("Banco criado!")