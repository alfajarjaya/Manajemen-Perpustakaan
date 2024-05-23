import cv2
import mysql.connector as sql
import winsound
import time
import os
import dotenv

dotenv.load_dotenv()

def database():
    return sql.connect(
        host=os.getenv('HOST'),
        user=os.getenv('USER'), 
        password=os.getenv('PASSWDORD'), 
        database=os.getenv('DATABASE_ADMIN'),
        port=os.getenv('PORT')
    )
    
def scan_and_save(frame):
    try:
        color = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        detector = cv2.QRCodeDetector()
        
        retval, decodeInfo, points, straight = detector.detectAndDecodeMulti(color)
        
        if retval:
            for i in range(len(points)):
                qr_data = proses_data(decodeInfo[i])
                
                if qr_data:
                    qrCode = (
                        qr_data['Nomor Induk'],
                        qr_data['Nama'],
                        qr_data['Kelas'],
                        qr_data['Jurusan']
                    )
                    
                    if all(qr_data.values()):
                        konektor = database()
                        cur = konektor.cursor()
                    
                        data = """
                            INSERT INTO database_pengunjung (nomor_induk,nama,kelas,jurusan
                            ) VALUES (%s,%s,%s,%s
                            )
                        """

                        cur.execute(data, qrCode)
                        konektor.commit()
                    
                        winsound.Beep(3000, 700)
                        return time.sleep(1.5)
                    else:
                        return None
                else:
                    print("Data QR code tidak valid.")
    except Exception as e:
        print(f'Error : {e}')

def proses_data(decodeInfo):
    try:
        qr_data = {
            'Nomor Induk': '',
            'Nama': '',
            'Kelas': '',
            'Jurusan': ''
        }
        
        lines = decodeInfo.split('\n')
        for line in lines:
            if ':' in line:
                key, value = line.split(':', 1)
                qr_data[key.strip()] = value.strip()
        
        return qr_data
    except Exception as e:
        print(f'Error: {e}')
        return None

def generate():
    cap = cv2.VideoCapture(0)
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Can't receive frame (stream end?). Exiting ...")
            break
            
        scan_and_save(frame)
        
        frame_with_qr = b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + cv2.imencode('.jpg', frame)[1].tobytes() + b'\r\n'
        yield frame_with_qr
    
    cap.release()
    cv2.destroyAllWindows()