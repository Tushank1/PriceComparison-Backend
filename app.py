from flask import Flask, jsonify , request
from flask_cors import CORS
from allproducts import allProducts
from productData import ProductData
from homeInterior import Interior
from gardernPatio import Patio
from kidsFamily import Family
from computing import Computing
from toysHobbie import Hobbie
from gamingEntertainment import Entertainment
from phoneWearables import Phone
from soundvision import Sound
from photography import Photography
from clothing import Clothing
from healthBeauty import Health
from sportsOutdoor import Outdoor
from doItYour import Yourself
from transport import Transport
from flask_sqlalchemy import SQLAlchemy
# from flask_jwt_extended import JWTManager, create_access_token, jwt_required
# from flask_bcrypt import Bcrypt
# import datetime
import psycopg2
import os

app = Flask(__name__)
CORS(app)
db = SQLAlchemy()

Allproducts = allProducts()
homeInteriorData = Interior()
gardernPatio = Patio()
kidsfamily = Family()
Computer = Computing()
toysHobbie = Hobbie()
gaming = Entertainment()
Wearables = Phone()
soundVision = Sound()
Photo = Photography()
cloth = Clothing()
HealthBeauty = Health()
SportsOutDoor = Outdoor()
DOITYOUSELF = Yourself()
motortransport = Transport()

database_uri = os.getenv("DATABASE_URL", "postgresql://surge:surge%123@localhost:5433/postgres")
app.config["SQLALCHEMY_DATABASE_URI"] = database_uri
app.config['JWT_SECRET_KEY'] = "PriceCompare backend"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
# bcrypt = Bcrypt(app)
# jwt = JWTManager(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(250), nullable=False)
    category = db.Column(db.String(250))
    price = db.Column(db.String(250))
    description = db.Column(db.Text)
    
    def __repr__(self) -> str:
        return f"<Product {self.name}"

# class Authentication(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(100), nullable=False)
#     email = db.Column(db.String(200),unique=True, nullable = False)
#     password = db.Column(db.String(60), nullable=False)
    
#     def __repr__(self) -> str:
#         return f"{self.username}"

#     def hash_password(self, password):
#         self.password = bcrypt.generate_password_hash(password).decode("utf-8")

#     def check_password_hash(hash,password):
#         return bcrypt.check_password_hash(hash, password)
    

with app.app_context():
    db.create_all()
    
def insert_all_products():
    for product in allProducts:
        db.session.add(Product(
            id=product[id],
            name=product["name"],
            category=product["category"],
            description=product["description"]
        ))
    db.session.commit()
    
insert_all_products()
    
# @app.route("/register" , methods=["POST"])
# def register():
#     data = request.get_json()
#     name = data["username"]
#     email = data["email"]
#     password = data["password"]
#     user = Authentication(username=name, email=email)
#     user.hash_password(password)
#     db.session.add(user)
#     db.session.commit()
#     return jsonify({"message":"Registered Successfully!!! "})


# @app.route("/login", methods=["POST"])
# def login():
#     data = request.get_json()
#     email = data["email"]
#     password = data["password"]
#     user = Authentication.query.filter_by(email=email).first()
#     if not user or not Authentication.check_password_hash(user.password,password):
#         return jsonify({"Message": "Invalid credentials"}), 401
#     access_token = create_access_token(identity=email)
#     return jsonify(access_token=access_token)

# @app.route("/logout", methods=["POST"])
# @jwt_required
# def logout():
#     return jsonify({"message": "Access token has been revoked"})

# fetch('/logout', {
#     method: 'POST',
#     headers: {
#         'Authorization': `Bearer ${localStorage.getItem('access_token')`
#     }).then(response => {
#     if (response.ok) {
#         localStorage.removeItem('access_token'); // Adjust based on where you store the token
#         // Redirect to login or update UI accordingly
#     }
# });

@app.route("/")
def home():
    return "Hello"

@app.route('/api/allproducts', methods=['GET'])
def allproducts():
    return jsonify(Allproducts)

@app.route("/product/<int:product_id>" , methods=["POST"])
def productData(product_id):
    productdata = ProductData(product_id)
    return jsonify(productdata)

@app.route("/home&Interior" , methods=["GET"])
def InteriorData():
    return jsonify(homeInteriorData)

@app.route("/gardern&Patio")
def gardern():
    return jsonify(gardernPatio)

@app.route("/kids&Family")
def Kids():
    return jsonify(kidsfamily)

@app.route("/computing")
def computing():
    return jsonify(Computer)

@app.route("/toys&Hobbie")
def hobbie():
    return jsonify(toysHobbie)

@app.route("/gaming&Entertainment")
def Gaming():
    return jsonify(gaming)

@app.route("/phone&Wearables")
def phone():
    return jsonify(Wearables)

@app.route("/sound&Vision")
def vision():
    return jsonify(soundVision)

@app.route("/photography")
def photo():
    return jsonify(Photo)

@app.route("/clothing&Accessories")
def clothing():
    return jsonify(cloth)

@app.route("/health&Beauty")
def beauty():
    return jsonify(HealthBeauty)

@app.route("/sports&Outdoor")
def Sports():
    return jsonify(SportsOutDoor)

@app.route("/doItYourself")
def yourself():
    return jsonify(DOITYOUSELF)

@app.route("/motorTransport")
def motor():
    return jsonify(motortransport)

if __name__ == "__main__":
    app.run(debug=True)