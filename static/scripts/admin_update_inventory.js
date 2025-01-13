function updateInventory(itemId) {
    const newName = $(`#name_${itemId}`).val();
    const newQuantity = $(`#quantity_${itemId}`).val();
    const newQuality = $(`#quality_${itemId}`).val();
    $.ajax({
        url: '/admin/update_inventory',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({
            item_id: itemId,
            name: newName,
            quantity: newQuantity,
            quality: newQuality
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