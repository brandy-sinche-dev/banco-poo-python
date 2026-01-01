from exceptions.usuario_ya_existe import UsuarioYaExiste
from models.usuario import Usuario
from models.cuenta import Cuenta
class Banco:
    def __init__(self):
        self.usuarios = []

    def agregar_usuario(self, dni, nombre):
        usuario = Usuario(dni,nombre,Cuenta(0.00))
        for u in self.usuarios:
            if u.dni == dni:
                raise UsuarioYaExiste("Esta cuenta ya ha sido registrado")
        self.usuarios.append(usuario)


    def buscar_usuario(self, dni):
        for u in self.usuarios:
            if u.dni == dni:
                return u
        return None
