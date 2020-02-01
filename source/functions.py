import pandas as pd
import requests
import os
import statistics as stat

def requestAtlas(endpoint):
       
    baseUrl = "https://www.boardgameatlas.com/api/"
    url = baseUrl+endpoint
    print(f"Requesting data from {url}")
    
    res = requests.get(url)
    if res.status_code != 200:
        print(res.text)
        raise ValueError("Bad Response")
    return res.json()

def getGameID (gamename, client_id="qaLdCno66F", exact=False, limit=1):
    # When give a gamename and a client_id, this function returns the game_id used in the API of boardgameatlas. 
    # The function orders by most popularity, and returns one gameID by default.
    try:
        game = requestAtlas(f'search?name={gamename}&client_id={client_id}&order_by=popularity&limit={limit}&exact={exact}')
        return game['games'][0]['id']
    except:
        return None


def getAvgPrice(gameID, client_id="qaLdCno66F"):
    # This function gets the average price of a game, from the US sellers with valid prices. 
    prices = requestAtlas(f'game/prices?game_id={gameID}&client_id={client_id}')
    
    pfloats = []
    for p in prices['prices']:
        try:
            if float(p['price']) > 0:
                pfloats.append(float(p['price']))
        except:
            continue
    try:
        return stat.mean(pfloats)
    except:
        return None # If none of the prices by the sellers are valid, the function returns None instead

def getGamePrices(games):
    # Takes a list of game names 
    # Returns a list of lists with gamename, and average price in USD (or None if game is not avaliable at retailers)
    game_price = []
    for game in games:
        #if count >= 2: break
        game_price.append([game, getAvgPrice(getGameID(game))])
    return game_price