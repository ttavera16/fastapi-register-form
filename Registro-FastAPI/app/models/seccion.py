from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Seccion(Base):
    __tablename__ = "secciones"

    sec_id = Column(Integer, primary_key=True, index=True)
    tanda = Column(String(40))
    aula = Column(String(20))
    asignatura_id = Column(Integer, ForeignKey("asignaturas.asig_id"))
    docente_id = Column(Integer, ForeignKey("docentes.doc_id"))

    asignatura = relationship("Asignatura", back_populates="secciones")
    docente = relationship("Docente", back_populates="secciones")
