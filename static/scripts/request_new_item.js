let table_request = document.getElementById('item-table');

table_request.addEventListener('click', async function(event) {
    let id = event.target.id;
    if (event.target.matches('button') && id) {
        $.ajax({
            url: '/User/send_new_item',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({
                'item_id': id
            }),
            success: function(response) {
                console.log(response);
                location.reload;
            },
            error: function(error) {
                console.log('Error!!!');
            }
        });
    }
});
