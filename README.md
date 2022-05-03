# Roblox Games Webscraper
> Scrapes Most Popular, Engaging, and Up-and-Coming games off of https://www.roblox.com/discover

# Where to find the data
> Data can be found on Kaggle: https://www.kaggle.com/datasets/databitio/roblox-games-data

# How to use
1. Download the files, then in the home folder create a 'proxies.txt' file and put at least 1 proxy of the form '255.255.255.0:8000' into it. Add as many proxies as necessary, one per line in the file.

2. Ensure you have Python3 and the requests-html library downloaded;
To install pip:

```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```


Navigate to file get-pip.py is in:

```
python get-pip.py
```

Then install requests-html:

```
pip3 install requests-html
```


3. Navigate to the /scripts directory and double click the runscrape.bat file to activate the web scraper

![image](https://user-images.githubusercontent.com/98235574/158307811-b5c3d9c4-525f-4400-a818-46a21df1239b.png)
Script running in action

All data is saved in the /data directory; example data can be found there.

![image](https://user-images.githubusercontent.com/98235574/158309783-2bc3b111-b9a1-4636-97d6-f29b3ebb550d.png)

