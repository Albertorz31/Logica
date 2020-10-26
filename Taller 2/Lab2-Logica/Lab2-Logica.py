#!/usr/bin/env python
# coding: utf-8

# Laboratorio N°2 Lógica y Teoría de la Computación
# Tema: Lógica Difusa
# Profesor: Daniel Vega Araya
# Integrantes: Diego Águila Tornería
#              Carlos Alvarez Silva
#              Alberto Rodríguez Zamorano
#              Chun-Zen Yu Chávez

import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import sys
import random
import getopt


############ BASE DE CONOCIMIENTOS #################

'''
#Proceso: Define los rangos y las funciones de pertenencia para los antecentes que son la forma,firmeza y cobertura
#Salida: Funciones de pertenencia de las entradas.
def definirAntecedentes():
    forma = ctrl.Antecedent(np.arange(0, 101, 1), 'forma')
    firmeza = ctrl.Antecedent(np.arange(0, 101, 1), 'firmeza')
    cobertura = ctrl.Antecedent(np.arange(0, 101, 1), 'cobertura')
'''


def generar_selector(altura,diametro,transparencia,coberturaE):

    #FUSIFICADOR

    # Antecedentes 
    # functions
    forma = ctrl.Antecedent(np.arange(0, 101, 1), 'forma')
    firmeza = ctrl.Antecedent(np.arange(0, 101, 1), 'firmeza')
    cobertura = ctrl.Antecedent(np.arange(0, 101, 1), 'cobertura')

    #Consecuentes
    calidad = ctrl.Consequent(np.arange(0, 11, 1), 'calidad')
    


    # Funcion de membresia de cada conjunto difuso 
    #Antecedentes
    etiqueta_forma = ['Angosta', 'Normal', 'Ancha']
    forma.automf(names=etiqueta_forma)
    etiqueta_firmeza = ['Podrida', 'Madura', 'Verde']
    firmeza.automf(names=etiqueta_firmeza)
    etiqueta_cobertura = ['Leve', 'Parcial', 'Completa']
    cobertura.automf(names=etiqueta_cobertura)

    #Consecuentes
    etiqueta_calidad = ['Desecho', 'Comercial', 'Exportable']
    calidad.automf(names=etiqueta_calidad)


    #La salida por la cual saldrá el fruto depende del diametro ingresado por el usuario
    if(diametro>= 18 and diametro<19):
        salida = 1
    elif(diametro>= 19 and diametro<20):
        salida = 2
    elif(diametro>= 20 and diametro<21):
        salida = 3
    elif(diametro>= 21 and diametro<22):
        salida = 4
    elif(diametro>=22 and diametro<23):
        salida = 5 
    elif(diametro>= 23 and diametro<24):
        salida=6
    elif(diametro>= 24 and diametro<25):
        salida=7
    elif(diametro>= 25 and diametro<26):
        salida=8
    elif(diametro>=26 and diametro<27):
        salida=9
    elif(diametro>=27 and diametro<28):
        salida=10
    elif(diametro>=28 and diametro<29):
        salida=11
    elif(diametro>=29 and diametro<30):
        salida=12
    elif(diametro>=30 and diametro<31):
        salida=13
    elif(diametro>= 31 and diametro<32):
        salida=14
    elif(diametro>=32 and diametro<33):
        salida=15

    # Caso particular menor a 18 mm o mayor a 33 (Desecho)
    elif(diametro<18 or diametro >=33):
        salida=16


    ############################DESCOMENTAR SI SE QUIERE VER GRAFICOS#############################
    # Mostrar gráficas componentes modelo
    #graficos antecedentes
    forma.view()
    #pausa()
    firmeza.view()
    #pausa()
    cobertura.view()
    #pausa()
    


    ###################SISTEMA DE INFERENCIA##########################

    #Aqui ocurre la logica principal del programa ya que se definen las reglas de la logica difusa de antecedentes->consecuencias y luego se calculan las 
    #defusificaciones de los valores concecuentes, los cuales son enviados para ser escritos en un archivo de texto.

    #####Reglas difusas####

    #La funcion Rule, crea las reglas a utilizar en la logica difusa, donde se anotan los antecedentes, con las variables logicas and, or, not segun corresponda
    #aplicando internamente mamdani

    #Finalmente, al realizar la defusificacion se usa ControlSystem para poder juntar todas las reglas y obtener los valores que mas se acomoden a las reglas.
    #Con controlSystemSimulation se simula el sistema difuso, y finalmente con input se ingresan las entradas. 
    

    #EL diametro definirá a cual salida debe ir cada cereza 
    
    rule1 = ctrl.Rule(forma['Angosta'] & firmeza['Verde'] & cobertura['Leve'], calidad['Exportable'])
    rule2 = ctrl.Rule(forma['Angosta'] & firmeza['Verde'] & cobertura['Parcial'], calidad['Comercial'])
    rule3 = ctrl.Rule(forma['Angosta'] & firmeza['Verde'] & cobertura['Completa'], calidad['Desecho'])
    rule4 = ctrl.Rule(forma['Angosta'] & firmeza['Madura'] & cobertura['Leve'], calidad['Exportable'])
    rule5 = ctrl.Rule(forma['Angosta'] & firmeza['Madura'] & cobertura['Parcial'], calidad['Comercial'])
    rule6 = ctrl.Rule(forma['Angosta'] & firmeza['Madura'] & cobertura['Completa'], calidad['Desecho'])
    rule7 = ctrl.Rule(forma['Angosta'] & firmeza['Podrida'] & cobertura['Leve'], calidad['Desecho'])
    rule8 = ctrl.Rule(forma['Angosta'] & firmeza['Podrida'] & cobertura['Parcial'], calidad['Desecho'])
    rule9 = ctrl.Rule(forma['Angosta'] & firmeza['Podrida'] & cobertura['Completa'], calidad['Desecho'])

    rule10 = ctrl.Rule(forma['Normal'] & firmeza['Verde'] & cobertura['Leve'], calidad['Exportable'])
    rule11 = ctrl.Rule(forma['Normal'] & firmeza['Verde'] & cobertura['Parcial'], calidad['Exportable'])
    rule12 = ctrl.Rule(forma['Normal'] & firmeza['Verde'] & cobertura['Completa'], calidad['Desecho'])
    rule13 = ctrl.Rule(forma['Normal'] & firmeza['Madura'] & cobertura['Leve'], calidad['Exportable'])
    rule14 = ctrl.Rule(forma['Normal'] & firmeza['Madura'] & cobertura['Parcial'], calidad['Exportable'])
    rule15 = ctrl.Rule(forma['Normal'] & firmeza['Madura'] & cobertura['Completa'], calidad['Desecho'])
    rule16 = ctrl.Rule(forma['Normal'] & firmeza['Podrida'] & cobertura['Leve'], calidad['Desecho'])
    rule17 = ctrl.Rule(forma['Normal'] & firmeza['Podrida'] & cobertura['Parcial'], calidad['Desecho'])
    rule18 = ctrl.Rule(forma['Normal'] & firmeza['Podrida'] & cobertura['Completa'], calidad['Desecho'])

    rule19 = ctrl.Rule(forma['Ancha'] & firmeza['Verde'] & cobertura['Leve'], calidad['Exportable'])
    rule20 = ctrl.Rule(forma['Ancha'] & firmeza['Verde'] & cobertura['Parcial'], calidad['Exportable'])
    rule21 = ctrl.Rule(forma['Ancha'] & firmeza['Verde'] & cobertura['Completa'], calidad['Desecho'])
    rule22 = ctrl.Rule(forma['Ancha'] & firmeza['Madura'] & cobertura['Leve'], calidad['Exportable'])
    rule23 = ctrl.Rule(forma['Ancha'] & firmeza['Madura'] & cobertura['Parcial'], calidad['Comercial'])
    rule24 = ctrl.Rule(forma['Ancha'] & firmeza['Madura'] & cobertura['Completa'], calidad['Desecho'])
    rule25 = ctrl.Rule(forma['Ancha'] & firmeza['Podrida'] & cobertura['Leve'], calidad['Desecho'])
    rule26 = ctrl.Rule(forma['Ancha'] & firmeza['Podrida'] & cobertura['Parcial'], calidad['Desecho'])
    rule27 = ctrl.Rule(forma['Ancha'] & firmeza['Podrida'] & cobertura['Completa'], calidad['Desecho'])
    

    # Control system
    selector_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10,
                                    rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19, rule20,
                                    rule21, rule22, rule23, rule24, rule25, rule26, rule27])

    selector = ctrl.ControlSystemSimulation(selector_ctrl)
    # Entradas de la Simulación
    selector.input['forma'] = diametro/altura
    selector.input['firmeza'] = transparencia
    selector.input['cobertura'] = coberturaE
    # Computar resultados
    selector.compute()
    # Mostrar resultados
    #calidad.view(sim=selector)
    #pausa()

    escribir_archivo( (altura,diametro,transparencia,coberturaE), (forma, firmeza,cobertura,calidad,salida))


    plt.show() # Descomentar si se quieren observar los graficos

    #escribir_archivo(altura,diametro,transparencia,coberturaE,forma,)

    return


