import mysql.connector as mysql
import datetime
import os
import dotenv

dotenv.load_dotenv()

def connectToDatabase_2():
    toSQL = mysql.connect(
        host=os.getenv('HOST'),
        user=os.getenv('USER'), 
        password=os.getenv('PASSWDORD'), 
        database=os.getenv('DATABASE_CLIENT'),
        port=os.getenv('PORT')
    )
    
    return toSQL

def peminjamanBuku(id_buku, nama_buku, nama_user, kelas_user, nisn_user, tanggal_peminjaman):
    konektor = connectToDatabase_2()
    cursor = konektor.cursor()
        
    tabelName = f'peminjaman_buku_{nama_user}'.replace(' ', '_')
    createTabel = f"""
        CREATE TABLE IF NOT EXISTS {tabelName} (
        id_peminjaman INT PRIMARY KEY AUTO_INCREMENT,
        id_buku VARCHAR(15) NULL,
        nama_buku TEXT NULL,
        nama_user TEXT NULL,
        kelas_user VARCHAR(10) NULL,
        nisn_user TEXT NULL,
        tanggal_peminjaman DATE NULL,
        tanggal_pengembalian DATE NULL
    )
    """

    formatTanggalPeminjaman = datetime.date.strftime(tanggal_peminjaman, '%Y-%m-%d')
    
    tanggalPengembalian = tanggal_peminjaman + datetime.timedelta(days=7)
    formatTanggalPengembalian = datetime.date.strftime(tanggalPengembalian, '%Y-%m-%d')
    
        
    insertData = f'''
        INSERT INTO {tabelName}
            (id_buku,nama_buku,nama_user,kelas_user,nisn_user, tanggal_peminjaman, tanggal_pengembalian)
        VALUES 
            (%s,%s,%s,%s,%s,%s,%s)
        
    '''
    insertValue = (id_buku, nama_buku, nama_user, kelas_user, nisn_user, formatTanggalPeminjaman, formatTanggalPengembalian)
    
    try:
        cursor.execute(createTabel)
        print(f'Tabel {tabelName} Berhasil Dibuat')
        
        cursor.execute(insertData, insertValue)
        print(f'Data berhasil di simpan')
        
        konektor.commit()
    except Exception as e:
        print(f'Error di : {e}')
        
# peminjamanBuku('BOOK002', 'cerita cuy', 'kimi hugo', 'XI TKJ 123', 121212, datetime.date(2008, 12, 23))

def selectUserDatabase(nama_user):
    try:
        konektor = connectToDatabase_2()
        cursor = konektor.cursor()
        
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        
        tabelName = f'peminjaman_buku_{nama_user}'.replace(' ', '_')
        
        if (tabelName,) in tables:
            selectTabel = f'SELECT `nama_buku`, `tanggal_peminjaman`, `tanggal_pengembalian` FROM `{tabelName}` WHERE nama_user = %s'
            cursor.execute(selectTabel, (nama_user,))
        
            result = cursor.fetchall()
        
            cursor.close()
            konektor.close()
        
            hasil = []
        
            for row in result:
                nama_buku = row[0]
                tanggal_peminjaman = row[1]
                tanggal_pengembalian = row[2]
                hasil.append((nama_buku, tanggal_peminjaman, tanggal_pengembalian))
            return hasil
        else:
            return None
        
    except Exception as e:
        print(f'Error di : {e}')