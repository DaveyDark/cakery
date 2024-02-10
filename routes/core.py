from flask import Blueprint, redirect, session, url_for, render_template, request
from flask_sqlalchemy import SQLAlchemy, query
from geopy import distance
from geopy.distance import geodesic
from geopy.geocoders import Nominatim
from decimal import Decimal
import random
from models import Buyer, Seller, db

from sqlalchemy.util import NoneType

core = Blueprint("core", __name__)


@core.get("/")
def root():
    return render_template("index.html")


@core.route("/register", methods=["GET", "POST"])
# register page route
def register():
    if request.method == "POST":
        form = request.form["form_id"]
        if form == "buyer":
            email = request.form["email"]
            name = request.form["name"]
            password = request.form["password"]
            state = request.form["state"]
            city = request.form["city"]
            geolocator = Nominatim(user_agent="geoapi")
            latitude = 0
            longitude = 0
            if request.form["latitude"] == "" or request.form["longitude"] == "":
                loc = geolocator.geocode(city + ", " + state + ", India")
                latitude = loc.latitude
                longitude = loc.longitude
            else:
                latitude = request.form["latitude"].split("°")[0]
                longitude = request.form["longitude"].split("°")[0]
            phone = request.form["phone"]
            if Seller.query.filter_by(email=email).first():
                # email already used
                return render_template("register.html")
            if latitude == "" or longitude == "":
                # location not entered
                return render_template("register.html")
            if (
                email == ""
                or name == ""
                or password == ""
                or state == ""
                or city == ""
                or phone == ""
            ):
                # details not entered
                return render_template("register.html")
            byr = Buyer(email, name, password, latitude, longitude, state, city, phone)
            db.session.add(byr)
            db.session.commit()
            return redirect(url_for("root"))
        else:
            # seller form
            email = request.form["email"]
            name = request.form["name"]
            password = request.form["password"]
            shop_state = request.form["state"]
            shop_city = request.form["city"]
            geolocator = Nominatim(user_agent="geoapi")
            latitude = 0
            longitude = 0
            if request.form["latitude"] == "" or request.form["longitude"] == "":
                loc = geolocator.geocode(shop_city + ", " + shop_state + ", India")
                latitude = loc.latitude
                longitude = loc.longitude
            else:
                latitude = request.form["latitude"].split("°")[0]
                longitude = request.form["longitude"].split("°")[0]
            shop_name = request.form["shopName"]
            shop_category = request.form["category"]
            phone = request.form["phone"]
            if Buyer.query.filter_by(email=email).first():
                # email already used
                return render_template("register.html")
            if latitude == "" or longitude == "":
                # location not entered
                return render_template("register.html")
            if (
                email == ""
                or name == ""
                or password == ""
                or shop_name == ""
                or shop_state == ""
                or shop_city == ""
                or phone == ""
            ):
                # details not entered
                return render_template("register.html")
            sllr = Seller(
                email,
                name,
                password,
                latitude,
                longitude,
                shop_state,
                shop_city,
                shop_name,
                phone,
                shop_category,
            )
            db.session.add(sllr)
            db.session.commit()
            return redirect(url_for("root"))
    return render_template("register.html")


@core.get("/design")
def design():
    return render_template("design.html")
