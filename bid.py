"""
This file contains the Bid class which handles the storage and retrieval of bid data.
"""


class Bid:
    def __init__(self):
        self.bids = {}

    def add_bid(self, name, bid_power, bid_price, bid_type):
        self.bids[name] = {
            "bid_power": bid_power,
            "bid_price": bid_price,
            "bid_type": bid_type,
        }

    def get_bids(self):
        return self.bids

    def clear_bids(self):
        self.bids = {}

    def bids_to_list(self):
        return [
            {
                "name": name,
                "bid_power": bid["bid_power"],
                "bid_price": bid["bid_price"],
                "bid_type": bid["bid_type"],
                "accepted_volume": 0,
                "remaining_volume": bid["bid_power"],
                "profit": 0,
            }
            for name, bid in self.bids.items()
        ]
