const [toTheReg] = document.getElementsByClassName('to-the-reg');
const [toTheLogin] = document.getElementsByClassName('to-the-login');

toTheReg.addEventListener('click', async function() {
    window.location.href = '/registration';
})

toTheLogin.addEventListener('click', async function() {
    window.location.href = '/login';
})
