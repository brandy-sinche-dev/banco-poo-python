from models.movimiento import Movimiento
from exceptions.monto_invalido import MontoInvalido

class Cuenta:
    def __init__(self, saldo):
        self._saldo = saldo
        self.movimientos = []

    def obtener_saldo(self):
        return self._saldo

    def agregar_saldo(self, monto):
        if monto <= 0:
            raise MontoInvalido("Monto inválido")
        self._saldo += monto
        self.movimientos.append(Movimiento("DEPOSITO", monto))

    def restar_saldo(self, monto):
        if monto <= 0 or monto > self._saldo:
            raise MontoInvalido("Saldo insuficiente o monto inválido")
        self._saldo -= monto
        self.movimientos.append(Movimiento("RETIRO", monto))
