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
//                location.reload;
                document.getElementById(id).remove();
                const cur_div = document.getElementById('div-' + id);
                const new_text = document.createElement('p');
                new_text.style = ''
                new_text.textContent = 'Вы сделали заказ.\n Сейчас ваша заявка на рассмотрении';
                cur_div.appendChild(new_text)
            },
            error: function(error) {
                console.log('Error!!!');
            }
        });
    }
});
