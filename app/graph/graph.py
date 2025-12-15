from app.graph.state import ChatState
from app.graph.nodes import (
    start_node,
    menu_node,
    add_to_cart_node,
    show_cart_node,
    end_node
)

def run_graph():
    state = ChatState()
    current_node = "START"

    nodes = {
        "START": start_node,
        "MENU": menu_node,
        "ADD_TO_CART": add_to_cart_node,
        "SHOW_CART": show_cart_node,
        "END": end_node
    }

    while current_node:
        current_node = nodes[current_node](state)
