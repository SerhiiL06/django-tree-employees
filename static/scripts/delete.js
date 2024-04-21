$(document).on('click', '#delete-button', function (event) {

    event.preventDefault();
    var emplId = $(this).val();
    console.log(emplId)
    var csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    console.log(csrftoken)
    $.ajax({
        type: 'POST',
        url: '/list/' + emplId + '/delete/',
        data: {
            'pk': emplId,
            csrfmiddlewaretoken: csrftoken,
        },
        success: function (data) {
            $('#search-results').html($(data).find('#search-results').html());
            $('.pagination').html($(data).find('.pagination').html());
        },
        error: function (xhr, textStatus, errorThrown) {
            console.log('Ajax error: ' + errorThrown);

        }
    });
});
