$(document).ready(function () {
    $('#clear-button').click(function () {
        clearFilters();
    });

    function clearFilters() {
        $.ajax({
            url: '/list/',
            method: 'GET',
            success: function (data) {
                $('#search-results').html($(data).find('#search-results').html());
                $('.pagination').html($(data).find('.pagination').html());
                $('#order-by-last').prop('checked', true);
                $('input[type="text"]').val('');
                $('input[type="date"]').val('');
            },
            error: function (xhr, textStatus, errorThrown) {
                console.log('Ajax error: ' + errorThrown);
            }
        });
    }
});


