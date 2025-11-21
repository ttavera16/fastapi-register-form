from fastapi import FastAPI, Form, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse, HTMLResponse
from sqlalchemy.orm import Session
from datetime import datetime
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI

# ← IMPORTA tu DB y modelos desde los nuevos módulos
from app.core.database import Base, engine, SessionLocal, get_db
from app.models.asignatura import Asignatura
from app.models.estudiante import Estudiante
from app.models.docente import Docente
from app.models.seccion import Seccion

# Crear tablas (si no existen)
Base.metadata.create_all(bind=engine)

# Siembra simple (opcional, y solo una vez)
def seed_asignaturas_si_faltan():
    db = SessionLocal()
    try:
        if not db.query(Asignatura).first():
            asignaturas = [
                Asignatura(nombre="Matemáticas", creditos=4),
                Asignatura(nombre="Física", creditos=3),
                Asignatura(nombre="Programación", creditos=5),
                Asignatura(nombre="Algoritmos y Estructuras de Datos", creditos=4),
                Asignatura(nombre="Bases de Datos", creditos=4),
                Asignatura(nombre="Desarrollo Web", creditos=3),
                Asignatura(nombre="Inteligencia Artificial", creditos=4),
                Asignatura(nombre="Machine Learning", creditos=4)
            ]
            db.add_all(asignaturas)
            db.commit()
    finally:
        db.close()

app = FastAPI()
# Monta la carpeta static
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")  # usa "app/templates" si las mueves

@app.on_event("startup")
def on_startup():
    seed_asignaturas_si_faltan()

# Rutas
@app.get("/")
def inicio(request: Request):
    return templates.TemplateResponse("inicio.html", {"request": request})

@app.get("/registro_est")
def mostrar_formulario_estudiante(request: Request):
    return templates.TemplateResponse("registro_est.html", {"request": request})

@app.get("/registro_doc")
def mostrar_formulario_docente(request: Request):
    return templates.TemplateResponse("registro_doc.html", {"request": request})

@app.post("/seleccionar_formulario")
def seleccionar_formulario(tipo_usuario: str = Form(...)):
    if tipo_usuario == "estudiante":
        return RedirectResponse(url="/registro_est", status_code=303)
    elif tipo_usuario == "docente":
        return RedirectResponse(url="/registro_doc", status_code=303)
    else:
        return {"error": "Selección no válida"}

@app.post("/registro_est", response_class=HTMLResponse)
def registrar_estudiante(
    request: Request,
    nombre: str = Form(...),
    apellidos: str = Form(...),
    cedula: str = Form(...),
    matricula: str = Form(...),
    fecha_nacimiento: str = Form(...),
    sexo: str = Form(...),
    seccion_id: int = Form(...),
    db: Session = Depends(get_db),
):
    estudiante = Estudiante(
        nombre=nombre,
        apellidos=apellidos,
        cedula=cedula,
        matricula=matricula,
        fecha_nacimiento=datetime.strptime(fecha_nacimiento, "%Y-%m-%d"),
        sexo=sexo,
        seccion_id=seccion_id,
    )
    db.add(estudiante)
    db.commit()
    db.refresh(estudiante)
    return templates.TemplateResponse("exito.html", {"request": request, "mensaje": "Estudiante registrado con éxito"})

@app.post("/registro_doc", response_class=HTMLResponse)
def registrar_docente(
    request: Request,
    nombre: str = Form(...),
    apellidos: str = Form(...),
    cedula: str = Form(...),
    fecha_nacimiento: str = Form(...),
    sexo: str = Form(...),
    db: Session = Depends(get_db),
):
    docente = Docente(
        nombre=nombre,
        apellidos=apellidos,
        cedula=cedula,
        fecha_nacimiento=datetime.strptime(fecha_nacimiento, "%Y-%m-%d"),
        sexo=sexo,
    )
    db.add(docente)
    db.commit()
    db.refresh(docente)
    return templates.TemplateResponse("exito.html", {"request": request, "mensaje": "Docente registrado con éxito"})
