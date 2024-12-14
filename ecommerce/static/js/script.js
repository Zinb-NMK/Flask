document.addEventListener("DOMContentLoaded", () => {
    // Fetch all products and display them on the page
    fetch("/products")
        .then(response => response.json())
        .then(products => {
            const productList = document.getElementById("product-list");
            products.forEach(product => {
                const productDiv = document.createElement("div");
                productDiv.innerHTML = `
                    <h2>${product.name}</h2>
                    <p>${product.description}</p>
                    <p>Price: $${product.price}</p>
                    <button onclick="selectProduct(${product.id})">Select Product</button>
                `;
                productList.appendChild(productDiv);
            });
        })
        .catch(error => {
            console.error("Error fetching products:", error);
        });
});

// Function to fetch the selected product by ID
function selectProduct(productId) {
    fetch(`/select_product/${productId}`)
        .then(response => response.json())
        .then(product => {
            const productDetails = document.getElementById("product-details");
            if (product.error) {
                productDetails.textContent = product.error;
            } else {
                productDetails.innerHTML = `
                    <strong>Name:</strong> ${product.name}<br>
                    <strong>Description:</strong> ${product.description}<br>
                    <strong>Price:</strong> $${product.price}
                `;
            }
        })
        .catch(error => {
            console.error("Error fetching product:", error);
        });
}
