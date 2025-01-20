function deleteItem(itemId) {
    $.ajax({
        url: '/admin/delete_item',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({
            item_id: itemId,
        }),
        success: function (response) {
            console.log(response.message);
            window.location.href = "/admin/main";
        },
        error: function (xhr, status, error) {
            console.log("Произошла ошибка при обновлении данных.");
            console.error('Error:', error);
        }
    });
}