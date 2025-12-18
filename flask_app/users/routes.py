from flask import Blueprint, render_template, url_for, redirect, request, flash, current_app
from flask_login import login_user, current_user, logout_user, login_required
from .. import bcrypt, client 
from ..forms import RegistrationForm, LoginForm, MakeADeck
from ..models import User, Deck
import pickle
import numpy as np
import os

users = Blueprint("users", __name__)

def get_model_path():
    root = current_app.root_path
    path = os.path.join(root, 'ml_models', 'clash_model.pkl')
    return path

def encode_single_deck(card_list, card_map, total_features):
    # Creates a list of zeros
    vec = np.zeros(total_features, dtype=int)
    
    # Loop through the user's card IDs
    for card_id in card_list:
        clean_id = str(card_id)
        
        # If this ID exists in our model's vocabulary, set that index to 1
        if clean_id in card_map:
            idx = card_map[clean_id]
            vec[idx] = 1
            
    return vec

@users.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("clashers.index"))

    form = RegistrationForm()
    if form.validate_on_submit():
        hashed = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        
        # Create user
        user = User(
            username=form.username.data, 
            email=form.email.data, 
            password=hashed,
            player_tag=form.player_tag.data
        )
        user.save()
        return redirect(url_for("users.login"))

    return render_template("register.html", form=form)

@users.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("clashers.index"))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.objects(username=form.username.data).first()
        
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for("users.account"))
        else:
            flash("Login Unsuccessful. Please check username and password")

    return render_template("login.html", form=form)

@users.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("clashers.index"))

@users.route("/account")
@login_required
def account():
    # Fetch user's saved decks
    user_decks = Deck.objects(author=current_user)
    
    # ************EITHER ISSUE HERE OR IN CLIENT.PY*************
    # Fetch user's live data from API
    player_stats = client.search_by_player_id(current_user.player_tag)
    
    # Error Handling: If API failed, tell the user
    if player_stats is None:
        flash("Could not load player stats. Is the Player Tag correct?")

    # Create a Map of Card ID -> Image URL
    all_cards = client.get_all_cards()
    card_img_map = {}
    
    if all_cards:
        for card in all_cards:
            c_id = str(card['id'])
            if 'iconUrls' in card:
                if 'medium' in card['iconUrls']:
                    card_img_map[c_id] = card['iconUrls']['medium']

    return render_template(
        "playerAccount.html", 
        stats=player_stats, 
        decks=user_decks, 
        card_map=card_img_map
    )

@users.route("/deck/build", methods=["GET", "POST"])
@login_required
def deck_builder():
    form = MakeADeck()
    all_cards = client.get_all_cards()

    if form.validate_on_submit():
        selected_cards = request.form.getlist("selected_cards")
        
        if len(selected_cards) != 8:
            flash("A deck must contain exactly 8 cards!")
        else:
            deck = Deck(
                author=current_user,
                title=form.title.data,
                description=form.description.data,
                cards=selected_cards
            )
            deck.save()
            flash("Deck Saved Successfully!")
            return redirect(url_for("users.account"))

    return render_template("deckBuilder.html", form=form, all_cards=all_cards)

@users.route("/deck/simulate", methods=["GET", "POST"])
@login_required
def deck_simulator():
    my_decks = Deck.objects(author=current_user)
    simulation_result = None
    
    if request.method == "POST":
        deck1_id = request.form.get("deck1")
        deck2_id = request.form.get("deck2")
        
        # Get Decks from Database
        deck1 = Deck.objects(id=deck1_id).first()
        deck2 = Deck.objects(id=deck2_id).first()
        
        if deck1 and deck2:
            model_path = get_model_path()
            file = open(model_path, 'rb')
            artifacts = pickle.load(file)
            file.close()
            
            # Extract data
            model = artifacts["model"]
            card_map = artifacts["card_map"]
            total_cards = len(artifacts["all_cards_list"])
            
            # Convert Deck 1 to Numbers
            d1_vec = encode_single_deck(deck1.cards, card_map, total_cards)
            
            # Convert Deck 2 to Numbers
            d2_vec = encode_single_deck(deck2.cards, card_map, total_cards)
            
            # Combine them
            input_vector = np.hstack([d1_vec, d2_vec]).reshape(1, -1)
            
            # Predict
            probability = model.predict_proba(input_vector)[0][1]
            
            if probability > 0.5:
                winner = deck1.title
                confidence = round(probability * 100, 1)
            else:
                winner = deck2.title
                confidence = round((1 - probability) * 100, 1)
                
            simulation_result = "Prediction: " + winner + " wins! (Confidence: " + str(confidence) + "%)"

    return render_template("deckSimulator.html", decks=my_decks, result=simulation_result)