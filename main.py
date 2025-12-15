from app.catalog.products import PRODUCTS

print("🤖 Bienvenido al chatbot de la tienda")

while True:
    mensaje = input("Tú: ")

    if mensaje.lower() == "salir":
        print("🤖 Gracias por usar el chatbot. ¡Hasta luego!")
        break

    elif "hola" in mensaje.lower():
        print("🤖 Hola 🙂 ¿Qué te gustaría hacer?")

    elif "productos" in mensaje.lower():
        print("🤖 Productos disponibles:")
        for p in PRODUCTS:
            print(f"- {p['id']}: {p['name']} - {p['price']}€")

    else:
        print("🤖 No he entendido el mensaje. Prueba con 'ver productos' o 'salir'.")
