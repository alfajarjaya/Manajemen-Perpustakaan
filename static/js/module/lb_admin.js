const script = document.createElement("script");
script.src = "/static/modules/sweetalert.js";
document.head.appendChild(script);

script.onload = () => {
    const editButtonsDesktop = document.querySelectorAll(".LB-Desktop .btn");
    const editButtonsMobile = document.querySelectorAll(".LB-Mobile .btn");
    const myAlert = document.getElementById("myAlert");

    const namaBukuInput = document.getElementById("nama_buku_input");
    const namaBuku = document.getElementById("nama_buku");
    const bookIdInput = document.getElementById("book_id");
    const sisaBukuInput = document.getElementById("sisa_buku");
    const sisaBukuAttribute = document.getElementById("sisa");
    const penerbitBukuTag = document.getElementById("penerbit");
    const cancelBtn = document.querySelector("#btn-cancel");

    cancelBtn.addEventListener("click", () => {
        myAlert.style.display = "none";
        bookIdInput.value = "";
        namaBukuInput.value = "";
        namaBuku.innerText = "";
        penerbitBukuTag.innerText = "";
        sisaBukuAttribute.innerText = "";
        sisaBukuInput.value = "";
    });

    for (const button of editButtonsDesktop) {
        button.addEventListener("click", (event) => {
            const clickedButton = event.currentTarget;
            const bookId = clickedButton.getAttribute("data-book-id");
            const bookName = clickedButton.getAttribute("data-book-name");
            const authorName = clickedButton.getAttribute("data-book-author");
            const sisa = clickedButton
                .closest(".list")
                .querySelector('[name="sisa_buku_input"]').value;

            Swal.fire({
                title: "Ubah sisa buku",
                html: ` ID Buku: ${bookId}<br>
                        Judul Buku: ${bookName}<br>
                        Penerbit: ${authorName}<br>
                        Sisa Buku saat ini: ${sisa}`,
                input: "number",
                inputAttributes: {
                    min: 1,
                },
                icon: "info",
                showCancelButton: true,
                confirmButtonText: "Ubah",
                cancelButtonText: "Batal",
                inputValidator: (value) => {
                    if (!value || value < 0) {
                        return "Input tidak boleh kosong atau kurang dari 0!";
                    }
                },
            }).then((result) => {
                if (result.isConfirmed) {
                    const newCount = result.value;
                    if (newCount !== null) {
                        NewCount(bookId, bookName, newCount);
                    }
                }
            });
        });
    }

    for (const button of editButtonsMobile) {
        button.addEventListener("click", (event) => {
            const clickedButton = event.currentTarget;
            const bookId = clickedButton.getAttribute("data-book-id");
            const bookName = clickedButton.getAttribute("data-book-name");
            const authorName = clickedButton.getAttribute("data-book-author");
            const sisa = clickedButton
                .closest(".list")
                .querySelector('[name="sisa_buku_input"]').value;
            Swal.fire({
                title: "Ubah sisa buku",
                html: ` ID Buku: ${bookId}<br>
                            Judul Buku: ${bookName}<br>
                            Penerbit: ${authorName}<br>
                            Sisa Buku saat ini: ${sisa}`,
                input: "number",
                inputAttributes: {
                    min: 1,
                },
                icon: "info",
                showCancelButton: true,
                confirmButtonText: "Ubah",
                cancelButtonText: "Batal",
                inputValidator: (value) => {
                    if (!value || value < 0) {
                        return "Input tidak boleh kosong atau kurang dari 0!";
                    }
                },
            }).then((result) => {
                if (result.isConfirmed) {
                    const newCount = result.value;
                    if (newCount !== null) {
                        NewCount(bookId, bookName, newCount);
                    }
                }
            });
        });
    }
};

function NewCount(bookId, bookName, newCount) {
    const xhr = new XMLHttpRequest();
    xhr.open("POST", "/updateBookCount", true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = () => {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            const response = JSON.parse(xhr.responseText);
            if (xhr.status === 200) {
                Swal.fire({
                    title: "Berhasil",
                    text: response.message,
                    icon: "success",
                    showCancelButton: false,
                    confirmButtonColor: "#3085d6",
                    cancelButtonColor: "#d33",
                    confirmButtonText: "Oke"
                }).then((result) => {
                    if (result.isConfirmed) {
                        Swal.fire({
                            text: "Mohon Tunggu Halaman sedang di reload",
                            confirmButtonText: "Oke",
                            icon: "warning"
                        });
                        window.location.reload();
                    }
                });
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
    const data = JSON.stringify({
        bookId: bookId,
        nama: bookName,
        newCount: newCount,
    });
    xhr.send(data);
}
