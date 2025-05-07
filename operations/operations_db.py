'''Aqui debes construir las operaciones que se te han indicado'''

from sqlalchemy.orm import Session
from data.models import Usuario, EstadoUsuario, EstadoTarea, Tarea


def crear_usuario(db: Session, nombre: str, correo: str, estado_id: int):
    nuevo_usuario = Usuario(nombre=nombre, correo=correo, estado_id=estado_id)
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario


def obtener_usuarios(db: Session):
    return db.query(Usuario).all()


def obtener_usuario(db: Session, usuario_id: int):
    return db.query(Usuario).filter(Usuario.id == usuario_id).first()


def actualizar_estado_usuario(db: Session, usuario_id: int, nuevo_estado_id: int):
    usuario = obtener_usuario(db, usuario_id)
    if usuario:
        usuario.estado_id = nuevo_estado_id
        db.commit()
        db.refresh(usuario)
    return usuario




def crear_estado_usuario(db: Session, nombre: str):
    estado = EstadoUsuario(nombre=nombre)
    db.add(estado)
    db.commit()
    db.refresh(estado)
    return estado


def obtener_estados_usuario(db: Session):
    return db.query(EstadoUsuario).all()



def crear_estado_tarea(db: Session, nombre: str):
    estado = EstadoTarea(nombre=nombre)
    db.add(estado)
    db.commit()
    db.refresh(estado)
    return estado


def obtener_estados_tarea(db: Session):
    return db.query(EstadoTarea).all()




def crear_tarea(db: Session, titulo: str, descripcion: str, usuario_id: int, estado_id: int):
    tarea = Tarea(titulo=titulo, descripcion=descripcion, usuario_id=usuario_id, estado_id=estado_id)
    db.add(tarea)
    db.commit()
    db.refresh(tarea)
    return tarea


def obtener_tareas(db: Session):
    return db.query(Tarea).all()


def obtener_tareas_por_usuario(db: Session, usuario_id: int):
    return db.query(Tarea).filter(Tarea.usuario_id == usuario_id).all()
