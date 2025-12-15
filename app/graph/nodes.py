from app.catalog.products import PRODUCTS

def start_node(state):
    print("🤖 Bienvenido a la tienda online")
    return "MENU"

def menu_node(state):
    message = input("Tú: ").lower()
    state.last_message = message

    if message == "salir":
        return "END"
    elif "productos" in message:
        print("🤖 Productos disponibles:")
        for p in PRODUCTS:
            print(f"- {p['id']} {p['name']} {p['price']}€")
        return "MENU"
    elif "añadir" in message:
        return "ADD_TO_CART"
    elif "carrito" in message:
        return "SHOW_CART"
    else:
        print("🤖 No he entendido el mensaje")
        return "MENU"

def add_to_cart_node(state):
    try:
        product_id = int(input("ID del producto: "))
        quantity = int(input("Cantidad: "))

        product = next((p for p in PRODUCTS if p["id"] == product_id), None)

        if not product:
            print("🤖 Producto no encontrado")
        else:
            print("🤖", state.cart.add_item(product, quantity))
    except ValueError:
        print("🤖 Entrada inválida")

    return "MENU"

def show_cart_node(state):
    print(state.cart.show_cart())
    return "MENU"

def end_node(state):
    print("🤖 Gracias por tu compra. ¡Hasta pronto!")
    return None
