import requests
import json
import pandas as pd
from time import sleep
import matplotlib.pyplot as plt

def get_response(data: str,cantidad : int ) -> list:

	'''Obtiene los primeros 'X' characteres una API.
	Los datos devueltos se guardan en una lista y es retornada

	Data = Url con una barra diagonal '/' como ultimo caracter.
	Cantidad = Personajes a retornar.

	Ejemplo : https://rickandmortyapi.com/api/character/ X-> La x se reemplazara luego por numeros entre 1-10

	'''

	characters = []
	for i in range(1,cantidad+1):

		url = f'{data}{i}'
		# Paso los datos a formato JSON O DICCIONARIO
		r =  requests.get(url).json()
		characters.append(r)
	return characters

def apariciones(dato : list) -> dict:
    '''
    :param dato: Lista con los datos de los personajes
    :return: Diccionario con las apariciones en episodios de cada uno
    '''
    diccionario = {}
    indice = 0
    for i in range(0,len(dato)):
        diccionario[dato[indice]['name']] = len(dato[indice]['episode'])
        indice  += 1
    return diccionario

rick_morty = get_response('https://rickandmortyapi.com/api/character/',10)

df = pd.DataFrame(rick_morty)

df.set_index('id',inplace=True)
df=df.drop('created',axis=1)
df=df.drop('url',axis=1)
df = df.drop('image',axis=1)
df = df.drop('location',axis=1)
df = df.drop('origin',axis=1)
df = df.drop('type',axis=1)
pd.set_option('display.max_columns',5)


df['episode'] = df['episode'].apply(len)

humanos = [i for i in df['species'] if i == 'Human']
males = [i for i in df['gender'] if i == 'Male']

# print(f"Hay {len(humanos)} humanos en la lista\n"
      #f"Hay {len(males)} hombres en la lista del total de  {len(df['name'])}")

#Diccionario con los valores de los episodios donde aparece cada uno

apar_episodios = apariciones(rick_morty)

#GRAFICO DE LAS APARICIONES

names = list(apar_episodios.keys())
valores = list(apar_episodios.values())


plt.bar(names,valores,width=.6)
plt.title('Apariciones en Episodios')
plt.xlabel('Personajes')
plt.ylabel('Cantidad De Episodios')
plt.xticks(fontsize=7)

plt.show()