'''
Función que escribe en un archivo de texto las salidas
Entrada: antecedentes->Arreglo con antecedentes, salidas->Arreglo con salidas defusificada
Proceso: Se escribe en el archivo los elementos de los arreglos de entrada
Salida:
'''
def escribir_archivo(antecedentes,salidas):  
    file = open("Cereza_" + str(antecedentes[0]) + "_" + str(antecedentes[1]) + "_" + str(antecedentes[2]) + "_" + str(antecedentes[3])+".txt", 'w')
    file.write("Niveles capturados: \n")
    file.write("\t Calibre:" +str(antecedentes[1])+"mm\n")
    file.write("\t Forma:" + str(salidas[0])+"\n")
    file.write("\t Firmeza de la pulpa:"+str(salidas[1])+"\n")
    file.write("\t Cobertura de manchas:"+str(salidas[2])+"\n")
    file.write("Comercialización:" + str(salidas[3])+"\n")
    file.write("Número salida:"+str(salidas[4])+ "\n")
    file.close()




''' 
Función que pausa la ejecución del programa
Entrada:
Proceso: Se printea un mensaje y se espera a una entrada cualquiera
Salida:
'''
def pausa():
    print("Ingrese un caracter para continuar: ")
    input()



def main(argv):
    #### MAIN ####

    altura = 1
    diametro = 1
    transparencia = 10
    cobertura = 15

    #Puede tener maximo

    try:
        opts, _ = getopt.getopt(sys.argv[1:], 'a:d:t:c:', ['altura=', 'diametro=', 'transparencia=', 'cobertura='])
    except getopt.GetoptError:
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-a', '--altura'):
            altura = int(arg)
        elif opt in ('-d', '--diametro'):
            diametro = int(arg)
        elif opt in ('-t', '--transparencia'):
            transparencia = int(arg)
        elif opt in ('-c', '--cobertura'):
            cobertura = int(arg)

    generar_selector(altura,diametro,transparencia,cobertura)

    return


if __name__ == "__main__":
    main(sys.argv[1:])