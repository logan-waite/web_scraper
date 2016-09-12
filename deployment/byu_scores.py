import urllib.request
import html.parser
import json
import os
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
from datetime import datetime

def get_sports_info(sport):
    # Lists
    dates = []
    opponents = []
    locations = []
    times = []
    final = []

    # Bounds checking
    date_len = 0
    time_len = 0

    # Just get the schedule table
    schedule_table = SoupStrainer('table', id='schedule-table')
    url = "http://byucougars.com/schedule/" + sport # + "/2016"
    print(url)
    # Get page and run it through the parser
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser', parse_only=schedule_table)

    for e in soup.find_all('br'):
        e.replace_with('|')

    # dates
    for node in soup.select('.date .regular'):
        dates.append(''.join(node.find_all(text=True)))
    date_len = len(dates)
    # opponents
    for node in soup.select('.opp .highlight'):
        opponents.append(''.join(node.find_all(text=True)))

    # locations
    for node in soup.select('.display-directions'):
        locations.append(''.join(node.find_all(text=True)))

    # times/results
    for node in soup.select('.time'):
        times.append(''.join(node.find_all(text=True)))
        # print(''.join(node.find_all(text=True)))
    time_len = len(times)

    i = 0
    # Make sure volleyball doesn't screw up my time list
    if date_len == (time_len - 1):
        times.pop(0)

    # Organize into a dictionary
    for date in dates:
        game_list = []
        temp_date = datetime.strptime(date, '%b %d, %Y')
        formatted_date = "%s-%s-%s %s:%s:%s" % (temp_date.year, temp_date.month, temp_date.day, temp_date.hour, temp_date.minute, temp_date.second)
        game_list.append(formatted_date)
        game_list.append(opponents[i])
        game_list.append(locations[i])
        game_list.append(times[i])
        # print(game_list)
        final.append(game_list)
        i += 1

    # print(final)
    return final

'''
THIS IS THE MAIN PART OF THE FILE
'''

# open sports json file
dir_path = os.path.dirname(os.path.realpath(__file__))

with open(dir_path+'/byu_sports.json', 'r') as sports_file:
    json_string = sports_file.read()
parsed_json = json.loads(json_string)

# Make a list of the keys for the scraper
sports = []
for key, value in parsed_json.items():
    sports.append(key)

# list for sports
sports_list = {}

# run scraper for each sport
for sport in sports:
    info = get_sports_info(sport)
    sports_list[sport.rstrip()] = info
# Create JSON file
json_file = open(dir_path+'/byu_games.json', 'w')
json_array = json.dump(sports_list, json_file)
json_file.close()
