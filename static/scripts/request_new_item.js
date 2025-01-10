let table_request = document.getElementById('item-table');

table_request.addEventListener('click', async function(event) {
    let id = event.target.id;
    if (event.target.matches('button') && id) {
        let input = document.getElementById('input-'+id);
        let value = parseInt(input.value, 10);
        if (0 < value && value < parseInt(input.max, 10)) {
            console.log(value);
        }
    }
});
