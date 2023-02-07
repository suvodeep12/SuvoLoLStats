from riotwatcher import LolWatcher, ApiError
import pandas as pd

# global variables
api_key = 'RGAPI-d396351a-0a22-4d9d-908c-1fac160df058'
watcher = LolWatcher(api_key)
my_region = 'sg2'

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
champ_dict = {}

print(static_champ_list['data'])

# for key in static_champ_list['data']:
#     row = static_champ_list['data'][key]
#     champ_dict[row['key']] = row['id']