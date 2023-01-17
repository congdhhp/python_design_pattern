from director import Director
from builder import *


if __name__ == '__main__':
    director = Director()
    builder = Product1Builder()
    director.builder = builder

    print("Standard basic product: ")
    director.build_minimal_viable_product()
    product = director.builder.get_product()
    print(product.list_parts())

    print("Standard full featured product: ")
    director.build_full_featured_product()
    product = director.builder.get_product()
    print(product.list_parts())
