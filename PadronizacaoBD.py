import pandas as pd
import matplotlib.pyplot as plt

# Site para aquisicao do banco de dados: 
# https://basedosdados.org/dataset/br-mme-consumo
# -energia-eletrica?bdm_table=uf

df = pd.read_csv('uf.csv')

# Definicao do tipo de consumo a ser analisado
def defineTipoConsumo():
    print("Escolha o tipo de consumo: ")
    print("1 - Residencial")
    print("2 - Comercial")
    print("3 - Industrial")
    print("4 - Total")
    tipo_consumoF = int(input("Digite o numero: "))
    return tipo_consumoF

# Definicao do tipo de consumo a ser analisado
validacao = False
while validacao == False:

    try:
        tipo_consumo = defineTipoConsumo()
    except:
        print("Valor deve ser um numero inteiro!")


    if tipo_consumo == 1:
        tipoC = "Residencial"
        df = df[df.tipo_consumo == tipoC]
        validacao = True
    elif tipo_consumo == 2:
        tipoC = "Comercial"
        df = df[df.tipo_consumo == tipoC]
        validacao = True
    elif tipo_consumo == 3:
        tipoC = 'Industrial'
        df = df[df.tipo_consumo == tipoC]
        validacao = True
    elif tipo_consumo == 4:
        tipoC = 'Total'
        df = df[df.tipo_consumo == tipoC]
        validacao = True
    else:
        print("Valor invalido!")

# Define estado como SP
df = df[df.sigla_uf == 'SP']

# Formata a data
data = pd.date_range(start='01/15/2004', end='12/15/2021', periods=len(df))
df['data'] = data.strftime('%Y-%m')
df = df.set_index('data')
df.index.freq='MS'

# Deleta coluna de numero de consumidores
df.drop(["numero_consumidores"], axis=1, inplace=True)
# Deleta coluna ano
df.drop(["ano"], axis=1, inplace=True)
# Deleta coluna mes
df.drop(["mes"], axis=1, inplace=True)
# Deleta coluna tipo_consumo
df.drop(["tipo_consumo"], axis=1, inplace=True)
# Deleta coluna sigla_uf
df.drop(["sigla_uf"], axis=1, inplace=True)
# Converte a tabela para .CSV
df.to_csv('Ai.csv')