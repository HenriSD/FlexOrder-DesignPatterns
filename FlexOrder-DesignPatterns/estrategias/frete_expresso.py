from .estrategia_frete import EstrategiaFrete

class FreteExpresso(EstrategiaFrete):
    def calcular(self, valor_base: float) -> float:
        custo = valor_base * 0.10 + 15.0
        print(f"Frete Expresso: R${custo:.2f}")
        return custo
