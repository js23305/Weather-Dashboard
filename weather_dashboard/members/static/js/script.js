function weather_result(event) {
    event.preventDefault();
    let userInput = document.getElementById("userInput").value.trim();
    if (userInput.length == "") {
        alert("Please enter a city name");
        return;
    }
    
    var formData = new FormData()
    formData.append('city', userInput)
    

    $.ajax(
        {
            url: "/weather_api/",
            type: "POST",
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                alert("Message sent successfully")
            },
            error: function(error) {
                alert("Message not sent")

            }
        }
    )

    return false;
}