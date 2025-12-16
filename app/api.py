from fastapi import FastAPI
from app.graph.state import ChatState
from app.catalog.products import PRODUCTS

app = FastAPI(title="Shopping Chatbot API")

state = ChatState()

@app.get("/")
def root():
    return {"message": "Shopping Chatbot API running"}

@app.get("/products")
def get_products():
    return PRODUCTS

@app.post("/cart/add")
def add_to_cart(product_id: int, quantity: int):
    product = next((p for p in PRODUCTS if p["id"] == product_id), None)
    if not product:
        return {"error": "Producto no encontrado"}
    return {"message": state.cart.add_item(product, quantity)}

@app.get("/cart")
def show_cart():
    return {
        "items": state.cart.items,
        "total": state.cart.total()
    }