# API Rest: interfaz de programacion de aplicaciones para transferir/compartir recursos

from fastapi import FastAPI, HTTPException
from typing import List, Optional
from pydantic import BaseModel
import uuid

# Inicializamos una variable donde tendrá todas las caracteristicas de una API REst
app = FastAPI()


# Acá definimos el modelo
class Curso(BaseModel):
    id: Optional[str] = None
    nombre: str
    descripcion: Optional[str] = None
    nivel: str
    duracion: int


# Simularemos una base de datos
cursos_db = []


# CRUD: Read (lectura) GET ALL: leeremos todos los cursos que haya en la db
@app.get("/cursos/", response_model=List[Curso])
def obtener_cursos():
    return cursos_db


# CRUD: Create (escribirt) POST: agregaremos un nuevo curso a nuestra base de datos
@app.post("/cursos/", response_model=Curso)
def crear_curso(curso: Curso):
    curso.id = str(uuid.uuid4())  # Usamos uuid para generar un ID unico e irrepetible
    cursos_db.append(curso)
    return curso


# CRUD Read: (lectura) GET (individual): Leeremos el curso que coincida con el id que pidamos
@app.get("/cursos/{curso_id}", response_model=Curso)
def obtener_curso(curso_id: str):
    curso = next(
        (curso for curso in cursos_db if curso.id == curso_id), None
    )  # Con next tomamos la primera coincidencia del array devuelto
    if curso is None:
        raise HTTPException(status_code=404, detail="curso no encontrado")
    return curso


# CRUD Update: (modificar) PUT: modificaremos un recurso que coincida con el ID que mandemos
@app.put("/cursos/{curso_id}", response_model=Curso)
def actualizar_curso(curso_id: str, curso_actualizado: Curso):
    curso = next(
        (curso for curso in cursos_db if curso.id == curso_id), None
    )  # Con next tomamos la primera coincidencia del array devuelto
    if curso is None:
        raise HTTPException(status_code=404, detail="curso no encontrado")
    curso_actualizado.id = curso_id
    index = cursos_db.index(
        curso
    )  # Buscamos el indice exacto donde está el curso en nuestra lista (DB)
    cursos_db[index] = curso_actualizado
    return curso_actualizado


# CRUD Delete: eliminaremos un recurso que coincida con el ID  que mandemos
@app.delete("/cursos/{curso_id}", response_model=Curso)
def eliminar_curso(curso_id: str):
    curso = next(
        (curso for curso in cursos_db if curso.id == curso_id), None
    )  # Con next tomamos la primera coincidencia del array devuelto
    if curso is None:
        raise HTTPException(status_code=404, detail="curso no encontrado")
    cursos_db.remove(curso)
    return curso
