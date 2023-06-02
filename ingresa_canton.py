from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pandas as pd

from genera_tablas import Canton, Provincia
from configuracion import cadena_base_datos
# se genera en enlace al gestor de base de datos
# para el ejemplo se usa la base de datos sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()
# leer el archivo de datos
# Separar cada columna del CSV
data = pd.read_csv('data/Listado-Instituciones-Educativas.csv', delimiter='|')
# Almacanar 
columnas_especificas = data[['Código División Política Administrativa Provincia', \
                             'Código División Política Administrativa  Cantón', 'Cantón']]
valores_unicos = columnas_especificas.drop_duplicates()

print(valores_unicos)

for index, row in valores_unicos.iterrows():
    codigo_divisionP = row['Código División Política Administrativa Provincia']
    codigo_division = row['Código División Política Administrativa  Cantón']
    canton1 = row['Cantón']

    provincia = session.query(Provincia).filter_by(codigoProvincia=codigo_divisionP).one()

    print(codigo_division, canton1)

    canton = Canton(codigoCanton=int(codigo_division), nombreCanton=canton1, provincias=provincia)
    session.add(canton)

session.commit()


