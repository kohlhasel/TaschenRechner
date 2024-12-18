import pytest
from pydantic import BaseModel

from schach import Schachbrett, Koenig, Position, Bauer, Laeufer, Springer


@pytest.fixture()
def leeres_brett():
    return Schachbrett()


class TestKoenig():
    def test_happy_path(self, leeres_brett):
        """Wenn der Koenig auf einem leeren Schachbrett steht, dann kann er sich in alle Richtungen bewegen"""
        # Arrange
        sut = Koenig(position=Position(x=4, y=4), farbe='weiss')
        leeres_brett.setze_Figur(sut)
        # Act
        result = sut.moegliche_zuege(leeres_brett)
        # Assert
        assert len(result.schlaegt) == 8
        assert Position(x=3, y=3) in result.schlaegt
        assert Position(x=4, y=3) in result.schlaegt
        assert Position(x=5, y=3) in result.schlaegt
        assert Position(x=5, y=4) in result.schlaegt
        assert Position(x=5, y=5) in result.schlaegt
        assert Position(x=4, y=5) in result.schlaegt
        assert Position(x=3, y=5) in result.schlaegt
        assert Position(x=3, y=4) in result.schlaegt
        assert len(result.bewegt) == 8
        assert Position(x=3, y=3) in result.bewegt
        assert Position(x=4, y=3) in result.bewegt
        assert Position(x=5, y=3) in result.bewegt
        assert Position(x=5, y=4) in result.bewegt
        assert Position(x=5, y=5) in result.bewegt
        assert Position(x=4, y=5) in result.bewegt
        assert Position(x=3, y=5) in result.bewegt
        assert Position(x=3, y=4) in result.bewegt

    def test_linker_rand_des_bretts(self, leeres_brett):
        """Wenn der Koenig auf einem leeren Schachbrett am linken Rand steht, dann kann er sich nicht vom Brett bewegen"""
        sut = Koenig(position=Position(x=0, y=4), farbe='weiss')
        leeres_brett.setze_Figur(sut)
        # Act
        result = sut.moegliche_zuege(leeres_brett)
        # Assert
        assert len(result.schlaegt) == 5
        assert Position(x=0, y=3) in result.schlaegt
        assert Position(x=1, y=3) in result.schlaegt
        assert Position(x=1, y=4) in result.schlaegt
        assert Position(x=1, y=5) in result.schlaegt
        assert Position(x=0, y=5) in result.schlaegt

    def test_unterer_rand_des_bretts(self, leeres_brett):
        """Wenn der Koenig auf einem leeren Schachbrett am unteren Rand steht, dann kann er sich nicht vom Brett bewegen"""
        # Arrange
        sut = Koenig(position=Position(x=4, y=0), farbe='weiss')
        leeres_brett.setze_Figur(sut)
        # Act
        result = sut.moegliche_zuege(leeres_brett)
        # Assert
        assert len(result.schlaegt) == 5
        assert Position(x=5, y=0) in result.schlaegt
        assert Position(x=5, y=1) in result.schlaegt
        assert Position(x=4, y=1) in result.schlaegt
        assert Position(x=3, y=1) in result.schlaegt
        assert Position(x=3, y=0) in result.schlaegt

    def test_oberer_rand_des_bretts(self, leeres_brett):
        """Wenn der Koenig auf einem leeren Schachbrett am oberen Rand steht, dann kann er sich nicht vom Brett bewegen"""
        # Arrange
        sut = Koenig(position=Position(x=4, y=7), farbe='weiss')
        leeres_brett.setze_Figur(sut)
        # Act
        result = sut.moegliche_zuege(leeres_brett)
        # Assert
        assert len(result.schlaegt) == 5
        assert Position(x=3, y=6) in result.schlaegt
        assert Position(x=4, y=6) in result.schlaegt
        assert Position(x=5, y=6) in result.schlaegt
        assert Position(x=5, y=7) in result.schlaegt
        assert Position(x=3, y=7) in result.schlaegt

    def test_rechter_rand_des_bretts(self, leeres_brett):
        """Wenn der Koenig auf einem leeren Schachbrett am rechten Rand steht, dann kann er sich nicht vom Brett bewegen"""
        # Arrange
        sut = Koenig(position=Position(x=7, y=4), farbe='weiss')
        leeres_brett.setze_Figur(sut)
        # Act
        result = sut.moegliche_zuege(leeres_brett)
        # Assert
        assert len(result.schlaegt) == 5
        assert Position(x=6, y=3) in result.schlaegt
        assert Position(x=7, y=3) in result.schlaegt
        assert Position(x=7, y=5) in result.schlaegt
        assert Position(x=6, y=5) in result.schlaegt
        assert Position(x=6, y=4) in result.schlaegt

    def test_bedrohte_Felder(self, leeres_brett):
        """Wenn der König auf einem Schachbrett mit anderen Figuren steht, dann kann er sich nicht auf ein bedrohtes Feld bewegen"""

        # Arrange
        sut = Koenig(position=Position(x=4, y=4), farbe='weiss')
        andere_figur = Koenig(position=Position(x=2, y=2), farbe='schwarz')
        leeres_brett.setze_Figur(sut)
        leeres_brett.setze_Figur(andere_figur)
        # Act
        result = sut.moegliche_zuege(leeres_brett)
        # Assert
        assert len(result.schlaegt) == 7
        assert Position(x=4, y=3) in result.schlaegt
        assert Position(x=5, y=3) in result.schlaegt
        assert Position(x=5, y=4) in result.schlaegt
        assert Position(x=5, y=5) in result.schlaegt
        assert Position(x=4, y=5) in result.schlaegt
        assert Position(x=3, y=5) in result.schlaegt
        assert Position(x=3, y=4) in result.schlaegt


