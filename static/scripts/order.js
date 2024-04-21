$(document).ready(function () {

    $('.custom-control-input').change(function () {

        var selectedValue = $(this).val();

        var searchText = $('#search-input').val();
        var dateRange = $('#date-range').val();

        $.ajax({
            url: '/list/',
            method: 'GET',
            data: { 'order': selectedValue, 'search': searchText, 'date': dateRange },
            success: function (data) {
                $('#search-results').html($(data).find('#search-results').html());

            },
            error: function (xhr, textStatus, errorThrown) {
                console.log('Ajax error: ' + errorThrown);
            }
        });
    });
});
