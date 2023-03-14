# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 15:21:43 2023

Análise de focos de calor da região norte do brasil com relação ao país

@author: Gabriel Ratão
"""
#%% importando as bibliotecas
import pandas as pd
import matplotlib.pyplot as plt


#%% importando base de dados

dados_regioes = pd.read_excel(r"C:\Users\User\Documents\Python\bases_dados\queimadas_brasil\analise\focos_calor_Brasil_Regioes.xlsx")
display(dados_regioes)


#%% análise de correlação entre os dados

groupDF = pd.DataFrame({'norte': dados_regioes["norte"],
                        'brasil': dados_regioes["brasil"]
    })

correlacao = groupDF.corr()


#%% criando a figura


fig, ax = plt.subplots()
ax.plot(dados_regioes["ano"], dados_regioes["brasil"], label="brasil")
ax.plot(dados_regioes["ano"], dados_regioes["norte"], label="norte")

plt.xlabel('ano (1999-2016)')
plt.ylabel('focos de queimada')

ax.legend()

plt.suptitle('Focos de Queimadas Brasil x Norte\n Correlação entre os dados: 90,75%')

plt.show()

#%%


