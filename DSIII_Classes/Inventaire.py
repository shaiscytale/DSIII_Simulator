# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 14:04:15 2018

@author: pixel14
"""

import DSIII_Classes.Item
import Tools as T
import copy as C

class Inventaire:
    def __init__(self, contenanceMax):
        self.ContenanceMax = contenanceMax
        self.Items = []
        self._armeAmeliorables = []
    
    def PoidsActuel(self):
        poidsTotal = 0
        for i in self.Items:
            poidsTotal += i.Poids
        return poidsTotal

    def PoidsDispo(self):
        return self.ContenanceMax - self.PoidsActuel()
    
    def Add(self, item):
        if isinstance(item, DSIII_Classes.Item.Item):
            if type(item) is DSIII_Classes.Item.Consommable:
                pds = item.PoidsStack()
            else:
                pds = item.Poids
            if self.PoidsDispo() >= pds:
                self.Items.append(item)
                print("L'objet {} a été ajouté à l'inventaire.".format(item.Nom))
            else:
                print("L'objet {} est trop lourd : votre inventaire ne peut plus contenir que {} kg.".format(item.Nom, self.PoidsDispo()))
        else:
            print("Vous ne pouvez ajouter {} à votre inventaire.".format(type(item)))
    
    def Del(self, item):
        if isinstance(item, DSIII_Classes.Item.Item):
            if item in self.Items:
                print("Suppression de {} de votre inventaire".format(item.Nom))
                self.Items.remove(item)
            else:
                print("Erreur : {} n'est pas dans votre inventaire".format(item.Nom))
        else:
            print("Erreur : {} n'est même pas un item".format(type(item)))
    
    def Afficher(self):
        T.Cls()
        x = 0
        pdsTotal = 0
        print("--- Liste des objets de l'inventaire ---\n")
        for i in self.Items:
            x += 1
            if type(i) is not DSIII_Classes.Item.Consommable:
                pds = i.Poids
                pdsTotal += pds
                print("{} - {} ({} kg)".format(x, i.Nom, pds))
            if type(i) is DSIII_Classes.Item.Consommable:
                pds = i.PoidsStack()
                pdsTotal += pds
                print("{} - {} : {} / {} (total de {} kg)".format(x, i.Nom, i.Stack, i.MaxStack, i.PoidsStack()))
        print("\nPoids total de l'inventaire : {} / {} kg max".format(pdsTotal, self.ContenanceMax))
    
    def AfficherArmesForge(self):
        T.Cls()
        x = 0
        self._armeAmeliorables = []
        print("--- Liste des armes pouvant être améliorées ---\n")
        for i in self.Items:
            if type(i) is DSIII_Classes.Item.Arme:
                if i.Niveau < i.NiveauMax:
                    self._armeAmeliorables.append(i)
        
        for arme in self._armeAmeliorables:
            x += 1
            print("{0} - {1}".format(x, arme.Nom))
    
    def MenuSuppression(self):
        choix = -42
        while (choix < 0 or choix > (len(self.Items)+1)):
            self.Afficher()
            choix = int(input("\nVeuillez saisir l'index de l'objet à supprimer (entre {} et {} - \"0\" pour annuler)\n".format(1, len(self.Items))))
        if choix != 0:
            itemCopie = C.copy(self.Items[choix-1])
            del self.Items[choix-1]
            print("Vous avez bien supprimé l'objet {} de votre inventaire.".format(itemCopie.Nom))
            if type(itemCopie) is DSIII_Classes.Item.Arme:
                print("\nVous serez déséquipé si l'objet supprimé était votre arme courante.")
                T.NextStep()
                return itemCopie
            else:
                return False
        else:
            print("Annulation de la suppression d'objet")
            return False
    
    def MenuArmeForge(self):
        choix = -42
        self.AfficherArmesForge()
        T.NextStep()
        
        