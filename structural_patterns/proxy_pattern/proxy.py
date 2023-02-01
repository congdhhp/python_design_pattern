from __future__ import annotations
from abc import ABC, abstractmethod


class ServiceInterface(ABC):
    @abstractmethod
    def request(self):
        pass


class Service(ServiceInterface):
    def request(self):
        print("RealSubject: Handling request.")


class Proxy(ServiceInterface):
    def __init__(self, service: Service):
        self._service = service

    def request(self):
        if self.check_access():
            self._service.request()
            self.log_access()

    @staticmethod
    def check_access() -> bool:
        print("Proxy: Checking access prior to firing a real request.")
        return True

    @staticmethod
    def log_access():
        print("Proxy: Logging the time of request.", end="")

