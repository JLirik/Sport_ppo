$(document).ready(function () {
    $('.accept-btn').on('click', function () {
        const requestId = $(this).data('id');
        const status = $(this).data('status');
        sendRequest(requestId, 'accept', status);
    });

    $('.reject-btn').on('click', function () {
        const requestId = $(this).data('id');
        const status = $(this).data('status');
        sendRequest(requestId, 'reject', status);
    });

    function sendRequest(id, action, status) {
        $.ajax({
            url: '/admin/update_request_status',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({
                id: id,
                action: action,
                status: status
            }),
            success: function (response) {
                if (response.success) {
                    location.reload();
                    console.log(response.message || 'Запрос успешно обработан');
                } else {
                    console.log('Ошибка: ' + response.message);
                }
            },
            error: function (xhr, status, error) {
                console.log('Произошла ошибка при обработке запроса.');
                console.error('Ошибка:', error);
            }
        });
    }
});