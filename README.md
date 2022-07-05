# Roblox Games Webscraper
> Scrapes all 15 categories of games from https://www.roblox.com/discover; simply download the project, install any missing dependencies, and run the runscrape.bat file. By default only the first three categories Most Engaging, Up-And-Coming and Popular are enabled, however all others can be uncommented.

# Where to find the data
> Data can be found on Kaggle: https://www.kaggle.com/datasets/databitio/roblox-games-data

# How to use
1. Download the project; feel free to include more proxies of the form '255.255.255.0:8000' into it. Only 1 proxy is needed, however you may add as many proxies as you'd like, one per line in the file.

2. Ensure you have Python3 and the requests-html library downloaded;

```
pip3 install requests-html
```

3. Double click the runscrape.bat file to activate the web scraper

![image](https://user-images.githubusercontent.com/98235574/158307811-b5c3d9c4-525f-4400-a818-46a21df1239b.png)
Script running in action

All data is saved in the /data directory; example data can be found there.

![image](https://user-images.githubusercontent.com/98235574/158309783-2bc3b111-b9a1-4636-97d6-f29b3ebb550d.png)


