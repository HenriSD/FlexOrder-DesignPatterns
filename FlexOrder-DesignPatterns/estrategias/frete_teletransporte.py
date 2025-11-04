from .estrategia_frete import EstrategiaFrete

class FreteTeletransporte(EstrategiaFrete):
    def calcular(self, valor_base: float) -> float:
        custo = 50.0
        print(f"Frete Teletransporte: R${custo:.2f}")
        return custo
