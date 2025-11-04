class Pedido:
    def __init__(self, itens: list, distancia_km: float = 10):
        self.itens = itens
        self.valor_base = sum(item['valor'] for item in itens)
        self.distancia = distancia_km
        self.estrategia_pagamento = None
        self.estrategia_frete = None

    def definir_pagamento(self, estrategia_pagamento):
        self.estrategia_pagamento = estrategia_pagamento

    def definir_frete(self, estrategia_frete):
        self.estrategia_frete = estrategia_frete

    def calcular_total(self) -> float:
        frete = self.estrategia_frete.calcular(self.valor_base)
        return self.valor_base + frete

    def processar_pagamento(self) -> bool:
        total = self.calcular_total()
        return self.estrategia_pagamento.pagar(total)

    # Para integração com Decorators
    def calcular(self) -> float:
        return self.calcular_total()
