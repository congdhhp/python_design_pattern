from __future__ import annotations
from abc import ABC, abstractmethod
from behavioral_patterns.observer.publisher import *


class Subscriber(ABC):
    @abstractmethod
    def update(self, publisher: Publisher):
        pass


class ConcreteSubscriberA(Subscriber):
    def update(self, publisher: Publisher):
        if publisher.state < 3:
            print("ConcreteSubscriberA: Reacted to the event")


class ConcreteSubscriberB(Subscriber):
    def update(self, publisher: Publisher):
        if publisher.state == 0 or publisher.state >= 2:
            print("ConcreteSubscriberB: Reacted to the event")
