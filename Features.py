import numpy as np
import pandas as pd
from DataAccessor import DataAccessor

def best_bid_quote(data):
    return data.bid1 * data.bid1vol

def best_ask_quote(data):
    return data.ask1 * data.ask1vol

class Formulas:

    def vimba(data):
        return data.bid1vol / (data.bid1vol + data.ask1vol)

    def quote_vimba(data):
        bid_quote = best_bid_quote(data)
        ask_quote = best_ask_quote(data)
        return bid_quote / (bid_quote + ask_quote)

    def spread(data):
        return data.ask1 - data.bid2

    def last_take_ask_diff(data):
        return data.ask1 - data.last_price

    def last_take_bid_diff(data):
        return data.last_price - data.bid1

    def interest_imbalance(data):
        return (data.opened_position_qty / data.transacted_qty).replace([np.inf, -np.inf], 1)

    def open_interest_imbalance(data):
        return (data.opened_position_qty / data.d_open_interest).replace([np.inf, -np.inf], 1)

class Features:
    def compute(data):
        feats = [feat(data) for feat in Formulas.__dict__.values() if callable(feat)]
        cols = [feat.__name__ for feat in Formulas.__dict__.values() if callable(feat)]
        feats = pd.concat(feats, axis=1)
        feats.columns = cols
        return feats
