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
    elif "eliminar" in message:
        return "REMOVE_ITEM"
    elif "modificar" in message:
        return "UPDATE_ITEM"
    elif "finalizar" in message or "comprar" in message:
        return "CONFIRM_PURCHASE"
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

def remove_item_node(state):
    try:
        product_id = int(input("ID del producto a eliminar: "))
        print("🤖", state.cart.remove_item(product_id))
    except ValueError:
        print("🤖 Entrada inválida")
    return "MENU"

def update_item_node(state):
    try:
        product_id = int(input("ID del producto: "))
        quantity = int(input("Nueva cantidad: "))
        print("🤖", state.cart.update_quantity(product_id, quantity))
    except ValueError:
        print("🤖 Entrada inválida")
    return "MENU"

def confirm_purchase_node(state):
    if state.cart.items == []:
        print("🤖 Tu carrito está vacío. No puedes finalizar la compra.")
        return "MENU"

    print("🤖 Estás a punto de finalizar la compra.")
    print(state.cart.show_cart())
    confirm = input("¿Confirmas la compra? (si/no): ").lower()

    if confirm == "si":
        return "COLLECT_USER_DATA"
    else:
        print("🤖 Compra cancelada.")
        return "MENU"

def collect_user_data_node(state):
    state.user_name = input("Introduce tu nombre: ")
    state.city = input("Introduce tu ciudad: ")

    print("🤖 Compra confirmada 🎉")
    print(f"Nombre: {state.user_name}")
    print(f"Ciudad: {state.city}")
    print("🤖 Gracias por tu compra. ¡Hasta pronto!")

    return None

def end_node(state):
    print("🤖 Gracias por tu visita. ¡Hasta pronto!")
    return None
