from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base

class Asignatura(Base):
    __tablename__ = "asignaturas"

    asig_id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(30))
    creditos = Column(Integer)
    secciones = relationship("Seccion", back_populates="asignatura")
