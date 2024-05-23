const script = document.createElement("script");
script.src = "/static/modules/sweetalert.js";
document.head.appendChild(script);

script.onload = () => {
    const btnDetails = document.querySelectorAll(".btn-details");
    btnDetails.forEach((btn) => {
        btn.addEventListener("click", () => {
            let info = btn.getAttribute("data-info");
            info = info.slice(1, -1);

            const arrayForInfo = info
                .split(",")
                .map((item) => item.trim().replace(/'/g, ""));

            let dataPinjamUser = document.querySelector(".data-pinjam-user");
            dataPinjamUser.innerHTML = "";

            dataPinjamUser.innerHTML = `
            <div class="desc">
                <h3>Informasi Peminjaman</h3>
                <hr>
                <p>ID Peminjaman : <span class="id">${arrayForInfo[0]}</span></p>
                <p>ID Buku : <span>${arrayForInfo[1]}</span></p>
                <p>Judul Buku : <span>${arrayForInfo[2]}</span></p>
                <p>Nama : <span class="nam">${arrayForInfo[3]}</span></p>
                <p>Kelas : <span>${arrayForInfo[4]}</span></p>
                <p>NISN : <span>${arrayForInfo[5]}</span></p>
                <p>Tgl Pinjam : <span>${arrayForInfo[6]}</span></p>
                <p>Tgl Kembali : <span>${arrayForInfo[7]}</span></p>
            </div>
            `;

            Swal.fire({
                title: "Informasi Peminjaman",
                html: dataPinjamUser.outerHTML,
                icon: "info",
                showCancelButton: true,
                cancelButtonText: "Cancel",
                cancelButtonColor: "green",
                showConfirmButton: true,
                confirmButtonText: "Remove",
                confirmButtonColor: "red",
                focusCancel: true,
                focusConfirm: false,
                buttonsStyling: true,
            }).then((result) => {
                if (result.isConfirmed) {
                    const name = document.querySelector("p .nam").textContent;
                    const id = document.querySelector("p .id").textContent;

                    Swal.fire({
                        title: "Apakah kamu yakin",
                        text: `Ingin menghapus Data dari  ${name} dengan ID peminjaman ${id} ?`,
                        icon: "warning",
                        showCancelButton: true,
                        confirmButtonColor: "red",
                        cancelButtonColor: "green",
                        confirmButtonText: "Yes",
                    }).then((res) => {
                        if (res.isConfirmed) {
                            const xhr = new XMLHttpRequest();

                            xhr.open("POST", "/remove_data", true);
                            xhr.setRequestHeader("Content-Type", "application/json");
                            xhr.onload = () => {
                                if (xhr.status === 200) {
                                    const response = JSON.parse(xhr.responseText);
                                    Swal.fire({
                                        text: response.message,
                                        icon: "success",
                                        confirmButtonText: "OKE",
                                    }).then(res => {
                                        if (res.isConfirmed) {
                                            window.location.reload();
                                        } else {
                                            const toats = Swal.mixin({
                                                toast: true,
                                                confirmButtonText: false,
                                                timerProgressBar: true,
                                                timer: 1000,

                                                didOpen: (toast) => {
                                                    toast.onmouseenter = Swal.stopTimer;
                                                    toast.onmouseleave = Swal.resumeTimer;
                                                },
                                                
                                            });
                                            toats.fire({
                                                icon: "warning",
                                                title: "Tunggu, Halaman sedang di reload"
                                            });
                                            setTimeout(() => {
                                                window.location.reload();
                                            }, 1000);
                                        }
                                    });
                                } else {
                                    Swal.fire({
                                        text: response.message,
                                        icon: "error",
                                        confirmButtonText: "OKE",
                                    });
                                }
                            };

                            xhr.send(
                                JSON.stringify({
                                    name: name,
                                    id: id,
                                })
                            );
                        }
                    });
                }
            });
        });
    });
};
