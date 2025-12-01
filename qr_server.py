from database.models import Producto
from database.db import Session
from flask import Flask, render_template, abort

app = Flask(__name__)

@app.route("/")
def home():
    return "QR SERVER HOME"

@app.route("/test")
def test():
    return "QR SERVER TEST"

@app.route("/producto/<int:id_producto>")
def ver_producto(id_producto):
    session = Session()

    producto = session.query(Producto).filter(
        Producto.id_producto == id_producto
    ).first()

    if not producto:
        abort(404)

    return render_template(
        "producto.html",
        producto=producto
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)

