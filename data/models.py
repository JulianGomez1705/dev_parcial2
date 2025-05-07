'''Aqui debes consignar el modelo que se te indico en el parcial
Escribe aquí el que te corresponde.

'''


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from utils.connection_db import Base  # asegúrate de que Base esté importado


class EstadoUsuario(Base):
    __tablename__ = "estados_usuario"
    id = Column(Integer, primary_key=True)
    nombre = Column(String, unique=True)
    usuarios = relationship("Usuario", back_populates="estado")


class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    correo = Column(String, unique=True)
    estado_id = Column(Integer, ForeignKey("estados_usuario.id"))
    estado = relationship("EstadoUsuario", back_populates="usuarios")
    tareas = relationship("Tarea", back_populates="usuario")


class EstadoTarea(Base):
    __tablename__ = "estados_tarea"
    id = Column(Integer, primary_key=True)
    nombre = Column(String, unique=True)
    tareas = relationship("Tarea", back_populates="estado")


class Tarea(Base):
    __tablename__ = "tareas"
    id = Column(Integer, primary_key=True)
    titulo = Column(String)
    descripcion = Column(String)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    estado_id = Column(Integer, ForeignKey("estados_tarea.id"))
    usuario = relationship("Usuario", back_populates="tareas")
    estado = relationship("EstadoTarea", back_populates="tareas")