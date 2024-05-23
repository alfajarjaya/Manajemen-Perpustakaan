const btnShow = document.getElementById('btn-show');
btnShow.addEventListener('click', function () {
    const data = document.querySelector('.data');

    if (data == null) {
        if (!false) {
            const body = document.querySelector('.main');
            const dataNull = () => {
                return (
                    `
                        <div class="data-body">
                            <div class="data">
                                <h4>Tidak ada data</h4>
                            </div>
                        </div> 
                    `
                );
            };
            body.insertAdjacentHTML('beforeend', dataNull());
            true;
        } else {
            return null;
        }
    } else {
        const dataBody = document.querySelector('.data-body');
        dataBody.style.display = 'block';
    }
});