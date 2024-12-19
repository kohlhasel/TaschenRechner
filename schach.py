from copy import deepcopy
from typing import List, Dict, Set
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class Position(BaseModel):
    x: int
    y: int

    def __eq__(self, other):
        return self.x== other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x,self.y))

    def str_notation(self):
        return "abcdefgh"[self.x]+str(self.y)

    def plus(self,x:int,y:int):
        return Position(x=self.x+x, y=self.y+y)
class Zuege(BaseModel):
    schlaegt: List[Position]
    bewegt: List[Position]


class Figur(BaseModel):
    position: Position
    farbe: str
    id_: UUID = Field(default_factory=uuid4)
    def moegliche_zuege(self, brett: 'Schachbrett', beachte_bedrohung=True) -> Zuege:
        raise NotImplementedError(f"Für die Figur: {__class__.__name__} wurden noch keine möglichen Züge implementiert")

    def selbe_farbe_wie(self, andere_figur: 'Figur'):
        return self.farbe == andere_figur.farbe


class LeeresFeld(Figur):
    def moegliche_zuege(self, brett, beachte_bedrohung=True) -> Zuege:
        return Zuege(bewegt=[], schlaegt=[])

class Schachbrett():
    brett: Dict[Position, Figur]

    def __init__(self):
        self.brett = {}
        for i in range(8):
            for j in range(8):
                position = Position(x=i,y=j)
                self.brett[position]= LeeresFeld(position = position, farbe='neutral')

    def setze_Figur(self, Figur):
        self.brett[Figur.position]= Figur

    def ist_Koenig_von_farbe_in_schach(self,farbe: str):
        pseudo_figur= Figur(position=Position(x=1,y=1), farbe=farbe)
        durch_gegner_bedrohte_felder=self.von_Farbe_bedrohte_Felder(gegner_farbe(pseudo_figur))
        for feld in durch_gegner_bedrohte_felder:
            figure = self.brett[feld]
            if figure.farbe==farbe:
                if figure.__class__.__name__ == 'Koenig':
                    return True
        return False

    def von_Farbe_bedrohte_Felder(self, farbe: str)-> Set[Position]:
        ret = set()
        for figure in self.brett.values():
            if figure.farbe==farbe:
                zuege = figure.moegliche_zuege(self, beachte_bedrohung=False)
                ret.update(zuege.schlaegt)
        return ret

class Koenig(Figur):
    def moegliche_zuege(self, brett: 'Schachbrett', beachte_bedrohung=True) -> Zuege:
        bewegt = [self.position.plus(1,1),
                  self.position.plus(1,0),
                  self.position.plus(1,-1),
                  self.position.plus(0,1),
                  self.position.plus(0,-1),
                  self.position.plus(-1,1),
                  self.position.plus(-1, 0),
                  self.position.plus(-1, -1),]
        bewegt = [x for x in bewegt if x in brett.brett]
        if beachte_bedrohung:
            bewegt = [x for x in bewegt if x not in brett.von_Farbe_bedrohte_Felder(gegner_farbe(self))]
        schlaegt = [x for x in bewegt]
        return Zuege(bewegt=bewegt, schlaegt=schlaegt)

class Bauer(Figur):
    def moegliche_zuege(self, brett: 'Schachbrett', beachte_bedrohung=True) -> Zuege:
        schwarz_weiss_multiplier=1
        if self.farbe=='weiss':
            schwarz_weiss_multiplier=-1
        if self.position.y == 0 or self.position.y==7:
            return Zuege(bewegt=[], schlaegt=[])
        bewegt = [self.position.plus(0,-1*schwarz_weiss_multiplier)]
        if brett.brett[bewegt[0]].farbe!='neutral':
            bewegt=[]
        if (self.position.y == 6 and self.farbe=='schwarz') or (self.position.y==1 and self.farbe=='weiss'):
            if brett.brett[self.position.plus(0,-1*schwarz_weiss_multiplier)].farbe=='neutral' and brett.brett[self.position.plus(0,-2*schwarz_weiss_multiplier)].farbe =='neutral':
                bewegt.append(self.position.plus(0,-2*schwarz_weiss_multiplier))

        schlaegt=[self.position.plus(-1,-1*schwarz_weiss_multiplier), self.position.plus(1,-1*schwarz_weiss_multiplier)]
        schlaegt = [x for x in schlaegt if brett.brett[x].farbe == gegner_farbe(self)]

        schlaegt=[x for x in schlaegt if x in brett.brett]
        bewegt=[x for x in bewegt if x in brett.brett]
        if beachte_bedrohung:
            ret_schlaegt = []
            ret_bewegt = []
            for zug in schlaegt:
                self.probier_zug_aus_ob_er_legal_waere(brett, ret_schlaegt, zug)
            for zug in bewegt:
                self.probier_zug_aus_ob_er_legal_waere(brett, ret_bewegt, zug)

            return Zuege(bewegt=ret_bewegt, schlaegt=ret_schlaegt)
        return Zuege(bewegt=bewegt, schlaegt=schlaegt)

    def probier_zug_aus_ob_er_legal_waere(self, brett, ret_schlaegt, zug):
        ausprobier_brett = Schachbrett()
        ausprobier_brett.brett = deepcopy(brett.brett)
        leeres_feld_figur = LeeresFeld(position=self.position, farbe='neutral')
        ausprobier_brett.setze_Figur(leeres_feld_figur)
        ausprobier_figur = Bauer(position=zug, farbe=self.farbe)
        ausprobier_brett.setze_Figur(ausprobier_figur)
        if not ausprobier_brett.ist_Koenig_von_farbe_in_schach(self.farbe):
            ret_schlaegt.append(zug)


