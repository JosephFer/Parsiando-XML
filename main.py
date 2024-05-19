import xml.etree.ElementTree as ET
from ElementoPadre import *
from Visitador import *

def construirArbolXML(ruta_archivo):
    try:
        arbol = ET.parse(ruta_archivo)
        raiz = arbol.getroot()

        def procesarNodo(nodo):
            nombre = nodo.tag
            atributos = nodo.attrib
            contenido = nodo.text.strip() if nodo.text else None

            if nodo.findall("*"):
                elementos_hijo = [procesarNodo(hijo) for hijo in nodo]
                return ElementoPadre(nombre, atributos, elementos_hijo)
            else:
                return ElementoHijo(nombre, atributos, contenido)

        return procesarNodo(raiz)
    
    except ET.ParseError as e:
        print(f"Error al parsear el XML: {e}")
        return None

def main():
    rutaArchivoXML = "./archivosEjemplos./archivo.xml" 
    arbolXML = construirArbolXML(rutaArchivoXML)

    
    if arbolXML:
        visitador = VisitadorImprimir()
        arbolXML.procesar(visitador, nivel=0)

if __name__ == "__main__":
    main()