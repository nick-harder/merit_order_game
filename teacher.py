"""
This file contains the Teacher class which handles the computation of market clearing price.
"""

from copy import deepcopy


class Teacher:
    def __init__(self):
        self.demand_level = 0
        self.vre_level = 0
        self.co2_price = 0

    def reset(self):
        self.demand_level = 0
        self.vre_level = 0
        self.co2_price = 0

    def compute_price(self, submitted_bids, power_plants):
        # make a copy of the bids list to avoid modifying the original list
        bids = deepcopy(submitted_bids)

        power_plants["marginal_cost"] = power_plants.apply(
            lambda x: self.calculate_marginal_cost(x), axis=1
        )

        sell_bids = [bid for bid in bids if bid["bid_type"] == "sell"]
        buy_bids = [bid for bid in bids if bid["bid_type"] == "buy"]

        # Sort buy bids descending by price and sell bids ascending by price
        buy_bids = sorted(buy_bids, key=lambda x: x["bid_price"], reverse=True)
        sell_bids = sorted(sell_bids, key=lambda x: x["bid_price"])

        accepted_sell = 0
        accepted_buy = 0
        market_clearing_price = None

        # check if total supply is less than total demand
        total_supply = sum([bid["bid_power"] for bid in sell_bids])
        total_demand = sum([bid["bid_power"] for bid in buy_bids])
        if total_supply < total_demand:
            return 3000, total_supply, total_supply

        i, j = 0, 0

        # Iterate to find the market clearing price
        while i < len(buy_bids) and j < len(sell_bids):
            buy_bid = buy_bids[i]
            sell_bid = sell_bids[j]

            if sell_bid["bid_price"] <= buy_bid["bid_price"]:
                # There is a match
                matched_power = min(
                    buy_bid["remaining_volume"], sell_bid["remaining_volume"]
                )
                buy_bid["remaining_volume"] -= matched_power
                sell_bid["remaining_volume"] -= matched_power

                buy_bid["accepted_volume"] += matched_power
                sell_bid["accepted_volume"] += matched_power

                accepted_buy += matched_power
                accepted_sell += matched_power

                # Update market clearing price
                market_clearing_price = sell_bid["bid_price"]

                # Move to next sell bid if this one is fully matched
                if sell_bid["remaining_volume"] == 0:
                    j += 1

                # Move to next buy bid if this one is fully matched
                if buy_bid["remaining_volume"] == 0:
                    i += 1
            else:
                # No more matches possible, move to next buy bid
                i += 1

        for bid in bids:
            if bid["bid_type"] == "sell":
                if bid["name"] == "VRE generation":
                    marginal_cost = 0
                elif bid["name"] in power_plants.index:
                    marginal_cost = power_plants.loc[bid["name"], "marginal_cost"]

                bid["profit"] = (
                    (market_clearing_price - marginal_cost)
                    * bid["accepted_volume"]
                    / 1000
                )
                # round to full value
                bid["profit"] = round(bid["profit"], 0)
            else:
                bid["profit"] = -market_clearing_price * bid["accepted_volume"] / 1000
                # round to full value
                bid["profit"] = round(bid["profit"], 0)

        return market_clearing_price, accepted_buy, bids

    def calculate_marginal_cost(self, power_plant):
        efficiency = power_plant["efficiency"] / 100
        cost = (
            power_plant["fuel_cost"] / efficiency
            + self.co2_price * power_plant["ef"] / efficiency
            + power_plant["variable_cost"]
        )

        return cost
