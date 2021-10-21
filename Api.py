import RequestHelper
from Game import *

import time
import pickle

import os
from dotenv import load_dotenv

load_dotenv()

headers = {"x-api-key": os.getenv('API_KEY')}

# Gets games for given player name
# Each page has 10 games
def get_games(player, pages = 1):
    userNum = get_user_nickname(player)
    return get_user_games(userNum, pages)


def get_user_games(userNum, pages):
    games = []

    i = pages
    next = None
    while (i > 0):
        url = RequestHelper.url_get_user_games(userNum, next)
        data = RequestHelper.send_get_request(url, headers)
        print(f"Processing games next: {next}...")
        for game in data['userGames']:
            instance = Game(game)
            games.append(instance)

        if 'next' in data:
            next = data['next']
        else:
            break
        i -= 1
        time.sleep(1)

    return games


# Returns userNum
def get_user_nickname(nickname):
    url = RequestHelper.url_get_user_nickname(nickname)
    data = RequestHelper.send_get_request(url, headers)
    return data['user']['userNum']


def pickle_items(filename, items):
    with open(filename, 'wb') as output:
        pickle.dump(items, output, -1)

def unpickle_items(filename):
    unpickled = None
    with open(filename, "rb") as input:
        unpickled = pickle.load(input)
    return unpickled
