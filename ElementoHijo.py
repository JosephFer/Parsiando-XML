import xml.etree.ElementTree as ET
from ElementoXml import *

class ElementoHijo(ElementoXML):
      
    def __init__(self, nombre, atributos, contenido):
        super().__init__(nombre, atributos)
        self.contenido = contenido

    def __str__(self):
        return f"{super().__str__()}>{self.contenido}</{self.nombre}>"

    def procesar(self, visitador, nivel):
        visitador.visitarHoja(self, nivel)  # Polimorfismo de inclusion: Invocación del método visitar_hoja dependiendo del tipo de objeto.
