from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pandas as pd
from genera_tablas import Canton, Parroquia
from configuracion import cadena_base_datos

# se genera en enlace al gestor de base de datos
# para el ejemplo se usa la base de datos sqlite

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

# leer el archivo de datos
 # Separar cada columna del CSV
 
data = pd.read_csv('data/Listado-Instituciones-Educativas.csv', delimiter='|')

#Almacenamiento de las columnas que nos sirven (Codigo de canton, codigo parroquia y parroquia)

columnas_especificas = data[['Código División Política Administrativa  Cantón', \
                             'Código División Política Administrativa  Parroquia', 'Parroquia']]
valores_unicos = columnas_especificas.drop_duplicates()

print(valores_unicos)

# Variable que devuelve la provincia de cada canton

for index, row in valores_unicos.iterrows():
    codigo_divisionC = row['Código División Política Administrativa  Cantón']
    codigo_division = row['Código División Política Administrativa  Parroquia']
    parroquia1 = row['Parroquia']

    canton = session.query(Canton).filter_by(codigoCanton=codigo_divisionC).one()

    print(codigo_divisionC,codigo_division, parroquia1)

    parroquia = Parroquia(codigoParroquia=int(codigo_division), nombreParroquia=parroquia1, cantones=canton)
    session.add(parroquia)

session.commit()