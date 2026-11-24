import pytest
from fichas import criar_ficha, ATRIBUTOS, DADOS_VALIDOS

ATRIBUTOS_OK = {
    "luta": "d20", "fuga": "d12", "mente": "d10",
    "musculo": "d8", "charme": "d6", "garra": "d4",
}


def montar(nome="Carlos"):
    """Cria uma ficha válida. Só o nome muda de um teste para outro."""
    return criar_ficha(nome, "Fulano", 15, "Altura", "Ajudar a família",
                       ["Teimoso", "Medroso"], ATRIBUTOS_OK)


def test_ficha_valida_tem_os_campos():
    ficha = montar()
    assert ficha["nome"] == "Carlos"
    assert ficha["jogador"] == "Fulano"
    assert ficha["idade"] == 15
    assert ficha["medo"] == "Altura"
    assert ficha["motivacao"] == "Ajudar a família"
    assert ficha["defeitos"] == ["Teimoso", "Medroso"]


def test_sistema_padrao_e_kids_on_bikes():
    assert montar()["sistema"] == "kids-on-bikes"


def test_atributos_ficam_na_ficha():
    assert montar()["atributos"] == ATRIBUTOS_OK

def test_constantes_do_sistema_sao_consistentes():
    # a ficha de exemplo usa exatamente os atributos e os dados do sistema
    assert list(ATRIBUTOS_OK) == ATRIBUTOS
    assert sorted(ATRIBUTOS_OK.values()) == sorted(DADOS_VALIDOS)