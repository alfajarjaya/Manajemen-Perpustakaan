import mysql.connector
import os
import dotenv

dotenv.load_dotenv()

def connect_to_database():
    
    try :
        return mysql.connector.connect(
            host=os.getenv('HOST'),
            user=os.getenv('USER'), 
            password=os.getenv('PASSWDORD'), 
            database=os.getenv('DATABASE_ADMIN'),
            port=os.getenv('PORT')
    )
        
    except Exception as e:
        print ("Error connecting to database")
        
def add_login(nama, password):
    try:
        konektor = connect_to_database()
        cur = konektor.cursor()

        cur.execute("""
                    CREATE TABLE IF NOT EXISTS database_login (
                        id_login INT PRIMARY KEY AUTO_INCREMENT,
                        nama VARCHAR(255) NOT NULL,
                        password VARCHAR(255) NOT NULL
                    )
                    
                    """)


        check_query = "SELECT * FROM `database_login` WHERE nama = '%(nama)s"
        cur.execute(check_query, (nama,))
        result = cur.fetchone()[0]

        if result == 0:
            insert_query = "INSERT INTO database_login (nama, password) VALUES (%s, %s)"
            insert_values = (nama, password)
            cur.execute(insert_query, insert_values)
            konektor.commit()
        else:
            print('Login sudah ada di database')

        konektor.close()
    except Exception as e:
        print(f'Error : {e}')
        
# add_login('0077079282', '0077079282')
        
def update_book_count_and_save_to_database(book_id, book_name, new_count):
    try:
        connection = connect_to_database()
        cursor = connection.cursor()
        
        cursor.execute("SELECT id_buku FROM database_buku WHERE id_buku = %s", (book_id,))
        existing_book = cursor.fetchone()

        if existing_book:
            cursor.execute("UPDATE database_buku SET sisa = %s WHERE id_buku = %s", (new_count, book_id))
            print("Data buku berhasil diperbarui.")
        else:
            cursor.execute("INSERT INTO database_buku (id_buku, nama_buku, penerbit_buku, sisa) VALUES (%s, %s, %s,%s)", (book_id, book_name, new_count))
            print("Data buku baru berhasil ditambahkan.")

        connection.commit()

        cursor.execute("SELECT id_buku, nama_buku, penerbit_buku, sisa FROM database_buku WHERE id_buku = %s", (book_id,))
        book_data = cursor.fetchone()

        
        cursor.close()
        connection.close()

    except Exception as e:
        print("Gagal memperbarui atau menambahkan data buku:", e)
def selectBook(book_id, book_name):
    try:
        connection = connect_to_database()
        cursor = connection.cursor()
        
        sql = "SELECT sisa FROM `database_buku` WHERE id_buku = %s AND nama_buku = %s"
        cursor.execute(sql, (book_id, book_name,))
        
        book_data = cursor.fetchone()
        
        cursor.close()
        connection.close()

        return book_data[0]
    except Exception as e:
        print("Error while fetching book data:", e)
        return None

def dataPengunjung():
    try:
        konektor = connect_to_database()
        cur = konektor.cursor()
        
        cur.execute('SELECT * FROM `database_pengunjung`')
        result = cur.fetchall()

        hasil = []
        
        for data in result:
            id_person = data[0]
            nomor_induk = data[1]
            nama = data[2]
            kelas = data[3]
            jurusan = data[4]

            data_user = [
                id_person,
                nomor_induk,
                nama,
                kelas,
                jurusan
            ]
            
            hasil.append(data_user)
            
        return hasil
    except Exception:
        return None
    
def hapusDataPengunjung(id):
    try:
        konektor = connect_to_database()
        cur = konektor.cursor()
        
        cur.execute('DELETE FROM `database_pengunjung` WHERE id_pengunjung = %s', (id,))
        konektor.commit()
        konektor.close()
    except Exception as e:
        print(f'Error : {e}')
        
class pinjamAdmin:
    def ambilTabel():
        try:
            konektor = mysql.connector.connect(
                host=os.getenv('HOST'),
                user=os.getenv('USER'), 
                password=os.getenv('PASSWDORD'), 
                database=os.getenv('DATABASE_CLIENT'),
                port=os.getenv('PORT')
            )
        
            cursor = konektor.cursor()

            cursor.execute('SHOW TABLES')
            results = cursor.fetchall()
            
            formatted_results = []
            for row in results:
                for table_name in row:
                    formatted_table_name = ' '.join(word.capitalize() for word in table_name.split('_'))
                    formatted_results.append(formatted_table_name)
                    
            return formatted_results
        except Exception as e:
            return None
    
    def removeTabel(nama_user):
        try:
            konektor = mysql.connector.connect(
                host=os.getenv('HOST'),
                user=os.getenv('USER'), 
                password=os.getenv('PASSWDORD'), 
                database=os.getenv('DATABASE_CLIENT'),
                port=os.getenv('PORT')
            )
            
            cursor = konektor.cursor()
            cursor.execute(f'DROP TABLE `{nama_user}`')
            
            cursor.close()
            konektor.close()
            
        except Exception as e:
            print(f'Error {e}')
            
    def ambilDataTabel(nama_user):
        try:
            konektor = mysql.connector.connect(
                host=os.getenv('HOST'),
                user=os.getenv('USER'), 
                password=os.getenv('PASSWDORD'), 
                database=os.getenv('DATABASE_CLIENT'),
                port=os.getenv('PORT')
            )
            
            cursor = konektor.cursor()
            cursor.execute('SHOW TABLES')
            tables = cursor.fetchall()
            
            if (nama_user,) in tables:
                selectTabel = f'SELECT * FROM `{nama_user}`'
                cursor.execute(selectTabel)
        
                result = cursor.fetchall()
        
                cursor.close()
                konektor.close()

                hasil = []

                for row in result:
                    idPeminjaman= row[0]
                    idBuku = row[1]
                    namaBuku = row[2]
                    namaUser = row[3]
                    kelasUser = row[4]
                    nisnUser = row[5]
                    pinjam = row[6].strftime("%Y-%m-%d")
                    kembali = row[7].strftime("%Y-%m-%d")
                    
                    hasil.append((
                        idPeminjaman, idBuku, namaBuku, namaUser, kelasUser, nisnUser, pinjam, kembali
                    ))
                    
                return hasil
            else:
                return None
            
        except Exception as e:
            print(f'Erorr {e}')
    
    def hapusDataDariTabel(nama_user, id_peminjaman):
        try:
            konektor = mysql.connector.connect(
                host=os.getenv('HOST'),
                user=os.getenv('USER'), 
                password=os.getenv('PASSWDORD'), 
                database=os.getenv('DATABASE_CLIENT'),
                port=os.getenv('PORT')
            )
            
            tabelUser = f'peminjaman_buku_{nama_user}'
        
            cursor = konektor.cursor()
            cursor.execute(f"DELETE FROM `{tabelUser}` WHERE `id_peminjaman` = '{id_peminjaman}'")
        
            konektor.commit()
            cursor.close()
            konektor.close()
        
        except Exception as e:
            print(f'Error {e}')
            