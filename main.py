from flask import Flask, render_template, request, redirect, url_for, session
from bid import Bid
from teacher import Teacher

app = Flask(__name__)
app.secret_key = "merit_order_game"
bid = Bid()
teacher = Teacher()

@app.route('/')
def index():
    # Teacher's view
    return render_template('index.html', bids=bid.get_bids(), demand_level=teacher.get_demand())

@app.route('/student')
def student():
    # Student's bid submission view
    return render_template('student.html')

@app.route('/submit_bid', methods=['POST'])
def submit_bid():
    power_plant_name = request.form['power_plant_name']
    bid_power = abs(float(request.form['bid_power']))
    bid_price = float(request.form['bid_price'])
    
    # Add the bid to the bid object
    bid.add_bid(power_plant_name, bid_power, bid_price)
    
    # Store the bid information in a session variable
    session['submitted_bid'] = {
        'power_plant_name': power_plant_name,
        'bid_power': bid_power,
        'bid_price': bid_price
    }
    
    return redirect(url_for('student'))

@app.route('/set_demand', methods=['POST'])
def set_demand():
    demand_level = float(request.form['demand_level'])
    teacher.set_demand(demand_level)
    return redirect(url_for('index'))

@app.route('/compute_price', methods=['POST'])
def compute_price():
    market_clearing_price = teacher.compute_price(bid.get_bids())
    # Sort bids by bid_price for plotting
    sorted_bids = sorted(bid.get_bids(), key=lambda x: x['bid_price'])
    return render_template('index.html', bids=bid.get_bids(), demand_level=teacher.get_demand(),
                           market_clearing_price=market_clearing_price, sorted_bids=sorted_bids)

@app.route('/clear_bids', methods=['POST'])
def clear_bids():
    bid.clear_bids()
    teacher.clear_demand()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
