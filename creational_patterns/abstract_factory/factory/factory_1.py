from __future__ import annotations
from creational_patterns.abstract_factory.factory.abstract import AbstractFactory
from creational_patterns.abstract_factory.product.product_a import ConcreteProductA1
from creational_patterns.abstract_factory.product.product_b import ConcreteProductB1


class ConcreteFactory1(AbstractFactory):
    def create_product_a(self) -> ConcreteProductA1:
        return ConcreteProductA1()

    def create_product_b(self) -> ConcreteProductB1:
        return ConcreteProductB1()

