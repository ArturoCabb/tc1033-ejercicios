import ejercicio5

class VehiclesIU:
    def __init__(self):
        self.matricula
        self.medio
        self.capacidad
        self.velocidad

    def terrestres(self, _matricula, _medio, _capacidad_pasajeros, 
                   _velocidad_maxima):
        self.matricula = _matricula
        self.medio = _medio
        self.capacidad = _capacidad_pasajeros
        self.velocidad = _velocidad_maxima
        self.caracteristicas = [Caracteristicas()]
        self.rueda = [Ruedas()]
        lista = [self.matricula,self.medio,self.capaciad,
                 self.velocidad,self.caracteristicas,
                 self.rueda]
        return lista

    def maritimos(self, _propulsion, _matricula, _medio, 
                  _capacidad_pasajeros, _velocidad_maxima):
        self.propulsion = _propulsion
        self.matricula = _matricula
        self.medio = _medio
        self.capacidad = _capacidad_pasajeros
        self.velocidad = _velocidad_maxima
        lista = [self.propulsion,self.matricula,self.medio,self.capaciad,
                 self.velocidad,self.caracteristicas,
                 self.rueda]
        return lista

    def aereos(self, _matricula, _medio, _capacidad_pasajeros, 
               _velocidad_maxima):
        self.matricula = _matricula
        self.medio = _medio
        self.capaciad = _capacidad_pasajeros
        self.velocidad = _velocidad_maxima
        self.caracteristicas = [Caracteristicas()]
        lista = [self.matricula,self.medio,self.capaciad,
                 self.velocidad,self.caracteristicas,
                 self.rueda]
        return lista
    
class Caracteristicas:
    def __init__(self):
        self.gasolina
        self.diesel
        self.turbosina
        self.fabricante
        self.potencia

class Ruedas:
    def __init__(self):
        self.tamaño
        self.presion
        self.fabricante

class VehiclesDP:
    def __init__(self):
        self

    def lista(self,a,t,m):
        lista_aereos = a
        lista_terrestres = t
        lista_maritimos = m
        regreso = (lista_aereos + "\n\r" + lista_terrestres 
                   + "\n\r" + lista_maritimos)
        return regreso

if __name__ == "__main__":
    while 1:
        print("1.Interactiar con el programa\n\r2.Salir")
        entrada = int(input())
        lista = ""
        if entrada == 1:
            v = VehiclesIU()
            matricula = input("Ingrese matricula")
            medio = input("Ingrese medio")
            capacidad = input("Ingrese capacidad")
            velocidad = input("Ingrese velocidad")
            x = v.terrestres(matricula,medio,capacidad,velocidad)
            propulsion = input("Ingrese propulsion")
            matricula = input("Ingrese matricula")
            medio = input("Ingrese medio")
            capacidad = input("Ingrese capacidad")
            velocidad = input("Ingrese velocidad")
            y = v.maritimos(propulsion,matricula,medio,capacidad,velocidad)
            matricula = input("Ingrese matricula")
            medio = input("Ingrese medio")
            capacidad = input("Ingrese capacidad")
            velocidad = input("Ingrese velocidad")
            z = v.aereos(matricula,medio,capacidad,velocidad)
            lista = VehiclesDP().lista(x,y,z)
        elif entrada == 2:
            print(lista)
            aaa = ejercicio5.VehiclesAD().metodo(lista)
            break