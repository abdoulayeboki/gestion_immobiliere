from enum import Enum


class Categorie(Enum):
    R0 = "R0"
    R1 = "R1"
    R2  = "R2"
    R3 = "R3"
    R4= "R4"
    R5  = "R5"
    R6 = "R6"
    R7 = "R7"
    R8  = "R8"
    R9 = "R9"
    R10 = "R10"
class Niveau(Enum):
    etage_0 = "etage_0"
    etage_1 = "etage_1"
    etage_2  = "etage_2"
    etage_3 = "etage_3"
    etage_4= "etage_4"
    etage_5  = "etage_5"
    etage_6 = "etage_6"
    etage_7 = "etage_7"
    etage_8  = "etage_8"
    etage_9 = "etage_9"
    etage_10 = "etage_10"

class TypeAppartement(Enum):
    studio = "studio"
    F2  = "F2"
    F3 = "F3"
    F4= "F4"
    F5  = "F5"
    F6 = "F6"
    F7 = "F7"
    F8  = "F8"
    F9 = "F9"
    F10 = "F10"
class EtatBien(Enum):
    neuf = "neuf"
    tresBonEtat  = "tresBonEtat"
    bonEtat = "bonEtat"
    mauvaisEtat= "mauvaisEtat"
