from flask import Flask, render_template, request, redirect, url_for, session
import pandas as pd
from bid import Bid
from teacher import Teacher
import os

app = Flask(__name__)
randomize_power_plants = False
if randomize_power_plants:
    app.secret_key = os.urandom(24)
else:
    app.secret_key = "merit_order_game"


bid = Bid()
teacher = Teacher()

load_storages = False
if load_storages:
    power_plants = pd.read_csv("powerplants_with_storages.csv")
else:
    power_plants = pd.read_csv("powerplants.csv")

# Shuffle the power plants DataFrame
power_plants = power_plants.sample(frac=1).reset_index(drop=True)
assigned_power_plants = []


@app.route("/")
def index():
    # Teacher's view
    return render_template(
        "index.html",
        bids=bid.get_bids(),
        inelastic_demand_level=teacher.demand_level,
        vre_level=teacher.vre_level,
    )


@app.route("/student")
def student():
    if "assigned_power_plant" in session:
        assigned_power_plant = session["assigned_power_plant"]
    else:
        if len(assigned_power_plants) == len(power_plants):
            return "All power plants have been assigned."

        available_power_plants = power_plants[
            ~power_plants["name"].isin(assigned_power_plants)
        ]
        assigned_power_plant = available_power_plants.sample().to_dict(
            orient="records"
        )[0]
        assigned_power_plants.append(assigned_power_plant["name"])
        session["assigned_power_plant"] = assigned_power_plant

    # Student's bid submission view
    return render_template("student.html", assigned_power_plant=assigned_power_plant)


@app.route("/submit_bid", methods=["POST"])
def submit_bid():
    power_plant_name = session["assigned_power_plant"]["name"]
    bid_power = abs(float(request.form["bid_power"]))
    bid_price = float(request.form["bid_price"])
    bid_type = request.form["bid_type"]

    # Add the bid to the bid object
    bid.add_bid(power_plant_name, bid_power, bid_price, bid_type)

    # Store the bid information in a session variable
    session["submitted_bid"] = {
        "power_plant_name": power_plant_name,
        "bid_power": bid_power,
        "bid_price": bid_price,
        "bid_type": bid_type,
    }

    return redirect(url_for("student"))


@app.route("/set_demand", methods=["POST"])
def set_demand():
    inelastic_demand_level = float(request.form["inelastic_demand_level"])
    bid.add_bid("Inelastic demand", inelastic_demand_level, 500, "buy")

    teacher.set_demand(inelastic_demand_level)

    return reload_bids()


@app.route("/set_vre", methods=["POST"])
def set_vre():
    vre_level = float(request.form["vre_level"])
    bid.add_bid("VRE generation", vre_level, 0, "sell")

    teacher.set_vre(vre_level)

    return reload_bids()


@app.route("/reload_bids", methods=["POST"])
def reload_bids():
    bids_as_list = bid.bids_to_list()

    return render_template(
        "index.html",
        bids=bid.get_bids(),
        demand_level=0,
        market_clearing_price=0,
        submitted_bids=bids_as_list,
        inelastic_demand_level=teacher.demand_level,
        vre_level=teacher.vre_level,
    )


@app.route("/compute_price", methods=["POST"])
def compute_price():
    bids_as_list = bid.bids_to_list()
    market_clearing_price, accepted_buy, accepted_sell = teacher.compute_price(
        bids_as_list
    )

    return render_template(
        "index.html",
        bids=bid.get_bids(),
        demand_level=accepted_buy,
        market_clearing_price=market_clearing_price,
        submitted_bids=bids_as_list,
        inelastic_demand_level=teacher.demand_level,
        vre_level=teacher.vre_level,
    )


@app.route("/clear_bids", methods=["POST"])
def clear_bids():
    bid.clear_bids()
    teacher.reset()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
