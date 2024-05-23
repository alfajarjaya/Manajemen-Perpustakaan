from flask import render_template
import app
import database.SQL.connect_to_SQL as database
import config.import_json as json
from config.client import client_valid as valClient
from database.client import peminjaman as db_pinjam_user

def home_user():
    user = app.session.get('user')
    return render_template('client/dashboard.html', userName=user)

def listBook():
    user = app.session.get('user')
    bookSisa = []
    book = json.listBook
    dataUser = valClient.databaseProfil(user)
    
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
            
    return render_template(
        'client/book_user.html', 
        userName=user, 
        bookSisa=bookSisa, 
        book=book, 
        data=dataUser
    )

def profil_users():
    user = app.session.get('user')
    data_user = valClient.databaseProfil(user)
    
    if isinstance(data_user, dict):
        return render_template(
            'client/profil.html', 
            userName=user,
            nama=data_user['nama'],
            nomor=data_user['nomor'],
            kelas=data_user['kelas'],
            img=data_user['img']
        )
        
def peminjaman_buku():
    user = app.session.get('user')
    data_user = valClient.databaseProfil(user)
    valueData = data_user['nama'].lower()
    
    data = db_pinjam_user.selectUserDatabase(valueData)
    
    if data is None:
        return '''
                    <div class="container">
                        <h2>Terjadi sedikit kesalahan</h2>
                            <hr>
                            <p>Data peminjaman tidak tersedia.</p>
                    </div>
                '''
                
    return render_template(
        'client/pinjam_user.html',
        userName=user,
        data=data
    )