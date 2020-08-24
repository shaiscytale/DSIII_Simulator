# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 09:27:25 2018

@author: pixel14
"""

import os

def Cls():
    os.system('cls' if os.name=='nt' else 'clear')

def NextStep():
    input("\nAppuyez sur ENTER pour continuer...")
    Cls()

def Revive():
    input("\nAppuyez sur ENTER pour revenir au dernier feu de camp...")
    Cls()
    
def InputChoice(mess, mini, maxi, errMess="Erreur : valeur invalide"):
    choix = None
    
    while choix is None:
        choix = input(mess)
        try:
            choix = int(choix)
            if choix < mini or choix > maxi:
                choix = None
            else:
                return choix
        except:
            choix = None
        
        if choix is None:
            print(errMess)
    
    
    