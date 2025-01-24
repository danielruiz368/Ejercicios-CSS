class empleados():
    numero_empleado = 0

    def __init__(self, nombre, apellido, cargo,salario):
        self.nombre = nombre
        self.apellido = apellido
        self.cargo = cargo
        self.salario = salario
        empleados.numero_empleado += 1

    def presentacion(self):
        print(f"Hola, soy {self.nombre} {self.apellido} y trabajo como {self.cargo}")

    def aumentar_salario(self, porcentaje):
        self.salario += self.salario * porcentaje / 100
        print(f"El nuevo salario de {self.nombre} {self.apellido} es de {self.salario}")

    @classmethod
    def numero_empleados(cls , datos_empleado):
        nombre, apellido, cargo, salario = datos_empleado.split(",")
        return cls(nombre, apellido, cargo, salario)
    
    @staticmethod
    def es_feriado(dia):
        feriados = ["1 , 10 , 25"]
        return dia in feriados
    

empleado1 = empleados.numero_empleados("Juan,Perez,Programador,2000")
empleado2 = empleados.numero_empleados("Maria,Gomez,Diseñador,2500")

empleado1.presentacion()
empleado2.presentacion()

print(empleados.es_feriado(10))


print("-------------------------------------------------------------")
#abstraccion

class vehiculo():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.encendido = False
        self.velocidad = 0

    def encender(self):
        self.encendido = True
        print("El vehiculo se ha encendido")

    def apagar(self):
        self.encendido = False
        print("El vehiculo se ha apagado")
        
    def acelerar(self, incremento):
        self.velocidad += incremento
        print(f"El vehiculo acelera a {self.velocidad} km/h")
    
    def frenar(self, decremento):
        if self.encendido:
            self.velocidad -= decremento
            print(f"El vehiculo frena a {self.velocidad} km/h")
        else:
            self.velocidad = 0
            print("El vehiculo se ha detenido") 
    

coche = vehiculo("Toyota", "Corolla")
coche.encender()
coche.acelerar(30)
coche.frenar(10)
coche.apagar()


print("-------------------------------------------------------------")
#encapsulamiento

class cuenta_bancaria():
    def __init__(self, numero_cuenta, titular, saldo):
        self.numero_cuenta = numero_cuenta
        self.titular = titular #atributo protegido
        self.__saldo = saldo #atributo privado
    def get_saldo(self):
        return self.__saldo
    
    def depositar(self, cantidad):
        self.__saldo += cantidad
        print(f"Se ha depositado {cantidad} en la cuenta de {self.titular}")
    
    def retirar(self, cantidad):
        if self.__saldo >= cantidad:
            self.__saldo -= cantidad
            print(f"Se ha retirado {cantidad} de la cuenta de {self.titular}")
        else:
            print("Fondos insuficientes")

cuenta = cuenta_bancaria("1234567890", "Juan Perez", 1000)
print(cuenta.get_saldo())
cuenta.depositar(500)
cuenta.retirar(200)
print(cuenta.get_saldo())

#herencia

class vehiculo_electrico(vehiculo):
    def __init__(self, marca, modelo, bateria):
        super().__init__(marca, modelo)
        self.bateria = bateria

