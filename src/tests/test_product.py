from daos.product_dao import ProductDAO
from models.product import Product
from decimal import Decimal

dao = ProductDAO()

def test_product_select():
    product = Product(None, "Keyboard", "Logitech", 79.99)
    assigned_id = dao.insert(product)

    product_list = dao.select_all()
    ids = [p.id for p in product_list]

    assert assigned_id in ids

    dao.delete(assigned_id)

def test_product_insert():
    product = Product(None, "Laptop", "Dell", 999.99)
    dao.insert(product)

    product_list = dao.select_all()
    names = [p.name for p in product_list]

    assert product.name in names

def test_product_update():
    product = Product(None, "Laptop", "Dell", 999.99)
    assigned_id = dao.insert(product)

    product.id = assigned_id
    product.price = 899.99

    dao.update(product)

    product_list = dao.select_all()
    prices = [p.price for p in product_list]

    assert Decimal("899.99") in prices

    dao.delete(assigned_id)

def test_product_delete():
    product = Product(None, "Mouse", "Logitech", 49.99)
    assigned_id = dao.insert(product)

    dao.delete(assigned_id)

    product_list = dao.select_all()
    ids = [p.id for p in product_list]

    assert assigned_id not in ids