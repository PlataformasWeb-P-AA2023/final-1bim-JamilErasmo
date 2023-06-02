from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func, distinct
# se genera enlace al gestor de base de datos para el ejemplo se usa la base de datos sqlite

from genera_tablas import Provincia, Canton, Parroquia, Institucion
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

# Los establecimientos ordenados por número de estudiantes; que tengan más de 100 profesores

consulta = session.query(Institucion).order_by(Institucion.numEstudiantes).filter(
    Institucion.numDocentes > 100).all()

for institucion in consulta:
    print(institucion.id, institucion.nombre_institucion)

print("----------------------")
print("Consulta 2")
# Los establecimientos ordenados por número de profesores; que tengan más de 100 profesores

consulta2 = session.query(Institucion).order_by(Institucion.numDocentes).filter(
    Institucion.numDocentes > 100).all()


for institucion in consulta2:
    
    print(institucion.id, institucion.nombre_institucion)