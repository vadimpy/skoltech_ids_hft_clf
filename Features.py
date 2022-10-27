import numpy as np
import pandas as pd
from DataAccessor import DataAccessor

def best_bid_quote(data):
    return data.bid[0] * data.bidvol[0]

def best_ask_quote(data):
    return data.ask[0] * data.askvol[0]

class Formulas:

    def vimba(data):
        return data.bidvol[0] / (data.bidvol[0] + data.askvol[0])

    def quote_vimba(data):
        bid_quote = best_bid_quote(data)
        ask_quote = best_ask_quote(data)
        return bid_quote / (bid_quote + ask_quote)

    def vimba_2(data):
        n = 2
        bid_vol = np.zeros(data.df.shape[0])
        ask_vol = np.zeros(data.df.shape[0])
        for i in range(n):
            bid_vol += data.bidvol[i]
            ask_vol += data.askvol[i]
        return bid_vol / (bid_vol + ask_vol)

    def vimba_3(data):
        n = 3
        bid_vol = np.zeros(data.df.shape[0])
        ask_vol = np.zeros(data.df.shape[0])
        for i in range(n):
            bid_vol += data.bidvol[i]
            ask_vol += data.askvol[i]
        return bid_vol / (bid_vol + ask_vol)

    def vimba_4(data):
        n = 4
        bid_vol = np.zeros(data.df.shape[0])
        ask_vol = np.zeros(data.df.shape[0])
        for i in range(n):
            bid_vol += data.bidvol[i]
            ask_vol += data.askvol[i]
        return bid_vol / (bid_vol + ask_vol)

    def vimba_5(data):
        n = 5
        bid_vol = np.zeros(data.df.shape[0])
        ask_vol = np.zeros(data.df.shape[0])
        for i in range(n):
            bid_vol += data.bidvol[i]
            ask_vol += data.askvol[i]
        return bid_vol / (bid_vol + ask_vol)

    ####################################

    def bid_diff_1(data):
        i = 1
        return data.bid[i-1] - data.bid[i]

    def bid_diff_2(data):
        i = 2
        return data.bid[i-1] - data.bid[i]

    def bid_diff_3(data):
        i = 3
        return data.bid[i-1] - data.bid[i]

    def bid_diff_4(data):
        i = 4
        return data.bid[i-1] - data.bid[i]

    ####################################
    
    def ask_diff_1(data):
        i = 1
        return data.ask[i-1] - data.ask[i]

    def ask_diff_2(data):
        i = 2
        return data.ask[i-1] - data.ask[i]

    def ask_diff_3(data):
        i = 3
        return data.ask[i-1] - data.ask[i]

    def ask_diff_4(data):
        i = 4
        return data.ask[i-1] - data.ask[i]

    ####################################
    
    def spread(data):
        return data.ask[0] - data.bid[0]

    def last_take_ask_diff(data):
        return data.ask[0] - data.last_price

    def last_take_bid_diff(data):
        return data.last_price - data.bid[0]

    def interest_imbalance(data):
        return (data.opened_position_qty / data.transacted_qty).replace([np.inf, -np.inf], 0)

    def open_interest_imbalance(data):
        return (data.d_open_interest / data.transacted_qty).replace([np.inf, -np.inf], 0)

class Features:
    def compute(data):
        feats = [feat(data) for feat in Formulas.__dict__.values() if callable(feat)]
        cols = [feat.__name__ for feat in Formulas.__dict__.values() if callable(feat)]
        feats = pd.concat(feats, axis=1)
        feats.columns = cols
        return feats
