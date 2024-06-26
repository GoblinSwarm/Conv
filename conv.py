
"""
Created on Sat Sep  3 21:14:58 2022

@author: Daniel Perdomo
"""

import xml.etree.cElementTree as ET
import os
import tkinter
from tkinter import filedialog 



def cabezal(elemento):

    header={}
        #Este elemento crea el cabezal y lo devuelve para el posterior armado
    aux= elemento.get('MATRICULA_MEDIO_TRANSPORTE')
    header.setdefault('IDENTIFICATION', aux)
    header.setdefault('DIRECTION', '1')
    fecha= elemento.get('FECHA_PROGRAMADA_TRANSPORTE')
    header.setdefault('FECHA', fecha)
    header.setdefault('METODOCARGA', '3')
    
    return header

def armadoPersona(elemento, nuevoNombre):
    pax={}
    archivo=nuevoNombre
    #Este elemento rearma a las personas del buque con los datos correspondientes
    if elemento.get('TRIPULANTE_PASAJERO') == 'T':
        pax.setdefault('Categoria', 'RTP')
    else:
        pax.setdefault('Categoria', 'NGN')
    
    pax.setdefault('IdDocumentosTipos', elemento.get('TIPO_DOCUMENTO'))
    pax.setdefault('IdPaisEmisor', elemento.get('PAIS_DOCUMENTO'))
    
    if elemento.get('PAIS_DOCUMENTO')== 'ARG' and elemento.get('NACIONALIDAD')!= 'ARG':
        pax.setdefault('IdDocumentosSubtipos', 'DNI')
    elif elemento.get('NACIONALIDAD')=='ARG' and elemento.get('TIPO_DOCUMENTO')=='ID':
        pax.setdefault('IdDocumentosSubtipos', 'DNI')
    else:
        pax.setdefault('IdDocumentosSubtipos', 'SIN')
    
    pax.setdefault('DocNumero', elemento.get('NUMERO_DOCUMENTO'))
    pax.setdefault('Apellido1', elemento.get('PRI_APELLIDO'))
    pax.setdefault('Apellido2', elemento.get('SEG_APELLIDO'))
    pax.setdefault('Nombre1', elemento.get('PRI_NOMBRE'))
    pax.setdefault('Nombre2', elemento.get('SEG_NOMBRE'))
    pax.setdefault('IdNacionalidad', elemento.get('NACIONALIDAD'))
    pax.setdefault('FecNac', elemento.get('FEC_NAC'))
    pax.setdefault('Sexo', elemento.get('SEXO'))
    pax.setdefault('DocVto', '')
    pax.setdefault('Direccion', '')
    pax.setdefault('IdOcupacion', '')
    
    #guardo2(pax, nuevoNombre)
    return pax

def nombreArch(header):
    #Header identification, header es un sub elemento de Manifiesto
    var1=header.get('IDENTIFICATION')
    var2=header.get('FECHA')
    #aux1=var1[10:]
    try:
        var2=var2.replace(':', ' ')
        var2=var2.replace('/', '-')
        nombreArchivo=var1 + ' ' + var2 + '.xml'
    except: 
        label.configure(text='El barco que se intenta ingresar no es de la empresa correspondiente o ya fue trabajado')
    return nombreArchivo

def guardo(header, barco, nuevoNombre):
    
    carpeta='./Barcos/'
    if os.path.exists(carpeta)==False:
        os.mkdir(carpeta)
    archivo=nuevoNombre
    
    rootoutput=ET.Element("MANIFIESTO")
    arbol = ET.ElementTree(rootoutput)
   
    ET.SubElement(rootoutput, 'HEADER', header)
    for pax in barco:
        ET.SubElement(rootoutput, 'ROW' , barco[pax])
    
    arbol.write(carpeta+archivo, xml_declaration=True, encoding="ISO-8859-1")
    #arbol.write(archivo)
        
    return

def main():
    
    direccion=label.cget("text")
    
    
    if '.xml' in direccion:
        archivo=ET.parse(direccion)
        root=archivo.getroot()
        aux=''
        cont= 0
        header={}
        pasajeros={}
        barco={}
        
        for elemento in root:
            #Esto imprime la lista de personas en el barco
            #imprimoPersona(elemento)
            if cont == 0:
                header=cabezal(elemento)
                nuevoNombre= nombreArch(header)
                cont= cont+1
            else:
                pasajeros= armadoPersona(elemento, nuevoNombre)
                barco[cont]=pasajeros
                cont=cont+1

        guardo(header, barco, nuevoNombre)    
        
        mensaje= cont-1 ,'pasajeros'
        
        label2.configure(text=mensaje)   
    else:
        label.configure(text='Primero seleccione un barco a convertir')
        
def explorador(): 
    #Si o si hay que ponerle todos los archivos.
    nombreArchivo = filedialog.askopenfilename(initialdir = "/", title = "Selecciona un archivo", 
                                          filetypes = (("Archivos xml","*.xml*"), 
                                                       ("all files", 
                                                        "*.*"))) 
    if nombreArchivo != '':
        label.configure(text=nombreArchivo) 
    else: 
        label.configure(text='Ingrese el archivo a convertir')
    return   


#---------------------------------------------------------------
#Ventana
top = tkinter.Tk()
top.geometry("600x100")   
#---------------------------------------------------------------
#Etiquetas
var = tkinter.StringVar()
label= tkinter.Label(top, text='Ingrese el archivo a convertir')
label2= tkinter.Label(top, text='')
#---------------------------------------------------------------
#Boton '...'
direccion=''
bot= tkinter.Button(top, text = 'Selecciona el archivo XML a convertir', command= explorador)
bot.pack()
#Boton 'de convertir'
convertir = tkinter.Button(top, text = 'Convertir', command= lambda: main())
convertir.pack()
#----------------------------------------------------------------
label.pack()
label2.pack()
top.mainloop()

