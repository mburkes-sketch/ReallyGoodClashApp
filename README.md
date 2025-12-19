# ReallyGoodClashApp

## Deployment Link
[https://really-good-clash-app.vercel.app/ ](https://really-good-clash-app.vercel.app/)

## Project Write Up CMSC388J

### Q1 Description of your final project idea:

Clash Royale app that lets users associate their account with their in-game account, see their player stats, look at decks others have built, build their own decks, and simulate decks against each other.

ML:
Simulate decks against each other, by having a model learn winners/losers from patterns in data (dataset contained almost 37 million matches of 1v1 decks, of which we used 1.1 million matches to train model due to time and RAM constraints)
*Citation: Bwando Wando. (2024). Clash Royale S18 Ladder Datasets (37.9M matches) [Data set]. Kaggle. https://doi.org/10.34740/KAGGLE/DSV/10035519*
**NOTE:** In the process of trying to better the model’s accuracy, we discovered a lot of real research that has been done in predicting winners/losers based on various factors. When predicting such skill-based games (i.e. Hearthstone, League of Legends, Clash Royale, etc.) based on previous matches, we saw that for many people (who did it for fun or for real research), their models’ accuracy was usually in the 55-60% range. This apparently is the best, with some models reaching 75% accuracy given that they had more context and factors to consider in deciding winners/losers. Our model’s accuracy is at 58.14%, so we thought that was sufficient enough given our data and constraints.
*Articles:*
1. https://medium.com/@jdleo/i-trained-ai-on-70-200-clash-royale-battles-to-settle-the-ultimate-debate-does-your-deck-actually-2e10fc27eff6
2. Hearthstone: https://slothlab.info/assets/pdf/eger2020fdg.pdf
3. https://ieeexplore.ieee.org/document/8860062


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

### Q4 List and describe your routes/blueprints (don’t need to list all routes/blueprints you may have–just enough for the requirement): 

User blueprint contains all routes that are related to user functionality. Users can login, register, build decks, and simulate decks against each other. Only users can do these actions.
@user.login - route to log users in
@user.register - route to let users register
@user.account - route to the user dashboard that displays CR stats and saved decks
@user.deck_builder - route to deck building page that lets users build a deck and save it in their profile
@user.deck_simulator - route to the deck simulation page that allows users to choose two decks and simulate a battle between them.

Cr blueprint for general functionality that isn’t associated with an account. 
@cr.player_search - search for a specific player based on their id

### Q5: Describe what will be stored/retrieved from MongoDB:
User information:
MongoDB will store User objects that contain usernames, passwords, and decks built by the user.

Decks:
Mongo will store decks published by different users for others to see. Decks are a set of 8 cards along with a name for the deck and a description of how to use it.

### Q6 Describe what Python package or API you will use and how it will affect the user experience:

We are going to use the Clash Royale Developer API. This API will provide the info needed based on what the user searches for. We will also need Pandas, Numpy, and Sklearn; however, these do not directly impact user experience, and are rather libraries needed for the backend functionality of the website.

The Clash Royale Developer API only works for a small set of whitelisted IP addresses. To get around this, we ran a virtual machine on the Google Cloud Platform with a static IP address. Using flask, we made 2 different routes on the proxy server that called the clash royale developer API querying for players and cards. We then made all of our API calls to the Clash Royale developer API by calling the routes in the server app. 
