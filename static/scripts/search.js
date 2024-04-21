$(document).ready(function () {
    $('#search-button').click(function () {
        performSearch();
    });

    function performSearch() {
        var searchText = $('#search-input').val();

        var dateRange = $('#date-range').val();

        var selectedValue = $('.custom-control-input').val();

        $.ajax({
            url: '/list/',
            method: 'GET',
            data: { 'order': selectedValue, 'search': searchText, 'date': dateRange },
            success: function (data) {
                $('#search-results').html($(data).find('#search-results').html());
                $('.pagination').html($(data).find('.pagination').html());
            },
            error: function (xhr, textStatus, errorThrown) {
                console.log('Ajax error: ' + errorThrown);
            }
        });
    }
});