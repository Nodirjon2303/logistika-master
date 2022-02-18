$.ajax({
                                                                type: "POST",
                                                                url: 'change/',
                                                                data: {
                                                                    'country_id': $("#country_id")
                                                                    .val(),
                                                                    'weight': higher_weight
                                                                },
                                                                success: function (data, text) {
                                                                    try {
                                                                        JSON.parse(data);
                                                                    } catch (e) {
                                                                        toastr.error(
                                                                            "No data exists");
                                                                        $("#spinner").hide();
                                                                        return;
                                                                    }
                                                                    if (data == '' || typeof data ==
                                                                        'undefined' || data == '[]'
                                                                        ) {
                                                                        $("#courier_content_id")
                                                                            .html("");
                                                                        toastr.error(
                                                                            "No data exists");
                                                                        $("#spinner").hide();
                                                                        return;
                                                                    }
                                                                    var obj = eval(data);
                                                                    courier_content =
                                                                        '<div class="table1">';
                                                                    for (i = 0; i < obj
                                                                        .length; i++) {
                                                                        country_id = obj[i]
                                                                            .country_id;
                                                                        country_name = obj[i]
                                                                            .country_name;
                                                                        courier_id = obj[i]
                                                                            .courier_id;
                                                                        courier_name = obj[i]
                                                                            .courier_name;
                                                                        file_picture =
                                                                            "https://takeandship.com/tns/public/" +
                                                                            obj[i].file_picture;
                                                                        edt_id = obj[i].edt_id;
                                                                        edt_name = obj[i].edt_name;
                                                                        id = obj[i].id;
                                                                        kg = obj[i].kg;
                                                                        service_type_id = obj[i]
                                                                            .service_type_id;
                                                                        service_type_name = obj[i]
                                                                            .service_type_name;
                                                                        rate = obj[i].rate;
                                                                        if (i == 0) {
                                                                            courier_content =
                                                                                courier_content +
                                                                                '<div id="header" class="row1"><div class="cell1"><b>Courier</b></div><div class="cell1"><b>Service Type</b></div><div class="cell1"><b>Transit Time</b></div><div class="cell1"><b>Rate</b></div></div>';
                                                                        }
                                                                        courier_content =
                                                                            courier_content +
                                                                            '<div class="row1"><div class="cell1"><img src="' +
                                                                            file_picture +
                                                                            '" style="width:100px;height:100px;"></div><div class="cell1"><span class="' +
                                                                            service_type_name +
                                                                            '">' +
                                                                            service_type_name +
                                                                            '</span></div><div class="cell1"><span class="shipping_time">' +
                                                                            edt_name +
                                                                            '</span></div><div class="cell1"><b>' +
                                                                            rate +
                                                                            ' USD</b></div></div>';
                                                                    }
                                                                    courier_content =
                                                                        courier_content + '</div>';
                                                                    $("#courier_content_id").html(
                                                                        courier_content);
                                                                    //store_html = $(".customer-login-block").html();
                                                                    //$(".customer-login-block").html(courier_content);
                                                                    $("#spinner").hide();
                                                                    //$("#input_form").hide();
                                                                    $("#result_id").show();
                                                                },
                                                                error: function (request, status,
                                                                error) {
                                                                    $("#spinner").hide();
                                                                }
                                                            });