import requests as req
import paho.mqtt.client as paho
import datetime

# Url do Servidor ESP32 com os dados dos sensores
url = 'http://172.16.38.100'

# Define cabeçalho HTTP
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
    "Accept-Encoding": "*",
    "Connection": "keep-alive"
}

print("Aguardando conexao com o servidor.")

x = 0
while(x == 0):
    try: 
        # Recebe o body da pagina web
        response = req.get(url, headers=headers)
        # Divide o body do html em uma string por espaçamento.
        parametro = response.text.split()
        print(response.text.split())
        x = 1
    except:
        x = 0

# Adiciona data e hora no pacote
horario = str(datetime.datetime.now())
parametro.append(horario)

# Define parametros para a conexao com o broker MQTT
broker="localhost"
port=1884

# Funcao para callback
def on_publish(client,userdata,result):
    print("Dados Publicados")
    pass

# Define objeto cliente
client1 = paho.Client("medidor1")

# Define função para callback
client1.on_publish = on_publish

# Inicia conexao com o broker
client1.connect(broker,port)

# Realiza a publicação no tópico "smartmeter1".
client1.publish(
    "smartmeter1",
    parametro[0] + " " + 
    parametro[1] + " " + 
    parametro[2] + " " +
    parametro[3]
    )