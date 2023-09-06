from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash

from cendak.deta import cendak_links
from cendak.utils import generate_id

routes_main = Blueprint("routes_main", __name__)

@routes_main.get("/")
def home():
    return render_template("home.html")

@routes_main.post("/add")
def add():
    link = request.form.get("shortLink", None)
    if not link:
        return redirect(url_for("routes_main.home"))

    id = generate_id()
    add = cendak_links.put({
        "value": link,
    }, id)

    flash("Sukses! ID: " + id, "success")
    return redirect(url_for("routes_main.home"))
