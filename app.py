from flask import Flask, render_template, redirect, request, session, jsonify
import os
from flask_session import Session
from controller import *
from model.entity import CallPrice
from model.entity.loadproduct import load

app = Flask(__name__, template_folder="view", static_folder="view/assets")
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/")
def home():
    return render_template("login.html")


@app.route("/required_product", methods=["POST", "GET"])
def required():
    if not (session.get('id') and session.get('type')):
        return render_template("login.html")
    if request.method == "GET":
        load()
        return render_template("required_product.html",
                               products=RequiredProductController.find_by_client_id(session.get('id')))
    if request.method == "POST":
        RequiredProductController.status(request.form.get('item_id'))
    return render_template("required_product.html",
                           products=RequiredProductController.find_by_client_id(session.get('id')))


@app.route("/callprice_for_client", methods=["POST", "GET"])
def callprice_client():
    if not (session.get('id') and session.get('type')):
        return render_template("login.html")
    if request.method == "POST":
        CallPriceController.edit_status(request.form.get('item_id'))
    return render_template("callprice_for_client.html",
                           products=CallPriceController.find_callprice_for_client(session.get('id')))


@app.route("/product_for_supplier", methods=["POST", "GET"])
def product_for_supplier():
    if not (session.get('id') and session.get('type')):
        return render_template("login.html")

    if request.method == "GET":
        session['item_id'] = RequiredProductController.find_by_id(request.args.get('item_id'))
        return render_template("product_for_supplier.html",
                               products=RequiredProductController.find_for_supplier(session.get('id')),
                               data=session.get('item_id'))

    if request.method == "POST":
        if session.get('item_id'):
            u_price = request.form.get("u_price")
            t_price = request.form.get("t_price")
            description = request.form.get("description")
            supplier_id = session.get('id')
            requiredproduct_id = session.get('item_id').id
            CallPriceController.save_supplier(requiredproduct_id, u_price, t_price, supplier_id, description)
            session['item_id'] = None
            return render_template("product_for_supplier.html",
                                   products=RequiredProductController.find_for_supplier(session.get('id')),
                                   data=session.get('item_id'))

    return render_template("product_for_supplier.html",
                           products=RequiredProductController.find_for_supplier(session.get('id')),
                           data=session.get('item_id'))


@app.route("/order_for_supplier", methods=["POST", "GET"])
def order_supplier():
    if not (session.get('id') and session.get('type')):
        return render_template("login.html")
    if request.method == "GET":
        session['item_id'] = CallPriceController.find_by_id(request.args.get('item_id'))
        return render_template("order_for_supplier.html",
                               products=CallPriceController.find_by_supplier_id(session.get('id')),
                               data=session.get('item_id'))

    if request.method == "POST":
        if session.get('item_id'):
            u_price = request.form.get("u_price")
            t_price = request.form.get("t_price")
            description = request.form.get("description")
            requiredproduct_id = session.get('item_id').requiredproduct_id
            supplier_id = session.get('id')
            id = session.get('item_id').id
            CallPriceController.edit(id, requiredproduct_id, u_price, t_price, description, supplier_id)
            session['item_id'] = None
            return render_template("order_for_supplier.html",
                                   products=CallPriceController.find_by_supplier_id(session.get('id')),
                                   data=session.get('item_id'))

    return render_template("order_for_supplier.html",
                           products=CallPriceController.find_by_supplier_id(session.get('id')),
                           data=session.get('item_id'))


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        key = request.form.get("option")
        match key:
            case 'supplier':
                data = SupplierController.login(username, password)
                session['id'] = data.id
                session['type'] = 'supplier'
                return render_template("profile_supplier.html", profile=data)
            case 'producer':
                data = ProducerController.login(username, password)
                session['id'] = data.id
                session['type'] = 'producer'
                return render_template("profile_producer.html", profile=data)
            case 'client':
                data = ClientController.login(username, password)
                session['id'] = data.id
                session['type'] = 'client'
                return render_template('profile_client.html', profile=data)