class TestBauer():
    class TestSchwarz():
        def test_happy_path(self, leeres_brett):
            '''Wenn ein schwarzer Bauer in der Mitte des Felds steht, dann kann er sich ein Feld runter bewegen'''
            # Arrange
            sut = Bauer(position=Position(x=4, y=4), farbe='schwarz')
            leeres_brett.setze_Figur(sut)
            # Act
            result = sut.moegliche_zuege(leeres_brett)
            # Assert
            assert len(result.bewegt) == 1
            assert Position(x=4, y=3) in result.bewegt
            assert len(result.schlaegt) == 0

        def test_kann_schlagen(self, leeres_brett):
            '''Wenn ein schwarzer Bauer schräg unter sich Figuren hat, dann kann er diese schlagen'''
            sut = Bauer(position=Position(x=4, y=4), farbe='schwarz')
            leeres_brett.setze_Figur(sut)

            figur1 = Bauer(position=Position(x=3, y=3), farbe='weiss')
            leeres_brett.setze_Figur(figur1)

            figur2 = Bauer(position=Position(x=5, y=3), farbe='weiss')
            leeres_brett.setze_Figur(figur2)
            # Act
            result = sut.moegliche_zuege(leeres_brett)
            # Assert
            assert len(result.schlaegt) == 2
            assert Position(x=3, y=3) in result.schlaegt
            assert Position(x=5, y=3) in result.schlaegt

        def test_start_linie(self, leeres_brett):
            '''Ein Bauer auf der Startlinie, kann sich zwei Felder nach vorne bewegen'''
            sut = Bauer(position=Position(x=4, y=6), farbe='schwarz')
            leeres_brett.setze_Figur(sut)
            # Act
            result = sut.moegliche_zuege(leeres_brett)
            # Assert
            assert len(result.bewegt) == 2
            assert Position(x=4, y=5) in result.bewegt
            assert Position(x=4, y=4) in result.bewegt

        def test_weg_blockiert(self, leeres_brett):
            '''Wenn vor einem Bauern eine Figur steht, dann kann der Bauer sich nicht dort hin bewegen'''
            sut = Bauer(position=Position(x=4, y=6), farbe='schwarz')
            leeres_brett.setze_Figur(sut)

            blocker = Bauer(position=Position(x=4, y=5), farbe='schwarz')
            leeres_brett.setze_Figur(blocker)
            # Act
            result = sut.moegliche_zuege(leeres_brett)
            # Assert
            assert len(result.bewegt) == 0

        def test_schach_verhindern_durch_schlagen(self, leeres_brett):
            '''Wenn der Koenig bedroht ist durch eine andere Figur die ein Bauer schlagen kann, dann ist dies der einzige mögliche Zug'''
            sut = Bauer(position=Position(x=4, y=6), farbe='schwarz')
            leeres_brett.setze_Figur(sut)

            koenig = Koenig(position=Position(x=2, y=6), farbe='schwarz')
            leeres_brett.setze_Figur(koenig)

            angreifer = Bauer(position=Position(x=3, y=5), farbe='weiss')
            leeres_brett.setze_Figur(angreifer)
            # Act
            result = sut.moegliche_zuege(leeres_brett)
            # Assert
            assert len(result.bewegt) == 0
            assert len(result.schlaegt) == 1
            assert Position(x=3, y=5) in result.schlaegt

        def test_kann_nicht_von_der_kante_springen(self, leeres_brett):
            '''Wenn der Bauer am unteren Rand steht, hat er keine möglichen Züge'''
            sut = Bauer(position=Position(x=4, y=0), farbe='schwarz')
            leeres_brett.setze_Figur(sut)
            # Act
            result = sut.moegliche_zuege(leeres_brett)
            # Assert
            assert len(result.bewegt) == 0

    class TestWeiss():
        def test_happy_path(self, leeres_brett):
            '''Wenn ein weisser Bauer in der Mitte des Felds steht, dann kann er sich ein Feld runter bewegen'''
            # Arrange
            sut = Bauer(position=Position(x=4, y=4), farbe='weiss')
            leeres_brett.setze_Figur(sut)
            # Act
            result = sut.moegliche_zuege(leeres_brett)
            # Assert
            assert len(result.bewegt) == 1
            assert Position(x=4, y=5) in result.bewegt
            assert len(result.schlaegt) == 0

        def test_kann_schlagen(self, leeres_brett):
            '''Wenn ein schwarzer Bauer schräg unter sich Figuren hat, dann kann er diese schlagen'''
            sut = Bauer(position=Position(x=4, y=4), farbe='weiss')
            leeres_brett.setze_Figur(sut)

            figur1 = Bauer(position=Position(x=5, y=5), farbe='schwarz')
            leeres_brett.setze_Figur(figur1)

            figur2 = Bauer(position=Position(x=3, y=5), farbe='schwarz')
            leeres_brett.setze_Figur(figur2)
            # Act
            result = sut.moegliche_zuege(leeres_brett)
            # Assert
            assert len(result.schlaegt) == 2
            assert Position(x=5, y=5) in result.schlaegt
            assert Position(x=5, y=5) in result.schlaegt

        def test_start_linie(self, leeres_brett):
            '''Ein Bauer auf der Startlinie, kann sich zwei Felder nach vorne bewegen'''
            sut = Bauer(position=Position(x=4, y=1), farbe='weiss')
            leeres_brett.setze_Figur(sut)
            # Act
            result = sut.moegliche_zuege(leeres_brett)
            # Assert
            assert len(result.bewegt) == 2
            assert Position(x=4, y=2) in result.bewegt
            assert Position(x=4, y=3) in result.bewegt

        def test_weg_blockiert(self, leeres_brett):
            '''Wenn vor einem Bauern eine Figur steht, dann kann der Bauer sich nicht dort hin bewegen'''
            sut = Bauer(position=Position(x=4, y=1), farbe='weiss')
            leeres_brett.setze_Figur(sut)

            blocker = Bauer(position=Position(x=4, y=2), farbe='schwarz')
            leeres_brett.setze_Figur(blocker)
            # Act
            result = sut.moegliche_zuege(leeres_brett)
            # Assert
            assert len(result.bewegt) == 0

        def test_schach_verhindern_durch_schlagen(self, leeres_brett):
            '''Wenn der Koenig bedroht ist durch eine andere Figur die ein Bauer schlagen kann, dann ist dies der einzige mögliche Zug'''
            sut = Bauer(position=Position(x=4, y=1), farbe='weiss')
            leeres_brett.setze_Figur(sut)

            koenig = Koenig(position=Position(x=2, y=1), farbe='weiss')
            leeres_brett.setze_Figur(koenig)

            angreifer = Bauer(position=Position(x=3, y=2), farbe='schwarz')
            leeres_brett.setze_Figur(angreifer)
            # Act
            result = sut.moegliche_zuege(leeres_brett)
            # Assert
            assert len(result.bewegt) == 0
            assert len(result.schlaegt) == 1
            assert Position(x=3, y=2) in result.schlaegt

        def test_kann_nicht_von_der_kante_springen(self, leeres_brett):
            '''Wenn der Bauer am unteren Rand steht, hat er keine möglichen Züge'''
            sut = Bauer(position=Position(x=4, y=7), farbe='weiss')
            leeres_brett.setze_Figur(sut)
            # Act
            result = sut.moegliche_zuege(leeres_brett)
            # Assert
            assert len(result.bewegt) == 0


