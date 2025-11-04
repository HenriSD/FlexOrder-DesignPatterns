from abc import ABC, abstractmethod

class CalculoValor(ABC):
    @abstractmethod
    def calcular(self) -> float:
        pass
