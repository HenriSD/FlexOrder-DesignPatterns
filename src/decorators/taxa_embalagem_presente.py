from .calculo_base import CalculoValor

class TaxaEmbalagemPresente(CalculoValor):
    def __init__(self, pedido: CalculoValor):
        self._pedido = pedido

    def calcular(self) -> float:
        valor = self._pedido.calcular()
        print("Adicionando R$5.00 de embalagem de presente.")
        return valor + 5.0
