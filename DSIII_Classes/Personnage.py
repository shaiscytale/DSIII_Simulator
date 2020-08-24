# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 11:33:54 2018

@author: pixel14
"""
import DSIII_Classes.Item
import DSIII_Classes.Inventaire as Inv
import DSIII_Classes.Enum as E
import Tools as T

class Perso :
    def __init__(self, nom, vita, memo, endu, vigu, forc, dext, inte, foi, luck):
        """Constructeur du personnage de base"""
        self.Nom = nom
        self.Vitalite = vita
        self.Memoire = memo
        self.Endurance = endu
        self.Vigueur = vigu
        self.Force = forc
        self.Dexterite = dext
        self.Intelligence = inte
        self.Foi = foi
        self.Chance = luck
        self.ArmeEquipee = None
        self.NiveauDispo = 0
        self.Niveau = 0
        self.Ames = 0
        self.AmesNextLevel = 0
        self.Classe = E.ClassHero.NULL
        self.Inventaire = Inv.Inventaire(self.Vigueur)
        self._calculerCaracSecondaires()
    
    @property
    def Nom(self):
        return self._nom

    @Nom.setter
    def Nom(self, value):
        if len(value) > 25 or len(value) == 0:
            raise ValueError("Erreur : nom trop long")
        else:
            self._nom = value
    
    @property
    def Vitalite(self):
        return self._vitalite
    @Vitalite.setter
    def Vitalite(self, value):
        if value < 0:
            raise ValueError("Erreur : une carac ne peut être négative")
        else:
            self._vitalite = value    
    
    @property
    def Memoire(self):
        return self._memoire
    @Memoire.setter
    def Memoire(self, value):
        if value < 0:
            raise ValueError("Erreur : une carac ne peut être négative")
        else:
            self._memoire = value    
    
    @property
    def Endurance(self):
        return self._endurance
    @Endurance.setter
    def Endurance(self, value):
        if value < 0:
            raise ValueError("Erreur : une carac ne peut être négative")
        else:
            self._endurance = value
    
    @property
    def Vigueur(self):
        return self._vigueur
    @Vigueur.setter
    def Vigueur(self, value):
        if value < 0:
            raise ValueError("Erreur : une carac ne peut être négative")
        else:
            self._vigueur = value
    
    @property
    def Force(self):
        return self._force
    @Force.setter
    def Force(self, value):
        if value < 0:
            raise ValueError("Erreur : une carac ne peut être négative")
        else:
            self._force = value
    
    @property
    def Dexterite(self):
        return self._dexterite
    @Dexterite.setter
    def Dexterite(self, value):
        if value < 0:
            raise ValueError("Erreur : une carac ne peut être négative")
        else:
            self._dexterite = value
    
    @property
    def Intelligence(self):
        return self._intelligence
    @Intelligence.setter
    def Intelligence(self, value):
        if value < 0:
            raise ValueError("Erreur : une carac ne peut être négative")
        else:
            self._intelligence = value
    
    @property
    def Foi(self):
        return self._foi
    @Foi.setter
    def Foi(self, value):
        if value < 0:
            raise ValueError("Erreur : une carac ne peut être négative")
        else:
            self._foi = value            
    
    @property
    def Chance(self):
        return self._chance
    @Chance.setter
    def Chance(self, value):
        if value < 0:
            raise ValueError("Erreur : une carac ne peut être négative")
        else:
            self._chance = value
            
    def __str__(self):
        """Quand on entre notre objet dans l'interpréteur"""
        return "Nom: {}\nHp : {} / {}\nFocus : {} / {}\nArme : {}".format(self.Nom, self.Hp, self.HpMax, self.Focus, self.FocusMax, self.ArmeEquipee)
    
    def _calculerNiveauActuel(self):
        totalCarac = 0
        totalCarac += self.Vitalite
        totalCarac += self.Memoire
        totalCarac += self.Vigueur
        totalCarac += self.Endurance
        totalCarac += self.Force
        totalCarac += self.Dexterite
        totalCarac += self.Intelligence
        totalCarac += self.Foi
        totalCarac += self.Chance
        
        if totalCarac <= 90:
            self.Niveau = 1
        else:
            self.Niveau = totalCarac - 90
        
    def _calculerNextLevelAmesRequises(self):
        base = 300        
        self.AmesNextLevel = int(base + (base * (self.Niveau / 3)))    
    
    def AfficherCarac(self):
        T.Cls()
        print("--- Détail des caractéristiques de {} ---\n".format(self.Nom))
        print("{0} de niveau {1}".format(self.Classe.value, self.Niveau))
        print("{0} âmes (coût prochain niveau : {1} âmes)\n".format(self.Ames, self.AmesNextLevel))
        print("Hp : {0} / {1}\nFocus : {2} / {3}\n".format(self.Hp, self.HpMax, self.Focus, self.FocusMax))
        print("{0:<12} : {1}".format("Vitalité", self.Vitalite))
        print("{0:<12} : {1}".format("Mémoire", self.Memoire))
        print("{0:<12} : {1}".format("Endurance", self.Endurance))
        print("{0:<12} : {1}".format("Vigueur", self.Vigueur))
        print("{0:<12} : {1}".format("Force", self.Force))
        print("{0:<12} : {1}".format("Dextérité", self.Dexterite))
        print("{0:<12} : {1}".format("Intelligence", self.Intelligence))
        print("{0:<12} : {1}".format("Foi", self.Foi))
        print("{0:<12} : {1}\n".format("Chance", self.Chance))
        T.NextStep()
    
    def AfficherArme(self):
        T.Cls()
        if self.ArmeEquipee != None and type(self.ArmeEquipee) is DSIII_Classes.Item.Arme:
            w = self.ArmeEquipee
            w.Afficher(self)
        else:
            print("Vous n'avez aucune arme équipée.")
        T.NextStep()
    
    def EquiperArme(self, arme, ok=True):
        T.Cls()
        if type(arme) is DSIII_Classes.Item.Arme:
            self.ArmeEquipee = arme
            if ok:
                print("{0} a équipé l'arme : {1}".format(self.Nom, self.ArmeEquipee.Nom))
        else:
            if ok:
                print("Equipement de l'arme impossible !")
        if ok:
            T.NextStep()

    def DesequiperArme(self)    :
        T.Cls()
        if self.ArmeEquipee is None:
            print("Il n'y a aucune arme à déséquiper.")
        else:
            print("Vous avez déséquipé l'arme {0}".format(self.ArmeEquipee.Nom))
            self.ArmeEquipee = None
    
    def _calculerDegatsArme(self):
        totalDeg = 0
        if self._isArmeEquipee():
            weapon = self.ArmeEquipee
            totalDeg += weapon.BaseDegat
            totalDeg += weapon.RatioForce * self.Force
            totalDeg += weapon.RatioDexterite * self.Dexterite
            totalDeg += weapon.RatioIntelligence * self.Intelligence
            totalDeg += weapon.RatioFoi * self.Foi
            totalDeg += weapon.RatioChance * self.Chance
            totalDeg = int(totalDeg)
        return totalDeg
    
    def _calculerDegatsMainsNues(self):
        totalDeg = 0
        
        totalDeg += self.Force * 2 + self.Dexterite * 1
        
        return totalDeg
    
    def _isArmeEquipee(self):
        if self.ArmeEquipee is not None and type(self.ArmeEquipee) is DSIII_Classes.Item.Arme:
            return True
        else:
            return False
    
    def SubirDegats(self, degats):
        if degats >= self.Hp :
            deg = self.Hp
            self.Hp = 0
            return deg
        else :
            self.Hp -= degats
            return degats
    
    def DefClasseHeros(self, classeHeros):
        if classeHeros in E.ClassHero:
            self.Classe = classeHeros
            print("{0} est désormais un {1}.".format(self.Nom, classeHeros.value))
        else:
            print("{0} n'est pas une classe de héros".format(type(classeHeros)))
    
    def UtiliserConso(self, cible, item):
        effet = item.Utiliser()
        if effet < 0:
            print("{0} utilise {1} sur {2} et lui inflige {3} points de dégâts.".format(self.Nom, item.Nom, cible.Nom, (effet * -1)))
        elif effet > 0:
            if item.Type == E.TypeConso.SOIN:
                mr = self.RestituerVie(effet)
                print("{0} utilise {1} et se soigne {2} points de vie.".format(self.Nom, item.Nom, mr))
            elif item.Type == E.TypeConso.FOCUS:
                mr = self.RestituerFocus(effet)
                print("{0} utilise {1} et se soigne {2} points de focus.".format(self.Nom, item.Nom, mr))
    
    def RestituerVie(self, qtte):
        montantRendu = 0
        if (self.Hp + qtte) < self.HpMax:
            montantRendu = qtte
            self.Hp += qtte
        else:
            montantRendu = self.HpMax - self.Hp
            self.Hp = self.HpMax
        return montantRendu
    
    def RestituerFocus(self, qtte):
        montantRendu = 0
        if (self.Focus + qtte) < self.FocusMax:
            montantRendu = qtte
            self.Focus += qtte
        else:
            montantRendu = self.FocusMax - self.Focus
            self.Focus = self.FocusMax
        return montantRendu
    
    def Attaquer(self, cible):
        if self._isArmeEquipee():
            atk = self._calculerDegatsArme()
            print("{0} a attaqué {1} avec {2} pour lui infliger {3} dégâts !".format(self.Nom, cible.Nom, self.ArmeEquipee.Nom, cible.SubirDegats(atk)))
        else:
            atk = self._calculerDegatsMainsNues()
            print("{0} a attaqué {1} à mains nues pour lui infliger {2} dégâts !".format(self.Nom, cible.Nom, cible.SubirDegats(atk)))
        if(cible.Hp <= 0):
            print("\n{0} a succombé à l'attaque de {1} !!".format(cible.Nom, self.Nom))
        T.NextStep()

    def _calculerCaracSecondaires(self):
        """On met à jour niveau et âmes requises pour next level"""
        self._calculerNiveauActuel()
        self._calculerNextLevelAmesRequises()
        
        """on met à jour les carac secondaires dépendant des caracs primaires"""
        self.HpMax = self.Vitalite * 30
        self.Hp = self.HpMax
        self.FocusMax = (self.Memoire * 9) + 30
        self.Focus = self.FocusMax
        self.Inventaire.ContenanceMax = self.Vigueur
    
    def GagnerAmes(self, qtteAmes):
        if qtteAmes > 0:
            self.Ames += qtteAmes
            print("{0} âmes gagnées...".format(qtteAmes))
        else:
            raise ValueError("Erreur : impossible de gagner montant négatif d'âmes")
    
    def _depenserAmesLevelUp(self):
        self.Ames -= self.AmesNextLevel
    
    def Mourir(self):
        self.Ames = 0
        print("Vous êtes mort...")
        T.Revive()
        self.Hp = self.HpMax
        self.Focus = self.FocusMax
        T.Cls()
    
    def MonterNiveau(self):
        T.Cls()
        if self.Ames >= self.AmesNextLevel:
            up = False
            print("--- MENU Personnage - Dépenser les âmes ---\n".format(self.Nom))
            print("1 -> Vitalité")
            print("2 -> Mémoire")
            print("3 -> Endurance")
            print("4 -> Vigueur")
            print("5 -> Force")
            print("6 -> Dexterite")
            print("7 -> Intelligence")
            print("8 -> Foi")
            print("9 -> Chance")
            print("0 -> Annuler")
            choix = T.InputChoice("\nChoisissez une caractéristiques à améliorer en tapant le nombre associé : ", 0, 9, "Veuillez saisir une option entre 0 et 9 SVP")
            
            if choix != 0:
                if choix == 1:
                    self.Vitalite += 1
                elif choix == 2:
                    self.Memoire += 1
                elif choix == 3:
                    self.Endurance += 1
                elif choix == 4:
                    self.Vigueur += 1
                elif choix == 5:
                    self.Force += 1
                elif choix == 6:
                    self.Dexterite += 1
                elif choix == 7:
                    self.Intelligence += 1
                elif choix == 8:
                    self.Foi += 1
                elif choix == 9:
                    self.Chance += 1
                else:                
                    pass                
                #descendre les ames du montant requis
                self._depenserAmesLevelUp()
                self._calculerCaracSecondaires()
                print("\nVous avez gagné un niveau..., il vous reste {0} âmes".format(self.Ames))
        else :
            print("\nVous n'avez pas assez d'âmes pour gagner un niveau...")
        T.NextStep()