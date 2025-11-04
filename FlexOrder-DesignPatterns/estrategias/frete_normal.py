from .estrategia_frete import EstrategiaFrete

class FreteNormal(EstrategiaFrete):
    def calcular(self, valor_base: float) -> float:
        custo = valor_base * 0.05
        print(f"Frete Normal: R${custo:.2f}")
        return custo
