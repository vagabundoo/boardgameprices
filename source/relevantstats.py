import pandas as pd
import requests
import os
import statistics as stat
import source.functions as s

df = pd.read_csv("input/topBGs2019")
#df.head()

dfp = pd.read_csv("output/top100price.csv", names=['names','avgPrice'])
#dfp.head()

dfc = df.merge(right = dfp, on = 'names', how = 'left')

# This code round the avgPrice column so it only shows two decimals
round2 = lambda x: round(x,2)
dfc.avgPrice = dfc.avgPrice.apply(round2)

top100 = dfc[:100]

dfplayers = dfc.groupby(['max_players']).names.count()

# Graph of number of max players by count of games
maxplayers_by_count = dfplayers.plot(xlim=[0,20]).set_ylabel('game count')

avgprice100 = top100.mean()['avgPrice']
medianprice100 = top100.median()['avgPrice']
avgplaytime = dfc.mean()['avg_time']
medianplaytime = dfc.median()['avg_time']
playtime_by_count = dfc.groupby(['avg_time']).names.count().plot(xlim=[0,200]).set_ylabel('avg_playtime')
