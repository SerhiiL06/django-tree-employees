$(document).ready(function () {
    $('#full-button').click(function (event) {
        console.log("work")
        openFull();
    });

    function openFull() {
        $.ajax({
            url: '/tree/',
            method: 'GET',
            data: { 'full': 1 },
            success: function (data) {
                var toUpdate = $(data).filter("#update").first();
                $('#update').replaceWith(toUpdate);

            },
            error: function (xhr, textStatus, errorThrown) {
                console.log('Ajax error: ' + errorThrown);
            }
        });
    }
});