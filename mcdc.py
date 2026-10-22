
from itertools import product, combinations


# a) Regra correta, diretamente da especificacao.
def regra(cartao, documento, grupo_chamado, prioridade):
    return cartao and documento and (
        grupo_chamado or prioridade
    )


def tabela_verdade():
    return list(product([False, True], repeat=4))


def pares_independentes(decisao, n):
    tabela = list(product([False, True], repeat=n))
    resultado = {}

    for condicao in range(n):
        pares = []

        for i, linha1 in enumerate(tabela):
            for j in range(i + 1, len(tabela)):
                linha2 = tabela[j]

                diferencas = [
                    k for k in range(n)
                    if linha1[k] != linha2[k]
                ]

                if diferencas == [condicao]:
                    if decisao(*linha1) != decisao(*linha2):
                        pares.append((i, j))

        resultado[condicao] = pares

    return resultado


def conjuntos_mcdc_minimos(decisao, n):
    pares = pares_independentes(decisao, n)
    candidatos = list(range(2 ** n))

    for tamanho in range(1, len(candidatos) + 1):
        validos = []

        for conjunto in combinations(candidatos, tamanho):
            selecionados = set(conjunto)

            if all(
                any(
                    i in selecionados and j in selecionados
                    for i, j in pares[k]
                )
                for k in range(n)
            ):
                validos.append(conjunto)

        if validos:
            return validos

    return []


if __name__ == "__main__":
    nomes = [
        "cartao",
        "documento",
        "grupo_chamado",
        "prioridade",
    ]

    pares = pares_independentes(regra, 4)
    conjuntos = conjuntos_mcdc_minimos(regra, 4)

    print("Pares independentes:")
    for i, nome in enumerate(nomes):
        print(nome, pares[i], "Total:", len(pares[i]))

    print("\nQuantidade de conjuntos minimos:", len(conjuntos))
    print("Casos por conjunto:", len(conjuntos[0]))

    for i, conjunto in enumerate(conjuntos, 1):
        print(f"Conjunto {i}: {conjunto}")


# b) Resultados:
#
# Cartao: 3 pares independentes.
# Documento: 3 pares independentes.
# Grupo chamado: 1 par independente.
# Prioridade: 1 par independente.
#
# Existem 4 conjuntos MC/DC minimos,
# cada um com 5 casos de teste.
#
# c) Os testes com todas as entradas True
# e todas False nao identificam o defeito.
#
# d) Dos 4 conjuntos minimos, 3 identificam
# o defeito e 1 nao identifica.
#
# O defeito ocorre porque "or prioridade"
# permite embarque sem cartao ou documento.
#
# O MCC sempre encontraria o defeito porque
# testa as 16 combinacoes das 4 condicoes.
