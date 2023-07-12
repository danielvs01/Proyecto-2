# Profe, esta calculadora está en fase beta, por lo que sólo se puede hacer 1 operación a la vez :)
# l para borrar el historial y q para salir de la calculadora, enter para el resultado

import os

def calculadora():
    while True:
        entrada = input("")
        
        if entrada == "q":
            break
        
        if entrada == "l":
            limpiar_terminal()
            continue
        
        primer_numero, operador, segundo_numero = saber_entrada(entrada)
        if operador == "+":
            resultado = primer_numero + segundo_numero
        elif operador == "-":
            resultado = primer_numero - segundo_numero
        elif operador == "*":
            resultado = primer_numero * segundo_numero
        elif operador == "/":
            resultado = primer_numero / segundo_numero
        print("=", resultado)

def saber_entrada(entrada):
    partes = entrada.split("+")
    if len(partes) == 2:
        return float(partes[0]), "+", float(partes[1])
    
    partes = entrada.split("-")
    if len(partes) == 2:
        return float(partes[0]), "-", float(partes[1])
    
    partes = entrada.split("*")
    if len(partes) == 2:
        return float(partes[0]), "*", float(partes[1])
    
    partes = entrada.split("/")
    if len(partes) == 2:
        return float(partes[0]), "/", float(partes[1])

def limpiar_terminal():
    if os.name == 'nt':
        os.system('cls')

calculadora()