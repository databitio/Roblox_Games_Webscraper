#***********************************************************************************************#
#                                                                                               #
#                                     Author: databitIO                                         #                                                     
#                                       Date: 1/20/2022                                         #
#                                                                                               #
#***********************************************************************************************#
from requests_html import HTMLSession
import re
import csv
from datetime import datetime
import sys
import random
from proxy_reader import proxy_reader

#***********************************************************************************************#
def main():
    #Proxy list

    file_path = '../proxies.txt'
    proxy_list = proxy_reader(file_path)

    random.shuffle(proxy_list)
    #URL being searched
    url = 'https://www.roblox.com/discover'

    #Final array to be returned
    final_data = []
    session = HTMLSession()

    #***********************************************************************************************#
    #Rotate proxies
    for proxy in proxy_list:
        try:
            #Transforming proxy into readable form
            complete_proxy = ('http://' + proxy)
            new_proxy = {'http': complete_proxy}

            #Getting the webpage through the proxy and rendering it
            r = session.get(url, proxies=new_proxy)

            r.html.render(sleep=1)
        except:
            continue

        #Category that system argument will choose
        category_lists = ['Most Engaging', 'Popular', 'Up-And-Coming']
        xpaths = ['//*[@id="games-carousel-page"]/div/div[1]/div/div',
                '//*[@id="games-carousel-page"]/div/div[3]/div/div', 
                '//*[@id="games-carousel-page"]/div/div[2]/div/div']

        games_list = r.html.xpath(xpaths[int(sys.argv[1])], first=True)

        count = 1
        #***********************************************************************************************#
        #Each loop goes to a game URL and scrapes the data
        for game_url in games_list.absolute_links:
            print("Getting game ", count, " data...")
            
            #Gets current time to be used as a feature
            current_time = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            try:
                #Go to the game_url page
                r = session.get(game_url)
                #Scrapes attributes 'Active Users', 'Favorites', 'Total Visits', 'Server Size', 'Game Genre', and 'URL'
                all_attributes = r.html.find('p.text-lead.font-caption-body')
                attribute_list = []
                attribute_list.append(current_time)
            except:
                continue

            #***********************************************************************************************#
            #Adds all attributes gathered from previous step to list
            for attribute in all_attributes:
                try:
                    if(attribute.text == ""):
                        continue
                    attribute_list.append(attribute.text)
                except:
                    attribute_list.append('-')
            #***********************************************************************************************#
            #Finds Game Title
            try:
                game_title = r.html.find('div.game-title-container')
                title = game_title[0].text
                title = "".join(title.split())
                attribute_list.append(title)
            except:
                attribute_list.append('-')

            #***********************************************************************************************#
            #Finds Creator Name
            try:
                creator_by_name = r.html.find('div.game-creator', first=True).text
                creator = re.search('(?<=By ).*', creator_by_name)
                attribute_list.append(creator.group(0))
            except:
                attribute_list.append('-')

            #***********************************************************************************************#
            #Finds GameID
            try:
                #From URL game ID can be derived
                game_ID_list = re.findall('[\d]*', game_url)
                for gameID in game_ID_list:
                    if(len(gameID) > 6):
                        attribute_list.append(gameID)
            except:
                attribute_list.append('-')

            #***********************************************************************************************#
            #Add Game Category and URL
            attribute_list.append(category_lists[int(sys.argv[1])])
            attribute_list.append(game_url)

            #***********************************************************************************************#
            #Gives game description
            try:
                gameDescription = r.html.find('pre.text.game-description.linkify')
                description = gameDescription[0].text
                description = description.replace('\n','')
                attribute_list.append(description)
            except:
                attribute_list.append('-')

            #***********************************************************************************************#
            #Data cleaning
            final_list = []
            for item in attribute_list:
                new_item = item.replace('\"','').replace('\'','').replace('|','').replace('\n','').replace(',','')
                final_list.append(new_item)
            #***********************************************************************************************#
            #Checks that all data has been scraped correctly; if there aren't exactly 15 entries, do not add to data
            count+=1
            if(len(final_list)==14):
                final_data.append(final_list)
                print(final_list)
            else:
                print('\n\n ERROR: ROW DID NOT HAVE CORRECT NUMBER OF FEATURES \n\n')
                with open('../data/incompleteData.txt', 'a', newline='', encoding='utf-8') as f:
                    f.write(r.text)
                    for attribute in final_list:
                        f.write(attribute)
                continue
        break
    #***********************************************************************************************#
    #Write results to log file
    current_time = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    category_lists = ['Most Engaging', 'Popular', 'Up-And-Coming']
    if(len(final_data)<5):
        with open('../data/dataLogs.txt', 'a', newline='', encoding='utf-8') as f:
            final_output = 'Error: Row did not have correct number of features for category "'+category_lists[int(sys.argv[1])]+ '" at time '+current_time+'\n'
            f.write(final_output)
        return 0
    else:
        with open('../data/dataLogs.txt', 'a', newline='', encoding='utf-8') as f:
            final_output = 'Success: Category "'+category_lists[int(sys.argv[1])]+'" at time '+current_time+ ' was entered correctly.'+'\n'
            f.write(final_output)
    
    #***********************************************************************************************#
    #Add all entries into the data.csv file
    file_creation_time = datetime.now().strftime('%Y-%m-%d_%H_%M_%S')
    write_file = '../data/'+file_creation_time+'.csv'
    head = 'Date|Active Users|Favorites|Total Visits|Date Created|Last Updated|Server Size|Genre|Title|Creator|gameID|Category|URL|Description\n'

    with open(write_file, 'a', newline='', encoding='utf-8') as f:
        f.write(head)
        output = csv.writer(f, delimiter='|')
        output.writerows(final_data)
    return 0
#***********************************************************************************************#

if __name__ == '__main__':
    main()