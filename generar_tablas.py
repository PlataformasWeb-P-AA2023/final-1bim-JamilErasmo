from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Table

# se importa información del archivo configuracion
from configuracion import cadena_base_datos

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Base = declarative_base()
           


class Distrito(Base):
    __tablename__ = 'distrito'
    id = Column(Integer, primary_key=True)
    descripcion = Column(String(100))
    canton = relationship("Canton", back_populates="distrito")

  
  
  

class Provincia(Base):
    __tablename__ = 'provincia'
    cod = Column(Integer, primary_key=True)
    provincia = Column(String(250))
    canton = relationship("Canton", back_populates="provincia")

    
    


class Canton(Base):
    __tablename__ = 'canton'
    cod = Column(Integer, primary_key=True)
    canton = Column(String(250))
    id_provincia = Column(Integer, ForeignKey('provincia.cod'))
    id_distrito = Column(Integer, ForeignKey('distrito.id'))


    provincia = relationship("Provincia", back_populates="canton")
    distrito = relationship("Distrito", back_populates="canton")

    parroquia = relationship("Parroquia", back_populates="canton")

   
    


class Parroquia(Base):
    __tablename__ = 'parroquia'
    cod = Column(Integer, primary_key=True)
    parroquia = Column(String(250))
    id_canton = Column(Integer, ForeignKey('canton.cod'))

    canton = relationship("Canton", back_populates="parroquia")

    institucion = relationship("Institucion", back_populates="parroquia")

   




class Institucion(Base):
    __tablename__ = 'institucion'
    cod = Column(String(20), primary_key=True)
    nombre = Column(String(550))
    num_est = Column(Integer)
    num_doc = Column(Integer)

    modalidad = Column(String(300))
    jornada = Column(String(300))


    id_parroquia = Column(Integer, ForeignKey('parroquia.cod'))
    id_acceso = Column(Integer, ForeignKey('tipo_acceso.id'))
    id_sostenimiento = Column(Integer, ForeignKey('tipos_sostenimiento.id'))
    id_tipo_educacion = Column(Integer, ForeignKey('tipos_educacion.id'))

    tipo_acceso = relationship("Tipo_acceso", back_populates="instituciones")
    tipos_sostenimiento = relationship("Tipos_sostenimiento", back_populates="institucion")
    tipos_educacion = relationship("Tipos_educacion", back_populates="institucion")
    parroquia = relationship("Parroquia", back_populates="institucion")
    





Base.metadata.create_all(engine)