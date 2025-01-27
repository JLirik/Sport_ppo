button = document.getElementsByClassName('create_report_button')[0]
button.addEventListener('click', function () {
        fetch('/admin/create_report')
                .then(response => response.blob())
                .then(blob => {
                    const url = window.URL.createObjectURL(blob);
                    const a = document.createElement('a');
                    a.style.display = 'none';
                    a.href = url;
                    a.download = 'data.xlsx';
                    a.click();
                    window.URL.revokeObjectURL(url);
                })
                .catch(error => console.error('Error downloading the file:', error));
})



