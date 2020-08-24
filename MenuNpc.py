# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 14:47:03 2018

@author: pixel14
"""
import Globals as G
import Tools as T


def MenuGardienneDuFeu():
    while G.StayInMenuGardienneDuFeu:
        T.Cls()
        print("--- Gardienne du Feu ---\n")
        print("1 -> Dépenser âmes ({0} âmes / {1} pour le prochain niveau)".format(G.joueur.Ames, G.joueur.AmesNextLevel))
        print("2 -> Discuter")
        print("3 -> Prendre congé")
        choix = T.InputChoice("\nChoisissez une option en tapant le nombre associé : ", 1, 3, "Veuillez saisir une option entre 1 et 3 SVP")
        LancerFonctionGardienneDuFeu(choix)

def LancerFonctionGardienneDuFeu(choix):
    if choix == 1:        
        #dépenser un niveau
        G.joueur.MonterNiveau()
    elif choix == 2:
        print("dialogue avec Gardienne du Feu")
        T.NextStep()
    elif choix == 3:
        G.StayInMenuGardienneDuFeu = False

def MenuServante():
    while G.StayInMenuServante:
        T.Cls()
        print("--- Servante du Sanctuaire ---\n")
        print("1 -> Acheter")
        print("2 -> Vendre")
        print("3 -> Discuter")
        print("4 -> Prendre congé")
        choix = T.InputChoice("\nChoisissez une option en tapant le nombre associé : ", 1, 4, "Veuillez saisir une option entre 1 et 4 SVP")
        LancerFonctionServante(choix)

def LancerFonctionServante(choix):
    if choix == 1:        
        #acheter
        print("Acheter menu")
        T.NextStep()
    elif choix == 2:
        #vendre
        print("Vendre menu...")
        T.NextStep()
    elif choix == 3:
        #discuter
        print("dialogue avec Servante du sanctuaire")
        T.NextStep()
    elif choix == 4:
        G.StayInMenuServante = False

def MenuForgeron():
    while G.StayInMenuForgeron:
        T.Cls()
        print("--- André, Forgeron du Sanctuaire ---\n")
        print("1 -> Améliorer une arme")
        print("2 -> Enchanter une arme")
        print("3 -> Discuter")
        print("4 -> Prendre congé")
        choix = T.InputChoice("\nChoisissez une option en tapant le nombre associé : ", 1, 4, "Veuillez saisir une option entre 1 et 4 SVP")
        LancerFonctionForgeron(choix)

def LancerFonctionForgeron(choix):
    if choix == 1:        
        #améliorer
        print("améliorer arme")
        T.NextStep()
    elif choix == 2:
        #vendre
        print("enchanter une arme")
        T.NextStep()
    elif choix == 3:
        #discuter
        print("dialogue avec André le forgeron")
        T.NextStep()
    elif choix == 4:
        G.StayInMenuForgeron = False

def MenuPyromancien():
    while G.StayInMenuPyromancien:
        T.Cls()
        print("--- Cornyx le pyromancien ---\n")
        print("1 -> Apprendre une pyromancie")
        print("2 -> Acheter")
        print("3 -> Discuter")
        print("4 -> Prendre congé")
        choix = T.InputChoice("\nChoisissez une option en tapant le nombre associé : ", 1, 4, "Veuillez saisir une option entre 1 et 4 SVP")
        LancerFonctionPyromancien(choix)

def LancerFonctionPyromancien(choix):
    if choix == 1:        
        #acheter pyro
        print("apprendre une pyromancie")
        T.NextStep()
    elif choix == 2:
        #acheter
        print("acheter")
        T.NextStep()
    elif choix == 3:
        #discuter
        print("dialogue avec Cornyx le pyromancien")
        T.NextStep()
    elif choix == 4:
        G.StayInMenuPyromancien = False

def MenuVoleur():
    while G.StayInMenuVoleur:
        T.Cls()
        print("--- Greirat ---\n")
        print("1 -> Acheter")
        print("2 -> Vendre")
        print("3 -> Discuter")
        print("4 -> Prendre congé")
        choix = T.InputChoice("\nChoisissez une option en tapant le nombre associé : ", 1, 4, "Veuillez saisir une option entre 1 et 4 SVP")
        LancerFonctionVoleur(choix)

def LancerFonctionVoleur(choix):
    if choix == 1:        
        #acheter
        print("Acheter menu")
        T.NextStep()
    elif choix == 2:
        #vendre
        print("Vendre menu...")
        T.NextStep()
    elif choix == 3:
        #discuter
        print("dialogue avec Greirat")
        T.NextStep()
    elif choix == 4:
        G.StayInMenuVoleur = False

def MenuOrbeck():
    while G.StayInMenuOrbeck:
        T.Cls()
        print("--- Orbeck, Sorcier-Assassin de Vinheim ---\n")
        print("1 -> Apprendre la sorcellerie")
        print("2 -> Acheter")
        print("3 -> Discuter")
        print("4 -> Prendre congé")
        choix = T.InputChoice("\nChoisissez une option en tapant le nombre associé : ", 1, 4, "Veuillez saisir une option entre 1 et 4 SVP")
        LancerFonctionOrbeck(choix)

def LancerFonctionOrbeck(choix):
    if choix == 1:        
        #acheter sorcellerie
        print("apprendre une sorcellerie")
        T.NextStep()
    elif choix == 2:
        #acheter
        print("acheter")
        T.NextStep()
    elif choix == 3:
        #discuter
        print("dialogue avec Orbeck")
        T.NextStep()
    elif choix == 4:
        G.StayInMenuOrbeck = False

def MenuIrina():
    while G.StayInMenuIrina:
        T.Cls()
        print("--- Irina, Prêtresse de Carim ---\n")
        print("1 -> Lire un miracle")
        print("2 -> Acheter")
        print("3 -> Discuter")
        print("4 -> Prendre congé")
        choix = T.InputChoice("\nChoisissez une option en tapant le nombre associé : ", 1, 4, "Veuillez saisir une option entre 1 et 4 SVP")
        LancerFonctionIrina(choix)

def LancerFonctionIrina(choix):
    if choix == 1:        
        #acheter miracle
        print("apprendre un miracle")
        T.NextStep()
    elif choix == 2:
        #acheter
        print("acheter")
        T.NextStep()
    elif choix == 3:
        #discuter
        print("dialogue avec Irina")
        T.NextStep()
    elif choix == 4:
        G.StayInMenuIrina = False

def MenuLondor():
    while G.StayInMenuLondor:
        T.Cls()
        print("--- Yoel et Yuria de Londor ---\n")
        print("1 -> Révéler la véritable puissance")
        print("2 -> Acheter")
        print("3 -> Discuter")
        print("4 -> Prendre congé")
        choix = T.InputChoice("\nChoisissez une option en tapant le nombre associé : ", 1, 4, "Veuillez saisir une option entre 1 et 4 SVP")
        LancerFonctionLondor(choix)

def LancerFonctionLondor(choix):
    if choix == 1:        
        #puissance carcasse 
        print("Révéler la véritable puissance")
        T.NextStep()
    elif choix == 2:
        #acheter
        print("acheter")
        T.NextStep()
    elif choix == 3:
        #discuter
        print("dialogue avec Yoel et Yuria")
        T.NextStep()
    elif choix == 4:
        G.StayInMenuLondor = False

def MenuLeonhard():
    while G.StayInMenuLeonhard:
        T.Cls()
        print("--- Leonhard, Phalange de Rosaria ---\n")
        print("1 -> Envahir")
        print("2 -> Discuter")
        print("3 -> Prendre congé")
        choix = T.InputChoice("\nChoisissez une option en tapant le nombre associé : ", 1, 3, "Veuillez saisir une option entre 1 et 3 SVP")
        LancerFonctionLeonhard(choix)

def LancerFonctionLeonhard(choix):
    if choix == 1:        
        #invasion 
        print("Envahir un joueur")
        T.NextStep()
    elif choix == 2:
        #discuter
        print("discuter avec Leonhard")
        T.NextStep()
    elif choix == 3:
        G.StayInMenuLeonhard = False