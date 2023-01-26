from __future__ import annotations
from creational_patterns.abstract_factory.factory.abstract import AbstractFactory
from creational_patterns.abstract_factory.product.product_a import ConcreteProductA2
from creational_patterns.abstract_factory.product.product_b import ConcreteProductB2


class ConcreteFactory2(AbstractFactory):
    def create_product_a(self) -> ConcreteProductA2:
        return ConcreteProductA2()

    def create_product_b(self) -> ConcreteProductB2:
        return ConcreteProductB2()

