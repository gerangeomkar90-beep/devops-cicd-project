let cart = [];

function addToCart(item) {
    const existing = cart.find(product => product.id === item.id);

    if (existing) {
        existing.quantity += 1;
    } else {
        cart.push({
            ...item,
            quantity: 1
        });
    }

    updateCart();
    alert(`${item.name} added to cart!`);
}

function updateCart() {
    const count = cart.reduce(
        (total, item) => total + item.quantity,
        0
    );

    document.getElementById("cart-count").textContent = count;

    const cartItems = document.getElementById("cart-items");

    if (cart.length === 0) {
        cartItems.innerHTML = "<p>Your cart is empty.</p>";
    } else {
        cartItems.innerHTML = cart.map(item => `
            <div class="cart-item">
                <span>
                    ${item.emoji} ${item.name}
                    × ${item.quantity}
                </span>
                <strong>
                    ₹${item.price * item.quantity}
                </strong>
            </div>
        `).join("");
    }

    const total = cart.reduce(
        (sum, item) => sum + item.price * item.quantity,
        0
    );

    document.getElementById("cart-total").textContent = total;
}

function openCart() {
    updateCart();
    document.getElementById("cart-modal").style.display = "flex";
}

function closeCart() {
    document.getElementById("cart-modal").style.display = "none";
}

async function placeOrder() {
    const customerName =
        document.getElementById("customer-name").value.trim();

    if (!customerName) {
        alert("Please enter your name.");
        return;
    }

    if (cart.length === 0) {
        alert("Your cart is empty.");
        return;
    }

    const response = await fetch("/api/order", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            customer_name: customerName,
            items: cart
        })
    });

    const result = await response.json();

    const message = document.getElementById("order-message");

    if (result.success) {
        message.textContent =
            `${result.message} Total: ₹${result.total}`;

        cart = [];
        updateCart();
    } else {
        message.textContent = result.message;
    }
}

updateCart();