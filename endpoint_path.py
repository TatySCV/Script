#SCRIPT QUE ENVIA AL ENDPOINT EL PATH EN PORTICOS-TERAFLEX-2
# import requests

# # Define la URL de tu API
# url = 'http://192.168.100.227:8000/api/upload-path/'

# # Define los parámetros de la solicitud
# path = 'C:/FTP/PLC/ABCD12_20250107100349620.jpg'

# # Función para realizar la solicitud
# def enviar_solicitud(path):
#     params = {'path': path}
    
#     # Realiza la solicitud GET
#     response = requests.get(url, params=params)
    
#     # Verifica el código de estado de la respuesta
#     if response.status_code == 200:
#         print('¡La solicitud fue exitosa!')
#         print('Respuesta:', response.json())  # Imprime la respuesta JSON del servidor
#     else:
#         print(f'Error: {response.status_code}')
#         print('Respuesta:', response.text)

# # Bucle para simular 1000 envíos
# for i in range(100):
#     print(f'Enviando solicitud {i+1}...')
#     enviar_solicitud(path)

import requests
from datetime import datetime, timedelta
import random
import string

# Define la URL de tu API
url = 'http://192.168.100.227:8000/api/upload-path/'

# Nombre base del archivo
path_base = 'C:/FTP/PLC/ABCD12_20250108100349620.jpg'

# Función para realizar la solicitud
def enviar_solicitud(path):
    params = {'path': path}
    
    # Realiza la solicitud GET
    response = requests.get(url, params=params)
    
    # Verifica el código de estado de la respuesta
    if response.status_code == 200:
        print('¡La solicitud fue exitosa!')
        print('Respuesta:', response.json())  # Imprime la respuesta JSON del servidor
    else:
        print(f'Error: {response.status_code}')
        print('Respuesta:', response.text)

# Función para generar una patente aleatoria de 6 caracteres
def generar_patente():
    letras = ''.join(random.choices(string.ascii_uppercase, k=4))  # 4 letras
    numeros = ''.join(random.choices(string.digits, k=2))  # 2 números
    return letras + numeros

# Obtener la fecha y hora inicial del nombre del archivo
fecha_hora_str = '20250107100349'  # Parte de la fecha/hora del nombre del archivo
fecha_hora = datetime.strptime(fecha_hora_str, '%Y%m%d%H%M%S')

# Bucle para simular 1000 envíos
for i in range(10):
    nueva_fecha_hora = fecha_hora + timedelta(minutes=i)  # Sumar minutos en cada vuelta
    nueva_fecha_hora_str = nueva_fecha_hora.strftime('%Y%m%d%H%M%S')
    
    # Generar una nueva patente aleatoria
    nueva_patente = generar_patente()
    
    # Crear el nuevo path con la fecha y la patente modificadas
    nuevo_path = path_base.replace('ABCD12', nueva_patente).replace(fecha_hora_str, nueva_fecha_hora_str)
    
    print(f'Enviando solicitud {i+1} con path: {nuevo_path}')
    enviar_solicitud(nuevo_path)
