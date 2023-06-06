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

#Se filtran los establecimientos según los números de profesores especificados en la lista num_Docentes
consulta = session.query(Canton).join(Parroquia).join(Institucion).filter(
    Institucion.parroquia_id == Parroquia.id,
    Parroquia.canton_id == Canton.id,
    Institucion.numDocentes.in_(num_Docentes)
    ).distinct()

#Se itera sobre la consulta anterior y se imprime el ID y el nombre de cada cantón
for canton in consulta:
    print(canton.id ,canton.nombreCanton)

print("---------------------------")
print("Consulta 2\n")

#Se filtran los establecimientos según la parroquia "Pindal" y la cantidad de estudiantes mayor o igual a 21.

consulta2 = session.query(Institucion).join(Parroquia).filter(Parroquia.id == Institucion.parroquia_id,\
    Parroquia.nombreParroquia == "PINDAL", Institucion.numEstudiantes >= 21).distinct()
#Se itera sobre la consulta anterior y se imprime el ID y el nombre de cada intitucion
for institucion in consulta2:
    print(institucion.id, institucion.nombre_institucion)
