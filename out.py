from flask import Flask

app = Flask(__name__)

products = [
    {
        "id": 1,
        "name": "Samsung Galaxy",
        "price": "₹15,999",
        "image": "mobile.jpg",
        "image2": "eren.jpg",
        "code": "SM001",
        "color": "red",
        "app":"1",
    },
    {
        "id": 2,
        "name": "Laptop",
        "price": "₹45,000",
        "image": "laptop.jpg",
        "code": "LP001",
        "color": "Black",
        "app":"2",
         "image2": "jiren.jpg",
    },
    {
        "id": 3,
        "name": "Smart Watch",
        "price": "₹2,999",
        "image": "watch.jpg",
        "code": "SW001",
        "color": "Black",
         "app":"3",
    },
    {
        "id": 4,
        "name": "Headphone",
        "price": "₹1,499",
        "image": "headphone.jpg",
        "code": "HP001",
       "color": "Black",
        "app":"4",
    },
    {
        "id": 5,
        "name": "Tablet",
        "price": "₹20,000",
        "image": "jiren.jpg",
        "code": "TB001",
        "color": "Black",
         "app":"5",
    },
    {
        "id": 6,
        "name": "eren doll",
        "price": "₹20,00",
        "image": "image.png",
        "code": "BT001",
        "color": "Black",
        "app":"6",
    },

]

@app.route("/")
def home():

    html = "<h1>Products</h1>"

    for p in products:
        html += f"""
        <div style="border:1px solid black; width:220px; padding:10px; margin:10px; display:inline-block;">
            <a href="/product/{p['id']}">
                <img src="/static/{p['image']}" width="200">
                <h3>{p['name']}</h3>
                
            </a>
            <p>{p['price']}</p>
         
        </div>
        """

    return html


@app.route("/product/<int:id>")
def product(id):

    for p in products:
        if p["id"] == id:
            return f"""
            <h1>{p['name']}</h1>

            <img src="/static/{p['image2']}" width="300">
            <h2>Price: {p['price']}</h2>
            <h3>Product Code: {p['code']}</h3>
          <h3>Color: {p['color']}</h3>
          <h4>app: {p['app']}</h4>

            <p>Product Details Here</p>
            """

    return "Product Not Found"


if __name__ == "__main__":
    app.run(debug=True)