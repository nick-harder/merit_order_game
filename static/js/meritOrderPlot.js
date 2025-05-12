document.addEventListener("DOMContentLoaded", function(event) {
    // Initialize arrays for sell and buy types
    var cumulativePowerSell = [];
    var pricesSell = [];
    var totalPowerSell = 0;

    var cumulativePowerBuy = [];
    var pricesBuy = [];
    var totalPowerBuy = 0;

    // Filter and process sell bids
    var sellBids = submittedBids.filter(bid => bid.bid_type === 'sell').sort((a, b) => a.bid_price - b.bid_price);
    if (sellBids.length > 0) {
        // Initialize with the first bid's price and power at zero
        cumulativePowerSell.push(0);
        pricesSell.push(sellBids[0].bid_price);
    }
    sellBids.forEach(bid => {
        totalPowerSell += bid.bid_power;
        cumulativePowerSell.push(totalPowerSell);
        pricesSell.push(bid.bid_price);
    });

    // Filter and process buy bids in descending order by price
    var buyBids = submittedBids.filter(bid => bid.bid_type === 'buy').sort((a, b) => b.bid_price - a.bid_price);
    if (buyBids.length > 0) {
        // Initialize with the first bid's price and power at zero
        cumulativePowerBuy.push(0);
        pricesBuy.push(buyBids[0].bid_price);
    }
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

    var data = [traceSell, traceBuy];
    
    // Check if market clearing price is provided and not set to "Not Available"
    if (marketClearingPrice && marketClearingPrice !== 'Not Available') {
        var traceDemand = {
            x: [powerLevel, powerLevel],
            y: [0, marketClearingPrice],
            type: 'lines',
            name: 'Market Clearing Level',
            line: {
                dash: 'dot',
                width: 2
            }
        };
        data.push(traceDemand);

        // Update the market clearing price display
        document.getElementById('marketClearingPrice').textContent = 'Market Clearing Price: ' + marketClearingPrice + ' €/MWh';
    }

    var layout = {
        xaxis: { title: 'Cumulative Power (MW)', range: [0, Math.max(totalPowerSell, totalPowerBuy)+100] },
        yaxis: { title: 'Bid Price (€/MWh)', range: [-5, Math.max(...pricesSell, ...pricesBuy)+100] },
        showlegend: true
    };

    Plotly.newPlot('plot', data, layout);
});