class TestLaeufer():
    def test_happy_path(self, leeres_brett):
        ''' Ein Läufer kann sich auf den Diagonalen bewegen'''
        # Arrange
        sut = Laeufer(position=Position(x=4, y=4), farbe='schwarz')
        leeres_brett.setze_Figur(sut)
        # Act
        result = sut.moegliche_zuege(leeres_brett)
        # Assert
        assert len(result.schlaegt) >= 13
        assert Position(x=3, y=5) in result.schlaegt
        assert Position(x=2, y=6) in result.schlaegt
        assert Position(x=1, y=7) in result.schlaegt
        assert Position(x=5, y=3) in result.schlaegt
        assert Position(x=6, y=2) in result.schlaegt
        assert Position(x=7, y=1) in result.schlaegt

        assert Position(x=0, y=0) in result.schlaegt
        assert Position(x=1, y=1) in result.schlaegt
        assert Position(x=2, y=2) in result.schlaegt
        assert Position(x=3, y=3) in result.schlaegt
        assert Position(x=5, y=5) in result.schlaegt
        assert Position(x=6, y=6) in result.schlaegt
        assert Position(x=7, y=7) in result.schlaegt

    def test_kann_nicht_vom_rand_springen(self, leeres_brett):
        '''Ein Läufer kann nicht über die Grenzen des Felds hinaus sich bewegen'''
        # Arrange
        sut = Laeufer(position=Position(x=4, y=4), farbe='schwarz')
        leeres_brett.setze_Figur(sut)
        # Act
        result = sut.moegliche_zuege(leeres_brett)
        # Assert
        assert len(result.schlaegt) == 13
        xes = [x.x for x in result.schlaegt]
        assert min(xes) == 0
        assert max(xes) == 7
        ys = [x.y for x in result.schlaegt]
        assert min(ys) == 0
        assert max(ys) == 7

    def test_blockiert(self, leeres_brett):
        '''Ein Läufer kann nicht durch Figuren der eigenen Farbe laufen'''
        # Arrange
        sut = Laeufer(position=Position(x=4, y=4), farbe='schwarz')
        leeres_brett.setze_Figur(sut)

        blocker1 = Bauer(position=Position(x=3, y=3), farbe='schwarz')
        leeres_brett.setze_Figur(blocker1)

        blocker2 = Bauer(position=Position(x=5, y=5), farbe='schwarz')
        leeres_brett.setze_Figur(blocker2)

        blocker3 = Bauer(position=Position(x=3, y=5), farbe='schwarz')
        leeres_brett.setze_Figur(blocker3)

        blocker4 = Bauer(position=Position(x=5, y=3), farbe='schwarz')
        leeres_brett.setze_Figur(blocker4)

        # Act
        result = sut.moegliche_zuege(leeres_brett)
        # Assert
        assert len(result.schlaegt) == 0

    def test_kann_schlagen(self, leeres_brett):
        '''Ein Läufer kann gegnerische Figuren schlagen, danach aber nicht weiter laufen'''
        # Arrange
        sut = Laeufer(position=Position(x=4, y=4), farbe='schwarz')
        leeres_brett.setze_Figur(sut)

        blocker1 = Bauer(position=Position(x=3, y=3), farbe='weiss')
        leeres_brett.setze_Figur(blocker1)

        blocker2 = Bauer(position=Position(x=5, y=5), farbe='weiss')
        leeres_brett.setze_Figur(blocker2)

        blocker3 = Bauer(position=Position(x=3, y=5), farbe='weiss')
        leeres_brett.setze_Figur(blocker3)

        blocker4 = Bauer(position=Position(x=5, y=3), farbe='weiss')
        leeres_brett.setze_Figur(blocker4)

        # Act
        result = sut.moegliche_zuege(leeres_brett)
        # Assert
        assert len(result.schlaegt) == 4
        assert Position(x=5, y=3) in result.schlaegt
        assert Position(x=3, y=5) in result.schlaegt
        assert Position(x=3, y=3) in result.schlaegt
        assert Position(x=5, y=5) in result.schlaegt

    def test_schach_verhindern_durch_schlagen(self, leeres_brett):
        '''Wenn der König im Schach ist durch eine Figur, die durch den Läufer schlagbar ist, dann ist dies der einzige möglich Zug'''
        # Arrange
        sut = Laeufer(position=Position(x=4, y=4), farbe='weiss')
        leeres_brett.setze_Figur(sut)

        koenig = Koenig(position=Position(x=6, y=4), farbe='weiss')
        leeres_brett.setze_Figur(koenig)

        angreifer = Laeufer(position=Position(x=5, y=5), farbe='schwarz')
        leeres_brett.setze_Figur(angreifer)
        # Act
        result = sut.moegliche_zuege(leeres_brett)
        # Assert
        assert len(result.schlaegt) == 1
        assert Position(x=5, y=5) in result.schlaegt

    def test_kann_in_den_Weg_gehen(self, leeres_brett):
        '''Wenn der König im Schach steht und der Läufer in den Weg springen kann, dann ist das der einzige mögliche Zug'''
        # Arrange
        sut = Laeufer(position=Position(x=5, y=3), farbe='weiss')
        leeres_brett.setze_Figur(sut)

        koenig = Koenig(position=Position(x=3, y=3), farbe='weiss')
        leeres_brett.setze_Figur(koenig)

        angreifer = Laeufer(position=Position(x=5, y=5), farbe='schwarz')
        leeres_brett.setze_Figur(angreifer)

        # Act
        result = sut.moegliche_zuege(leeres_brett)
        # Assert
        assert len(result.schlaegt) == 1
        assert Position(x=4, y=4) in result.schlaegt


