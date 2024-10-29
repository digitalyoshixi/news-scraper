// function to get url from the url form button


function sendUrl(){
  const inputdata = document.getElementById("inputField").value;
  const formdata = new FormData();
  formdata.append("url", inputdata); 
  console.log(formdata);
  // validate the data

  // send this as a request to backend
  fetch("http://localhost:5500/scrape", {
    method : "POST",
    body : formdata
  }).catch(error => {
    console.error("Error:", error);
  });

}

