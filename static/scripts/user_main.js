let table_request = document.getElementById('item-table');

table_request.addEventListener('click', async function(event) {
    let item = event.target.id;
    if (item) {
        console.log(item);
        $.ajax({
            url: '/User/fix_item',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({
                'item_id': item
            }),
            success: function(response) {
                console.log(response);
                console.log('G))D!');
                window.location.href = '/user/main';
            },
            error: function(error) {
                console.log('Error (:/)');
            }
        });
    }
});
