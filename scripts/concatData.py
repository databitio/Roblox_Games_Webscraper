import numpy as np
import pandas as pd
import glob
import os

files = os.path.join("./data", "*.csv")
files = glob.glob(files)
df_from_each_file = (pd.read_csv(f, sep='|') for f in files)
df_merged = pd.concat(df_from_each_file, ignore_index=True)
df_merged.set_index('Date')
df_merged.to_csv('roblox_games_data.csv')