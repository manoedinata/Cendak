from flask import Blueprint
from flask import redirect
from flask import url_for
from flask import flash

from cendak.deta import cendak_links

routes_redirect = Blueprint("routes_redirect", __name__)

@routes_redirect.route("/<id>")
def redirect_id(id):
    link = cendak_links.get(id)
    if not link:
        flash("Error: ID tidak ditemukan", "danger")
        return redirect(url_for("routes_main.home"))

    target = link["value"]
    return redirect(target)
