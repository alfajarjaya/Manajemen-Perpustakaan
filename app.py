from flask import Flask, render_template, request, session, redirect, url_for, Response, jsonify
import datetime
import os
import dotenv
import time

import config.admin.admin as admin
from config.admin import scannerQRCODE as adminQr
import config.admin.val_admin as validateUserAdmin

import config.client.client as client
from config.client.client_valid import name_and_pw_client
from config.client.client_valid import user_client_valid
from database.client import peminjaman

# import config.import_json as json
import database.SQL.connect_to_SQL as db

app = Flask(__name__)
dotenv.load_dotenv()
app.secret_key = os.getenv('SECRET_KEY')

# dataAdmin = json.adminUser
# dataClient = json.clientUser

@app.route('/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form.get('username')
        password = request.form.get('password')

        if user:
            if validateUserAdmin.val_user_and_pw_admin(user, password):
                session['user'] = user
                session['password'] = password

                return redirect(url_for('home'))
            
            elif name_and_pw_client(user, password):
                session['user'] = user
                session['password'] = password
            
                return redirect(url_for('home'))
            else:
                return render_template('login.html', nf='Username or Password is wrong')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/dashboard')
def home():
    user = session.get('user')

    if user:
        if validateUserAdmin.val_user_admin(user):
            return admin.home()

        if user_client_valid(user):
            return client.home_user()

    return redirect(url_for('login'))

@app.route('/daftarBuku', methods=['POST', 'GET'])
def list_book_admin():
    user = session.get('user')
    
    if validateUserAdmin.val_user_admin(user):
        
        session['user'] = user
        
        if request.method == 'POST':
            return admin.list_book()

        return admin.list_book()
    
    return redirect(url_for('login'))
                
@app.route('/admin_pinjam')
def pinjam_admin():
    user = session.get('user')
        
    if validateUserAdmin.val_user_admin(user):
        return admin.peminjaman()
            
    else:
        return redirect(url_for('login'))
    
@app.route('/remove_table', methods=['POST'])
def remove_table():
    if request.method == 'POST':
        table_name = request.json['tableName'].replace(' ','_')
        db.pinjamAdmin.removeTabel(table_name)
        time.sleep(1)

    return jsonify({'message': 'Tabel berhasil dihapus.'}), 200

@app.route('/admin_pinjam/<name>')
def showData(name):
    user = session.get('user')
    
    if validateUserAdmin.val_user_admin(user):
        return admin.showDataPeminjaman(name)
    else:
        return redirect(url_for('login'))

@app.route('/remove_data', methods=['POST'])
def remove_data():
    if request.method == 'POST':
        data = request.json
        nama = data['name'].replace(' ', '_').lower()
        id = data['id']
        name = data['name']
        db.pinjamAdmin.hapusDataDariTabel(nama, id)
        
        time.sleep(1)

    return jsonify({'message': f'Data {name} dengan id peminjaman {id} berhasil dihapus.'}), 200

@app.route('/remove_data_pengunjung', methods=['POST'])
def remove_data_pengunjung():
    if request.method == 'POST':
        data = request.json
        id = data['id']
        name = data['name']
        
        db.hapusDataPengunjung(id)
        
        time.sleep(1)
        
    return jsonify({'message': f'Data {name} dengan id pengunjung {id} berhasil dihapus.'}), 200

@app.route('/profil')
def profil():
    user = session.get('user')

    if validateUserAdmin.val_user_admin(user):
        return admin.profil()
    if user_client_valid(user):
        return client.profil_users()
    
    return redirect(url_for('login'))


@app.route('/updateBookCount', methods=['POST'])
def update_book_count():
    if request.method == 'POST':
        data = request.json
        namaBuku = data.get('nama')
        bookId = data.get('bookId')
        newCount = data.get('newCount')

        if bookId is not None and newCount is not None:
            if int(newCount) < 0:
                return jsonify({'message' : f'Jumlah buku yang anda masukkan tidak valid'}), 400
            else:
                db.update_book_count_and_save_to_database(bookId, namaBuku, newCount)
            
                session['bookId'] = bookId
                session['namaBuku'] = namaBuku
            return jsonify({'message' : f'Jumlah buku "{namaBuku}" telah berhasil dirubah'}), 200
        else:
            return jsonify({'message' : f'Jumlah buku "{namaBuku}" gagal dirubah'}), 400
        
    return redirect(url_for('list_book_admin'))
            
@app.route('/data-pengunjung')
def dataPengunjung():
    return admin.dataPengunjung()

@app.route('/Scanner')
def scanner_qrCode():
    return admin.scanner()

@app.route('/video_feed')
def video_feed():
    return Response(adminQr.generate(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/daftar-buku')
def list_book_client():
    user = session.get('user')
    
    if user_client_valid(user):
        return client.listBook()
    
    return redirect(url_for('login'))

@app.route('/pinjamBuku', methods=['POST'])
def pinjam_buku():
    if request.method == 'POST':
        data = request.json
        idBuku = data['bookId']
        namaBuku = data['bookName']
        sisaBuku = data['newCount']
        
        namaUser = data['nama']
        kelasUser = data['kelas']
        nisnUser = data['nisn']
        tglPinjam = data['tglPinjam']
        
        sisaBukuTerbaru = int(sisaBuku) - 1
        
        if sisaBukuTerbaru < 0:
            return jsonify({'message': f'Buku "{namaBuku}" lagi tidak tersedia.'}), 400
        if tglPinjam == '' or tglPinjam is None:
            return jsonify({'message': 'Tanggal Pinjam tidak boleh kosong.'}), 400
        else:
            formatTglPinjam = datetime.datetime.strptime(tglPinjam, '%Y-%m-%d').date()
            
            if formatTglPinjam < datetime.date.today():
                return jsonify({'message': 'Tanggal Pinjam tidak boleh kurang dari hari ini.'}), 400
            if formatTglPinjam > datetime.date.today():
                return jsonify({'message': 'Tanggal Pinjam tidak boleh melebihi dari hari ini.'}), 400
            else:
                peminjaman.peminjamanBuku(
                    idBuku, namaBuku, namaUser, kelasUser, nisnUser, formatTglPinjam
                )
            
                db.update_book_count_and_save_to_database(idBuku, namaBuku, sisaBukuTerbaru)
                
                
                
                return jsonify({'message' : f'Berhasil meminjam buku dengan judul "{namaBuku}" dan ID buku "{idBuku}", segera ambil buku di Perpustakaan.'}), 200

@app.route('/data-peminjaman')
def dataPeminjaman():
    return client.peminjaman_buku()
    
    
if __name__ == '__main__':
    app.run(
        host=os.getenv('HOST_RUNNING_APP'),
        port=os.getenv('PORT_RUNNING_APP'),
        debug= os.getenv('DEBUG_RUNNING_APP')
    )