from flask import render_template
import app
import database.SQL.connect_to_SQL as database
import config.import_json as fileJson

list_Book = fileJson.listBook

def home():
    user = app.session.get('user')
    notif = app.session.get('notif')
    
    print(notif)
    return render_template('admin/dashboard.html', userName=user)

def peminjaman():
    user = app.session.get('user')
    tabel = database.pinjamAdmin

    return render_template('admin/pinjam_admin.html', userName=user, tabel=tabel.ambilTabel())

def profil():
    user = app.session.get('user')
    
    return render_template('admin/profil.html', user=user, nomor='-',kelas='-', userName=user)
        
def list_book():
    user = app.session.get('user')
    bookSisa = []
    book = list_Book
    
    for key, val in book.items():
        for title, fill in val.items():
            book_id = fill['id']
            nama_buku = fill['nama']
            sisa = database.selectBook(book_id, nama_buku)
            bookSisa.append({'fill': fill, 'sisa': sisa})
            
            for books in bookSisa:
                if books['sisa'] is None:
                    return '''
                            <div class="container">
                                <h2>Terjadi sedikit kesalahan</h2>
                                <hr>
                                <p>Data buku tidak tersedia</p>
                            </div>
                        '''
                    
    return render_template('admin/book_admin.html', userName=user, bookSisa=bookSisa, bookClick=books, jpg=fileJson.listGambarBuku)


def scanner():
    return render_template('admin/scanner.html', video=app.video_feed())

def dataPengunjung():
    user = app.session.get('user')
    data = database.dataPengunjung()
    if data is None:
        return '''
                <div class="container">
                    <h2>Terjadi sedikit kesalahan</h2>
                        <hr>
                    <p>Data pengunjung tidak ditemukan.</p>
                </div>
            '''

    return render_template('admin/data_pengunjung.html', userName=user, data=data)

def showDataPeminjaman(name):
    user = app.session.get('user')
    
    name_formatted = name.replace(' ', '_').lower()
    
    data = database.pinjamAdmin.ambilDataTabel(name_formatted)
    
    return render_template('admin/show_data_peminjaman.html', userName=user, data=data)