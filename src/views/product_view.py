from models.product import Product
from controllers.product_controller import ProductController


class ProductView:
    @staticmethod
    def show_options():
        controller = ProductController()

        while True:
            print("\n1. Montrer la liste des produits\n2. Ajouter un produit\n3. Quitter")
            choice = input("Choisissez une option: ")

            if choice == '1':
                products = controller.list_products()
                ProductView.show_products(products)

            elif choice == '2':
                name, brand, price = ProductView.get_inputs()
                product = Product(None, name, brand, price)
                controller.create_product(product)

            elif choice == '3':
                controller.shutdown()
                break

            else:
                print("Cette option n'existe pas.")

    @staticmethod
    def show_products(products):
        print(
            "\n".join(
                f"{product.id}: {product.name} - {product.brand} - {product.price}$"
                for product in products
            )
        )

    @staticmethod
    def get_inputs():
        name = input("Nom du produit : ").strip()
        brand = input("Marque : ").strip()
        price = float(input("Prix : "))
        return name, brand, price