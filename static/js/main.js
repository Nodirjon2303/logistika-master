


function share_all_data() {
    country = document.getElementById(`country_id`).value
    length = document.getElementById(`length`).value
    width = document.getElementById(`width`).value
    height = document.getElementById(`height`).value
    var url = `/change/`
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            'weight': higher_weight,
            'country': country,
            'length': length,
            'width': width,
            'height': height,

        })
    })
        .then((response) => {
            response.json().then((data) => {
                data = data['data']
            })
        })
}









