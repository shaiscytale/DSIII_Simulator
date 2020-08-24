# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 14:52:26 2018

@author: pixel14
"""
from DSIII_Classes.Personnage import Perso
from DSIII_Classes.Item import Arme, Consommable, ForgeItem
from DSIII_Fonctions import MainFunctions as Main
import DSIII_Classes.Enum as E
import Globals as G
import Tools as T
import MenuNpc as NPC


def MenuPrincipal():
    T.Cls()
    print("--- MENU PRINCIPAL - Aventure de {} ---\n".format(G.joueur.Nom))
    print("1 -> Gestion du personnage")
    print("2 -> Sanctuaire de Lige Feu")
    print("3 -> Téléportation vers zone de combat")
    print("4 -> Quitter")
    choix = T.InputChoice("\nChoisissez une option en tapant le nombre associé : ", 1, 4, "Veuillez saisir une option entre 1 et 4 SVP")
    LancerFonctionPrincipale(choix)

def MenuCombat():
    T.Cls()
    print("--- MENU DE COMBAT - Options ---")
    print("1 -> Attaquer")
    print("2 -> Utiliser magie")
    print("3 -> Lever son bouclier")
    print("4 -> Utiliser objet")
    choix = T.InputChoice("\nChoisissez une option en tapant le nombre associé : ", 1, 4, "Veuillez saisir une option entre 1 et 4 SVP")
    LancerFonctionCombat(choix)

def MenuNewGame():
    T.Cls()
    print("--- Aucun personnage chargé ---\n")
    print("1 -> Créer un nouveau personnage")
    print("2 -> Charger un personnage existant")
    print("3 -> Quitter")
    choix = T.InputChoice("\nChoisissez une option en tapant le nombre associé : ", 1, 3, "Veuillez saisir une option entre 1 et 3 SVP")
    LancerFonctionNewGame(choix)

def MenuPersonnage():
    while G.StayInMenuPerso:
        T.Cls()
        print("--- MENU PERSONNAGE ---\n")
        print("1 -> Afficher fiche perso")
        print("2 -> Afficher détails arme")
        print("3 -> Inventaire")
        print("4 -> Retourner au menu principal")
        choix = T.InputChoice("\nChoisissez une option en tapant le nombre associé : ", 1, 4, "Veuillez saisir une option entre 1 et 4 SVP")
        LancerFonctionPersonnage(choix)

def MenuInventaire():    
    while G.StayInMenuInventaire:
        T.Cls()
        print("--- MENU INVENTAIRE ---\n")
        print("1 -> Afficher l'inventaire")
        print("2 -> Supprimer un objet")
        print("3 -> Retourner au menu personnage")
        choix = T.InputChoice("\nChoisissez une option en tapant le nombre associé : ", 1, 3, "Veuillez saisir une option entre 1 et 3 SVP")
        LancerFonctionInventaire(choix)

def MenuSanctuaire():
    while G.StayInMenuSanctuaire:
        T.Cls()
        print("--- Sanctuaire de Lige Feu ---\n")
        print("1 -> Gardienne du Feu")
        print("2 -> Servante du Sanctuaire")
        print("3 -> André, forgeron du Sanctuaire")
        print("4 -> Cornyx, pyromancien des Grands Marais")
        print("5 -> Greirat, voleur")
        print("6 -> Orbeck, sorcier de Vinheim")
        print("7 -> Yoel et Yuria, carcasses de Londor")
        print("8 -> Irina, Prêtresse de Carim")
        print("9 -> Leonhard, Phalange de Rosaria")
        print("0 -> Quitter")
        choix = T.InputChoice("\nParlez au personnage en tapant le nombre associé : ", 0, 9, "Veuillez saisir une option entre 0 et 9 SVP")
        LancerFonctionSanctuaire(choix)

def LancerFonctionCombat(choix):
    if choix == 1:
        #attaquer
        pass
    elif choix == 2:
        #magie
        #G.StayInMenuChoixMagie = True
        #menu choix magie
        pass
    elif choix == 3:
        #bouclier
        pass
    elif choix == 4:
        #consommable
        #menu conso & stay in menu conso
        pass

def LancerFonctionSanctuaire(choix):
    if choix == 1:
        #gardienne du feu
        G.StayInMenuGardienneDuFeu = True
        NPC.MenuGardienneDuFeu()
    elif choix == 2:
        #servante
        G.StayInMenuServante = True
        NPC.MenuServante()
    elif choix == 3:
        #André
        G.StayInMenuForgeron = True
        NPC.MenuForgeron()
    elif choix == 4:
        #Cornyx
        G.StayInMenuPyromancien = True
        NPC.MenuPyromancien()
    elif choix == 5:
        #Greirat
        G.StayInMenuVoleur = True
        NPC.MenuVoleur()
    elif choix == 6:
        #Orbeck de Vinheim
        G.StayInMenuOrbeck = True
        NPC.MenuOrbeck()
    elif choix == 7:
        #Yoel et Yuria de Londor
        G.StayInMenuLondor = True
        NPC.MenuLondor()
    elif choix == 8:
        #Irina de Carim
        G.StayInMenuIrina = True
        NPC.MenuIrina()
    elif choix == 9:
        #Leonhard
        G.StayInMenuLeonhard = True
        NPC.MenuLeonhard()
    elif choix == 0:
        #quitter le menu du sanctuaire
        G.StayInMenuSanctuaire = False

def LancerFonctionInventaire(choix):
    if choix == 1:
        G.joueur.Inventaire.Afficher()
        T.NextStep()
    elif choix == 2:
        w = G.joueur.Inventaire.MenuSuppression()
        if w != False:
            if G.joueur.ArmeEquipee.Nom == w.Nom:
                G.joueur.DesequiperArme()
        T.NextStep()
    elif choix == 3:
        G.StayInMenuInventaire = False

def LancerFonctionNewGame(choix):
    if choix == 1:
        #créer un nouveau personnage
        Main.NewHero()
    elif choix == 2:
        #charger une partie
        """
        creation par défaut d'un personnage en attendant la gestion des sauvegardes
        """
        G.joueur = Perso("Hilda", 100, 100, 100, 100, 100, 100, 100, 100, 100)
        weapon = Arme("Lance de Longinus", 1000, 1000, 0.7, 1.5, 0.7, 2.5, 0, 0, 1.7, 0, E.RareteArme.UNIQUE, 2, 0.1, 0.5, 0, 0, 0.2)
        titanites = ForgeItem("Titanite", 10, 10, E.UpgradeMaterial.TITANITE, 30)
        weapon.Forger(titanites)
        weapon.Forger(titanites)
        G.joueur.Inventaire.Add(weapon)
        G.joueur.EquiperArme(weapon)
        conso1 = Consommable("Bombe(s)", 50, 10, 0.3, E.TypeConso.OFFENSIF, 100, 5, 30)
        G.joueur.Inventaire.Add(conso1)
    elif choix == 3:
        #fonction quitter jeu
        G.ContinueGame = False
    
def LancerFonctionPersonnage(choix):
    if choix == 1:
        #détails des caractéristiques du joueur
        G.joueur.AfficherCarac()
    elif choix == 2:
        #détails de l'arme équipée
        G.joueur.AfficherArme()
    elif choix == 3:
        #gestion de l'inventaire
        G.StayInMenuInventaire = True
        MenuInventaire()
    elif choix == 4:
        #quitter le menu personnage
        G.StayInMenuPerso = False

def LancerFonctionPrincipale(choix):
    if choix == 1:
        Main.GestionPersonnage()
    elif choix == 2:
        G.StayInMenuSanctuaire = True
        MenuSanctuaire()
    elif choix == 3:
        #fonction combat
        """à remplacer par le menu de téléportation dans le monde aventure"""
        Main.Combat()
    elif choix == 4:
        #fonction quitter jeu
        G.ContinueGame = False
    else:
        #fonction cachée de dev
        pass

def MenuChoixClasse(nom):
    T.Cls()
    print("--- Choix de la classe ---\n")
    print("1 -> Chevalier")
    print("2 -> Assassin")
    print("3 -> Sorcier")
    print("4 -> Prêtre")
    print("5 -> Empoisonneur")
    #choix = int(input("\nChoisissez la classe de votre personnage {} en tapant le nombre associé : ".format(nom)))
    choix = T.InputChoice("\nChoisissez la classe de votre personnage {} en tapant le nombre associé : ".format(nom), 1, 5, "Choisissez une option qui existe !!")
    LancerFonctionChoixClasse(choix, nom)

def LancerFonctionChoixClasse(choix, nom):
    #nom, vita, memo, endu, vigu, forc, dext, inte, foi, luck
    if choix == 1:
        """Chevalier"""
        G.joueur = Perso(nom, 12, 7, 12, 16, 13, 12, 9, 9, 7)
        weapon = Arme("Epee", 100, 100, 4.5, 30, 2.5, 1.5, 0, 0, 1)
        G.joueur.Inventaire.Add(weapon)
        G.joueur.EquiperArme(weapon)
        G.joueur.DefClasseHeros(E.ClassHero.CHEVALIER)
    elif choix == 2:
        """Assassin"""
        G.joueur = Perso(nom, 10, 10, 10, 8, 7, 13, 9, 5, 6)
        weapon = Arme("Estoc", 100, 100, 2.7, 18, 0.7, 2.5, 0, 0, 1.7)
        G.joueur.Inventaire.Add(weapon)
        G.joueur.EquiperArme(weapon)
        G.joueur.DefClasseHeros(E.ClassHero.ASSASSIN)
    elif choix == 3:
        """Sorcier"""
        G.joueur = Perso(nom, 8, 16, 9, 6, 5, 7, 15, 5, 4)
        weapon = Arme("Dague Magique", 100, 100, 0.5, 1, 0.7, 1.5, 2.5, 0, 1.7)
        G.joueur.Inventaire.Add(weapon)
        G.joueur.EquiperArme(weapon)
        G.joueur.DefClasseHeros(E.ClassHero.SORCIER)
    elif choix == 4:
        """Pretre"""
        G.joueur = Perso(nom, 13, 13, 13, 13, 9, 7, 5, 15, 4)
        weapon = Arme("Masse sacrée", 100, 100, 0.7, 13, 1.3, 1.3, 0, 1.3, 0.1)
        G.joueur.Inventaire.Add(weapon)
        G.joueur.EquiperArme(weapon)
        G.joueur.DefClasseHeros(E.ClassHero.PRETRE)
    elif choix == 5:
        """Empoisonneur"""
        G.joueur = Perso(nom, 10, 10, 10, 10, 7, 11, 9, 9, 16)
        weapon = Arme("Dague", 100, 100, 0.7, 3, 0.7, 1.5, 0, 0, 2.7)
        G.joueur.Inventaire.Add(weapon)
        G.joueur.EquiperArme(weapon)
        G.joueur.DefClasseHeros(E.ClassHero.EMPOISONNEUR)
    else:
        print("Choisissez une option qui existe !!")
        T.NextStep()
        MenuChoixClasse(nom)

def MenuArmeForge():
    #lister les armes améliorables
    pass