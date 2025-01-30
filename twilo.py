from twilio.rest import Client

# Credenciales de Twilio (reemplaza con las tuyas)
account_sid = 'AC675d6faca5eee561ba565a907bc57ce7'
auth_token = 'a9646171df15491ec5f55df71ef4361e'
client = Client(account_sid, auth_token)

# Mensaje a enviar
message = client.messages.create(
    from_='whatsapp:+14155238886',  # Número habilitado por Twilio
    body='Hola, este es un mensaje de prueba desde la API de Twilio!',  # El cuerpo del mensaje
    to='whatsapp:+56966705257'  # Número del destinatario (reemplazar con el número real)
)

print(f"Mensaje enviado con SID: {message.sid}")