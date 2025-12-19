# ReallyGoodClashApp

## Project Write Up CMSC388J

### Q1 Description of your final project idea:

Clash Royale app that lets users associate their account with their in-game account, see their player stats, look at decks others have built, build their own decks, and simulate decks against each other.

ML:
Simulate decks against each other, by having a model learn about card interactions from patterns in data (almost 37 million matches of 1v1 decks)

Non-ML:
Lets users log in
Associate their account with their in game account

### Q2 Describe what functionality will only be available to logged-in users:
Having access to their player stats
Deck simulations

Logged-in users will have access to a more detailed account of their player stats. They’ll also be able to make decks, store them, and simulate battles with them.

### Q3: List and describe at least 4 forms:

Login form:
Lets users log in to their account

Register form:
Lets users create an account associated with a real player account for the game

Player lookup form:
Allows users to search a player by in game id and get their player stats

Make a deck form:
Allows users to make a deck from the 100ish cards in the game. The deck will be saved as a part of their user profile.

### Q4 List and describe your routes/blueprints (don’t need to list all routes/blueprints you may 

User blueprint contains all routes that are related to user functionality. Users can login, register, build decks, and simulate decks against each other. Only users can do these actions.
@user.login - route to log users in
@user.register - route to let users register
@user.deck_builder - route to deck building page that lets users build a deck and save it in their profile
@user.deck_simulator - route to the deck simulation page that allows users to choose two decks and simulate a battle between them.

Cr blueprint for general functionality that isn’t associated with an account. 
@cr.player_search - search for a specific player based on their id
@cr.top_decks - see the top decks that are in use

### Q5: Describe what will be stored/retrieved from MongoDB:
User information:
MongoDB will store User objects that contain usernames, passwords, and decks built by the user.

Decks:
Mongo will store decks published by different users for others to see. Decks are a set of 8 cards along with a name for the deck and a description of how to use it.

### Q6 Describe what Python package or API you will use and how it will affect the user experience:

We are going to use the Clash Royale Developer API. This API will provide the info needed based on what the user searches for. We will also need Pandas, Numpy, and Sklearn; however, these do not directly impact user experience, and are rather libraries needed for the backend functionality of the website.

The Clash Royale Developer API only works for a small set of whitelisted IP addresses. To get around this, we ran a virtual machine on the Google Cloud Platform with a static IP address. Using flask, we made 2 different routes on the proxy server that called the clash royale developer API querying for players and cards. We then made all of our API calls to the clash roayle developer API by calling the routes in the server app. 
