# Shopping Chatbot con LangGraph

Este proyecto consiste en un chatbot conversacional de carrito de compra desarrollado en Python.
Simula el flujo de compra de una tienda online y utiliza LangGraph para modelar los distintos
estados de la conversación (navegación, edición del carrito, confirmación de pedido, etc.).

El objetivo del proyecto es mostrar la estructura del código, el manejo de estados y
la lógica de negocio, no construir un producto final completo.

## Demo web (opcional)

El proyecto incluye una demo web mínima usando FastAPI como interfaz adicional.
Esta interfaz expone una API HTTP para interactuar con el carrito de compra.

Para ejecutar la demo web:

```bash
uvicorn app.api:app --reload
La documentación interactiva está disponible en http://127.0.0.1:8000/docs
Desde esta interfaz se pueden:
Consultar productos
Añadir productos al carrito
Ver el contenido del carrito
---

## Tecnologías utilizadas

- Python 3
- LangGraph (modelado de estados)
- Pytest (tests automatizados)
- Interfaz por línea de comandos (CLI)
- (Opcional) FastAPI para demo web

---

## Instalación

Requisitos:
- Python 3.10 o superior

Clonar el repositorio:
```bash
git clone https://github.com/mariosf1520/shopping-chatbot-langgraph.git
cd shopping-chatbot-langgraph

