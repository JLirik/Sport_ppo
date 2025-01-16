let SubmitButton = document.getElementById('success');

SubmitButton.addEventListener('click', async function() {
    let name = document.getElementById('name').value;
    let price = document.getElementById('cost').value;
    let provider = document.getElementById('provider').value;
    if (name && price && provider) {
        $.ajax({
            url: '/admin/add_item',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({
                'name': name,
                'price': price,
                'provider': provider
            }),
            success: function(response) {
                window.location.href = "/admin/purchases";
            },
            error: function(error) {
                console.log(error);
            }
        });
    }

});
