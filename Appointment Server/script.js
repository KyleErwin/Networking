$(document).ready(function() {
    console.log("ready!");
    setInterval(setTime, 1);
});

function setTime() {
    var date = "";
    var time = "";
    var currentdate = new Date();

    if ($('#location').html() == "Las Angeles") {
        time = "" + (currentdate.getHours() - 9) + ":" + currentdate.getMinutes() + ":" + currentdate.getSeconds();

        date = "" + currentdate.getFullYear() + " - " + (currentdate.getMonth() + 1) + " - " + currentdate.getDate();
    }

    if ($('#location').html() == "London") {
        time = "" + (currentdate.getHours() - 2) + ":" + currentdate.getMinutes() + ":" + currentdate.getSeconds();

        date = "" + currentdate.getFullYear() + " - " + (currentdate.getMonth() + 1) + " - " + currentdate.getDate();
    }

    if ($('#location').html() == "Cape Town") {
        time = "" + currentdate.getHours() + ":" + currentdate.getMinutes() + ":" + currentdate.getSeconds();

        date = "" + currentdate.getFullYear() + " - " + (currentdate.getMonth() + 1) + " - " + currentdate.getDate();
    }

    if ($('#location').html() == "Johannesburg") {
        time = "" + currentdate.getHours() + ":" + currentdate.getMinutes() + ":" + currentdate.getSeconds();

        date = "" + currentdate.getFullYear() + " - " + (currentdate.getMonth() + 1) + " - " + currentdate.getDate();
    }

    if ($('#location').html() == "Hong Kong") {
        time = "" + (currentdate.getHours() + 6) + ":" + currentdate.getMinutes() + ":" + currentdate.getSeconds();

        date = "" + currentdate.getFullYear() + " - " + (currentdate.getMonth() + 1) + " - " + currentdate.getDate();
    }

    if ($('#location').html() == "Sydney") {
        time = "" + (currentdate.getHours() + 9) + ":" + currentdate.getMinutes() + ":" + currentdate.getSeconds();

        date = "" + currentdate.getFullYear() + " - " + (currentdate.getMonth() + 1) + " - " + currentdate.getDate();
    }

    $('#time').html(time);
    $('#date').html(date);

    time = "" + currentdate.getHours() + ":" + currentdate.getMinutes() + ":" + currentdate.getSeconds();

    date = "" + currentdate.getFullYear() + " - " + (currentdate.getMonth() + 1) + " - " + currentdate.getDate();
    
    $('#staticJohannesburgTime').html(time);
}
