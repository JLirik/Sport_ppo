document.addEventListener('DOMContentLoaded', () => {
    const acceptButtons = document.querySelectorAll('.accept-btn');
    const rejectButtons = document.querySelectorAll('.reject-btn');

    const updateRequestStatus = (id, action) => {
        fetch('/admin/update_request_status', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ id: id, action: action }),
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('Статус обновлён успешно');
                location.reload();
            } else {
                alert(`Ошибка: ${data.message}`);
            }
        })
        .catch(error => alert('Ошибка при обновлении статуса.'));
    };

    acceptButtons.forEach(button => {
        button.addEventListener('click', () => {
            const id = button.getAttribute('data-id');
            updateRequestStatus(id, 'accept');
        });
    });

    rejectButtons.forEach(button => {
        button.addEventListener('click', () => {
            const id = button.getAttribute('data-id');
            updateRequestStatus(id, 'reject');
        });
    });
});
