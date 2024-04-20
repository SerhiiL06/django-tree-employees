$(document).on('click', '#delete-button', function (event) {

    event.preventDefault();
    var emplId = $(this).val();
    var csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

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
            console.log('Помилка при відправці запиту: ' + errorThrown);

        }
    });
});

