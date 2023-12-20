import pytest
import requests as requests

from Hausaufgabe import dumme_addition, groesste_n_zahlen_implementation_1, groesste_n_zahlen_implementation_2


class TestAufgabeEins():
    def test_happy_path_1(self):
        '''addition verhält sich so wie man es erwartet'''
        # Arrange
        input1 = 5
        input2 = 6
        # Act
        result = dumme_addition(input1, input2)
        # Assert
        assert result == 11

    def test_happy_path_2(self):
        '''addition verhält sich so wie man es erwartet'''
        # Arrange
        input1 = 0
        input2 = 5
        # Act
        result = dumme_addition(input1, input2)
        # Assert
        assert result == 5

    def test_assoziativ(self):
        '''addition ist assoziativ <==> (a+b)+c= a+(b+c)'''
        # Arrange
        summanden = [1, 2, 3]
        # Act
        result = dumme_addition(dumme_addition(summanden[0], summanden[1]), summanden[2])
        # Assert
        assert result == dumme_addition(summanden[0], dumme_addition(summanden[1], summanden[2]))


    def test_0_neutrales_element(self):
        '''0 ist neutrales Element der addition <==> a+0=a '''
        # Arrange
        input = 5
        # Act
        result = dumme_addition(0, input)
        # Assert
        assert result == input

    @pytest.mark.parametrize("summand1,summand2,expected,beschreibung"
            , [
                                     (1, 2, 3, 'positiv + positiv'),
                                     (4, 5, 9, 'positiv + positiv'),
                                     (42, 69, 111, 'positiv + positiv'),
                                     (111, 222, 333, 'Grosse positive Zahlen')])
    def test_verschiedene_werte(self,summand1, summand2, expected, beschreibung):
            '''Testet in verschiedenen Szenarien, dass die richtigen Werte berechnet werden'''
            #Arrange
            #Act
            result = dumme_addition(summand1, summand2)
            #Assert
            assert result == expected




class TestAufgabeZwei():

    def test_findet_hoechste_5_implementation_1(self):
        #Arrange
        liste=[1,2,3,4,5,6,7,8,9,10]
        #Act
        result = groesste_n_zahlen_implementation_1(liste,5)
        #Assert
        assert result == [6,7,8,9,10]


    def test_findet_hoechste_5_implementation_2(self):
        #Arrange
        liste=[1,2,3,4,5,6,7,8,9,10]
        #Act
        result = groesste_n_zahlen_implementation_2(liste,5)
        #Assert
        assert result == [10,9,8,7,6]

class TestAufgabeFuenf():
    def test_richtige_rueckgabe(self):
        #Arrange
        url = "https://api.predic8.de/shop/v2/products"
        product_name = "Test -Mangos"
        product_price = 2.79
        #Act
        result = requests.post(url= url, json = {"name" : product_name, "price" : product_price}, headers={"Content-Type": "application/json"})
        #Assert
        json = result.json()
        #assert json['id']== -1
        #assert json['self_link'] == '/shop/v2/products/-1'
        assert json['name'] == product_name
        assert json['price'] == product_price
