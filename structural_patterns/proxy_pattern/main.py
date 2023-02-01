from __future__ import annotations
from structural_patterns.proxy_pattern.proxy import *


def client_code(service: ServiceInterface):
    service.request()


if __name__ == '__main__':
    print("===> Client: Executing the client code with a real service:")
    real_service = Service()
    client_code(real_service)

    print("===" * 30)

    print("===> Client: Executing the same client code with a proxy:")
    proxy = Proxy(real_service)
    client_code(proxy)
