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
# print(match_detail['info']['participants'])
for row in match_detail['info']['participants']:
    participants_row = {}
    participants_row['champion'] = row['championId']
    participants_row['summonerspell1'] = row['summoner1Id']
    participants_row['summonerspell2'] = row['summoner2Id']
    participants_row['win'] = row['win']
    participants_row['kills'] = row['kills']
    participants_row['deaths'] = row['deaths']
    participants_row['assists'] = row['assists']
    participants_row['totalDamageDealt'] = row['totalDamageDealt']
    participants_row['goldEarned'] = row['goldEarned']
    participants_row['champLevel'] = row['champLevel']
    participants_row['totalMinionsKilled'] = row['totalMinionsKilled']
    participants_row['item0'] = row['item0']
    participants_row['item1'] = row['item1']
    participants.append(participants_row)

# print(participants)

df = pd.DataFrame(participants)
print(df)