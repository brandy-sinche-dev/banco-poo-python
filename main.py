import json
from models.banco import Banco
from models.usuario import Usuario
from models.cuenta import Cuenta
from models.movimiento import Movimiento
from exceptions.monto_invalido import MontoInvalido

ARCHIVO = "data/banco.json"

def cargar_banco():
    banco = Banco()
    try:
        with open(ARCHIVO, "r") as f:
            data = json.load(f)
            for u in data:
                cuenta = Cuenta(u["saldo"])
                for m in u["movimientos"]:
                    cuenta.movimientos.append(Movimiento(m["tipo"], m["monto"]))
                banco.usuarios.append(Usuario(u["dni"], u["nombre"], cuenta))
    except FileNotFoundError:
        pass
    return banco

def guardar_banco(banco):
    data = []
    for u in banco.usuarios:
        data.append({
            "dni": u.dni,
            "nombre": u.nombre,
            "saldo": u.cuenta.obtener_saldo(),
            "movimientos": [
                {"tipo": m.tipo, "monto": m.monto}
                for m in u.cuenta.movimientos
            ]
        })
    with open(ARCHIVO, "w") as f:
        json.dump(data, f, indent=4)

banco = cargar_banco()

while True:
    dni = input("Ingrese DNI: ")
    usuario = banco.buscar_usuario(dni)

    if usuario:
        break
    print("Usuario no encontrado")

while True:
    print("1. Saldo\n2. Depositar\n3. Retirar\n4. Movimientos\n5. Salir")
    try:
        op = int(input("Opción: "))
    except ValueError:
        continue

    try:
        if op == 1:
            print("Saldo:", usuario.cuenta.obtener_saldo())
        elif op == 2:
            usuario.cuenta.agregar_saldo(float(input("Monto: ")))
            print("Saldo Actualizado: ", usuario.cuenta.obtener_saldo())
        elif op == 3:
            usuario.cuenta.restar_saldo(float(input("Monto: ")))
            print("Saldo actualizado: ",usuario.cuenta.obtener_saldo())
        elif op == 4:
            for m in usuario.cuenta.movimientos:
                print(m.tipo, m.monto)
        elif op == 5:
            guardar_banco(banco)
            break
    except MontoInvalido as e:
        print(e)
