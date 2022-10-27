class DataAccessor:

    def __init__(self, df):
        self.df = df
        
        self.id = self.df['id']
        self.last_price = self.df['last_price']
        self.mid = self.df['mid']
        self.opened_position_qty = self.df['opened_position_qty']
        self.closed_position_qty = self.df['closed_position_qty']
        self.transacted_qty = self.df['transacted_qty']
        self.d_open_interest = self.df['d_open_interest']
        
        self.bid = []
        self.bid.extend([self.df['bid1'], self.df['bid2'], 
                         self.df['bid3'], self.df['bid4'], self.df['bid5']])
        
        self.ask = []
        self.ask.extend([self.df['ask1'], self.df['ask2'], 
                         self.df['ask3'], self.df['ask4'], self.df['ask5']])
        
        self.bidvol = []
        self.bidvol.extend([self.df['bid1vol'], self.df['bid2vol'], 
                         self.df['bid3vol'], self.df['bid4vol'], self.df['bid5vol']])
        
        self.askvol = []
        self.askvol.extend([self.df['ask1vol'], self.df['ask2vol'], 
                         self.df['ask3vol'], self.df['ask4vol'], self.df['ask5vol']])
