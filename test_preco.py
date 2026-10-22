
import pytest

from preco import (
    preco_final,
    preco_final_original,
)


# a) Definicoes e usos no codigo original.
#
# Numeracao conforme o PDF:
#
# Variavel total:
# D2: linha 2 - definicao inicial
# U5: linha 5 - c-use
# D5: linha 5 - redefinicao
# U6: linha 6 - p-use
# D7: linha 7 - redefinicao
# U8: linha 8 - c-use
#
# Variavel desconto:
# D4: linha 4 - definicao
# U5: linha 5 - c-use
#
# Pares du de total:
# (2,5)
# (2,6)
# (2,8)
# (5,6)
# (5,8)
# (7,8)
#
# Par du de desconto:
# (4,5)
#
# Para p-use, considera-se cada resultado
# possivel da decisao na linha 6.
#
# b) A suite original contem:
#
# preco_final(60, True) == 50
# preco_final(200, False) == 200
#
# A suite percorre todos os ramos,
# mas nao percorre o par (5,8).
#
# Esse par exige que o valor calculado na
# linha 5 chegue ao retorno da linha 8
# sem ser sobrescrito na linha 7.
#
# c) O teste (200, True) revela o defeito.
# Esperado: 160
# Original: 120
#
# O erro acontece porque o desconto de 20%
# e aplicado duas vezes.
#
# A suite original nao detectava o problema
# pois, com preco 60 e VIP, o resultado
# incorreto era mascarado pelo minimo de 50.


# Suite original do enunciado.
@pytest.mark.parametrize(
    "preco, vip, esperado",
    [
        (60, True, 50),
        (200, False, 200),
    ],
)
def test_suite_original(preco, vip, esperado):
    assert preco_final_original(preco, vip) == esperado


def test_par_du_faltante():
    assert preco_final(200, True) == 160


def test_defeito_original():
    assert preco_final_original(200, True) == 120
    assert preco_final(200, True) == 160


@pytest.mark.parametrize(
    "preco, vip, esperado",
    [
        (60, True, 50),
        (200, False, 200),
        (200, True, 160),
        (100, True, 80),
        (100, False, 100),
        (50, False, 50),
        (50, True, 50),
        (40, False, 50),
        (40, True, 50),
        (250, True, 200),
    ],
)
def test_preco_corrigido(preco, vip, esperado):
    assert preco_final(preco, vip) == pytest.approx(
        esperado
    )


@pytest.mark.parametrize(
    "preco, vip",
    [
        (0, False),
        (10, True),
        (30, False),
        (60, True),
    ],
)
def test_preco_minimo(preco, vip):
    assert preco_final(preco, vip) >= 50
