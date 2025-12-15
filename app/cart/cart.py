class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        if quantity <= 0:
            return "Cantidad inválida"

        # Comprobar si el producto ya está en el carrito
        for item in self.items:
            if item["id"] == product["id"]:
                item["quantity"] += quantity
                return f"Cantidad actualizada de {product['name']}"

        # Si no está, añadirlo
        self.items.append({
            "id": product["id"],
            "name": product["name"],
            "price": product["price"],
            "quantity": quantity
        })

        return f"{product['name']} añadido al carrito"

    def show_cart(self):
        if not self.items:
            return "El carrito está vacío"

        message = "🛒 Carrito de la compra:\n"
        total = 0

        for item in self.items:
            subtotal = item["price"] * item["quantity"]
            total += subtotal
            message += f"- {item['name']} x{item['quantity']} = {subtotal:.2f}€\n"

        message += f"Total: {total:.2f}€"
        return message
