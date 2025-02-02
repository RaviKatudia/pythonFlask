from flask import Flask,render_template

ravi=Flask(__name__)

@ravi.route("/")
def home():
    return render_template("index.html")

@ravi.route("/404")
def errorr():
    return render_template("404.html")

@ravi.route("/cart")
def cart():
    return render_template("cart.html")

@ravi.route("/checkout")
def checkout():
    return render_template("checkout.html")

@ravi.route("/contact")
def con():
    return render_template("contact.html")

@ravi.route("/shop")
def shop():
    return render_template("shop.html")

@ravi.route("/shop-detail")
def shopdetails():
    return render_template("shop-detail.html")


ravi.run(debug=True)




