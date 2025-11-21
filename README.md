# fastapi-register-form

Aplicación web desarrollada con FastAPI, SQLAlchemy, Jinja2, HTML, CSS y estructura modular.
Permite registrar estudiantes y docentes en una base de datos, seleccionando secciones y asignaturas.
**
¿Qué hace el proyecto?**

Muestra una página de inicio donde el usuario puede elegir si desea registrar un estudiante o un docente.

Cada formulario permite ingresar información personal como:

-nombre
-apellidos
-cédula
-fecha de nacimiento
-sexo
-(En el caso de estudiantes) número de matrícula y sección

Los datos enviados se guardan en la base de datos.
Luego de registrar la información, la aplicación muestra un mensaje de éxito.
**
Estructura básica**

El proyecto está organizado en una carpeta app/ con:

main.py → archivo principal con las rutas de la aplicación

templates/ → archivos HTML

static/ → estilos CSS u otros archivos estáticos

models/ → modelos utilizados para guardar los datos

core/ → configuración de la base de datos




**
Treisi Tavera**
Estudiante de Analítica y Ciencia de Datos — ITLA
