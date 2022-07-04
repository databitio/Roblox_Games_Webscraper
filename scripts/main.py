import sys
from Session import get_valid_session
from Roblox_Scrape import *

def main():

    url = 'https://www.roblox.com/discover'

    session = get_valid_session(url)
    game_list = get_game_urls(session, int(sys.argv[1]))

    for count, game_url in enumerate(game_list.absolute_links):
        print("Getting game ", count, " data...")
        
        game_object = []
        current_time = get_current_time()
        game_category = get_game_category()
        
        game_object.append(current_time)
        game_object.extend(get_game_attributes(session))
        game_object.append(get_game_title(session))
        game_object.append(get_creator_name(session))
        game_object.append(get_creator_name(session))
        game_object.append(get_gameid(game_url))
        game_object.append(game_category)
        game_object.append(game_url)
        game_object.append(get_game_description(session))
        print(game_object)
        game_object = remove_special_characters(game_object)
        game_object = validate_game_data(session, game_object)
        print(game_object)
        data_logger(game_object, game_category)
        write_data_to_csv(game_object)

if __name__ == '__main__':
    main()