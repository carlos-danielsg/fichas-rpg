import sqlite3

def conectar(caminho="fichas.db"):
    conexao = sqlite3.connect(caminho)
    conexao.execute("PRAGMA foreign_keys = ON")
    return conexao

def criar_banco(caminho="fichas.db"):
    conexao = conectar(caminho)
    with open("schema.sql", encoding="utf-8") as arquivo:
        conexao.executescript(arquivo.read())
    conexao.commit()
    conexao.close()

if __name__ == "__main__":
    criar_banco()
    print("Banco criado!")