@REM bash downloadS3.sh
python connectionTest.py 1
python robloxscraper.py 0
python robloxscraper.py 1
python robloxscraper.py 2
@REM bash uploadS3.sh
@REM read -p Adding data: %date% %time% desc  
pause