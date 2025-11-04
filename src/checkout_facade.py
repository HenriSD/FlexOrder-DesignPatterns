from .subsistemas.sistema_estoque import SistemaEstoque
from .subsistemas.gerador_nota_fiscal import GeradorNotaFiscal

class CheckoutFacade:
    def __init__(self, pedido):
        self.pedido = pedido
        self.estoque = SistemaEstoque()
        self.nota_fiscal = GeradorNotaFiscal()

    def concluir_transacao(self):
        print("=====================================")
        print("INICIANDO CHECKOUT (via Facade)...")
        print("-------------------------------------")

        # 1. Reserva no estoque
        self.estoque.reservar_item()

        # 2. Processamento de pagamento
        sucesso = self.pedido.processar_pagamento()

        # 3. Emissão de nota fiscal
        if sucesso:
            self.nota_fiscal.gerar()
            print("Compra concluída com sucesso! 🎉")
        else:
            print("Falha no pagamento. Transação cancelada.")
