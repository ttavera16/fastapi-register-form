from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from app.core.database import Base

class Docente(Base):
    __tablename__ = "docentes"

    doc_id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(30))
    apellidos = Column(String(50))
    cedula = Column(String(11))
    fecha_nacimiento = Column(Date)
    sexo = Column(String(15))
    secciones = relationship("Seccion", back_populates="docente")
