from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pandas as pd
from genera_tablas import Provincia
from configuracion import cadena_base_datos

# se genera en enlace al gestor de base de datos
# para el ejemplo se usa la base de datos sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

# leer el archivo de datos

data = pd.read_csv('data/Listado-Instituciones-Educativas.csv', delimiter='|')

#Almacenamiento de las columnas que nos sirven (Codigo y Provincia)

columnas_especificas = data[['Código División Política Administrativa Provincia', 'Provincia']]
valores_unicos = columnas_especificas.drop_duplicates()

print(valores_unicos)

for index, row in valores_unicos.iterrows():
    codigo_division = row['Código División Política Administrativa Provincia']
    provincia1 = row['Provincia']
    print(codigo_division, provincia1)

    provincia = Provincia(codigoProvincia= int(codigo_division), nombreProvincia=provincia1)
    session.add(provincia)

session.commit()