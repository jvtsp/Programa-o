#!/bin/usr/python
import re, os

def Nome():
    nome = str(input('nome: '))
    if re.findall('[!@#$%&*()_+{}?:>1234567890/;]', nome):
       print('Error') 
       Nome()
    else:
       print('Normal')
       Numero()
def Numero():
    numero = str(input('Número: '))
    if re.findall('', numero):
	print('')
    else:
	print('')   

Nome()
