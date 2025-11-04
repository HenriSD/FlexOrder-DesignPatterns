from .estrategia_pagamento import EstrategiaPagamento

class PagamentoCredito(EstrategiaPagamento):
    def pagar(self, valor: float) -> bool:
        print(f"Processando R${valor:.2f} via Cartão de Crédito...")
        if valor < 1000:
            print("   -> Pagamento com Crédito APROVADO.")
            return True
        else:
            print("   -> Pagamento com Crédito REJEITADO (limite excedido).")
            return False
