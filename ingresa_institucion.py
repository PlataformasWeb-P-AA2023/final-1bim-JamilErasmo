from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pandas as pd

from genera_tablas import Canton, Provincia, Institucion, Parroquia
from configuracion import cadena_base_datos

# se genera en enlace al gestor de base de datos
# para el ejemplo se usa la base de datos sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()
# leer el archivo de datos
data = pd.read_csv('data/Listado-Instituciones-Educativas.csv', delimiter='|')

# Creacion de cada objeto de tipo establecimiento
print(data.columns)
columnas_especificas = data[['Código AMIE', 'Nombre de la Institución Educativa',\
                             'Código División Política Administrativa  Parroquia', 'Código de Distrito',\
                             'Sostenimiento', 'Tipo de Educación', 'Modalidad', 'Jornada',\
                             'Acceso (terrestre/ aéreo/fluvial)', 'Número de estudiantes',\
                             'Número de docentes']]
valores_unicos = columnas_especificas.drop_duplicates()

print(valores_unicos)

for index, row in valores_unicos.iterrows():

    amie1 = row['Código AMIE']
    institucion1 = row['Nombre de la Institución Educativa']
    codigo_divisionP = row['Código División Política Administrativa  Parroquia']
    codigo_Distrito1 = row['Código de Distrito']
    sostenimiento1 = row['Sostenimiento']
    tipoEducacion1 = row['Tipo de Educación']
    modalidad1 = row['Modalidad']
    jornada1 = row['Jornada']
    acceso1 = row['Acceso (terrestre/ aéreo/fluvial)']
    numEstudiante1 = row['Número de estudiantes']
    numDocentes1 = row['Número de docentes']

    parroquia = session.query(Parroquia).filter_by(codigoParroquia=codigo_divisionP).one()

    institucion = Institucion(amie = amie1, nombre_institucion = institucion1, codigo_Distrito = codigo_Distrito1,
                              sostenimiento = sostenimiento1, tipoEducacion = tipoEducacion1, modalidad = modalidad1,
                              jornada = jornada1, acceso = acceso1, numEstudiantes = numEstudiante1,
                              numDocentes = numDocentes1, parroquias = parroquia)
    
    session.add(institucion)

session.commit()