from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
from random import randrange
from behavioral_patterns.observer.subscriber import *


class Publisher(ABC):
    @abstractmethod
    def attach(self, subscriber: Subscriber):
        pass

    @abstractmethod
    def detach(self, subscriber: Subscriber):
        pass

    @abstractmethod
    def notify(self):
        pass


class ConcretePublisher(Publisher):
    _state: int = None
    _subscribers: List[Subscriber] = []

    @property
    def state(self):
        return self._state

    def attach(self, subscriber: Subscriber):
        print("Publisher: Attached an subscriber.")
        self._subscribers.append(subscriber)

    def detach(self, subscriber: Subscriber):
        print("Publisher: Detached an subscriber.")
        self._subscribers.remove(subscriber)

    def notify(self):
        print("Publisher: Notifying subscribers...")
        for subscriber in self._subscribers:
            subscriber.update(self)

    def some_business_logic(self):
        print("\nPublisher: I'm doing something important.")
        self._state = randrange(0, 10)

        print(f"Publisher: My state has just changed to: {self._state}")
        self.notify()

