from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ 
from genera_tablas import Institucion, Parroquia, Provincia, Canton
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de datos para el ejemplo se usa la base de datos sqlite

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

establecimiento = session.query(Institucion).all()
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

#recuperamos todos los institucion que pertenecen a la Parroquia con un código de 110553, utilizando una operación de unión (join)

Institucion = session.query(Institucion).join(Parroquia, Canton, Provincia).filter(Parroquia.codigo == 110553).all()
print("Todos las instituciones que pertenecen al Código División Política Administrativa Parroquia con valor 110553")
for e in Institucion:
    print(e, "\n")

# Establecimientos de la provincia del Oro, el resultado se almacena en la variable establecimientos.
Institucion = session.query(Institucion).join(Parroquia, Canton, Provincia).filter(Provincia.provincia == 'EL ORO').all()
print("Todos las instituciones de la provincia del Oro.")
for e in Institucion:
    print(e, "\n")

# Establecimientos del cantón de Portovelo.
Institucion = session.query(Institucion).join(Parroquia, Canton).filter(Canton.canton == 'PORTOVELO').all()
print("Todos las instituciones del cantón de Portovelo.")
for e in Institucion:
    print(e, "\n")

# Establecimientos del cantón de Zamora.
Institucion = session.query(Institucion).join(Parroquia, Canton).filter(Canton.canton == 'ZAMORA').all()
print("Todos los instituciones del cantón de Zamora.")
for e in Institucion:
    print(e, "\n")

