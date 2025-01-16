let SubmitButton = document.getElementById('success');
SubmitButton.addEventListener('click', async function() {
    let name = document.getElementById('name').value;
    let quality = document.getElementById('quality').value;
    let count = document.getElementById('count').value;
    if (name && quality) {
        $.ajax({
            url: '/admin/main_add_item_to_db',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({
                'name': name,
                'quality' : quality,
                'count' : count
            }),
            success: function(response) {
                console.log(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    }

});
