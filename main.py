import pandas as pd
import requests
import os
import statistics as stat
import source.functions as s
import source.relevantstats as d
import argparse
import weasyprint

# Arguments for parser
parser = argparse.ArgumentParser(description='Get boardgame info and statistics, from top 5000 boardgames according to BoardGameGeek')
parser.add_argument('-n','--name', help='Given a boardgame name, returns a dict of data related to the particular game')
parser.add_argument('-t','--top', type=int, help='Returns top x board games, where x is int given by user')
parser.add_argument('--avgprice100', action='store_true', help='Returns the average and median price of the top 100 games')
parser.add_argument('--playtime', action='store_true', help='Get playtime statistics')
parser.add_argument('--topaspdf', type=int, help='Returns top x board games as a PDF')
args = parser.parse_args()

# Functions
def getGameInfo(name):
    return d.dfc[d.dfc['names'] == name].to_dict(orient='list') 

def getTopX (num):
    return d.dfc[d.dfc['rank'] <= num][['rank','names','year','avgPrice']].set_index(['rank'])

def createPDFtop(num):
    df = getTopX(num)
    intermediate_html = './input/intermediate.html'
    df.to_html(intermediate_html, index=True, columns=['year','names','avgPrice'], justify='left')
    out_pdf= 'output/test.pdf'
    weasyprint.HTML(intermediate_html).write_pdf(out_pdf)

# Execution of parser
if __name__ == '__main__':
    if args.name:
        print(getGameInfo(args.name))
    elif args.top:
        print(getTopX(args.top))
    elif args.avgprice100:
        print(f'{round(d.avgprice100,2)} USD is the average price among the top 100 board games\n{round(d.medianprice100,2)} USD is the median price among the top 100 boardgames')
    elif args.topaspdf:
        createPDFtop(args.topaspdf)
    elif args.playtime:
        print(f'Median playtime: {round(d.medianplaytime)} minutes\nMean playtime: {round(d.avgplaytime)} minutes')



