document.addEventListener("DOMContentLoaded", function(event) {
    // Initialize arrays for sell and buy types
    var cumulativePowerSell = [0];
    var pricesSell = [0];
    var totalPowerSell = 0;

    var cumulativePowerBuy = [0];
    var pricesBuy = [0];
    var totalPowerBuy = 0;

    // Filter and process sell bids
    var sellBids = submittedBids.filter(bid => bid.bid_type === 'sell').sort((a, b) => a.bid_price - b.bid_price);
    sellBids.forEach(bid => {
        totalPowerSell += bid.bid_power;
        cumulativePowerSell.push(totalPowerSell);
        pricesSell.push(bid.bid_price);
    });

    // Filter and process buy bids in descending order by price
    var buyBids = submittedBids.filter(bid => bid.bid_type === 'buy').sort((a, b) => b.bid_price - a.bid_price);
    buyBids.forEach(bid => {
        totalPowerBuy += bid.bid_power;
        cumulativePowerBuy.push(totalPowerBuy);
        pricesBuy.push(bid.bid_price);
    });

    // Create traces for sell and buy bids
    var traceSell = {
        x: cumulativePowerSell,
        y: pricesSell,
        type: 'scatter',
        mode: 'lines+markers',
        line: { shape: 'vh' },
        name: 'Sell Bids'
    };

    var traceBuy = {
        x: cumulativePowerBuy,
        y: pricesBuy,
        type: 'scatter',
        mode: 'lines+markers',
        line: { shape: 'vh' },
        name: 'Buy Bids'
    };
    
    var traceDemand = {
        x: [demandLevel, demandLevel],
        y: [0, marketClearingPrice],  // Adjust to the market clearing price
        type: 'lines',
        name: 'Market Clearing Level',
        line: {
            dash: 'dot',  // Set the line style to dotted
            width: 2      // Optional: adjust the line width if needed
        }
    };

    var layout = {
        title: 'Merit Order Curve',
        xaxis: { title: 'Cumulative Power (MW)' },
        yaxis: { title: 'Bid Price (€/MWh)' },
        showlegend: true
    };

    var data = [traceSell, traceBuy, traceDemand];

    Plotly.newPlot('plot', data, layout);

    // Update the market clearing price display
    document.getElementById('marketClearingPrice').textContent = 'Market Clearing Price: ' + marketClearingPrice + ' €/MWh';
});
