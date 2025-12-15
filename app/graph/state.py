from app.cart.cart import Cart

class ChatState:
    def __init__(self):
        self.cart = Cart()
        self.last_message = ""
