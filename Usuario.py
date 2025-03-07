class Usuario:
    def __init__(self, nombre_de_usuario, contrasena):
        self.nombre_de_usuario = nombre_de_usuario
        self.contrasena = contrasena
    
    def iniciar_sesion(self, nombre, contrasena):
        return self.nombre_de_usuario == nombre and self.contrasena == contrasena

class Administrador(Usuario):
    def gestionar_usuarios(self):
        return "Gestionando usuarios..."

class Cliente(Usuario):
    def realizar_compra(self):
        return "Realizando compra..."

admin = Administrador("admin", "3105")
cliente = Cliente("cliente", "abcd")

print("Inicio de sesión admin:", admin.iniciar_sesion("admin", "3105"))
print("Inicio de sesión cliente:", cliente.iniciar_sesion("cliente", "abcd"))
print(admin.gestionar_usuarios())
print(cliente.realizar_compra())
