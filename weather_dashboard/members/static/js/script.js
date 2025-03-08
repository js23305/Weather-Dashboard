function weather_result(uid, city) {
    var formData = new FormData()
    formData.append('uid', uid)
    formData.append('city', city)
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