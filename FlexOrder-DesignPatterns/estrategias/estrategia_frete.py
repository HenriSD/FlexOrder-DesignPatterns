from abc import ABC, abstractmethod

class EstrategiaFrete(ABC):
    @abstractmethod
    def calcular(self, valor_base: float) -> float:
        pass