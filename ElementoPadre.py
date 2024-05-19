import xml.etree.ElementTree as ET
from ElementoHijo import *
from ElementoXml import *

class ElementoPadre(ElementoXML):
    """Clase para representar elementos XML padre (con subelementos)."""
    
    # Herencia: ElementoPadre hereda de ElementoXML
    def __init__(self, nombre, atributos, elementosHijos):
        super().__init__(nombre, atributos)
        self.elementosHijos = elementosHijos
        
    def __str__(self, nivel=0):
        elemento_str = f"{super().__str__()}\n"
        for hijo in self.elementosHijos:
            elemento_str += f"{'    ' * (nivel+1)}{hijo.__str__(nivel+1)}\n"
        elemento_str += f"{'    ' * nivel}</{self.nombre}>"
        return elemento_str

    def procesar(self, visitador, nivel):
        visitador.visitarPadre(self, self.elementosHijos, nivel)  # Polimorfismo de inclusion: Invocación del método visitar_padre dependiendo del tipo de objeto.