@app.route("/product_for_producer", methods=["POST", "GET"])
def product_for_producer():
    if not (session.get('id') and session.get('type')):
        return render_template("login.html")

    if request.method == "GET":
        session['item_id'] = RequiredProductController.find_by_id(request.args.get('item_id'))
        return render_template("product_for_producer.html",
                               products=RequiredProductController.find_for_producer(session.get('id')),
                               data=session.get('item_id'))

    if request.method == "POST":
        if session.get('item_id'):
            u_price = request.form.get("u_price")
            t_price = request.form.get("t_price")
            description = request.form.get("description")
            producer_id = session.get('id')
            requiredproduct_id = session.get('item_id').id
            CallPriceController.save_producer(requiredproduct_id, u_price, t_price, producer_id, description)
            print(CallPriceController.save_producer(requiredproduct_id, u_price, t_price, producer_id, description))
            session['item_id'] = None
            return render_template("product_for_producer.html",
                                   products=RequiredProductController.find_for_producer(session.get('id')),
                                   data=session.get('item_id'))
    # todo have bug
    return render_template("product_for_producer.html",
                           products=RequiredProductController.find_for_producer(session.get('id')),
                           data=session.get('item_id'))


@app.route("/order_for_producer", methods=["POST", "GET"])
def order_producer():
    if not (session.get('id') and session.get('type')):
        return render_template("login.html")
    if request.method == "GET":
        session['item_id'] = CallPriceController.find_by_id(request.args.get('item_id'))
        return render_template("order_for_producer.html",
                               products=CallPriceController.find_by_producer_id(session.get('id')),
                               data=session.get('item_id'))

    if request.method == "POST":
        if session.get('item_id'):
            u_price = request.form.get("u_price")
            t_price = request.form.get("t_price")
            description = request.form.get("description")
            requiredproduct_id = session.get('item_id').requiredproduct_id
            producer_id = session.get('id')
            id = session.get('item_id').id
            CallPriceController.edit_for_roducer(id, requiredproduct_id, u_price, t_price, description, producer_id)
            session['item_id'] = None
            return render_template("order_for_producer.html",
                                   products=CallPriceController.find_by_producer_id(session.get('id')),
                                   data=session.get('item_id'))

    return render_template("order_for_producer.html",
                           products=CallPriceController.find_by_producer_id(session.get('id')),
                           data=session.get('item_id'))


@app.route("/profile", methods=["POST", "GET", "DELETE"])
def profile():
    if not (session.get('id') and session.get('type')):
        return render_template("login.html")
    key = session.get('type')
    match key:
        case 'supplier':
            if request.method == "POST":
                name = request.form.get("name")
                family = request.form.get("family")
                phonenumber = request.form.get("phonenumber")
                email = request.form.get("email")
                address = request.form.get("address")
                username = request.form.get("username")
                password = request.form.get("password")
                data = SupplierController.edit(session.get("id"), name, family, phonenumber, email, address, username,
                                               password)
                return render_template("profile_supplier.html", profile=data)
            return render_template("profile_supplier.html", profile=SupplierController.find_by_id(session.get("id")))
        case 'producer':
            if request.method == "POST":
                name = request.form.get("name")
                family = request.form.get("family")
                phonenumber = request.form.get("phonenumber")
                email = request.form.get("email")
                address = request.form.get("address")
                username = request.form.get("username")
                password = request.form.get("password")
                data = ProducerController.edit(session.get("id"), name, family, phonenumber, email, address, username,
                                               password)
                return render_template("profile_producer.html", profile=data)
            return render_template("profile_producer.html", profile=ProducerController.find_by_id(session.get("id")))
        case 'client':
            if request.method == "POST":
                name = request.form.get("name")
                family = request.form.get("family")
                phonenumber = request.form.get("phonenumber")
                email = request.form.get("email")
                address = request.form.get("address")
                username = request.form.get("username")
                password = request.form.get("password")
                data = ClientController.edit(session.get("id"), name, family, phonenumber, email, address, username,
                                             password)
                return render_template("profile_client.html", profile=data)
            return render_template("profile_client.html", profile=ClientController.find_by_id(session.get("id")))


@app.route("/project", methods=["POST", "GET", "DELETE"])
def project():
    pass


@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        # if request.form.get("password") == request.form.get("repeat_password"):
        name = request.form.get("name")
        family = request.form.get("family")
        phonenumber = request.form.get("phonenumber")
        email = request.form.get("email")
        address = request.form.get("address")
        username = request.form.get("username")
        password = request.form.get("password")
        key = request.form.get("option")
        match key:
            case 'supplier':
                SupplierController.save(name, family, phonenumber, email, address, username, password)
            case 'producer':
                ProducerController.save(name, family, phonenumber, email, address, username, password)
            case 'client':
                ClientController.save(name, family, phonenumber, email, address, username, password)
        return render_template("login.html")

    return render_template("register.html")


#
#

# @app.route("/forget")
# def forget():
#     return render_template("forget-password.html")


@app.route("/logout")
def logout():
    session["id"] = None
    session['type'] = None
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
