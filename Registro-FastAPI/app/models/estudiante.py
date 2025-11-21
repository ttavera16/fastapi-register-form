from sqlalchemy import Column, Integer, String, Date, ForeignKey
from app.core.database import Base

class Estudiante(Base):
    __tablename__ = "estudiantes"

    est_id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(30))
    apellidos = Column(String(50))
    cedula = Column(String(15))
    matricula = Column(String(15))
    fecha_nacimiento = Column(Date)
    sexo = Column(String(15))
    seccion_id = Column(Integer, ForeignKey("secciones.sec_id"))
