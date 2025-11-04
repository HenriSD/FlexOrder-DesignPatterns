from .estrategia_pagamento import EstrategiaPagamento

class PagamentoPix(EstrategiaPagamento):
    def pagar(self, valor: float) -> bool:
        print(f"Processando pagamento de R${valor:.2f} via PIX...")
        print("   -> Pagamento com PIX APROVADO (QR Code gerado).")
        return True
