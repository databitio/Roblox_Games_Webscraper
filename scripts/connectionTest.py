import sys
from requests_html import HTMLSession
from proxy_reader import proxy_reader

url = 'https://www.roblox.com/discover'

#Final array to be returned
finalData = []

file_path = '../proxies.txt'
proxy_list = proxy_reader(file_path)

session = HTMLSession()

#Transforming proxy into readable form
completeProxy = ('http://' + proxy_list[int(sys.argv[1])])
newProxy = {'http': completeProxy}

#Getting the webpage through the proxy and rendering it
r = session.get(url, proxies=newProxy)
print("Success!")