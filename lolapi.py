from riotwatcher import LolWatcher, ApiError
import pandas as pd
import os
from dotenv import load_dotenv

# global variables

# api = os.getenv('API_KEY')
# print(api)
api = "RGAPI-d396351a-0a22-4d9d-908c-1fac160df058"
watcher = LolWatcher(api)
my_region = 'sg2'

#Define my profile
me = watcher.summoner.by_name(my_region, 'Suvo')
# print(me)

#Get ranked stats
my_ranked_stats = watcher.league.by_summoner(my_region, me['id'])
print(my_ranked_stats)

#Get latest version
latest = watcher.data_dragon.versions_for_region(my_region)['n']['champion']

static_champ_list = watcher.data_dragon.champions(latest, False, 'en_US')

# champ static list data to dict for looking up
champ_list = []
champ_dict = {}

# print(type(static_champ_list['data']))

for key in static_champ_list['data'].keys():
    champ_list.append(key)

for key in static_champ_list['data'].keys():
    if key in champ_list:
        champ_dict[static_champ_list['data'][key]['key']] = key

# print(champ_dict)