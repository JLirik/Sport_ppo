const [submitButton] = document.getElementsByClassName('get-values');


submitButton.addEventListener('click', async function() {
    let username = document.getElementById('username').value;
    let password = document.getElementById('password').value;
    if (username && password) {
        $.ajax({
            url: '/Auth/login_check',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ 'username': username, 'password': password}),
            success: function(response) {
                console.log(response)
                if (response === 'Wrong login or password') {
                    document.getElementById('output').innerHTML = 'Неверный логин или пароль';
                }
                else if (response === 'Successfully logged in;0') {
                    window.location.href = '/user/main';
                }
                else if (response === 'Successfully logged in;1') {
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
