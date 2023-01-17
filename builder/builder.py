from __future__ import annotations
from abc import ABC, abstractmethod
from product import *


class Builder(ABC):

    @abstractmethod
    def make_part_a(self) -> None:
        pass

    @abstractmethod
    def make_part_b(self) -> None:
        pass

    @abstractmethod
    def make_part_c(self) -> None:
        pass

    @abstractmethod
    def get_product(self):
        pass


class Product1Builder(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self):
        self._product = Product1()

    def get_product(self) -> Product1:
        product = self._product
        self.reset()
        return product

    def make_part_a(self) -> None:
        self._product.add('PartA1')

    def make_part_b(self) -> None:
        self._product.add('PartB1')

    def make_part_c(self) -> None:
        self._product.add('PartC1')
