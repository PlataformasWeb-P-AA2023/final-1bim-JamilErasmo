from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos, echo = True)

Base = declarative_base()


#Tiene tres columnas: id, codigoProvincia y nombreProvincia
#La clase también tiene una relación de uno a muchos con la clase Canton a través del atributo cantones

class Provincia(Base):
    __tablename__ = 'provincia'
    id = Column(Integer, primary_key=True)
    codigoProvincia = Column(Integer, nullable=False)
    nombreProvincia = Column(String(100)) 

    cantones = relationship("Canton", back_populates="provincias")

    def __repr__(self):
        return "Provincia: id=%d codigoPronvicia=%d nomnreProvincia=%s" % (
                          self.id, 
                          self.codigoProvincia, 
                          self.nombreProvincia)

#Tiene cuatro columnas: id, codigoCanton, nombreCanton y provincia_id
class Canton(Base):
    __tablename__ = 'canton'
    id = Column(Integer, primary_key=True)
    codigoCanton = Column(Integer)
    nombreCanton = Column(String(100), nullable=False)

    provincia_id = Column(Integer, ForeignKey('provincia.id'))

    provincias  = relationship("Provincia", back_populates="cantones")

    parroquias = relationship("Parroquia", back_populates="cantones")
    
    def __repr__(self):
        return "id: %d - codigoCanton: %d - nombreCanton: %s - pronvicia_id: %d" % (
                self.id, self.codigoCanton, self.nombreCanton, self.provincia_id)
    
class Parroquia(Base):  
    __tablename__ = 'parroquia'
    id = Column(Integer, primary_key=True)
    codigoParroquia = Column(Integer)
    nombreParroquia = Column(String(100), nullable=False)

    canton_id = Column(Integer, ForeignKey('canton.id'))

    cantones = relationship("Canton", back_populates="parroquias")

    instituciones = relationship("Institucion", back_populates="parroquias") 
    
    def __repr__(self):
        return "id: %d - codigoParroquia: %d - nombreParroquia: %s - canton_id: %d" % (
                self.id, self.codigoParroquia, self.nombreParroquia, self.canton_id)


class Institucion(Base):
    __tablename__ = 'institucion'
    id = Column(Integer, primary_key=True)
    amie = Column(String(100))
    nombre_institucion = Column(String(100))
    codigo_Distrito = Column(String(100))
    sostenimiento = Column(String(100))
    tipoEducacion = Column(String(100))
    modalidad = Column(String(100))
    jornada = Column(String(100))
    acceso = Column(String(100))
    numEstudiantes = Column(Integer)
    numDocentes = Column(Integer)

    parroquia_id = Column(Integer, ForeignKey('parroquia.id'))

    parroquias = relationship("Parroquia", back_populates="instituciones")   

Base.metadata.create_all(engine)