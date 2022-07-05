import sys
from Session import get_valid_session
from Roblox_Scrape import *
from requests_html import HTMLSession

def main():

    url = 'https://www.roblox.com/discover'

    session = HTMLSession()
    res = get_valid_session(url)
    res.html.render(sleep=1)

    games_list = get_game_urls(res, int(sys.argv[1]))
    final_data = []

    for count, game_url in enumerate(games_list.absolute_links):
        print("Getting game ", count, " data...")
        res = session.get(game_url)
        
        game_object = []
        current_time = get_current_time()
        game_category = get_game_category()
        
        game_object.append(current_time)
        game_object.extend(get_game_attributes(res))
        game_object.append(get_game_title(res))
        game_object.append(get_creator_name(res))
        game_object.append(get_gameid(game_url))
        game_object.append(game_category)
        game_object.append(game_url)
        game_object.append(get_game_description(res))
        game_object = remove_special_characters(game_object)
        game_object = validate_game_data(res, game_object)
        final_data.append(game_object)
        print(game_object, len(game_object))
    data_logger(final_data, game_category)
    write_data_to_csv(final_data)

if __name__ == '__main__':
    main()