const script = document.createElement("script");
script.src = "/static/modules/sweetalert.js";
document.head.appendChild(script);

const emailjsScript = document.createElement("script");
emailjsScript.src = "https://cdn.emailjs.com/dist/email.min.js";
document.head.appendChild(emailjsScript);

script.onload = () => {
    emailjsScript.onload = () => {
        emailjs.init("-7k1PYuT2Y3Tzfi0d");

        const pinjamButtonsDesktop = document.querySelectorAll(".LB-Desktop .btn");
        const pinjamButtonsMobile = document.querySelectorAll(".LB-Mobile .btn");
        const myAlert = document.querySelector(".overlay");

        const namaBukuInp = document.getElementById("nama_buku_input");
        const namaBukuTag = document.getElementById("nama_buku");

        const bookIdInp = document.getElementById("book_id");

        const sisaBukuAtt = document.getElementById("sisa");

        const penerbitBukuTagHtml = document.getElementById("penerbit");

        let globalSisa;

        pinjamButtonsDesktop.forEach((button, index) => {
            button.addEventListener("click", () => {
                myAlert.style.display = "block";
                const bookId = button.getAttribute("data-book-id");
                const bookName = button.getAttribute("data-book-name");
                const authorName = button.getAttribute("data-book-author");
                const sisa = button
                    .closest(".list")
                    .querySelector('[name="sisa_buku_input"]').value;

                bookIdInp.value = bookId;
                namaBukuInp.value = bookName;
                namaBukuTag.innerText = "Judul : " + bookName;
                penerbitBukuTagHtml.innerText = "Penerbit : " + authorName;
                sisaBukuAtt.innerText = "Sisa : " + sisa;

                globalSisa = sisa;
            });
        });

        pinjamButtonsMobile.forEach((button, index) => {
            button.addEventListener("click", () => {
                myAlert.style.display = "block";
                const bookId = button.getAttribute("data-book-id");
                const bookName = button.getAttribute("data-book-name");
                const authorName = button.getAttribute("data-book-author");
                const sisa = button
                    .closest(".list")
                    .querySelector('[name="sisa_buku_input"]').value;

                bookIdInp.value = bookId;
                namaBukuInp.value = bookName;
                namaBukuTag.innerText = "Judul : " + bookName;
                penerbitBukuTagHtml.innerText = "Penerbit : " + authorName;
                sisaBukuAtt.innerText = "Sisa : " + sisa;

                globalSisa = sisa;
            });
        });

        const cancelBtn = document.querySelector("#btn-cancel");
        cancelBtn.addEventListener("click", () => {
            myAlert.style.display = "none";
        });

        const btnPinjam = document.getElementById("btn-pinjam");
        const namaClient = document.getElementById("nama");
        const kelasClient = document.getElementById("kelas");
        const nisnClient = document.getElementById("NISN");
        const tglPinjam = document.getElementById("pinjam");

        btnPinjam.addEventListener("click", () => {
            const bookId = bookIdInp.value;
            const bookName = namaBukuInp.value;
            const nama = namaClient.value;
            const kelas = kelasClient.value;
            const nisn = nisnClient.value;
            const tglValue = tglPinjam.value;
            const newCount = globalSisa;

            sendToServer(bookId, bookName, newCount, nama, kelas, nisn, tglValue);
        });

        function sendToServer(
            bookId,
            bookName,
            newCount,
            nama,
            kelas,
            nisn,
            tglPinjam
        ) {
            if (newCount !== null) {
                const xhr = new XMLHttpRequest();
                xhr.open("POST", "/pinjamBuku", true);
                xhr.setRequestHeader("Content-Type", "application/json");
                xhr.onreadystatechange = () => {
                    if (xhr.readyState === XMLHttpRequest.DONE) {
                        const response = JSON.parse(xhr.responseText);
                        if (xhr.status === 200) {
                            sendToEmailJS(bookId, bookName, newCount, nama, kelas, nisn, tglPinjam);
                            Swal.fire({
                                title: "Berhasil",
                                text: response.message,
                                icon: "success",
                                showCancelButton: false,
                                confirmButtonColor: "#3085d6",
                                cancelButtonColor: "#d33",
                                confirmButtonText: "Oke",
                            }).then((result) => {
                                if (result.isConfirmed) {
                                    Swal.fire({
                                        text: "Mohon Tunggu Halaman sedang di reload.",
                                        icon: "warning",
                                        showConfirmButton: false,
                                    });
                                    window.location.reload();
                                } else {
                                    const Toats = Swal.mixin({
                                        showConfirmButton: false,
                                        timerProgressBar: true,
                                        timer: 2000,
                                    });
                                    Toats.fire({
                                        icon: "warning",
                                        title: "Mohon tunggu halaman sedang di reload.",
                                    });
                                    setTimeout(() => {
                                        window.location.reload();
                                    }, 2000);
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
                                confirmButtonText: "Oke",
                            });
                        }
                    }
                };
                const data = JSON.stringify({
                    bookId: bookId,
                    bookName: bookName,
                    newCount: newCount,
                    nama: nama,
                    kelas: kelas,
                    nisn: nisn,
                    tglPinjam: tglPinjam,
                });
                xhr.send(data);
                tglPinjam.value = "";
            }
        }

        function sendToEmailJS(
            bookId,
            bookName,
            newCount,
            nama,
            kelas,
            nisn,
            tglPinjam
        ) {
            const newNewCount = newCount - 1;
            const tglKembali = new Date(tglPinjam);
            tglKembali.setDate(tglKembali.getDate() + 7);
            const tglKembaliFormatted = tglKembali.toISOString().split("T")[0];

            emailjs.send("alfajjar", "alfajjar", {
                bookId: bookId,
                bookName: bookName,
                newCount: newCount,
                newNewCount: newNewCount,
                nama: nama,
                kelas: kelas,
                nisn: nisn,
                tglPinjam: tglPinjam,
                tglKembali: tglKembaliFormatted,
            });
        }
    };
};
