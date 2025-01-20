let SubmitButton = document.getElementById('success');
SubmitButton.addEventListener('click', async function() {
    let name = document.getElementById('name').value;
    let count = document.getElementById('count').value;
    let quality = document.getElementById('quality-select').value;
    let qual_list = ['Новый', 'Сломанный'];

    if (name && count && qual_list.includes(quality)) {
        $.ajax({
            url: '/admin/main_add_item_to_db',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({
                'name': name,
                'quality': quality,
                'count' : count
            }),
            success: function(response) {
                console.log(response);
                window.location.href = "/admin/main_add_item";
            },
            error: function(error) {
                console.log(error);
            }
        });
    }

});
