document.addEventListener("DOMContentLoaded", function(event) {
    // Use the global variables directly
    // Initialize arrays to hold cumulative power and prices
    var cumulativePower = [0]; // Start from zero power
    var prices = [sortedBids[0].bid_price]; // Start with the price of the first bid
    var totalPower = 0;

    // Calculate cumulative power and corresponding prices
    sortedBids.forEach(bid => {
        totalPower += bid.bid_power;
        cumulativePower.push(totalPower);
        prices.push(bid.bid_price);
    });

    var trace1 = {
        x: cumulativePower,
        y: prices,
        type: 'scatter',
        mode: 'lines+markers',
        line: {shape: 'vh'},  // Set the line shape to horizontal-then-vertical
        name: 'Supply Curve'
    };

    var trace2 = {
        x: [demandLevel, demandLevel],
        y: [0, marketClearingPrice],
        type: 'lines',
        name: 'Demand Level'
    };

    var layout = {
        title: 'Merit Order Curve',
        xaxis: { title: 'Cumulative Power (MW)' },
        yaxis: { title: 'Bid Price (€/MWh)' },
        showlegend: true
    };

    var data = [trace1, trace2];

    Plotly.newPlot('plot', data, layout);

    // Update the market clearing price display
    document.getElementById('marketClearingPrice').textContent = 'Market Clearing Price: ' + marketClearingPrice + ' €/MWh';
});
