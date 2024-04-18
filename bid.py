'''
This file contains the Bid class which handles the storage and retrieval of bid data.
'''
class Bid:
    def __init__(self):
        self.bids = []
    def add_bid(self, power_plant_name, bid_power, bid_price):
        self.bids.append({
            'power_plant_name': power_plant_name,
            'bid_power': bid_power,
            'bid_price': bid_price
        })
    def get_bids(self):
        return self.bids
    def clear_bids(self):
        self.bids = []