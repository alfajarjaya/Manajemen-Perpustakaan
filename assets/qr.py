from flask import render_template
import PySimpleGUI as sg
import numpy as np
import mysql.connector
import cv2
import mysql.connector
import app

mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="database_user", port=3306)
mycursor = mysqldb.cursor()

def scan_and_save_qr_code(frame, worksheet):
    try:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        qr_code_detector = cv2.QRCodeDetector()
        retval, decoded_info, points, straight_qrcode = qr_code_detector.detectAndDecodeMulti(gray)

        if retval:
            for i in range(len(points)):
                cx = int(np.mean(points[i][:, 0]))
                cy = int(np.mean(points[i][:, 1]))

                points_int32 = points[i].astype(np.int32)

                cv2.polylines(frame, [points_int32], isClosed=True, color=(0, 255, 0), thickness=2)

                qr_data = process_qr_data(decoded_info[i])

                i = f'Nomor Induk : {qr_data["Nomor Induk"]}, \nNama : {qr_data["Nama"]} ,\nKelas : {qr_data["Kelas"]},\nJurusan : {qr_data["Jurusan"]}'

                # Print pesan debug
                print(f'QRCode data : \n {i}')

                if any(qr_data.values()):
                    if worksheet.max_row == 1:
                        worksheet.append(['Nomor Induk', 'Nama', 'Kelas', 'Jurusan'])

                    worksheet.append([
                        qr_data['Nomor Induk'],
                        qr_data['Nama'],
                        qr_data['Kelas'],
                        qr_data['Jurusan']
                    ])

                    sql = "INSERT INTO qrcode (Nomor_Induk, Nama, Kelas, Jurusan) VALUES (%s, %s, %s, %s)"
                    values = (qr_data['Nomor Induk'], qr_data['Nama'], qr_data['Kelas'], qr_data['Jurusan'])
                    mycursor.execute(sql, values)
                    mysqldb.commit()

                    book = app.workbook

                    book.save('D:\\produktif bu Tya\\manajemen_perpustakaan\\static\\data.xlsx')

                    print('Data telah tersimpan!')
    except Exception as e:
        print(f"Error in scan_and_save_qr_code: {e}")
    finally:
        cv2.waitKey(1)
        
def process_qr_data(frame):
    try:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        qr_code_detector = cv2.QRCodeDetector()
        retval, decoded_info, points, straight_qrcode = qr_code_detector.detectAndDecodeMulti(gray)

        if retval:
            for i in range(len(points)):
                cx = int(np.mean(points[i][:, 0]))
                cy = int(np.mean(points[i][:, 1]))

                points_int32 = points[i].astype(np.int32)

                cv2.polylines(frame, [points_int32], isClosed=True, color=(0, 255, 0), thickness=2)

                qr_data = {
                    'Nomor Induk': '',
                    'Nama': '',
                    'Kelas': '',
                    'Jurusan': ''
                }

                lines = decoded_info[i].split('\n')

                for line in lines:
                    if ':' in line:
                        key, value = line.split(': ', 1)
                        qr_data[key.strip()] = value.strip()

                i = f'Nomor Induk : {qr_data["Nomor Induk"]}, \nNama : {qr_data["Nama"]} ,\nKelas : {qr_data["Kelas"]},\nJurusan : {qr_data["Jurusan"]}'
                
                # Print pesan debug
                sg.popup(f'QRCode data : \n {i}')

                if any(qr_data.values()):
                    if app.worksheet.max_row == 1:
                        app.worksheet.append(['Nomor Induk', 'Nama', 'Kelas', 'Jurusan'])

                    app.worksheet.append([
                        qr_data['Nomor Induk'],
                        qr_data['Nama'],
                        qr_data['Kelas'],
                        qr_data['Jurusan']
                    ])
                
                    sql = "INSERT INTO qrcode (Nomor_Induk, Nama, Kelas, Jurusan) VALUES (%s, %s, %s, %s)"
                    values = (qr_data['Nomor Induk'], qr_data['Nama'], qr_data['Kelas'], qr_data['Jurusan'])
                    mycursor.execute(sql, values)
                    mysqldb.commit()

                    book = app.workbook

                    book.save('D:\\produktif bu Tya\\manajemen_perpustakaan\\static\\data.xlsx')

                    sg.popup('Data telah tersimpan!')
    except Exception as e:
        print(f"Error in process_qr_data: {e}")
    finally:
        cv2.waitKey(1)


def generate_frames():
    # Inisialisasi kamera
    cap = cv2.VideoCapture(0)

    while True:
        success, frame = cap.read()

        if not success:
            break
        else:
            # Lakukan pemrosesan frame di sini (misalnya deteksi QR code)
            process_qr_data(frame)

            # Perbaiki bagian ini
            ret, buffer = cv2.imencode('.jpg', frame)
            if not ret:
                print("Error encoding frame to JPEG.")
                break

            frame = buffer.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

        # Tunggu 1 ms dan cek jika tombol 'q' ditekan untuk keluar
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Bebaskan sumber daya dan tutup kamera setelah loop selesai
    cap.release()
    cv2.destroyAllWindows()