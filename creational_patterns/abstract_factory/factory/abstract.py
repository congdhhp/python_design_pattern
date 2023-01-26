from __future__ import annotations
from abc import ABC, abstractmethod
from creational_patterns.abstract_factory.product.product_a import AbstractProductA
from creational_patterns.abstract_factory.product.product_b import AbstractProductB


class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass
