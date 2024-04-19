from flask import Flask, render_template, request, redirect, url_for, session
from bid import Bid
from teacher import Teacher

app = Flask(__name__)
app.secret_key = "merit_order_game"
bid = Bid()
teacher = Teacher()


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
    # Student's bid submission view
    return render_template("student.html")


@app.route("/submit_bid", methods=["POST"])
def submit_bid():
    power_plant_name = request.form["power_plant_name"]
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

    return redirect(url_for("index"))


@app.route("/set_vre", methods=["POST"])
def set_vre():
    vre_level = float(request.form["vre_level"])
    bid.add_bid("VRE generation", vre_level, 0, "sell")

    teacher.set_vre(vre_level)

    return redirect(url_for("index"))


@app.route("/reload_bids", methods=["POST"])
def reload_bids():

    return redirect(url_for("index"))


@app.route("/compute_price", methods=["POST"])
def compute_price():
    market_clearing_price, accepted_buy, accepted_sell = teacher.compute_price(
        bid.get_bids()
    )

    # Sort bids by bid_price for plotting
    submitted_bids = bid.get_bids()
    return render_template(
        "index.html",
        bids=bid.get_bids(),
        demand_level=accepted_buy,
        market_clearing_price=market_clearing_price,
        submitted_bids=submitted_bids,
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
