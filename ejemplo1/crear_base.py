from sqlalchemy import create_engine

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite

from configuracion import engine

#Es la superclase que necesitan todas las clases que las van a vincular con SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


from sqlalchemy import Column, Integer, String

class Saludo(Base):
    __tablename__ = 'saludos'

    id = Column(Integer, primary_key=True)
    mensaje = Column(String(200))
    tipo = Column(String(200))


"""
class Saludo2(Base):
    __tablename__ = 'saludo2'
    id = Column(Integer, primary_key=True)
    mensaje = Column(String(200))
    tipo = Column(String(200))
    origen = Column(String(200))
"""

Base.metadata.create_all(engine)
