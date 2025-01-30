import os
import time
from ftplib import FTP
from datetime import datetime

# Configuración del FTP
FTP_HOST = "34.237.148.7"
FTP_USER = "ftp-user-1"
FTP_PASS = "12345678"
FTP_DIR = "/home/ftp-user-1"  # Directorio destino en el FTP

# Ruta de la imagen original para enviar
ORIGINAL_IMAGE_PATH = "/Users/taty/Desktop/Personal/Script/ABCD29_20250109162147686.jpg"  # Cambia esto a la ruta de tu imagen original

# Función para conectar al FTP
def connect_ftp():
    ftp = FTP(FTP_HOST)
    ftp.login(FTP_USER, FTP_PASS)
    return ftp

# Función para subir una imagen al FTP
def upload_image(ftp, local_path, remote_path):
    with open(local_path, 'rb') as f:
        ftp.storbinary(f"STOR {remote_path}", f)
    print(f"Imagen subida: {remote_path}")

# Función principal
def main():
    # Conectar al FTP
    ftp = connect_ftp()

    # Número de veces que se desea enviar la imagen
    num_sends = 1000

    for i in range(num_sends):
        # Generar el nombre del archivo con la fecha y hora actual
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")  # AñoMesDíaHoraMinutoSegundo
        new_file_name = f"ABCD12_{timestamp}_{i+1}.jpg"

        # Subir la imagen con el nuevo nombre
        upload_image(ftp, ORIGINAL_IMAGE_PATH, os.path.join(FTP_DIR, new_file_name))


    # Cerrar la conexión FTP
    ftp.quit()

if __name__ == "__main__":
    main()