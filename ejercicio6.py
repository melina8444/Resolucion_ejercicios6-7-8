""" 6. Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los
siguientes métodos para la clase:
 Un constructor, donde los datos pueden estar vacíos.
 Los setters y getters para cada uno de los atributos. Hay que validar las entradas de
datos.
 mostrar(): Muestra los datos de la persona.
 Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad. """

import ejercicio_excepciones #con esto importo a todas las excepciones


class Persona():
    def __init__(self, nombre="", edad=0, dni=""):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    @property
    def nombre(self):
        return self.__nombre
        
    @property
    def edad(self):
        return self.__edad
        
    @property
    def dni(self):
        return self.__dni
        
    @nombre.setter
    def nombre(self, nuevo_dato):
        self.__nombre = nuevo_dato

    def __validar_dni(self, numero):
        try:
            dni = int(numero)
        except ValueError:
            mensaje = f"Persona con DNI incorrecto: {dni}"
            print(mensaje)
            raise ejercicio_excepciones.PersonaDatoInvalidoError(mensaje)
        if len (str(dni))< 7:
            mensaje = f"Persona con DNI incorrecto: {dni}"
            print(mensaje)
            raise ejercicio_excepciones.PersonaDatoInvalidoError(mensaje)
        
    @dni.setter
    def dni(self, nuevo_dato):
        self.__validar_dni(nuevo_dato)
        self.__dni= int(nuevo_dato)

    @edad.setter
    def edad (self, nuevo_dato):
        if nuevo_dato < 0:
            mensaje = f"Persona con edad Incorrecta{nuevo_dato}"
            print(mensaje)
            raise ejercicio_excepciones.PersonaDatoInvalidoError(mensaje)
        else:
            self.__edad = nuevo_dato

    def mostrar(self):
        return f"Nombre: {self.nombre},Edad: {str(self.edad)},Dni: {self.dni}"

    def mayor_edad(self):
        return self.edad >= 18


