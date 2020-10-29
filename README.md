### What's Included:
This repository holds the Python client for interacting with an API that allows one to play Pig, a dice game.  The application itself is deployed on AWS.

### Roles of the Game:
In Pig, players seek to earn more than 100 points in their primary score.  They earn points by rolling 2 die, adding points to their staged score, until they choose to HOLD, or refrain from rolling, at which time their staged points are added to the primary score.  The 4 possible outcomes and their effects are:
- Two 1's: Primary score goes to 0, staged score goes to 0, it's the next players turn (herein referred to as `ALL_1`)
- One 1, One other number: Staged score goes to 0, it's the next players turn (`ONE_1`)
- Two non-matching numbers: Sum of rolled die is added to staged score (`ALL_MISMATCHED_NON_1`)
- Two matching numbers: Sum of rolled die is added to staged score, player must roll again (`ALL_MATCHING_NON_1`)

At some points a player may choose to HOLD, instead of rolling.  Complete details of the game can be found elsewhere.


### The API:
There are 3 endpoints used in this app:
- `POST /games`:  Allows one to create a game
- `GET /games/{gameId}`:  Allows one to get the state of a game
- `POST /games/{gameId}/turns`: Allows own to choose a `Turn`, which modifies the game state by advancing the game.

All 3 endpoints, when responding with HTTP 200, return a `Game`.  `Game` describes the state of a current game and has self explanatory fields.  Users are encouraged to explore the API using `curl`, though they should be sure to include the `content-type: application/json` header.

At the moment, users can conduct a `Turn` that allow one of two `Actions`: `ROLL` or `HOLD`.

The result of a `ROLL` `Turn` can take on one of the four `Result` which are listed in the above section.

The current `Game`'s state is found under `state` and is either `AWAITING_TURN` or `FINISHED`.


### Using the Client:
1.  First, `export PIG_API_ENDPOINT='https://fdw9nciwsd.execute-api.us-east-1.amazonaws.com/dev'`.
2.  Then, `python interactive_client.py`.  The interactive client will display game state and allow you the choose which turn to conduct.  View the `allowedNextTurns` field of the `Game` object and supply a Turn Choice Identifier to the client.  Turn Choice Indetifiers are keys within the `allowedNextTurns` field.  
    -   Note: The first API may take several seconds.  Subsequent calls won't have this problem.
