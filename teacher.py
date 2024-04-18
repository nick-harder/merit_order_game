'''
This file contains the Teacher class which handles the computation of market clearing price.
'''
from bid import Bid
class Teacher:
    def __init__(self):
        self.demand_level = 0
    def set_demand(self, demand_level):
        self.demand_level = demand_level
    def get_demand(self):
        return self.demand_level
    def compute_price(self, bids):
        sorted_bids = sorted(bids, key=lambda x: x['bid_price'])
        total_power = 0
        market_clearing_price = 0
        for bid in sorted_bids:
            total_power += bid['bid_power']
            if total_power >= self.demand_level:
                market_clearing_price = bid['bid_price']
                break
        if total_power < self.demand_level:
            market_clearing_price = 3000

        return market_clearing_price
    def clear_demand(self):
        self.demand_level = 0