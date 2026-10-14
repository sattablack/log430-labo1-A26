"""
Store manager application
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""
from views.product_view import ProductView
from views.user_view import UserView

if __name__ == '__main__':
    print("===== LE MAGASIN DU COIN =====")

    while True:
            print("\n1. Utilisateurs\n2. Produits\n3. Quitter")
            choice = input("Choisissez une option: ")

            if choice == '1':
                UserView.show_options()

            elif choice == '2':
                ProductView.show_options()

            elif choice == '3':
                break

            else:
                print("Cette option n'existe pas.")