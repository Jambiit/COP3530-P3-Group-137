function optionSelect(){
  var selectedOption = document.querySelector('input[name="radioGroup"]:checked').value;
  switch(selectedOption){
    case 'option1':
      searchCSV();
      break;
    case 'option2':
      searchCSVTags();
      break;
    default:
      break;
  }
}

function processAndDisplay(websites) {
  // Remove special characters and whitespace, leaving only words separated by commas
    var cleanString = websites.replace(/[^\w\s,]/g, '').trim();
    
    // Split the cleaned string into an array of words separated by commas
    var websitesArray = cleanString.split(/\s*,\s*/);

    // Modify websites to hyperlinks
    var hyperlinks = websitesArray.map(function(website) {
        return '<a href="https://' + website + '.neocities.org" target="_blank">' + website + '</a>';
    });

    // Return hyperlinks separated by newlines
    return hyperlinks.join('<br>');
}

function searchCSV() {
    var searchText = document.getElementById("searchInput").value.trim().toLowerCase();
    var searchResults = document.getElementById("searchResults");
    var flavorText = document.getElementById("searchText");
    var searchLink = document.getElementById("searchLink");
    // Clear previous search results
    searchResults.innerHTML = "";
    flavorText.innerHTML = "";

    // Read the CSV file
    fetch("smalldata_sitelist.csv")
    .then(response => response.text())
    .then(data => {
        // Split CSV data into rows
        var rows = data.split('\n');
        
        // Search for the input text in the first column of each row
        var found = false;
        for (var i = 0; i < rows.length; i++) {
            var separated = rows[i].split(/,(.*)/s);
            var firstColumn = separated[0].trim().toLowerCase();
            
            if (firstColumn === searchText) {
                // Pass the second data to processAndDisplay function
                flavorText.innerHTML = "<p>We found " + searchText + "!</p>";
                //searchLink.innerHTML = '<a href="https://' + website + '.neocities.org" target="_blank">' + website + '</a>'
                var processedRow = processAndDisplay(separated[1]);
                searchResults.innerHTML = processedRow;
                found = true;
                break;
            }
        }

        // If input text is not found, display a message
        if (!found) {
            searchResults.innerText = "No matching results found.";
        }
    })
    .catch(error => console.error('Error reading CSV:', error));
}

function searchCSVTags() {
    var searchText = document.getElementById("searchInput").value.trim().toLowerCase();
    var searchResults = document.getElementById("searchResults");
    var flavorText = document.getElementById("searchText");
    var searchLink = document.getElementById("searchLink");
    // Clear previous search results
    searchResults.innerHTML = "";
    flavorText.innerHTML = "";

    // Read the CSV file
    fetch("smalldata_taglist.csv")
    .then(response => response.text())
    .then(data => {
        // Split CSV data into rows
        var rows = data.split('\n');
        
        // Search for the input text in the first column of each row
        var found = false;
        for (var i = 0; i < rows.length; i++) {
            var separated = rows[i].split(/,(.*)/s);
            var firstColumn = separated[0].trim().toLowerCase();
            
            if (firstColumn === searchText) {
                flavorText.innerHTML = "<p>We found " + "pixels" + "!</p>";
                //searchLink.innerHTML = '<a href="https://' + website + '.neocities.org" target="_blank">' + website + '</a>'
                var processedRow = processAndDisplay(separated[1]);
                searchResults.innerHTML = processedRow;
                found = true;
                break;
            }
        }

        // If input text is not found, display a message
        if (!found) {
            searchResults.innerText = "No matching results found.";
        }
    })
    .catch(error => console.error('Error reading CSV:', error));
}