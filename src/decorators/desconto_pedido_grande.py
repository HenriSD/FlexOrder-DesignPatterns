from .calculo_base import CalculoValor

class DescontoPedidoGrande(CalculoValor):
    def __init__(self, pedido: CalculoValor):
        self._pedido = pedido

    def calcular(self) -> float:
        valor = self._pedido.calcular()
        if valor > 500:
            print("Aplicando 10% de desconto para pedidos grandes.")
            return valor * 0.90
        return valor
