from .calculo_base import CalculoValor

class DescontoPix(CalculoValor):
    def __init__(self, pedido: CalculoValor):
        self._pedido = pedido

    def calcular(self) -> float:
        valor = self._pedido.calcular()
        print("Aplicando 5% de desconto PIX.")
        return valor * 0.95
