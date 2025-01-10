$(document).ready(function() {
    const updateRequestStatus = (id, action) => {
        $.ajax({
            url: '/admin/update_request_status',
            method: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ id: id, action: action }),
            success: function(data) {
                if (data.success) {
                    alert('Статус обновлён успешно');
                    location.reload();
                } else {
                    alert(`Ошибка: ${data.message}`);
                }
            },
            error: function() {
                alert('Ошибка при обновлении статуса.');
            }
        });
    };

    $('.accept-btn').on('click', function() {
        const id = $(this).data('id');
        updateRequestStatus(id, 'accept');
    });

    $('.reject-btn').on('click', function() {
        const id = $(this).data('id');
        updateRequestStatus(id, 'reject');
    });
});
