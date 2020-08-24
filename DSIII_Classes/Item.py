# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 13:50:32 2018

@author: pixel14
"""

import DSIII_Classes.Enum as E

class Item:
    def __init__(self, nom, pxAchat, pxVente, poids):
        self._nom = nom
        self._prixAchat = pxAchat
        self._prixVente = pxVente
        self._poids = poids
    
    @property
    def Nom(self):
        return self._nom

    @Nom.setter
    def Nom(self, value):
        if len(value) > 20 or len(value) == 0:
            raise ValueError("Erreur : nom incorrect")
        self._nom = value
    
    @property
    def PrixAchat(self):
        return self._prixAchat
    
    @property
    def PrixVente(self):
        return self._prixVente
    
    @property
    def Poids(self):
        return self._poids


class Arme(Item):
    def __init__(self, nom, pxAchat, pxVente, poids, baseDeg, ratioForce, ratioDex, ratioInt, ratioFoi, ratioLuck, 
                 niveau=0, rareteArme=E.RareteArme.BASIQUE, 
                 baseDegParNv=0, rForceParNv=0, rDexteParNv=0, rIntelParNv=0, rFoiParNv=0, rChanceParNv=0):
        super().__init__(nom, pxAchat, pxVente, poids)
        self._baseDegat = baseDeg
        self._ratioForce = ratioForce
        self._ratioDexterite = ratioDex
        self._ratioIntelligence = ratioInt
        self._ratioFoi = ratioFoi
        self._ratioChance = ratioLuck
        self._niveau = niveau
        
        #print(rareteArme in E.RareteArme)
        if (not E.RareteArme.has_value(rareteArme)):
            raise ValueError('ERROR')
        if rareteArme in E.RareteArme:
            self._rarete = rareteArme
        self._niveauMax = self._rarete.value
        self._baseDegatParNv = baseDegParNv
        self._rForceParNv = rForceParNv
        self._rDexteParNv = rDexteParNv
        self._rIntelParNv = rIntelParNv
        self._rFoiParNv = rFoiParNv
        self._rChanceParNv = rChanceParNv
    
    @property
    def BaseDegat(self):
        return self._baseDegat + (self._baseDegatParNv * self.Niveau)
    
    @property
    def RatioForce(self):
        return self._ratioForce + (self._rForceParNv * self.Niveau)
    
    @property
    def RatioDexterite(self):
        return self._ratioDexterite + (self._rDexteParNv * self.Niveau)
    
    @property
    def RatioIntelligence(self):
        return self._ratioIntelligence + (self._rIntelParNv * self.Niveau)
    
    @property
    def RatioFoi(self):
        return self._ratioFoi + (self._rFoiParNv * self.Niveau)
    
    @property
    def RatioChance(self):
        return self._ratioChance + (self._rChanceParNv * self.Niveau)
    
    @property
    def Niveau(self):
        return self._niveau
    
    @property
    def NiveauMax(self):
        return self._niveauMax
    
    @property
    def Rarete(self):
        if self._rarete is E.RareteArme.BASIQUE:
            return "Arme de base"
        elif self._rarete is E.RareteArme.UNIQUE:
            return "Arme unique"
        else:
            return "Arme d'âme de boss"
    
    def Afficher(self, perso=False):
        if perso == False:
            print("--- Détail de l'arme \"{0}\" - niveau {1} ---\n".format(self.Nom, self.Niveau))
            print("Dégâts de base : {}\n".format(self.BaseDegat))
            print("Ratios")
            print(" -> {0:>12} : {1:>4%}".format("Force", self.RatioForce))
            print(" -> {0:>12} : {1:>4%}".format("Dextérité", self.RatioDexterite))
            print(" -> {0:>12} : {1:>4%}".format("Intelligence", self.RatioIntelligence))
            print(" -> {0:>12} : {1:>4%}".format("Foi", self.RatioFoi))
            print(" -> {0:>12} : {1:>4%}".format("Chance", self.RatioChance))
        else:
            totalDeg = self.BaseDegat
            degForce = self.RatioForce * perso.Force
            degDexte = self.RatioDexterite * perso.Dexterite
            degIntel = self.RatioIntelligence * perso.Intelligence
            degFoi = self.RatioFoi * perso.Foi
            degChance = self.RatioChance * perso.Chance
            totalDeg += degForce
            totalDeg += degDexte
            totalDeg += degIntel
            totalDeg += degFoi
            totalDeg += degChance
            totalDeg = int(totalDeg)
            print("--- Détail de l'arme \"{0}\" - niveau {1} ---\n".format(self.Nom, self.Niveau))
            print("Dégâts de base : {}\n".format(self.BaseDegat))
            print("Ratios")
            print(" -> {0:>12} : {1:>4.0%} = {2:>3d}".format("Force", self.RatioForce, int(degForce)))
            print(" -> {0:>12} : {1:>4.0%} = {2:>3d}".format("Dextérité", self.RatioDexterite, int(degDexte)))
            print(" -> {0:>12} : {1:>4.0%} = {2:>3d}".format("Intelligence", self.RatioIntelligence, int(degIntel)))
            print(" -> {0:>12} : {1:>4.0%} = {2:>3d}".format("Foi", self.RatioFoi, int(degFoi)))
            print(" -> {0:>12} : {1:>4.0%} = {2:>3d}".format("Chance", self.RatioChance, int(degChance)))
            print("\n -> Total dégâts : {}".format(totalDeg))
    
    def _calculerMaterielRequis(self):
        req = 0
        if self._rarete is E.RareteArme.BASIQUE:
            if self.Niveau == 0 or self.Niveau == 3 or self.Niveau == 6:
                req = 2
            elif self.Niveau == 1 or self.Niveau == 4 or self.Niveau == 7:
                req = 4
            elif self.Niveau == 2 or self.Niveau == 5 or self.Niveau == 8:
                req = 6
            elif self.Niveau == 9:
                req = 1
        else:
            if self.Niveau == 0:
                req = 2
            elif self.Niveau == 1:
                req = 4
            elif self.Niveau == 2:
                req = 6
            elif self.Niveau == 3:
                req = 8
            elif self.Niveau == 4:
                req = 1
        return req
    
    def Forger(self, upgradeMaterial):
        letsForge = False
        QtteReq = self._calculerMaterielRequis()
        if type(upgradeMaterial) == ForgeItem:
            # on vérifie qu'on a assez de matos d'upgrade
            if QtteReq > upgradeMaterial.Quantite:
                print("Matériaux insuffisants")
            else:
                if self._rarete is E.RareteArme.BASIQUE:
                    #on vérifie le type de matériel en fonction du niveau
                    if self.Niveau < 4 and upgradeMaterial.Type is E.UpgradeMaterial.TITANITE:
                        letsForge = True
                    elif self.Niveau >= 4 and self.Niveau <6 and upgradeMaterial.Type is E.UpgradeMaterial.GRANDE_TITANITE:
                        letsForge = True
                    elif self.Niveau >= 6 and self.Niveau <9 and upgradeMaterial.Type is E.UpgradeMaterial.ECLAT_TITANITE:
                        letsForge = True
                    elif self.Niveau == 9 and upgradeMaterial.Type is E.UpgradeMaterial.TABLETTE_TITANITE:
                        letsForge = True
                    else:
                        print("Impossible d'améliorer : niveau de l'arme max ou mauvais matériel")
                elif self._rarete is E.RareteArme.UNIQUE:
                    if self.Niveau < 4 and upgradeMaterial.Type is E.UpgradeMaterial.ECAILLE_TITANITE:
                        letsForge = True
                    elif self.Niveau == 4 and upgradeMaterial.Type is E.UpgradeMaterial.TABLETTE_TITANITE:
                        letsForge = True   
                    else:
                        print("Impossible d'améliorer : niveau de l'arme max ou mauvais matériel") 
                elif self._rarete is E.RareteArme.BOSS:
                    if self.Niveau < 4 and upgradeMaterial.Type is E.UpgradeMaterial.TITANITE_SCINTILLANTE:
                        letsForge = True
                    elif self.Niveau == 4 and upgradeMaterial.Type is E.UpgradeMaterial.TABLETTE_TITANITE:
                        letsForge = True   
                    else:
                        print("Impossible d'améliorer : niveau de l'arme max ou mauvais matériel") 
                else:
                    raise ValueError("Erreur : type de l'arme non défini, impossible de forger")
                
                if letsForge:
                    self.GagnerNiveau()
        else:
            raise ValueError("Ceci n'est pas un matériel de forge : {0}".format(upgradeMaterial))
        
        return letsForge
    
    def GagnerNiveau(self):
        if self.Niveau < self._niveauMax:
            self._niveau += 1
            print("Votre {0} a gagné un niveau.".format(self.Nom))
        else:
            raise ValueError("Erreur : impossible d'améliorer l'arme au dessus de son niveau maximum")


class Consommable(Item):
    def __init__(self, nom, pxAchat, pxVente, poids, typeConso, points, stack, maxStack):
        super().__init__(nom, pxAchat, pxVente, poids)
        if typeConso in E.TypeConso:
            self.Type = typeConso
        else:
            self.Type = E.TypeConso.NULL
            print("Erreur : le conso n'a pas de type définit")
        self.PointsEffet = points
        self.Stack = stack
        self.MaxStack = maxStack    
    
    def PoidsStack(self):
        return self.Stack * self.Poids
    
    def AfficherType(self):
        print("{}".format(self.Type.value))
    
    def Utiliser(self):
        """On va retourner les points d'effets, qui seront utilisés comme :
            en cas de conso de soin : degats negatifs sur le joueur
            en cas de conso offensif : degats positifs sur l'ennemi"""
        effet = 0
        if self.Stack > 0:
            if self.Type == E.TypeConso.OFFENSIF:
                effet -= self.PointsEffet
            elif self.Type != E.TypeConso.NULL:
                effet += self.PointsEffet
            self.Stack -= 1
            print("Vous avez utilisé {}, il vous en reste {}.".format(self.Nom, self.Stack))
        else:
            print("Vous n'avez plus de {}".format(self.Nom))
        return effet
    
    def AddToStack(self, qtte):
        if qtte > 0:
            if (self.Stack + qtte) < self.MaxStack:
                self.Stack += qtte
            else:
                self.Stack = self.MaxStack
            print("Vous avez désormais {} {}, sur un maximum de {}".format(self.Stack, self.Nom, self.MaxStack))
        else:
            print("Vous ne pouvez pas ajouter une quantité négative d'objets")
    
    def Vendre(self, qtte):
        prixTotal = 0
        if qtte > 0 and qtte <= self.Stack and self.Stack > 0:
            prixTotal = qtte * self.PrixVente
            self.Stack -= qtte
            print("Vous avez vendu {} {} pour en retirer {} âmes.".format(qtte, self.Nom, prixTotal))
        return prixTotal


class ForgeItem(Item):
    def __init__(self, nom, pxAchat, pxVente, typeForgeItem, quantite=0):
        super().__init__(nom, pxAchat, pxVente, 0)
        if typeForgeItem in E.UpgradeMaterial:
            self._type = typeForgeItem
        else:
            self._type = E.UpgradeMaterial.NULL
        self._quantite = quantite
    
    @property
    def Type(self):
        return self._type
    
    @property
    def Quantite(self):
        return self._quantite
    
    def AddToStack(self, qtte):
        if qtte > 0:
            self._quantite += qtte
            print("Vous avez désormais {0} {1}.".format(self.Quantite, self.Nom))
        else:
            raise ValueError("Impossible d'ajouter une quantité négative à la stack")
    
    def Utiliser(self, qtte):
        if qtte <= self.Quantite:
            self._quantite -= qtte
            print("Vous avez utilisé {0} {1}.".format(self.Quantite, self.Nom))
        else:
            print("Vous n'avez pas assez de {0}".format(self.Nom))
        