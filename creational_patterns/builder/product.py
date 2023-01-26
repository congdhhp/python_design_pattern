class Product1:
    def __init__(self):
        self._parts = []

    def add(self, part):
        self._parts.append(part)

    def list_parts(self):
        return self._parts
