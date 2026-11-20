import pytest
from dados import rolar_dados

def test_um_dado_fica_no_intervalo():
    total, rolagens = rolar_dados("1d6")
    assert len(rolagens) == 1
    assert 1 <= total <= 6

def test_entrada_invalida_levanta_erro():
    with pytest.raises(ValueError):
        rolar_dados("abc")

def test_2d6_estrutura_correta():
    for _ in range(500):
        total, rolagens = rolar_dados("2d6")
        assert len(rolagens) == 2
        assert total == sum(rolagens)
        assert 2 <= total <= 12
        for valor in rolagens:
            assert 1 <= valor <= 6

def test_d_sem_quantidade_e_maiuscula():
    total, rolagens = rolar_dados("d20")
    assert len(rolagens) == 1
    assert 1 <= total <= 20

    total, rolagens = rolar_dados("D8")
    assert len(rolagens) == 1
    assert 1 <= total <= 8