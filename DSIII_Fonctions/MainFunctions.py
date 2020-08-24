# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 14:27:12 2018

@author: pixel14
"""
from DSIII_Classes.Personnage import Perso
from DSIII_Classes.Item import Arme, Consommable, ForgeItem
import DSIII_Classes.Enum as E
import Globals as G
import Tools as T
import MenuDivers as Menu

import random as R



def MainGame():
    while G.ContinueGame:
        if G.joueur == False:
            Menu.MenuNewGame()
        else:
            Menu.MenuPrincipal()

def NewHero():
    T.Cls()
    print("--- Création d'un nouveau héros ---\n")
    nom = input("Quel est le nom de votre personnage ?\n")
    #choix de la classe
    Menu.MenuChoixClasse(nom)
    print("\nCréation du personnage OK...!")    
    T.NextStep()
    print("\nPuisse votre aventure se faire dans la souffrance, {}...".format(G.joueur.Nom))
    T.NextStep()

def GestionPersonnage():
    G.StayInMenuPerso = True
    Menu.MenuPersonnage()

def TestFunc():
    T.Cls()
    print("--- FONCTION DE TEST / DEV SPACE ---\n")
    
    T.NextStep()

def GenererEnnemi(niveau):
    points = niveau + 90
    prefixList = ["Phalange", "Ombre", "Carcasse", "Squelette", "Réanimé", "Assassin", "Gargouille", "Sorcier", "Chien-Zombie", "Chevalier"]
    nameList = ["Boucher", "DarkSasougay", "Orochipartu", "Naizu", "Gérard", "Nexflix-Fanboy", "Netflix-Fangirl", "Quick-addict", "Ronald", "Serge"]
    nom = R.choice(prefixList) + " " + R.choice(nameList)
    caracList = [0,0,0,0,0,0,0,0,0]
    while points > 0:
        carac = R.randint(0, 8)
        caracList[carac] +=1
        points -= 1
    E = Perso(nom, caracList[0], caracList[1], caracList[2], caracList[3], caracList[4], caracList[5], caracList[6], caracList[7], caracList[8])
    return E

def GenererArme(degBaseMin, degBaseMax, totalRatio):
    """nom, pxAchat, pxVente, poids, baseDeg, ratioForce, ratioDex, ratioInt, ratioFoi, ratioLuck"""
    points = totalRatio
    nameList = ["Dague", "Épée", "Lance", "Masse"]
    suffixList = ["Longue", "Lourde", "Magique", "Chaotique", "Bénie", "Tempêtueuse", "Ténébreuse"]
    nom = R.choice(nameList) + " " + R.choice(suffixList)
    degBase = R.randint(degBaseMin, degBaseMax)
    poids = (R.randint(5, 50) / 10)
    caracList = [0, 0, 0, 0, 0]
    while points > 0:
        carac = R.randint(0, 4)
        caracList[carac] += 0.1
        points -= 0.1
    W = Arme(nom, 100, 100, poids, degBase, caracList[0], caracList[1], caracList[2], caracList[3], caracList[4])
    return W

def GenererLootAmes():
    return R.randint(30, 1200)

def FightTurn(Atk, Def):
    if type(Atk) is Perso and type(Def) is Perso:
        Attaquant = Atk
        Defenseur = Def
        print("--- COMBAT ---\n")
        print("Tour de {} ->\n".format(Attaquant.Nom))
        Attaquant.Attaquer(Defenseur)

def Combat():
    T.Cls()
    ennemi = GenererEnnemi(10)
    w = GenererArme(1, 10, 5)
    ennemi.EquiperArme(w, False)
    print("Nouveau Combat !!! L'ennemi {} apparait !!".format(ennemi.Nom))
    T.NextStep()
    
    while(G.joueur.Hp > 0 and ennemi.Hp > 0):
        FightTurn(G.joueur, ennemi)
        if ennemi.Hp > 0:
            FightTurn(ennemi, G.joueur)

    if(G.joueur.Hp == 0):
        G.joueur.Mourir()
    elif(ennemi.Hp == 0):
        print("Vous avez remporté le combat et il vous reste {} points de vie !!".format(G.joueur.Hp))
        G.joueur.GagnerAmes(GenererLootAmes())
    
    T.NextStep()
    
   