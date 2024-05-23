const script = document.createElement("script");
script.src = "/static/modules/sweetalert.js";
document.head.appendChild(script);

script.onload = () => {
    const checkboxes = document.querySelectorAll(".check");
    checkboxes.forEach(function (checkbox) {
        checkbox.addEventListener("click", function () {
            const value = this.checked ? this.value : "false";
            return value;
        });
    });

    const arrayCheckId = [];
    const arrayCheckName = [];

    const btnHref = document.getElementById("btnHref");
    btnHref.addEventListener("click", () => {
        arrayCheckId.length = 0;
        arrayCheckName.length = 0;

        checkboxes.forEach((checkbox) => {
            if (checkbox.checked) {
                const checked = checkbox.value;
                const parts = checked.split("'");
                const id_peminjaman =checkbox.getAttribute('data-index');

                const nama = parts[3];

                arrayCheckId.push(id_peminjaman);
                arrayCheckName.push(nama);
            }
        });

        if (arrayCheckId.length === 0) {
            const Toast = Swal.mixin({
                toast: true,
                position: "top-end",
                showConfirmButton: false,
                timer: 3000,
                timerProgressBar: true,
                didOpen: (toast) => {
                    toast.onmouseenter = Swal.stopTimer;
                    toast.onmouseleave = Swal.resumeTimer;
                },
            });
            Toast.fire({
                icon: "warning",
                title: "Mohon pilih salah satu data yang ingin dihapus!",
            });
        } else {
            const arrayCheckString = arrayCheckName.join(", ");

            Swal.fire({
                title: "Are you sure?",
                text: `Apakah kamu yakin ingin menghapus data pengunjung dari ${arrayCheckString} ?`,
                icon: "warning",
                showCancelButton: true,
                cancelButtonColor: "#d33",
                buttonsStyling: "red",
            }).then((result) => {
                if (result.isConfirmed) {
                    arrayCheckId.forEach((id) => {
                        removeData(id, arrayCheckString);
                    });
                }
            });
        }
    });
};

function removeData(id, name) {
    const xhr = new XMLHttpRequest();
    xhr.open("POST", "/remove_data_pengunjung", true);
    xhr.setRequestHeader("Content-Type", "application/json");

    xhr.onreadystatechange = () => {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            const response = JSON.parse(xhr.responseText);
            if (xhr.status === 200) {
                Swal.fire({
                    text: response.message,
                    icon: "success",
                    confirmButtonText: "OKE",
                }).then((result) => {
                    if(result.isConfirmed) {
                        window.location.reload();
                    } else {
                        const toats = Swal.mixin({
                            toast: true,
                            confirmButtonText: false,
                            timerProgressBar: true,
                            timer: 3000,

                            didOpen: (toast) => {
                                toast.onmouseenter = Swal.stopTimer;
                                toast.onmouseleave = Swal.resumeTimer;
                            },
                        });
                        toats.fire({
                            icon: "warning",
                            title: `Berhasil menghapus data ${name}`,
                            text: "Tunggu, Halaman sedang di reload"
                        });
                        setTimeout(() => {
                            window.location.reload();
                        }, 3000);
                    }
                })
            } else {
                Swal.fire({
                    title: "Gagal",
                    text: response.message,
                    icon: "error",
                    showCancelButton: false,
                    confirmButtonColor: "#3085d6",
                    cancelButtonColor: "#d33",
                    confirmButtonText: "Oke"
                });
            }
        }
    };
    xhr.send(JSON.stringify({ id: id , name: name}));
}
