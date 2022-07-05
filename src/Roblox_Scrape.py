import re
import sys
import csv
from datetime import datetime
from requests_html import HTMLSession

def get_game_category():
    game_categories = ['Most Engaging', 'Up-And-Coming', 'Popular',
                       'Top Rated', 'Free Private Servers', 'Learn & Explore',
                       'Featured', 'Popular Among Premium', 'Top Earning',
                       'People Love', 'Roleplay', 'Adventure', 'Fighting',
                       'Obby', 'Tycoon', 'Simulator']
    return game_categories[int(sys.argv[1])]

def get_game_xpaths():
    xpaths = []
    #There are 15 different categories on roblox discover main page
    for count in range(2, 18):
        xpaths.append(f'//*[@id="games-carousel-page"]/div[{count}]/div/div/div[1]/ul',)
    return xpaths

def get_game_urls(session, option: int):
    xpaths = get_game_xpaths()
    return session.html.xpath(xpaths[option], first=True)

def get_current_time():
    return str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

#Scrapes attributes 'Active Users', 'Favorites', 'Total Visits', 'Server Size', 'Game Genre', and 'URL'
def get_game_attributes(res):
    attributes = res.html.find('p.text-lead.font-caption-body')
    attribute_list = []

    for count, attribute in enumerate(attributes):
        if(count>=7):
            break
        try:
            attribute_list.append(attribute.text)
        except:
            attribute_list.append('-')
    return attribute_list

def get_game_title(session: HTMLSession):
    try:
        html_title = session.html.find('div.game-title-container')
        title = html_title[0].text
        return title
    except:
        return '-'

def get_creator_name(session: HTMLSession):
    try:
        creator_by_name = session.html.find('div.game-creator', first=True).text
        creator = re.search('(?<=By ).*', creator_by_name)
        return creator.group(0)
    except:
        return '-'

def get_gameid(game_url: str):
    game_ID_list = re.findall('[\d]*', game_url)
    for gameID in game_ID_list:
        if(len(gameID) > 6):
            return gameID
    return '-'

def get_game_description(session: HTMLSession):
    try:
        html_description = session.html.find('pre.text.game-description.linkify')
        game_description = html_description[0].text
        game_description = game_description.replace('\n','')
        return game_description
    except:
        return '-'

def remove_special_characters(data: list):
    cleaned_data = []
    for item in data:
        cleaned_item = str(item).replace('\"','').replace('\'','').replace('|','').replace('\n','').replace(',','')
        cleaned_data.append(cleaned_item)
    return cleaned_data

def validate_game_data(session:HTMLSession, data:list):
    if(len(data)==14):
        return data
    else:
        print('\n\n ERROR: ROW DID NOT HAVE CORRECT NUMBER OF FEATURES \n\n')
        with open('../data/incompleteData.txt', 'a', newline='', encoding='utf-8') as f:
            f.write(session.text)
            for attribute in data:
                f.write(attribute)
    return []

def data_logger(data:list, game_category:str):
    current_time = get_current_time()

    if(len(data)<=1):
        with open('./data/dataLogs.txt', 'a', newline='', encoding='utf-8') as f:
            final_output = 'Error: No rows written for category "'+game_category+ '" at time '+current_time+'\n'
            f.write(final_output)
        return 
    else:
        with open('./data/dataLogs.txt', 'a', newline='', encoding='utf-8') as f:
            final_output = 'Success: Category "'+game_category+'" at time '+current_time+ ' was entered correctly.'+'\n'
            f.write(final_output)
        return

def write_data_to_csv(data: list):
    file_creation_time = datetime.now().strftime('%Y-%m-%d_%H_%M_%S')
    file_location = './data/'+file_creation_time+'.csv'
    head = 'Date|Active Users|Favorites|Total Visits|Date Created|Last Updated|Server Size|Genre|Title|Creator|gameID|Category|URL|Description\n'

    with open(file_location, 'a', newline='', encoding='utf-8') as f:
        f.write(head)
        output = csv.writer(f, delimiter='|')
        output.writerows(data)
    print('pass!')
    return 