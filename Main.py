# Purpose of this is to map out ranked MMR histogram in a line
from Api import *

import matplotlib.pyplot as plt
import numpy as np
from enum import Enum

class Season(Enum):
    Normal = 0
    SeasonOne = 1
    PreSeasonTwo = 2
    SeasonTwo = 3


cached_game_data = 'Rhiknow_games_data.pkl'

def fetch_games(pages, overwrite_cache = False):
    games = []
    if overwrite_cache:
        games = get_games("Rhiknow", pages)
        pickle_items(cached_game_data, games)
    else:
        games = unpickle_items(cached_game_data)

    games.reverse()
    return games


total_games = fetch_games(40, True)
ranked_filter = filter(lambda game: game.seasonId == Season.SeasonTwo.value, total_games)
ranked_mmrs = list(map(lambda game: game.mmrBefore, ranked_filter))

ypoints = np.array(ranked_mmrs)

plt.plot(ypoints)
plt.show()
