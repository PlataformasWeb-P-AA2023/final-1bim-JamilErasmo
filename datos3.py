from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func, distinct

from genera_tablas import Provincia, Canton, Parroquia, Institucion

from configuracion import cadena_base_datos

# se genera enlace al gestor de base de datos para el ejemplo se usa la base de datos sqlite

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

# Los cantones que tiene establecimientos con 0 número de profesores, 5 profesores, 11, profesores
num_Docentes = [0, 5, 11]

consulta = session.query(Canton).join(Parroquia).join(Institucion).filter(
    Institucion.parroquia_id == Parroquia.id,
    Parroquia.canton_id == Canton.id,
    Institucion.numDocentes.in_(num_Docentes)
    ).distinct()

# Establecimientos que pertenecen a la parroquia Pindal con estudiantes mayores o iguales a 21

for canton in consulta:
    print(canton.id ,canton.nombreCanton)

print("---------------------------")
print("Consulta 2\n")

consulta2 = session.query(Institucion).join(Parroquia).filter(Parroquia.id == Institucion.parroquia_id,\
    Parroquia.nombreParroquia == "PINDAL", Institucion.numEstudiantes >= 21).distinct()

for institucion in consulta2:
    print(institucion.id, institucion.nombre_institucion)
