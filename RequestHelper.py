import requests

SCHEMA = "https://open-api.bser.io/"
VERSION = "v1"


def send_get_request(url, headers={}, params={}):
    r = requests.get(url = SCHEMA + url, headers = headers, params = params)
    data = r.json()
    return data


def url_get_game(gameId):
    return f"{VERSION}/games/{gameId}"

def url_get_user_games(userNum, next=None):
    return f"{VERSION}/user/games/{userNum}?next={next}" if next != None else f"{VERSION}/user/games/{userNum}"

def url_get_user_nickname(nickname):
    return f"{VERSION}/user/nickname?query={nickname}"
