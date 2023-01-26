from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractProductA(ABC):
    @abstractmethod
    def useful_function_a(self):
        pass


class ConcreteProductA1(AbstractProductA):
    def useful_function_a(self):
        return "The result of the product A1."


class ConcreteProductA2(AbstractProductA):
    def useful_function_a(self):
        return "The result of the product A2."
