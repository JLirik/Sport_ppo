const [SubmitButton] = document.getElementById('success');


SubmitButton.addEventListener('click', async function() {
    let name = document.getElementByName('name').value;
    let cost = document.getElementByName('cost').value;
    let provider = document.getElementByName('provider').value;
    if (name && cost && provider) {
        $.ajax({
            url: '/admin/add_item',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({
                'name': name,
                'cost': cost,
                'provider': provider
            }),
            success: function(response) {
                console.log(response);
            }
            error: function(error) {
                console.log(error);
            }
        });
    }

});
