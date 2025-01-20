console.log(1)
function deleteItem(itemId) {
    $.ajax({
        url: '/admin/deleteItem',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({
            item_id: itemId
        }),
        success: function (response) {
            if (response.success) {
                console.log(response.message);
            } else {
                console.log("Ошибка: " + response.message);
            }
        },
        error: function (xhr, status, error) {
            console.log("Произошла ошибка при обновлении данных.");
            console.error('Error:', error);
        }
    });
}