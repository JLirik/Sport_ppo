document.querySelector('.get-values').onclick = Get_info;

function encryptPassword(password) {
    let encryptedPassword = "";
    let alphabet = "abcdefghijklmnopqrstuvwxyz";
    for (let i = 0; i < password.length; i++) {
        encryptedPassword += alphabet[i % alphabet.length] + "2" + password[i];
    }
    return encryptedPassword.split("").reverse().join("");
}

function decryptPassword(encryptedPassword) {
    let decryptedPassword = "";
    let reversedEncryptedPassword = encryptedPassword.split("").reverse().join("");
    for (let i = 0; i < reversedEncryptedPassword.length; i += 3) {
        decryptedPassword += reversedEncryptedPassword[i + 2];
    }
    return decryptedPassword;
}

function Get_info() {
    let username = document.getElementById('username').value;
    let password = encryptPassword(document.getElementById('password').value);
    let admin = document.getElementById('admin-code').value;
    if (username && password) {
        $.ajax({
            url: '/Auth/reg_check',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ 'username': username, 'password': password, 'admin': admin }),
            success: function(response) {
                console.log('GOOD!');
                console.log(response);
                document.getElementById('output').innerHTML = response;
            },
            error: function(error) {
                console.log(error);
            }
        });
    }
}
