from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from utils.connection_db import SessionLocal, engine, Base
import operations.operations_db as ops
from data.models import Usuario

Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Usuarios y Tareas", description="Parcial 2")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.post("/usuarios/")
def crear_usuario(nombre: str, correo: str, estado_id: int, db: Session = Depends(get_db)):
    return ops.crear_usuario(db, nombre, correo, estado_id)


@app.get("/usuarios/")
def obtener_usuarios(db: Session = Depends(get_db)):
    return ops.obtener_usuarios(db)


@app.get("/usuarios/{usuario_id}")
def obtener_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario = ops.obtener_usuario(db, usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario


@app.patch("/usuarios/{usuario_id}/estado")
def actualizar_estado(usuario_id: int, nuevo_estado_id: int, db: Session = Depends(get_db)):
    return ops.actualizar_estado_usuario(db, usuario_id, nuevo_estado_id)


@app.patch("/usuarios/{usuario_id}/premium")
def hacer_usuario_premium(usuario_id: int, db: Session = Depends(get_db)):
    return ops.actualizar_estado_usuario(db, usuario_id, nuevo_estado_id=2)


@app.get("/usuarios/inactivos/")
def usuarios_inactivos(db: Session = Depends(get_db)):
    return db.query(Usuario).filter(Usuario.estado_id == 3).all()


@app.get("/usuarios/premium-inactivos/")
def usuarios_premium_inactivos(db: Session = Depends(get_db)):
    return db.query(Usuario).filter(Usuario.estado_id.in_([2, 3])).all()
