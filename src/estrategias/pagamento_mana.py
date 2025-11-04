from .estrategia_pagamento import EstrategiaPagamento

class PagamentoMana(EstrategiaPagamento):
    def pagar(self, valor: float) -> bool:
        print(f"Processando R${valor:.2f} via Transferência de Mana...")
        print("   -> Pagamento com Mana APROVADO (requer 10 segundos de espera).")
        return True
