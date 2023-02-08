from riotwatcher import LolWatcher, ApiError
import pandas as pd
import os
from dotenv import load_dotenv

# global variables

api = os.getenv('API_KEY')
print(api)
watcher = LolWatcher(api)
my_region = 'sg2'
if my_region == 'sg2':
    my_area = 'sea'

#Define my profile
me = watcher.summoner.by_name(my_region, 'Suvo')
# print(me)

#Get ranked stats
my_ranked_stats = watcher.league.by_summoner(my_region, me['id'])
# print(my_ranked_stats)

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

my_matches = watcher.match.matchlist_by_puuid(my_area, me['puuid'])

# fetch last match detail
last_match = my_matches[0]

match_detail = watcher.match.by_id(my_area, last_match)

participants = []
print(match_detail['metadata']['participants'])
for row in match_detail['metadata']['participants']:
    participants_row = {}