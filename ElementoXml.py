import xml.etree.ElementTree as ET

class ElementoXML:
    def __init__(self, nombre, atributos):
        self.nombre = nombre
        self.atributos = atributos

    def __str__(self):
        atributos_str = " ".join(f'{k}="{v}"' for k, v in self.atributos.items())
        return f"<{self.nombre} {atributos_str}>"

    def atributos_str(self):
        if self.atributos:
            return " ".join(f'{k}="{v}"' for k, v in self.atributos.items())
        else:
            return ""

    def procesar(self, visitador):
        # Polimorfismo de inclusion: Invocación del método visitar 
        # dependiendo del tipo de objeto.
        visitador.visitar(self)  
