document.getElementById("convert").addEventListener("click",convertCheckboxValues)
hideSpinner();
const block3 = document.getElementById("report");
block3.style.display = "none";

function formatValue(value) {
  // Check if the value is a number before using toFixed
  return typeof value === 'number' ? value.toFixed(2) : value;
}

function showSpinner() {
    const spinner = document.querySelector('.spinner-border');
    spinner.style.display = 'inline-block';  // Show the spinner
}

function hideSpinner() {
    const spinner = document.querySelector('.spinner-border');
    spinner.style.display = 'none';  // Hide the spinner
}

function getCurrentTabUrl(callback) {  
    var queryInfo = {
      active: true, 
      currentWindow: true
    };
  
    chrome.tabs.query(queryInfo, function(tabs) {
      var tab = tabs[0]; 
      var url = tab.url;
      callback(url);
    });
}

function convertCheckboxValues(){
	const block1 = document.getElementById("output");
	const block2 = document.getElementById("output1");
	const block3 = document.getElementById("report");
	block1.style.display = "none";
	block2.style.display = "none";
	block3.style.display = "none";
    var values = [];
chrome.tabs.query({'active': true, 'windowId': chrome.windows.WINDOW_ID_CURRENT},
   function(tabs){
    values.push(tabs[0].url);
	showSpinner();  // Show spinner before fetching data
    buttonSend(values);
   });
}

function printData(data) {
    const resul1 = document.getElementById('output1');
    resul1.style.display = "block";

    let htmlContent = "";
    let statusContent = "";

    // Iterate over all entries in the data object
    Object.entries(data).forEach(([key, value]) => {
        // Check if the value is not zero
        if (value !== 0) {
            // Separate handling for "Autism Friendliness Status"
            if (key === "Autism Friendliness Status") {
                statusContent = "<strong>" + formatKey(key) + ":</strong> " + formatValue(value) + "<br />";
            } else {
                htmlContent += "<strong>" + formatKey(key) + ":</strong> " + formatValue(value) + "<br />";
            }
        }
    });

    // Append status content at the bottom with a space after all other data
    if (statusContent) {
        htmlContent += "<br />" + statusContent; // Adds a line space before the status
    }

    resul1.innerHTML = htmlContent;
    console.log(data);
    hideSpinner();
    document.getElementById('report').style.display = "block";  // Make sure this ID is correct
}



function formatKey(key) {
    // Convert camelCase or snake_case keys to readable text if necessary
    return key.replace(/([A-Z])/g, ' $1')  // Adds a space before capital letters
              .replace(/_/g, ' ')  // Replaces underscores with spaces
              .trim()  // Removes any leading/trailing whitespace
              .replace(/\b\w/g, l => l.toUpperCase());  // Capitalizes the first letter of each word
}

function formatValue(value) {
    // Format value, e.g., rounding numbers or converting to fixed decimal places
    return typeof value === 'number' ? value.toFixed(2) : value;
}

function buttonSend(values) {   
    const checkboxes = document.querySelectorAll('input[type="checkbox"]');
    const radioval = document.querySelectorAll('input[type="radio"]:checked'); // Select only the checked radio buttons
    
    checkboxes.forEach(checkbox => {
        values.push(checkbox.checked);
    });

    let radioValue = null;
    if (radioval.length > 0) {
        radioValue = radioval[0].value; // Assuming only one radio button can be selected at a time
    }

    var res="";
    const resul = document.getElementById('output');
    const resul1 = document.getElementById('output1');
    resul.textContent = JSON.stringify(values);

    // Construct the URL with the radio value included
    const url = `http://127.0.0.1:5000/scan?data1=${values[0]}&data2=${values[1]}&data3=${values[2]}&data4=${values[3]}&data5=${values[4]}&data6=${values[5]}&data7=${radioValue}`;

    fetch(url, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        },
    })
    .then(response => response.json())
    .then(data => printData(data))
    .catch(error => {
        hideSpinner();  // Hide spinner in case of an error
        console.error('Error:', error);
    });
}

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('report').addEventListener('click', function() {
        fetch('http://127.0.0.1:5000/generate_report', {
            method: 'POST', // Use POST method to send data to the backend
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({}) // You can pass data to the backend if needed
        })
        .then(response => {
            if (response.ok) {
                // Report generation successful
                console.log('Report generated successfully');
                
                // Extract the filename from the Content-Disposition header
                const filename = response.headers.get('Content-Disposition').split('=')[1];
                
                // Start downloading the file
                response.blob().then(blob => {
                    const url = window.URL.createObjectURL(blob);
                    const a = document.createElement('a');
                    a.href = url;
                    a.download = filename; // Set the filename for download
                    document.body.appendChild(a);
                    a.click();
                    window.URL.revokeObjectURL(url);
                });
            } else {
                // Report generation failed
                console.error('Report generation failed');
            }
        })
        .catch(error => {
            console.error('Error generating report:', error);
        });
    });
});

         
