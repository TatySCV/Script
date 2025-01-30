import os
import boto3

# Configuración de AWS
AWS_ACCESS_KEY = "AKIAYZ2FA4O7BG56WTOS"  # Reemplaza con tu Access Key
AWS_SECRET_KEY = "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"  # Reemplaza con tu Secret Key
BUCKET_NAME = "process-image-portix"  # Reemplaza con el nombre de tu bucket
S3_FOLDER = "PLC1/"  # Carpeta dentro del bucket (terminar con "/")
LOCAL_FOLDER = "C:/FTP/PLC1"  # Carpeta local con las imágenes

# Crear cliente S3
s3_client = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY
)

def subir_imagenes():
    """Sube todas las imágenes de la carpeta LOCAL_FOLDER a S3_FOLDER."""
    for archivo in os.listdir(LOCAL_FOLDER):
        ruta_local = os.path.join(LOCAL_FOLDER, archivo)

        # Filtrar solo imágenes (opcional)
        if os.path.isfile(ruta_local) and archivo.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".bmp")):
            ruta_s3 = S3_FOLDER + archivo  # Ruta destino en S3
            try:
                s3_client.upload_file(ruta_local, BUCKET_NAME, ruta_s3)
                print(f"✅ Subido: {archivo} → {ruta_s3}")
            except Exception as e:
                print(f"❌ Error subiendo {archivo}: {e}")

if __name__ == "__main__":
    subir_imagenes()