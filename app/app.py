from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

MENU = [
    {
        "id": 1,
        "name": "Margherita Pizza",
        "description": "Classic cheese pizza with tomato and fresh basil.",
        "price": 249,
        "category": "Pizza",
        "emoji": "🍕"
    },
    {
        "id": 2,
        "name": "Veg Burger",
        "description": "Crispy veggie patty with fresh vegetables and sauce.",
        "price": 149,
        "category": "Burger",
        "emoji": "🍔"
    },
    {
        "id": 3,
        "name": "Masala Dosa",
        "description": "Crispy dosa served with potato masala and chutney.",
        "price": 129,
        "category": "Indian",
        "emoji": "🥞"
    },
    {
        "id": 4,
        "name": "Paneer Tikka",
        "description": "Grilled paneer with peppers and Indian spices.",
        "price": 229,
        "category": "Indian",
        "emoji": "🍢"
    },
    {
        "id": 5,
        "name": "Veg Biryani",
        "description": "Aromatic basmati rice cooked with vegetables and spices.",
        "price": 199,
        "category": "Rice",
        "emoji": "🍚"
    },
    {
        "id": 6,
        "name": "Cold Coffee",
        "description": "Chilled creamy coffee served with ice.",
        "price": 99,
        "category": "Drinks",
        "emoji": "🥤"
    }
]


@app.route("/")
def home():
    return render_template("index.html", menu=MENU)


@app.route("/health")
def health():
    return jsonify({"status": "healthy"})


@app.route("/api/menu")
def menu():
    return jsonify(MENU)


@app.route("/api/order", methods=["POST"])
def create_order():
    data = request.get_json(silent=True) or {}

    customer_name = data.get("customer_name", "").strip()
    items = data.get("items", [])

    if not customer_name:
        return jsonify({"success": False, "message": "Customer name is required"}), 400

    if not items:
        return jsonify({"success": False, "message": "Cart is empty"}), 400

    total = sum(
        item.get("price", 0) * item.get("quantity", 1)
        for item in items
    )

    return jsonify({
        "success": True,
        "message": f"Order placed successfully for {customer_name}!",
        "total": total
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
