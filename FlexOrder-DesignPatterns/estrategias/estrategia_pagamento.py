from abc import ABC, abstractmethod

class EstrategiaPagamento(ABC):
    @abstractmethod
    def pagar(self, valor: float) -> bool:
        pass