class TestSpringer():



    def test_springer_kann_nicht_vom_brett_springen_unten(self,leeres_brett):
        '''Wenn der Springer am unteren Rand steht, kann er nicht vom Brett springen'''
        # Arrange
        sut = Springer(position=Position(x=0, y=4), farbe='weiss')
        leeres_brett.setze_Figur(sut)
        # Act
        result = sut.moegliche_zuege(leeres_brett)
        # Assert
        assert len(result.bewegt) == 4
        assert Position(x=1, y=6) in result.bewegt
        assert Position(x=2, y=5) in result.bewegt
        assert Position(x=1, y=2) in result.bewegt
        assert Position(x=2, y=3) in result.bewegt
    def test_springer_kann_nicht_vom_brett_springen_rechts(self,leeres_brett):
        '''Wenn der Springer am unteren Rand steht, kann er nicht vom Brett springen'''
        # Arrange
        sut = Springer(position=Position(x=4, y=7), farbe='weiss')
        leeres_brett.setze_Figur(sut)
        # Act
        result = sut.moegliche_zuege(leeres_brett)
        # Assert
        assert len(result.bewegt) == 4
        assert Position(x=5, y=5) in result.bewegt
        assert Position(x=6, y=6) in result.bewegt
        assert Position(x=3, y=5) in result.bewegt
        assert Position(x=2, y=6) in result.bewegt
    def test_springer_kann_nicht_vom_brett_springen_links(self,leeres_brett):
        '''Wenn der Springer am unteren Rand steht, kann er nicht vom Brett springen'''
        # Arrange
        sut = Springer(position=Position(x=0, y=4), farbe='weiss')
        leeres_brett.setze_Figur(sut)
        # Act
        result = sut.moegliche_zuege(leeres_brett)
        # Assert
        assert len(result.bewegt) == 4
        assert Position(x=1, y=6) in result.bewegt
        assert Position(x=2, y=5) in result.bewegt
        assert Position(x=1, y=2) in result.bewegt
        assert Position(x=2, y=3) in result.bewegt
    def test_springer_kann_nicht_vom_brett_springen_oben(self,leeres_brett):
        '''Wenn der Springer am unteren Rand steht, kann er nicht vom Brett springen'''
        # Arrange
        sut = Springer(position=Position(x=7, y=4), farbe='weiss')
        leeres_brett.setze_Figur(sut)
        # Act
        result = sut.moegliche_zuege(leeres_brett)
        # Assert
        assert len(result.bewegt) == 4

        assert Position(x=5, y=5) in result.bewegt
        assert Position(x=6, y=6) in result.bewegt
        assert Position(x=6, y=2) in result.bewegt
        assert Position(x=5, y=3) in result.bewegt


    @pytest.mark.parametrize("farbe,figur,beschreibung",
        [
            ('weiss',Bauer,'Springer kann über weisse Bauern springern'),
            ('weiss',Laeufer,'Springer kann über weisse Laeufer springern'),
            ('weiss',Springer,'Springer kann über weisse Springer springern'),
            ('schwarz',Bauer,'Springer kann über schwarze Bauern springern'),
            ('schwarz',Laeufer,'Springer kann über schwarze Bauern springern'),
            ('schwarz',Springer,'Springer kann über schwarze Bauern springern'),
        ])
    def test_springer_kann_drueberspringen(self, farbe, figur,beschreibung,leeres_brett):
        '''Ein Springer kann über andere Figuren rüberspringen, egal welche Farbe oder welches Teil es ist'''
        # Arrange
        sut = Springer(position=Position(x=4, y=4), farbe='weiss')
        leeres_brett.setze_Figur(sut)
        leeres_brett.setze_Figur(figur(farbe=farbe, position = sut.position.plus(1,0)))
        leeres_brett.setze_Figur(figur(farbe=farbe, position = sut.position.plus(1,1)))
        leeres_brett.setze_Figur(figur(farbe=farbe, position = sut.position.plus(1,-1)))
        leeres_brett.setze_Figur(figur(farbe=farbe, position = sut.position.plus(0,1)))
        leeres_brett.setze_Figur(figur(farbe=farbe, position = sut.position.plus(0,-1)))
        leeres_brett.setze_Figur(figur(farbe=farbe, position = sut.position.plus(-1,1)))
        leeres_brett.setze_Figur(figur(farbe=farbe, position = sut.position.plus(-1,0)))
        leeres_brett.setze_Figur(figur(farbe=farbe, position = sut.position.plus(-1,-1)))
        # Act
        result = sut.moegliche_zuege(leeres_brett)
        # Assert
        assert len(result.bewegt) == 8
        assert Position(x=5, y=6) in result.bewegt
        assert Position(x=6, y=5) in result.bewegt
        assert Position(x=5, y=2) in result.bewegt
        assert Position(x=2, y=5) in result.bewegt
        assert Position(x=3, y=6) in result.bewegt
        assert Position(x=6, y=3) in result.bewegt
        assert Position(x=3, y=2) in result.bewegt
        assert Position(x=2, y=3) in result.bewegt

    def test_springer_kann_nicht_aus_dem_weg_wenn_es_schach_waere(self, leeres_brett):
        '''Wenn ein Springer durch seine Anwesenheit ein Schach verhindert von einem Laueufer (Spiess), dann darf der Springer nicht weg ziehen'''
        # Arrange
        sut = Springer(position=Position(x=4, y=4), farbe='weiss')
        leeres_brett.setze_Figur(sut)
        koenig = Koenig(position=Position(x=3,y=3), farbe=sut.farbe)
        leeres_brett.setze_Figur(koenig)

        angreifer = Laeufer(position=Position(x=5,y=5), farbe='schwarz')
        leeres_brett.setze_Figur(angreifer)
        # Act
        result = sut.moegliche_zuege(leeres_brett)
        # Assert
        assert len(result.bewegt) == 0