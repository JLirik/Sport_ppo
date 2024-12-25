const [submitButton] = document.getElementsByClassName('get-values');


submitButton.addEventListener('click', async function() {
    let username = document.getElementById('username').value;
    let password = document.getElementById('password').value;
    let admin = document.getElementById('admin-code').value;
    if (username && password) {
        $.ajax({
            url: '/Auth/reg_check',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ 'username': username, 'password': password, 'admin': admin }),
            success: function(response) {
                if (response === 'This user already exists') {
                    document.getElementById('output').innerHTML = 'Это имя пользователя уже занято';
                }
                else if (response === 'Successfully registered;0') {
                    window.location.href = '/user/main';
                }
                else if (response === 'Successfully registered;1') {
                    window.location.href = '/admin/main';
                }
                else {
                    document.getElementById('output').innerHTML = 'Возникла неизвестная ошибка';
                }

            },
            error: function(error) {
                document.getElementById('output').innerHTML = 'Возникла ошибка:' + error;
            }
        });
    }
});
