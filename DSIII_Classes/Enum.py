# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 11:10:23 2018

@author: pixel14
"""

from enum import Enum

class TypeConso(Enum):
    SOIN = "Consommable de restauration de points de vie"
    FOCUS = "Consommable de restauration de points de focus"
    OFFENSIF = "Consommable utilisé pour infliger des dégâts"
    NULL = "Aucun type défini pour le consommable"

class ClassHero(Enum):
    CHEVALIER = "Chevalier"
    ASSASSIN = "Assassin"
    SORCIER = "Sorcier"
    PRETRE = "Prêtre"
    EMPOISONNEUR = "Empoisonneur"
    NULL = "Aucune classe définie pour le héros"

class UpgradeMaterial(Enum):
    TITANITE = "Petite titanite"
    GRANDE_TITANITE = "Grande titanite"
    ECLAT_TITANITE = "Éclat de titanite"
    TABLETTE_TITANITE = "Tablette de titanite"
    ECAILLE_TITANITE = "Écaille de titanite"
    TITANITE_SCINTILLANTE = "Titanite scintillante"
    NULL = "Aucun type défini pour le matériel de forge"

class RareteArme(Enum):
    BASIQUE = 10
    UNIQUE = 5
    BOSS = 5
    
    @classmethod
    def has_value(cls, name):
        return any(name == item for item in cls)

class EcoleMagie(Enum):
    SORCELLERIE = "Art de manier les arcanes de la magie pure"
    MIRACLE = "Faire acte de foi en la puissance divine"
    PYRO = "Forme primitive de magie du feu des Grands-Marais"
    NULL = "Aucune école définie pour le sort"
    
    @classmethod
    def has_value(cls, name):
        return any(name == item for item in cls)
   
class Element(Enum):
    PHYSIQUE = "Élément associé aux armes traditionnelles (tranchantes, contondantes ou perforantes)"
    FEU = "Brûle et peut provoquer la panique"
    LUMIERE = "Élément sacré, bannissant les serviteurs des ténèbres, associé aux miracles"
    FOUDRE = "Élément puissant contre les armues de métal et les dragons, associé aux miracles"
    MAGIE = "Élément associé aux sorcelleries"
    TENEBRES = "Élément opposé à la lumière, associé à toutes les écoles de magie"
    NULL = "Aucun élément défini"
    
    @classmethod
    def has_value(cls, name):
        return any(name == item for item in cls)


"""
heal
hot
heal zone
hot zone
cleanse
cleanse zone
larme du déni
buffdef
buffdefelem
buffoff
buffarme
buffshield
degat mono hit
degat multi hit
dot
bleed
poison
malediction
voeu de silence
anti aggro
boost aggro
invisibilité
"""

class TypeSpell(Enum):
    HEAL = "Régénère les points de santé"
    CLEANSE = "Supprime les effets néfastes"
    BUFFDEF = "Améliore la défense"
    BUFFAR = "Améliore les dégâts"
    BUFFWEAPON = "Ajoute un bonus de dégâts élémentaire à l'arme"
    BUFFSHIELD = "Améliore la stabilité du bouclier"
    DAMAGE = "Sort offensif infligeant des dégâts"
    AUX = "Sort offensif infligeant un effet auxiliaire (poison, saignement, givre ou malédiction"
    UTILITY = "Sort utilitaire"
    
    @classmethod
    def has_value(cls, name):
        return any(name == item for item in cls)