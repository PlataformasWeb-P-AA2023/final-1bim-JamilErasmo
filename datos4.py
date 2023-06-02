from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func, distinct

# se importa la clase(s) del  archivo genera_tablas

from genera_tablas import Provincia, Canton, Parroquia, Institucion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de datos para el ejemplo se usa la base de datos sqlite

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

# Los establecimientos ordenados por nombre de parroquia que tengan más de 40 profesores y la cadena "Educación regular" en tipo de educación.

consulta = session.query(Institucion).join(Parroquia).order_by(Parroquia.nombreParroquia).filter(
    Parroquia.id == Institucion.parroquia_id, Institucion.numDocentes > 40, 
    Institucion.tipoEducacion == "Educación regular").all()


# Establecimientos ordenados por sostenimiento y tengan código de distrito 11D04.
for institucion in consulta:
    print(institucion.id, institucion.nombre_institucion)

print("-----------------------")
print("Consulta 2\n")

consulta2 = session.query(Institucion).order_by(Institucion.sostenimiento).filter(
    Institucion.codigo_Distrito != "11D04").all()

for institucion in consulta2:
    print(institucion.id, institucion.nombre_institucion)