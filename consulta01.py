from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ 
from generar_tablas import Institucion, Parroquia, Provincia, Canton
from configuracion import cadena_base_datos
engine = create_engine(cadena_base_datos)

