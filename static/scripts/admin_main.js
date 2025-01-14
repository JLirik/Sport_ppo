button = document.getElementsByClassName('create_report_button')[0]

button.addEventListener('click', function () {
        $.ajax({
            url: '/admin/create_report',
            type: 'GET',
            contentType: 'application/json',
            success: function(response) {
                console.log(response);
            },
            error: function(error) {
                console.log('Error');
            }
        });
})



