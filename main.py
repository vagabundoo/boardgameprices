import pandas as pd
import requests
import os
import statistics as stat
import source.functions as s
import source.relevantstats as d
import argparse

# Arguments for parser
parser = argparse.ArgumentParser(description='Get boardgame info and statistics, from top 5000 boardgames according to BoardGameGeek')
parser.add_argument('-n','--name', help='Given a boardgame name, returns a dict of data related to the particular game')
parser.add_argument('-t','--top', type=int, help='Returns top x board games, where x is int given by user')
parser.add_argument('--avgprice100', action='store_true', help='Returns the average and median price of the top 100 games')
args = parser.parse_args()

# Functions
def getGameInfo(name):
    return d.dfc[d.dfc['names'] == name].to_dict(orient='list') 

def getTopX (num):
    return d.dfc[d.dfc['rank'] <= num][['rank','names']].set_index(['rank'])

# avgprice100 = top100.mean()['avgPrice']
# medianprice100 = top100.median()['avgPrice']
# avgplaytime = dfc.mean()['avg_time']
# medianplaytime = dfc.median()['avg_time']
# playtime_by_count =

# Execution of parser
if __name__ == '__main__':
    if args.name:
        print(getGameInfo(args.name))
    elif args.top:
        print(getTopX(args.top))
    elif args.avgprice100:
        print(f'{round(d.avgprice100,2)} USD is the average price among the top 100 board games\n{round(d.medianprice100,2)} USD is the median price among the top 100 boardgames')
    

   
# getGameInfo('Gloomhaven')

# d.dfc.loc[d.dfc['year'] > 2000]
# d.dfc[d.dfc['year'] > 2000]