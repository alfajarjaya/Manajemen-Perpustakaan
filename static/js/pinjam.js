document.addEventListener("DOMContentLoaded", function () {
    var submitButton = document.getElementById("to-pinjam-user");
    var form = document.getElementById("pinjam-form");
    var dataContainer = document.getElementById("value-data");

    // Load data from local storage on page load
    // loadOldData();

    submitButton.addEventListener("click", function () {
        var nama = document.getElementById("nama").value;
        var kelas = document.getElementById('kelas').value;
        var pinjam = document.getElementById("pinjam").value;
        var kembali = document.getElementById("kembali").value;

        if (!nama || !kelas || !pinjam || !kembali) {
            alert('Input Harus di isi');
        } else {
            return false
            // var newDiv = document.createElement("div");
            // newDiv.classList.add("data");
            // newDiv.innerHTML =
            //     "<h6>" + nama + "</h6><h6>" + pinjam + "</h6><h6>" + kembali + "</h6>";

            // dataContainer.insertBefore(newDiv, dataContainer.firstChild);

            // // Save data to local storage
            // saveDataToLocalStorage();

            // form.reset();
        }
    });
});

//     function loadOldData() {
//         // Retrieve data from local storage
//         var storedData = JSON.parse(localStorage.getItem("formData"));

//         if (storedData) {
//             // Recreate div elements from stored data
//             storedData.forEach(function (data) {
//                 var newDiv = document.createElement("div");
//                 newDiv.classList.add("data");
//                 newDiv.innerHTML =
//                     "<h6>" + data.nama + "</h6><h6>" + data.pinjam + "</h6><h6>" + data.kembali + "</h6>";

//                 dataContainer.appendChild(newDiv);
//             });
//         }
//     }

//     function saveDataToLocalStorage() {
//         // Get existing data from local storage
//         var existingData = JSON.parse(localStorage.getItem("formData")) || [];

//         // Add new data to the existing data
//         existingData.unshift({ nama: nama, pinjam: pinjam, kembali: kembali });

//         // Save the updated data back to local storage
//         localStorage.setItem("formData", JSON.stringify(existingData));
//     }
// });
