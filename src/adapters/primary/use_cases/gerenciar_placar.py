def obter_informacoes_placar(fase_model):

    return {
        'pedidos': fase_model.pedido,
        'pedidos_coletados': fase_model.pedido_coletado
    }