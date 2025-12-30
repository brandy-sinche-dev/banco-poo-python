from exceptions.usuario_ya_existe import UsuarioYaExiste

class Banco:
    def __init__(self):
        self.usuarios = []

    def agregar_usuario(self, usuario):
        for u in self.usuarios:
            if u.dni == usuario.dni:
                raise UsuarioYaExiste("DNI duplicado")
        self.usuarios.append(usuario)

    def buscar_usuario(self, dni):
        for u in self.usuarios:
            if u.dni == dni:
                return u
        return None
