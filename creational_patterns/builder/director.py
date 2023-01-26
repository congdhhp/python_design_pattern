from builder import *


class Director:
    def __init__(self):
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder):
        self._builder = builder

    def build_minimal_viable_product(self) -> None:
        self.builder.make_part_a()

    def build_full_featured_product(self) -> None:
        self.builder.make_part_a()
        self.builder.make_part_b()
        self.builder.make_part_c()
    