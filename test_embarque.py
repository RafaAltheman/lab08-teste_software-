
import pytest

from embarque import (
    pode_embarcar,
    pode_embarcar_original,
)
from mcdc import (
    regra,
    tabela_verdade,
    pares_independentes,
    conjuntos_mcdc_minimos,
)


def test_pares_independentes():
    pares = pares_independentes(regra, 4)

    assert [len(pares[i]) for i in range(4)] == [
        3, 3, 1, 1
    ]


def test_conjuntos_minimos():
    conjuntos = conjuntos_mcdc_minimos(regra, 4)

    assert len(conjuntos) == 4
    assert all(len(c) == 5 for c in conjuntos)


@pytest.mark.parametrize(
    "valores",
    [
        (True, True, True, True),
        (False, False, False, False),
    ],
)
def test_extremos(valores):
    esperado = regra(*valores)

    assert pode_embarcar_original(*valores) == esperado
    assert pode_embarcar(*valores) == esperado


def test_deteccao_defeito_mcdc():
    tabela = tabela_verdade()
    conjuntos = conjuntos_mcdc_minimos(regra, 4)

    detectaram = []

    for conjunto in conjuntos:
        encontrou = any(
            pode_embarcar_original(*tabela[i])
            != regra(*tabela[i])
            for i in conjunto
        )
        detectaram.append(encontrou)

    assert detectaram.count(True) == 3
    assert detectaram.count(False) == 1


def test_conjunto_que_nao_detecta():
    tabela = tabela_verdade()

    for i in [6, 10, 12, 13, 14]:
        valores = tabela[i]
        assert pode_embarcar_original(*valores) == regra(
            *valores
        )


def test_defeito_original():
    valores = (False, False, False, True)

    assert regra(*valores) is False
    assert pode_embarcar_original(*valores) is True


@pytest.mark.parametrize("valores", tabela_verdade())
def test_mcc_versao_corrigida(valores):
    assert pode_embarcar(*valores) == regra(*valores)


# Mostra que MCC encontra o defeito original.
def test_mcc_detecta_defeito():
    diferencas = [
        valores
        for valores in tabela_verdade()
        if pode_embarcar_original(*valores)
        != regra(*valores)
    ]

    assert len(diferencas) > 0
