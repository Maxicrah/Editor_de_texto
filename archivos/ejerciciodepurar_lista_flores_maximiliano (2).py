# -*- coding: utf-8 -*-
"""Ejerciciodepurar_lista_Flores_Maximiliano.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LfMiXmFzk1zM5RlFLbyydWPGdUtQY_6R

Definir una función que reciba 2 parámetros, el primero de ellos es un booleano y el segundo una lista de números enteros. La función deberá depurar dicha lista de números enteros, eliminando todos los números pares en caso de que el primer parámetro sea True y en caso contrario, cuando el primer parámetro sea False, serán eliminados los números impares que se encuentren en la lista.
"""

def depurar_numeros(par,lista):
  """funcion que recorre lista de impares o pares (segun lo que desee el usuario)"""
  lista_imp=[]
  lista_par=[]
  if par == True:
      for num in lista:
          if not num % 2 == 0:
           lista_imp.append(num)
      return lista_imp      
              
  else:
        for num in lista:
          if  num % 2 == 0:
            lista_par.append(num)
        return lista_par     

numeros = [11, 7, 21, 32, 41, 2, 40]
print(depurar_numeros(False,numeros))

# list of numbers
list1 = [10, 21, 4, 45, 66, 93]
 
# iterating each number in list
for num in list1:
 
    # checking condition
    if num % 2 == 0:
        print(num)