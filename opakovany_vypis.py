# -*- coding: utf-8 -*-
"""
Vzorový program python
Name: opakovany_vypis
Author: Miroslav Janota
"""

def vypis(a):
    for b in range(a):
        print("číslo -", b)
        
a=int(input("Zadej počet opakování: "))
vypis(2*a)
       
