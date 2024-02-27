document.addEventListener("DOMContentLoaded", function () {
    var tersisaElement = document.querySelectorAll('.tersisa');
    var tersisaValueInput = document.querySelectorAll('.tersisa_value');
    var btnPlus = document.querySelectorAll('.plus');
    var btnMinus = document.querySelectorAll('.minus');
    var jumlahTersisa = 0;

    function tambahJumlah() {
        jumlahTersisa++;
        updateTersisa();
    }

    function kurangJumlah() {
        if (jumlahTersisa > 0) {
            jumlahTersisa--;
            updateTersisa();
        }
    }

    function updateTersisa() {
        tersisaElement.forEach(function(sisa) {
            sisa.textContent = "Tersisa : " + jumlahTersisa;
            tersisaValueInput.value = jumlahTersisa;
        })
        
    }

    btnPlus.forEach(function(button) {
        button.addEventListener("click", function(event) {
            event.preventDefault();
            tambahJumlah();
        });
    });

    btnMinus.forEach(function(minus) {
        minus.addEventListener("click", function(event) {
            event.preventDefault();
            kurangJumlah();
        })
    });
});
