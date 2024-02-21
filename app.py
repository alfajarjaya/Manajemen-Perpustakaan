from flask import Flask, render_template, request, url_for, session, send_file, Response
import assets.data_json as json
import assets.val as val
import mysql.connector
import assets.qr as qr
import os
import openpyxl

db = mysql.connector.connect(host="localhost", user="root", password="", database="database_user", port=3306)
db_cursor = db.cursor()

app = Flask(__name__)
app.secret_key = '1'

dataUser = json.dataUser
dataAdmin = json.dataAdmin
    
@app.route('/')
def index():
    return render_template('login.html', url='dashboard')

@app.route('/dashboard', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        userName = request.form.get('username')
        password = request.form.get('password')
        
        for key, value in dataAdmin.items():
            name = value['user']
            pw = value['password']
            
            session['name'] = name
            
            if userName == name and password == pw:
                session['userName'] = userName
                session['password'] = password
                return render_template('admin/dashboard.html', userName=userName, url='admin')
                

        for key, value in dataUser.items():
            nama = value["nama"]
            nomor = value["pw"]

            if userName == nama and str(password) == str(nomor):
                session['userName'] = userName
                session['password'] = password
                return render_template('user/dashboard.html', userName=userName, url='user')
        
        return render_template('login.html', error='username/password is wrong')
    
    user = session.get('userName')
    adminUser = session.get('name')

    if user == adminUser:
        return render_template('admin/dashboard.html', userName=user, url='dashboard')
        
    return render_template('user/dashboard.html', userName=user, url='dashboard')

@app.route('/admin')
def profilAdmin():
    user = session.get('userName')
    
    return render_template('admin/profil.html', user=user, nomor_induk='-', kelas='-', url='dashboard')
    
@app.route('/data_pengunjung')
def download_excel():
    excel_path = 'D:\\produktif bu Tya\\manajemen_perpustakaan\\static\\data.xlsx'
    return send_file(excel_path, as_attachment=True)

@app.route('/scanner')
def scanner():
    return render_template('scanner.html', video=url_for('video_feed'))

@app.route('/video_feed')
def video_feed():
    return Response(qr.generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

#       <-- Halamann yang memuat -->
#          ``User Client / siswa``

@app.route('/user')
def profilUser():
    user = session.get('userName')
    userValid = val.validateNama(user)
    
    data_user = val.database(user)
    
    if userValid and data_user:
        return render_template('user/profil.html', user=data_user['nama'], kelas=data_user['kelas'], nomor=data_user['nomor_induk'], url='/')
    else:
        return "User not found or not validated"
    
    
    # Pinjam user and admin
    
@app.route('/admin_pinjam', methods=['POST', 'GET'])
def pinjamAdmin():
    
    user = session.get('userName')
    
    if request.method == 'POST':
        name = request.form.get('nama')
        kelas = request.form.get('kelas')
        pinjam = request.form.get('pinjam')
        kembali = request.form.get('kembali')
        
        mysql = "INSERT INTO data (nama, kelas, tanggal_pinjam, tanggal_kembali) VALUES (%s,%s,%s,%s)"
        values = (name, kelas, pinjam, kembali)
        db_cursor.execute(mysql, values)
        db.commit()
        
        return render_template('pinjam/pinjam_admin.html',data=dataUser, nama=name,pinjam=pinjam,kembali=kembali, success='Data telah dimasukkan.', userName=user)
        
    return render_template('pinjam/pinjam_admin.html', data=dataUser, userName=user)
    
@app.route('/user_pinjam', methods=['GET'])
def pinjamUser():
    user = session.get('userName')
    
    return render_template('pinjam/pinjam_user.html', userName=user)

# RUN PROJECT

if __name__ == '__main__':
    if os.path.exists('D:\\produktif bu Tya\\manajemen_perpustakaan\\static\\data.xlsx'):
        workbook = openpyxl.load_workbook('D:\\produktif bu Tya\\manajemen_perpustakaan\\static\\data.xlsx')
        worksheet = workbook.active
    else:
        workbook = openpyxl.Workbook()
        worksheet = workbook.active

    app.run(debug=True)
