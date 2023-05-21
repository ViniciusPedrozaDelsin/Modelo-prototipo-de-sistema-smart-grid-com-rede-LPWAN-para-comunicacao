import numpy as np
import sqlite3
import matplotlib.pyplot as plt

con = sqlite3.connect('bancoDeDados.db')
cur = con.cursor()

sqlite_select_query = """SELECT * from registros"""
cur.execute(sqlite_select_query)
records = cur.fetchall()

cur.close()

con.close()

data = []
tensao = []
corrente = []
frequencia = []

for row in records:
    print("Data: ", row[0])
    print("Tensão: ", row[1])
    print("Corrente: ", row[2])
    print("Frequência: ", row[3])
    print("\n")
    data.append(row[0])
    tensao.append(row[1])
    corrente.append(row[2])
    frequencia.append(row[3])

def listaParaDecimal(lista):
    listaDecimal = []
    for item in lista:
        listaDecimal.append(float(item))
    return listaDecimal

def separaData(datas):
    listaFinalDatas = []
    for d in datas:
        listaDatas = d.split()
        finalDatas = listaDatas[1]
        listaFinalDatas.append(finalDatas[:-7])
    return listaFinalDatas

tensaoF = listaParaDecimal(tensao)
correnteF = listaParaDecimal(corrente)
frequenciaF = listaParaDecimal(frequencia)
datasF = separaData(data)

plt.figure(1)
plt.title("Corrente X Horário")
plt.xlabel("Horário")
plt.ylabel("Corrente [A]")
plt.grid()
plt.plot(datasF, correnteF)
plt.show()

plt.figure(2)
plt.title("Tensão X Horário")
plt.xlabel("Horário")
plt.ylabel("Tensão [V]")
plt.grid()
plt.plot(datasF, tensaoF)
plt.show()