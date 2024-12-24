document.querySelector('.get-values').onclick = Get_info;

function Get_info() {
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;
    var admin = document.getElementById('admin-code').value;
    console.log(username, password, admin)
    $.ajax({
        url: '/registration',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({ 'username': username, 'password': password, 'admin': admin }),
        success: function(response) {
            console.log('GOOD!')
        },
        error: function(error) {
            console.log(error);
        }
    });
}
