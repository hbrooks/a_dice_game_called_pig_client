### Pig
This repository holds the Python client for interacting with an API that allows one to play Pig, a dice game.  In Pig, players seek to earn more than 100 points in their primary score.  They earn points by rolling 2 die, adding points to their staged score, until they choose to HOLD, or refrain from rolling, at which time their staged points are added to the primary score.  The 4 possible outcomes and their effects are:
- Two 1's: Primary score goes to 0, staged score goes to 0, it's the next players turn
- One 1, One other number: Staged score goes to 0, it's the next players turn
- Two non-matching numbers: Sum of rolled die is added to staged score
- Two matching numbers: Sum of rolled die is added to staged score, player must roll again

At some points a player may choose to HOLD, instead of rolling.  


### The API:
There are 3 endpoints used in this app:
- `POST /games`:  Allows one to create a game
- `GET /games/{gameId}`:  Allows one to get the state of a game
- `POST /games/{gameId}/turns`: Allows own to choose a Turn, which modifies the game state.


### Using the Client:
1.  First, `$ export PIG_API_ENDPOINT='https://fdw9nciwsd.execute-api.us-east-1.amazonaws.com/dev'`
2.  Then, `$ python interactive_client.py`.  The interactive client will display game state and allow you the choose which turn to conduct.

