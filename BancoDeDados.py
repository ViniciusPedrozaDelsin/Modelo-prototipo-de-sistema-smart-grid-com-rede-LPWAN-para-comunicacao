import paho.mqtt.client as paho
import sqlite3

con = sqlite3.connect('bancoDeDados.db')
cur = con.cursor()

def salvaBD(mensagem):
    m = mensagem.split()
    lista = [
        (m[3]+ " " + m[4], m[0], m[1], m[2]),
    ]
    cur.executemany("insert into registros values (?, ?, ?, ?)", lista)
    con.commit()

def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)
    salvaBD(str(message.payload.decode("utf-8")))

broker_address="localhost" 
print("creating new instance")
client = paho.Client("medidor")
print("connecting to broker")
client.connect(broker_address, 1884)
print("Subscribing to topic","smartmeter1")
client.on_message = on_message
client.subscribe("smartmeter1",1)

# Manter o script sempre ligado para caso de publicacoes
client.loop_forever()
con.close()