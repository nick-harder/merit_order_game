"""
This file contains the Bid class which handles the storage and retrieval of bid data.
"""


class Bid:
    def __init__(self):
        self.bids = {}

    def add_bid(self, power_plant_name, bid_power, bid_price, bid_type):
        self.bids[power_plant_name] = {
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
                "power_plant_name": power_plant_name,
                "bid_power": bid["bid_power"],
                "bid_price": bid["bid_price"],
                "bid_type": bid["bid_type"],
            }
            for power_plant_name, bid in self.bids.items()
        ]
