from datetime import datetime

class cuenta:

    total_abiertas = 0
    
    existen = dict()

    def __init__(self,cliente,saldo):
        cuenta.total_abiertas += 1
        self.cliente = cliente
        self.saldo = saldo
        self.numero = f"{cuenta.total_abiertas:04d}"
        self.fecha_apertura = datetime.now()
        cuenta.existentes[self.numero] = self
        print(f"Cuenta creada con exito \nNumero de cuenta: {self.numero} Titular: {self.cliente}  Creada el: {self.fecha_apertura}")

    def __str__(self):
        return f"Cuenta nro: {self.numero}, Titular: {self.cliente}, Saldo: {self.saldo}$"
    

    def depositar(self,monto):
        if monto < 0:
            print("ERROR: el monto no puede ser negativo")
        else:
            self.saldo+= monto
            print(f"Se deposito exitosamente {monto}$ en la cuenta{self.numero}. Su nuevo saldo es {self.saldo}$")

    def retirar(self,monto):
        if monto < 0:
            print("ERROR: el monto no puede ser negativo")
        elif monto > self.saldo:
            print("ERROR: fondo insuficiente")
        else:
            self.saldo-= monto
            print(f"Se retiro exitosamente {monto}$ de la cuenta{self.numero}. Su nuevo saldo es de: {self.saldo}$")
 
    def transferir(self,monto,otra_cuenta):
        if monto < 0:
            print("ERROR: el monto no puede ser negativo")
        elif monto > self.saldo:
            print("ERROR: fondo insuficiente")
        if otra_cuenta not in cuenta.existentes:
            print("ERROR: cuenta destino no existente")
        else:
            self.saldo-= monto
            cuenta.existentes[otra_cuenta].saldo += monto
            print(f"Se transfirio {monto}$ de la cuenta nro: {self.numero} a la cuenta nro: {otra_cuenta}")

    def getSaldo(self):
        return self.saldo
    


opcion = -1

while (6 != opcion):
        opcion = int(input("""
                           
*********************************
Ingrese una operacion a realizar:
                           
1-Crear cuenta
2-Estatus cuenta
3-Depositar
4-Retirar
5-Transferir
6-Salir
*********************************                       
"""))
        if opcion == 1:
            print("Creando una cuenta: ")
            nombre = input("Ingrese nombre y apellido del titular: ")
            saldo = int(input("Ingrese saldo inicial: "))
            c1 = cuenta(nombre,saldo)

        if opcion == 2:
            print("Revisando estatus de la cuenta: ")
            numero = input("Ingrese numero de cuenta: ")

            if numero in cuenta.existentes:
                cuenta_actual = cuenta.existentes[numero]
                print("Datos de la cuenta:")
                print(cuenta_actual)
            else:
                print("La cuenta ingresada no existe.")

        if opcion == 3:
            print("Deposito bancario:  ")
            numero = input("Ingrese numero de cuenta a depositar: ")
            monto = int(input("Ingrese monto: "))

            if numero in cuenta.existentes:
                cuenta_actual = cuenta.existentes[numero]
                cuenta_actual.depositar(monto)  
            else:
                print("La cuenta ingresada no existe.")

        if opcion == 4:
            print("Retirar: ")
            numero = input("Ingrese numero de cuenta a retirar: ")
            monto = int(input("Ingrese monto: "))

            if numero in cuenta.existentes:
                cuenta_actual = cuenta.existentes[numero]
                cuenta_actual.retirar(monto)  
            else:
                print("La cuenta ingresada no existe.")

        if opcion == 5:
            print("Transferir a terceros: ")
            numero = input("Ingrese numero de tu cuenta: ")
            monto = int(input("Ingrese monto: "))
            otra = input("Ingrese numero de cuenta a transferir: ")

            if numero in cuenta.existentes:
                cuenta_actual = cuenta.existentes[numero]
                cuenta_actual.transferir(monto, otra)  
            else:
                print("La cuenta ingresada no existe.")


            

        

                
            
