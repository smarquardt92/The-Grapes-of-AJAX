d3.csv("https://raw.githubusercontent.com/GreciaWhite/Winos-Across-America/atc_branch/us_wine_db.csv", function(d) {
    return {
        winery : d.winery,
        designation : d.designation,
        variety : d.variety,
        province : d.province,
        country : d.country,
        points : +d.points,
        price : +d.price,
        description : d.description
    }
}).then(function(data) {
    
    console.log(data[58]);
    var wineData = data;
    var tbody = d3.select("tbody");

    var submit = d3.select("#submit")

    submit.on("click", function() {
        d3.event.preventDefault();
        //getting price input
        var priceElement = d3.select("#price-search-input");
        var priceValue = +priceElement.property("value");

        //getting points input
        var pointElement = d3.select("#point-search-input");
        var pointValue = +pointElement.property("value");


        //getting state input
        var stateElement = d3.select("#state-search-input");
        var stateValue = stateElement.property("value");


        //getting variety input
        var varietyElement = d3.select("#variety-search-input");
        var varietyValue = varietyElement.property("value");

        console.log(priceValue);
        console.log(pointValue);
        console.log(stateValue);
        console.log(varietyValue)

        var Filter = wineData.filter(encounter => encounter.price === priceValue)
                             .filter(encounter => encounter.points === pointValue)
                             .filter(encounter => encounter.variety === varietyValue)
                             .filter(encounter => encounter.province === stateValue)
        console.log(Filter)

        document.getElementById("search_results").innerHTML="";

        Filter.forEach(function(display) {
            var row = tbody.append("tr");
            Object.entries(display).forEach(function([key, value]) {
            var cell = tbody.append("td");
            cell.text(value);
        })
        // pointFilter.forEach(function(display) {
        //     var row = tbody.append("tr");
        //     Object.entries(display).forEach(function([key, value]) {
        //         var cell = tbody.append("td");
        //         cell.text(value);
        //     })
        // })
    })

    })
  });