def gegner_farbe(figur: Figur):
    if figur.farbe=='schwarz':
        return 'weiss'
    elif figur.farbe=='weiss':
        return 'schwarz'
    else:
        return 'neutral'


class Laeufer(Figur):

    def moegliche_zuege(self, brett: 'Schachbrett', beachte_bedrohung=True) -> Zuege:
        schlaegt=[]
        for i in range(6):
            position=self.position.plus(i+1,i+1)
            if position in brett.brett:
                figur = brett.brett[position]
                if figur.farbe == 'neutral':
                    schlaegt.append(position)
                else:
                    if figur.farbe!=self.farbe:
                        schlaegt.append(position)
                    break
        for i in range(6):
            position=self.position.plus(-1-i,-1-i)
            if position in brett.brett:
                figur = brett.brett[position]
                if figur.farbe == 'neutral':
                    schlaegt.append(position)
                else:
                    if figur.farbe!=self.farbe:
                        schlaegt.append(position)
                    break
        for i in range(6):
            position = self.position.plus(i + 1, -i -1)
            if position in brett.brett:
                figur = brett.brett[position]
                if figur.farbe == 'neutral':
                    schlaegt.append(position)
                else:
                    if figur.farbe != self.farbe:
                        schlaegt.append(position)
                    break
        for i in range(6):
            position = self.position.plus(-i - 1, i + 1)
            if position in brett.brett:
                figur = brett.brett[position]
                if figur.farbe == 'neutral':
                    schlaegt.append(position)
                else:
                    if figur.farbe != self.farbe:
                        schlaegt.append(position)
                    break
        schlaegt = [x for x in schlaegt if x in brett.brett]
        bewegt=[x for x in schlaegt]

        if beachte_bedrohung:
            ret_schlaegt = []
            ret_bewegt = []
            for zug in schlaegt:
                self.probier_zug_aus_ob_er_legal_waere(brett, ret_schlaegt, zug)
            for zug in bewegt:
                self.probier_zug_aus_ob_er_legal_waere(brett, ret_bewegt, zug)

            return Zuege(bewegt=ret_bewegt, schlaegt=ret_schlaegt)
        return Zuege(bewegt=bewegt, schlaegt=schlaegt)


    def probier_zug_aus_ob_er_legal_waere(self, brett, ret_schlaegt, zug):
        ausprobier_brett = Schachbrett()
        ausprobier_brett.brett = deepcopy(brett.brett)
        leeres_feld_figur = LeeresFeld(position=self.position, farbe='neutral')
        ausprobier_brett.setze_Figur(leeres_feld_figur)
        ausprobier_figur = Laeufer(position=zug, farbe=self.farbe)
        ausprobier_brett.setze_Figur(ausprobier_figur)
        if not ausprobier_brett.ist_Koenig_von_farbe_in_schach(self.farbe):
            ret_schlaegt.append(zug)

class Turm(Figur):
    def moegliche_zuege(self, brett: 'Schachbrett', beachte_bedrohung=True) -> Zuege:
        ret = []
        for i in range(7):
            position = self.position.plus(i + 1, 0)
            if position in brett.brett:
                figur = brett.brett[position]
                if figur.farbe == 'neutral':
                    ret.append(position)
                else:
                    if figur.farbe != self.farbe:
                        ret.append(position)
                    break
        for i in range(7):
            position = self.position.plus(-1 -i, 0)
            if position in brett.brett:
                figur = brett.brett[position]
                if figur.farbe == 'neutral':
                    ret.append(position)
                else:
                    if figur.farbe != self.farbe:
                        ret.append(position)
                    break
        for i in range(7):
            position = self.position.plus(0, i+1)
            if position in brett.brett:
                figur = brett.brett[position]
                if figur.farbe == 'neutral':
                    ret.append(position)
                else:
                    if figur.farbe != self.farbe:
                        ret.append(position)
                    break
        for i in range(7):
            position = self.position.plus(0,-1-i)
            if position in brett.brett:
                figur = brett.brett[position]
                if figur.farbe == 'neutral':
                    ret.append(position)
                else:
                    if figur.farbe != self.farbe:
                        ret.append(position)
                    break

        ret = [x for x in ret if x in brett.brett]
        schlaegt = [x for x in ret]
        bewegt = [ x for x in ret]
        if beachte_bedrohung:
            ret_schlaegt = []
            ret_bewegt = []
            for zug in schlaegt:
                self.probier_zug_aus_ob_er_legal_waere(brett, ret_schlaegt, zug)
            for zug in bewegt:
                self.probier_zug_aus_ob_er_legal_waere(brett, ret_bewegt, zug)

            return Zuege(bewegt=ret_bewegt, schlaegt=ret_schlaegt)
        return Zuege(bewegt=ret, schlaegt=[x for x in ret])
    def probier_zug_aus_ob_er_legal_waere(self, brett, ret_schlaegt, zug):
        ausprobier_brett = Schachbrett()
        ausprobier_brett.brett = deepcopy(brett.brett)
        leeres_feld_figur = LeeresFeld(position=self.position, farbe='neutral')
        ausprobier_brett.setze_Figur(leeres_feld_figur)
        ausprobier_figur = Laeufer(position=zug, farbe=self.farbe)
        ausprobier_brett.setze_Figur(ausprobier_figur)
        if not ausprobier_brett.ist_Koenig_von_farbe_in_schach(self.farbe):
            ret_schlaegt.append(zug)
