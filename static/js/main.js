function weight_data() {
    country = document.getElementById(`country_id1`).value
    higher_weight = 35
    var url = `company/`
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            'country': country,
            'weight': higher_weight,
        })
    })
        .then((response) => {
            response.json().then((data) => {
                data = data['data']
                html = `   <tr >
                                                                                            <th style="width:18% !important;">Logo</th>
                                                                                            <th style="width:18% !important;">Courier</th>
                                                                                            <th style="width:18% !important;">Service Type</th>
                                                                                            <th style="width:18% !important;">Transit Time</th>
                                                                                        <th style="width:18% !important;" >Rate</th>
                                                                                        </tr>
                                                                                        `
                for (var i = 0; i < data.length; i++) {
                    html += `
                                                                                    <tr >
                                                                                        <td style="width:20px; height: 20px !important;"><img src="${data[i].logo}" alt="Company logo" ></td>
                                                                                        <td style="width:18% !important;">${data[i].name} </td>
                                                                                        <td style="width:18% !important;">${data[i].type}</td>
                                                                                        <td style="width:18% !important;">${data[i].time}</td>
                                                                                        <td style="width:18% !important;">
                                                                                                <div >
                                                                                                        <button style="padding:0 !important;min-width: auto !important;  border: 1px solid black !important;  background-color: red; !important;" onclick='d2("${data[i].name}", ${data[i].price})' >${data[i].price} $</button> </div>
                                                                                                        </td> </tr>`
                }
                html2 = `<style>
                                                                table {
                                                                    border-collapse: collapse !important;
                                                                    border-spacing: 0 !important;
                                                                    padding: 0 !important;
                                                                    width: 90% !important;
                                                                }
                                                                tr,
                                                                th,
                                                                td {
                                                                    padding: 0;
                                                                }
                                                                tr:hover {
                                                                    background-color: coral !important;
                                                                }
                                                            </style>
                                                            <table id="tr" style=" display: inline-block !important; ">
                                                            `
                html2 += html
                document.getElementById('3div').innerHTML = html2
                //
            })
        })
}


function sherzamon() {
        country = document.getElementById(`country_id1`).value
        weight = document.getElementById(`weight`).value
        if (country != "" && weight != "") {
            weight_data()
            document.getElementById("1div").hidden = !document.getElementById("1div").hidden;
            // {#document.getElementById("2div").hidden = !document.getElementById("2div").hidden;#}
        } else {
            document.getElementById("text12").innerHTML = `<b style="color:red" >  Sizda qaysidir bo'lim to'ldirilmagan please</b>`
        }
    }


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









