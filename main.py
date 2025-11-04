from src.pedido import Pedido
from src.estrategias.pagamento_pix import PagamentoPix
from src.estrategias.pagamento_credito import PagamentoCredito
from src.estrategias.pagamento_mana import PagamentoMana
from src.estrategias.frete_normal import FreteNormal
from src.estrategias.frete_expresso import FreteExpresso
from src.estrategias.frete_teletransporte import FreteTeletransporte
from src.decorators.desconto_pix import DescontoPix
from src.decorators.desconto_pedido_grande import DescontoPedidoGrande
from src.decorators.taxa_embalagem_presente import TaxaEmbalagemPresente
from src.checkout_facade import CheckoutFacade

if __name__ == "__main__":
    print("\n===== CENÁRIO 1: PIX + FRETE NORMAL =====")
    itens1 = [{'nome': 'Capa da Invisibilidade', 'valor': 150.0},
              {'nome': 'Poção de Voo', 'valor': 80.0}]
    pedido1 = Pedido(itens1)
    pedido1.definir_pagamento(PagamentoPix())
    pedido1.definir_frete(FreteNormal())

    pedido1_valor = DescontoPix(pedido1)
    checkout1 = CheckoutFacade(pedido1)
    checkout1.concluir_transacao()

    print("\n===== CENÁRIO 2: CRÉDITO + FRETE EXPRESSO + EMBALAGEM =====")
    itens2 = [{'nome': 'Cristal Mágico', 'valor': 600.0}]
    pedido2 = Pedido(itens2)
    pedido2.definir_pagamento(PagamentoCredito())
    pedido2.definir_frete(FreteExpresso())

    pedido2_valor = TaxaEmbalagemPresente(DescontoPedidoGrande(pedido2))
    checkout2 = CheckoutFacade(pedido2)
    checkout2.concluir_transacao()

    print("\n===== CENÁRIO 3: MANA + FRETE TELETRANSPORTE =====")
    itens3 = [{'nome': 'Varinha de Carvalho', 'valor': 300.0}]
    pedido3 = Pedido(itens3)
    pedido3.definir_pagamento(PagamentoMana())
    pedido3.definir_frete(FreteTeletransporte())

    checkout3 = CheckoutFacade(pedido3)
    checkout3.concluir_transacao()
