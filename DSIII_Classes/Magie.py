# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 18:24:18 2019

@author: Abscience
"""

import DSIII_Classes.Enum as E

class Spell:
    def __init__(self, nom, ecole, typeSpell, coutFP, spellBoostRatio, base):
        self._nom = nom
        if (not E.EcoleMagie.has_value(ecole)):
            raise ValueError('ERROR')
        if ecole in E.EcoleMagie:
            self._ecole = ecole
        self._coutFocus = coutFP
        if (not E.TypeSpell.has_value(typeSpell)):
            raise ValueError('ERROR')
        if typeSpell in E.TypeSpell:
            self._typeSpell = typeSpell
        self._spellBoostRatio = spellBoostRatio
        self._base = base
    
    @property
    def Nom(self):
        return self._nom
    
    @property
    def Ecole(self):
        return self._ecole
    
    @property
    def CoutFocus(self):
        return self._coutFocus
    
    @property
    def TypeSpell(self):
        return self._typeSpell
    
    @property
    def SpellBoostRatio(self):
        return self._spellBoostRatio
    
    @property
    def Base(self):
        return self._base



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