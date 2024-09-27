
const name = document.querySelector(".name")
console.log("HELLO");

function handleSubmit(event) {
    event.preventDefault(); // Prevent the form from submitting normally
    
    const inputValue = document.getElementById('inputField').value;
    console.log('Form submitted with value:', inputValue);
    
    // Add your custom logic here
    
    return false; // Prevent the form from submitting
}

