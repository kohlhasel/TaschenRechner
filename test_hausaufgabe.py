import pytest
import requests as requests

from Hausaufgabe import dumme_multiplikation, groesste_n_zahlen_implementation_1, groesste_n_zahlen_implementation_2


class TestAufgabeEins():
    def test_happy_path(self):
        '''multiplikation verhält sich so wie man es erwartet'''
        # Arrange
        input1 = 5
        input2 = 6
        # Act
        result = dumme_multiplikation(input1, input2)
        # Assert
        assert result == 30

    'def test_happy_path_weiterer_Testfall(self):
        '''Multiplikation, wenn input 2 kleiner ist als input 1'''
       ' # Arrange
       ' input1 = 8
       ' input2 = 5
       ' # Act
       ' result = dumme_multiplikation(input1, input2)
        # Assert
      '  assert result == 40
        

    def test_multiplikation_mit_null(self):
        '''Die Multiplikation mit 0 soll 0 ergeben'''
        # Arrange
        input1 = 2
        input2 = 0
        # Act
        result = dumme_multiplikation(input1, input2)
        # Assert
        assert result == 0

    def test_assoziativ(self):
        '''Multiplikation ist assoziativ <==> (a*b)*c= a*(b*c)'''
        # Arrange
        summanden = [1, 2, 3]
        # Act
        result = dumme_multiplikation(dumme_multiplikation(summanden[0], summanden[1]), summanden[2])
        # Assert
        assert result == dumme_multiplikation(summanden[0], dumme_multiplikation(summanden[1], summanden[2]))


    def test_1_neutrales_element(self):
        '''1 ist neutrales Element der multiplikation <==> a*1=a '''
        # Arrange
        input = 5
        # Act
        result = dumme_multiplikation(1, input)
        # Assert
        assert result == input

    @pytest.mark.parametrize("faktor1,faktor2,expected,beschreibung"
            , [
                                     (1, 2, 2, 'positiv * positiv'),
                                     (4, 5, 20, 'positiv * positiv'),
                                     (42, 69, 2898, 'positiv * positiv'),
                                     (111, 222, 24642, 'Grosse positive Zahlen')])
    def test_verschiedene_werte(self, faktor1, faktor2, expected, beschreibung):
            '''Testet in verschiedenen Szenarien, dass die richtigen Werte berechnet werden'''
            #Arrange
            #Act
            result = dumme_multiplikation(faktor1, faktor2)
            #Assert
            assert result == expected




class TestAufgabeZwei():
    #Sowohl implementation2 als auch implementation sind valide Antworten um die höchsten n elemente einer Liste zu finden.
    # Was wurde bei der Auswahl der Asserts falsch gemacht, sodass einer der Tests scheitert und der andere erfolgreich ist?
    def test_findet_hoechste_5_implementation_1(self):
        #Arrange
        liste=[1,2,3,4,5,6,7,8,9,10]
        #Act
        result = groesste_n_zahlen_implementation_1(liste,5)
        #Assert
        assert set(result) == set([6,7,8,9,10])


    def test_findet_hoechste_5_implementation_2(self):
        #Arrange
        liste=[1,2,3,4,5,6,7,8,9,10]
        #Act
        result = groesste_n_zahlen_implementation_2(liste,5)
        #Assert
        assert set(result) == set([6,7,8,9,10])

