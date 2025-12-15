from app.cart.cart import Cart

def test_add_item():
    cart = Cart()
    product = {"id": 1, "name": "Test", "price": 10}
    result = cart.add_item(product, 2)

    assert result == "Test añadido al carrito"
    assert len(cart.items) == 1
    assert cart.items[0]["quantity"] == 2

def test_total_cart():
    cart = Cart()
    product = {"id": 1, "name": "Test", "price": 10}
    cart.add_item(product, 2)

    message = cart.show_cart()
    assert "20.00€" in message

def test_invalid_quantity():
    cart = Cart()
    product = {"id": 1, "name": "Test", "price": 10}
    result = cart.add_item(product, -1)

    assert result == "Cantidad inválida"
