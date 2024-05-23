const script = document.createElement("script");
script.src = "/static/modules/sweetalert.js";
document.head.appendChild(script);

script.onload = () => {
    const btnRemove = document.querySelectorAll(".btn-remove");

    btnRemove.forEach((button) => {
        button.addEventListener("click", (event) => {
            let tableName = button.getAttribute("data-name");

            Swal.fire({
                title: "Apakah kamu yakin",
                text: `Ingin menghapus Tabel ${tableName} ?`,
                icon: "warning",
                showCancelButton: true,
                confirmButtonColor: "#3085d6",
                cancelButtonColor: "#d33",
                confirmButtonText: "Yes",
            }).then((result) => {
                if (result.isConfirmed) {
                    const xhr = new XMLHttpRequest();
                    xhr.open("POST", "/remove_table", true);
                    xhr.setRequestHeader("Content-Type", "application/json");
                    xhr.onload = () => {
                        if (xhr.status === 200) {
                            let tableRow = event.target.closest(".t-row");
                            tableRow.parentNode.removeChild(tableRow);
                            Swal.fire({
                                title: "Berhasil!",
                                text: `Tabel " ${tableName} " berhasil di hapus.`,
                                icon: "success",
                            });
                        } else {
                            Swal.fire({
                                title: "Error!",
                                text: `Gagal menghapus tabel ${tableName}.`,
                                icon: "error",
                            });
                        }
                    };
                    xhr.send(JSON.stringify({ tableName: tableName }));
                }
            });
        });
    });
};
