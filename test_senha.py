
import pytest
from senha import forca


# a) GFC e complexidade ciclomatica
#
# Nos de decisao:
# 1. len(senha) < 8
# 2. for c in senha
# 3. c.isdigit()
# 4. not c.isalnum()
# 5. pontos >= 4
#
# V(G) = numero de decisoes + 1 = 5 + 1 = 6
#
# Pela formula V(G) = E - N + 2P:
# Considerando 13 nos, 17 arestas e P = 1:
# V(G) = 17 - 13 + 2 = 6
#
# b) Base de 6 caminhos:
#
# P1: senha curta -> "fraca"
# P2: senha valida, zero iteracoes -> inviavel
# P3: apenas letras -> "media"
# P4: letras e um digito -> "media"
# P5: letras e um simbolo -> "media"
# P6: pontos >= 4 -> "forte"
#
# P1 desvia pelo retorno antecipado.
# P2 representa a saida imediata do laco.
# P3 percorre o caminho sem pontuar.
# P4 adiciona o ramo de digito.
# P5 adiciona o ramo de simbolo.
# P6 adiciona o retorno "forte".
#
# P2 e inviavel porque uma senha que passa
# pelo primeiro if tem pelo menos 8 caracteres.
# Portanto, o for obrigatoriamente executa.


@pytest.mark.parametrize(
    "senha, esperado",
    [
        ("abc", "fraca"),
        ("abcdefgh", "media"),
        ("abcdefg1", "media"),
        ("abcdefg!", "media"),
        ("abcd12!!", "forte"),
    ],
)
def test_caminhos_viaveis(senha, esperado):
    assert forca(senha) == esperado


# c) Cobertura de ramos
#
# V(G) = 6, mas um caminho e inviavel.
# Com apenas 3 testes e possivel atingir
# 100% de cobertura de ramos:
# - senha curta
# - senha longa somente com letras
# - senha longa com letras, numeros e simbolos
#
# A base possui 6 caminhos independentes,
# mas nao e necessario executar 6 testes
# para obter 100% de cobertura de ramos.


@pytest.mark.parametrize(
    "senha, esperado",
    [
        ("abc", "fraca"),
        ("abcdefgh", "media"),
        ("abcd12!!", "forte"),
    ],
)
def test_cobertura_minima(senha, esperado):
    assert forca(senha) == esperado


# d) Teste de lacos
#
# Zero iteracoes: inviavel apos passar pelo if.
# Uma iteracao: inviavel.
# Duas iteracoes: inviavel.
# O minimo para entrar no for e 8 iteracoes.
# Nao existe limite maximo definido no codigo.
#
# Casos adicionais: 8, 9 e varias iteracoes.


@pytest.mark.parametrize(
    "senha, esperado",
    [
        ("abcdefgh", "media"),
        ("abcdefghi", "media"),
        ("abcdefghij", "media"),
        ("12345678", "forte"),
        ("!!!!!!!!", "forte"),
        ("abcde123456789", "forte"),
    ],
)
def test_lacos(senha, esperado):
    assert forca(senha) == esperado
