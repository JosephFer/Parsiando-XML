import xml.etree.ElementTree as ET
from ElementoPadre import *

class Visitador:
    """Interfaz para definir cómo procesar los elementos XML."""

    def visitar(self, elemento):
        raise NotImplementedError

    def visitarHoja(self, elementoHoja):
        raise NotImplementedError

    def visitarPadre(self, elementoPadre, elementoHijo):
        raise NotImplementedError
    


class VisitadorImprimir(Visitador):
    """Visitador que imprime la información de los elementos XML."""

    def visitar(self, elemento):
        print(f"Elemento: {elemento.nombre}")
        print(f"Atributos: {elemento.atributos}")

    def visitarHoja(self, elementoHoja, nivel):
        atributos_str = " ".join(f'{k}="{v}"' for k, v in elementoHoja.atributos.items())
        print(f"{'    ' * nivel}Elemento: {elementoHoja.nombre} {atributos_str}")
        if elementoHoja.contenido is not None:
            print(f"{'    ' * (nivel+1)}Contenido: {elementoHoja.contenido}")

    def visitarPadre(self, elementoPadre, elementoHijo, nivel=0):
        atributos_str = " ".join(f'{k}="{v}"' for k, v in elementoPadre.atributos.items())
        print(f"{'    ' * nivel}Elemento: {elementoPadre.nombre} {atributos_str}")
        print(f"{'    ' * nivel}SubElementos:")
        for elemento_hijo in elementoHijo:
            elemento_hijo.procesar(self, nivel + 1)  # Polimorfismo de inclusion: Invocación del método procesar dependiendo del tipo de objeto.