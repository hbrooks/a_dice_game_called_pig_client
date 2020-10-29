import os
import pprint
import requests


class PigApiInterface:
    def __init__(self, endpoint):
        self.endpoint = endpoint

    def create_game(self, number_of_players=None, number_of_die=None, score_to_win=None):
        request_body = {}
        for field_name, field_value in dict({
            'numberOfPlayers': number_of_players,
            'numberOfDie': number_of_die,
            'scoreToWin': score_to_win}).items():
            if field_value != None:
                request_body[field_name] = field_value
        return requests.post(
            url=f'{self.endpoint}/games',
            json=request_body
        )

    def conduct_turn(self, game_id, turn_id):
        return requests.post(
            url=f'{self.endpoint}/games/{game_id}/turns',
            json={
                "turnIdToConduct": turn_id
            }
        )


class PigInteractiveClient:
    def __init__(self, api):
        self.api = api

    def start(self):
        game_state = self.api.create_game().json()
        game_id = game_state['gameId']
        print('New game started with ID:', game_id)
        self._print_game_state(game_state)
        while game_state['state'] != 'FINISHED':
            turn_id_to_execute = input("which Turn would you like to conduct? ")
            response = self.api.conduct_turn(game_id, turn_id_to_execute)
            if not response.ok:
                print('Error!', response.json())
                continue
            game_state = response.json()
            self._print_game_state(game_state)
        
        print("Game over, winner:", game_state['metadata']['winner'])
        
    def _print_game_state(self, response_body):
        pprint.pprint(response_body)
        print('\n')


pig_api = PigApiInterface(os.environ['PIG_API_ENDPOINT'])
client = PigInteractiveClient(pig_api)
client.start()