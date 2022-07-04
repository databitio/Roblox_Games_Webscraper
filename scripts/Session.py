import random
from requests_html import HTMLSession

def proxy_file_to_list(proxy_file: str):
    proxy_list = []
    with open(proxy_file, 'r', newline='', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            proxy_list.append(line)
        random.shuffle(proxy_list)
    return proxy_list

def create_proxy_url_list(proxy_file: str):
    proxy_list = proxy_file_to_list(proxy_file)
    complete_proxy_list = []

    for proxy in proxy_list:
        proxy_url = ('http://' + proxy)
        complete_proxy = {'http': proxy_url}
        complete_proxy_list.append(complete_proxy)

    return complete_proxy_list

def get_valid_session(url: str):
    file_path = '../myproxies.txt'
    proxy_list = create_proxy_url_list(file_path)
    print(proxy_list)

    htmlsession = HTMLSession()
    for proxy in proxy_list:
        try:
            session = htmlsession.get(url, proxies=proxy)
            session.html.render(sleep=1)
            return session
            
        except:
            continue

    print("All proxies exhausted; none work!")
    return