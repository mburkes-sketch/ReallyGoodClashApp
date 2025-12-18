from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..forms import PlayerLookupForm
from .. import client

clashers = Blueprint("clashers", __name__)

@clashers.route("/", methods=["GET", "POST"])
def index():
    return render_template("home.html")

@clashers.route("/search", methods=["GET", "POST"])
def player_search():
    form = PlayerLookupForm()
    stats = None
    error = None

    if form.validate_on_submit():
        stats = client.search_by_player_id(form.player_tag.data[1:])
        
        if stats is None:
            flash(f"Player with tag {form.player_tag.data} not found.")
            
    return render_template("playerSearch.html", form=form, stats=stats, error=error)