// function to get url from the url form button
async function handleSubmit(event) {
    event.preventDefault(); // Prevent the form from submitting normally
    
    const inputValue = document.getElementById('inputField').value;
    
    const data = {
        url : inputValue
    };
    console.log(data)

    fetch("../../scrape", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
      })
      .then(response => response.json())
      .then(result => console.log(result))
      .catch(error => console.error('Error:', error));
       

    
    return false; // Prevent the form from submitting
}

