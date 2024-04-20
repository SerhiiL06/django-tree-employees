$(document).ready(function () {
    $('.see').click(function (event) {
        openFull();
    });

    function openFull() {
        $.ajax({
            url: '/tree/',
            method: 'GET',
            data: { 'full': 1 },
            success: function (data) {
                console.log('success')

                $('.root').html(data);
            },
            error: function (xhr, textStatus, errorThrown) {
                console.log('Помилка при виконанні Ajax запиту: ' + errorThrown);
            }
        });
    }
});
