const searchInput = document.getElementById("filter");
const bookItems = document.querySelectorAll(".list");
searchInput.addEventListener("input", () => {
    const searchTerm = searchInput.value.toLowerCase().trim();
    
    bookItems.forEach((bookItem) => {
        const bookTitle = bookItem
            .querySelector("#jdl-buku")
            .textContent.toLowerCase()
            .trim();
    
        const idBook = bookItem
            .querySelector('#id-book')
            .textContent.toLowerCase()
            .trim();
    
        if (bookTitle.includes(searchTerm)) {
            bookItem.style.display = "block";
        } else if (idBook.includes(searchTerm)) {
            bookItem.style.display = "block";
        } else {
            bookItem.style.display = "none";
        }
    });

});
