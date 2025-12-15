from app.catalog.products import PRODUCTS
from app.cart.cart import Cart

cart = Cart()

print("🤖 Bienvenido al chatbot de la tienda")

while True:
    mensaje = input("Tú: ").lower()

    if mensaje == "salir":
        print("🤖 Gracias por usar el chatbot. ¡Hasta luego!")
        break

    elif "productos" in mensaje:
        print("🤖 Productos disponibles:")
        for p in PRODUCTS:
            print(f"- {p['id']}: {p['name']} - {p['price']}€")

    elif "añadir" in mensaje:
        try:
            product_id = int(input("ID del producto: "))
            quantity = int(input("Cantidad: "))

            product = next((p for p in PRODUCTS if p["id"] == product_id), None)

            if not product:
                print("🤖 Producto no encontrado")
            else:
                result = cart.add_item(product, quantity)
                print(f"🤖 {result}")

        except ValueError:
            print("🤖 Entrada inválida")

    elif "carrito" in mensaje:
        print(cart.show_cart())

    else:
        print("🤖 No he entendido el mensaje")
