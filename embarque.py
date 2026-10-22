
def pode_embarcar_original(
    cartao, documento, grupo_chamado, prioridade
):
    # Codigo original com defeito.
    return (
        cartao and documento and grupo_chamado
        or prioridade
    )


def pode_embarcar(
    cartao, documento, grupo_chamado, prioridade
):
    # Versao corrigida conforme a especificacao.
    return (
        cartao
        and documento
        and (grupo_chamado or prioridade)
    )
