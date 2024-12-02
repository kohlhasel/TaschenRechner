import pytest

from calcs import Taschenrechner


class Testaddition:
    def test_happy_path(self):
        '''addition verhält sich so wie man es erwartet'''
        # Arrange
        sut= Taschenrechner()
        input1 = 5
        input2 = 6
        # Act
        result = sut.addition(input1, input2)
        # Assert
        assert result == 11

    def test_kommutativ(self):
        '''addition ist kommutativ <==> a+b==b+a'''
        # Arrange
        sut= Taschenrechner()
        input1 = 5
        input2 = 6
        # Act
        result = sut.addition(input1, input2)
        # Assert
        assert result == sut.addition(input2, input1)

    def test_assoziativ(self):
        '''addition ist assoziativ <==> (a+b)+c= a+(b+c)'''
        # Arrange
        sut= Taschenrechner()
        summanden = [1, 2, 3]
        # Act
        result = sut.addition(sut.addition(summanden[0], summanden[1]), summanden[2])
        # Assert
        assert result == sut.addition(summanden[0], sut.addition(summanden[1], summanden[2]))

    def test_0_neutrales_element(self):
        '''0 ist neutrales Element der addition <==> a+0=a '''
        # Arrange
        sut= Taschenrechner()
        input = 5
        # Act
        result = sut.addition(5, 0)
        # Assert
        assert result == input

    @pytest.mark.parametrize("summand1,summand2,expected,beschreibung"
        , [
                                 (1, 2, 3, 'positiv + positiv'),
                                 (-1, 1, 0, 'negativ+positiv'),
                                 (-1, -1, -2, 'negativ+negativ'),
                                 (-11111111, -22222222, -33333333, 'Grosse Negative Zahlen'),
                                 (1111111, 2222222, 3333333, 'Grosse positive Zahlen')])
    def test_verschiedene_werte(self, summand1, summand2, expected, beschreibung):
        '''Testet in verschiedenen Szenarien, dass die richtigen Werte berechnet werden'''
        #Arrange
        sut= Taschenrechner()
        #Act
        result = sut.addition(summand1,summand2)
        #Assert
        assert result == expected

    class TestFalscheInputs():
        '''addition gibt valueErrors zurück wenn der input sich nicht sauber zu einer Zahl verarbeiten lásst'''
        def test_falscher_input_zuerst(self):
            #Arrange
            sut = Taschenrechner()
            input1 = 'wurst'
            input2 = 1
            #Act & Assert
            with pytest.raises(ValueError):
                result = sut.addition(input1,input2)

        def test_falscher_input_als_zweites(self):
            #Arrange
            sut = Taschenrechner()
            input1 = 1
            input2 = 'input'
            #Act & Assert
            with pytest.raises(ValueError):
                result = sut.addition(input1,input2)

        def test_beide_inputs_falsch(self):
            # Arrange
            sut = Taschenrechner()
            input1 = 'wurst'
            input2 = 'käse'
            # Act & Assert
            with pytest.raises(ValueError):
                result = sut.addition(input1, input2)

class TestSubtraktion:
    def test_happy_path(self):
        '''Subtraktion verhält sich so wie man es erwartet'''
        # Arrange
        sut= Taschenrechner()
        input1 = 5
        input2 = 6
        # Act
        result = sut.subtraktion(input1, input2)
        # Assert
        assert result == -1

    def test_0_neutrales_element(self):
        '''0 ist neutrales Element der subtraktion <==> a+0=a '''
        # Arrange
        sut= Taschenrechner()
        input = 5
        # Act
        result = sut.subtraktion(5, 0)
        # Assert
        assert result == input

    @pytest.mark.parametrize("summand1,summand2,expected,beschreibung"
        , [
                                 (1, 2, -1, 'positiv - positiv'),
                                 (-1, 1, -2, 'negativ-positiv'),
                                 (-1, -1, 0, 'negativ-negativ'),
                                 (-11111111, -22222222, 11111111, 'Grosse Negative Zahlen'),
                                 (1111111, 2222222, -1111111, 'Grosse positive Zahlen')])
    def test_verschiedene_werte(self, summand1, summand2, expected, beschreibung):
        '''Testet in verschiedenen Szenarien, dass die richtigen Werte berechnet werden'''
        #Arrange
        sut= Taschenrechner()
        #Act
        result = sut.subtraktion(summand1,summand2)
        #Assert
        assert result == expected

    class TestFalscheInputs():
        '''subtraktion gibt valueErrors zurück wenn der input sich nicht sauber zu einer Zahl verarbeiten lásst'''
        def test_falscher_input_zuerst(self):
            #Arrange
            sut = Taschenrechner()
            input1 = 'wurst'
            input2 = 1
            #Act & Assert
            with pytest.raises(ValueError):
                result = sut.subtraktion(input1,input2)

        def test_falscher_input_als_zweites(self):
            #Arrange
            sut = Taschenrechner()
            input1 = 1
            input2 = 'input'
            #Act & Assert
            with pytest.raises(ValueError):
                result = sut.subtraktion(input1,input2)

        def test_beide_inputs_falsch(self):
            # Arrange
            sut = Taschenrechner()
            input1 = 'wurst'
            input2 = 'käse'
            # Act & Assert
            with pytest.raises(ValueError):
                result = sut.subtraktion(input1, input2)

class TestMultiplikation:
    def test_happy_path(self):
        '''Multiplikation verhält sich so wie man es erwartet'''
        # Arrange
        sut= Taschenrechner()
        input1 = 5
        input2 = 6
        # Act
        result = sut.multiplikation(input1, input2)
        # Assert
        assert result == 30

    def test_kommutativ(self):
        '''mMltiplikation ist kommutativ <==> a*b=b*a'''
        #Arrange
        sut = Taschenrechner()
        input1=5
        input2=6
        #Act
        result = sut.multiplikation(input1,input2)
        #Assert
        assert result == sut.multiplikation(input2,input1)

    def test_assoziativ(self):
        '''Multiplikation ist assoziativ, a*(b*c) = (a*b)*c'''
        #Arrange
        sut = Taschenrechner()
        input1,input2,input3=[2,3,4]
        #Act
        result = sut.multiplikation(input1,sut.multiplikation(input2,input3))
        #Assert
        assert result == sut.multiplikation(sut.multiplikation(input1,input2),input3)

    def test_multiplikation_mit_0(self):
        '''0 mal x ist 0  <==> a*0=a '''
        # Arrange
        sut= Taschenrechner()
        input = 5
        # Act
        result = sut.multiplikation(input, 0)
        # Assert
        assert result == 0


    def test_1_neutrales_element(self):
        '''1 ist neutrales Element der Multiplikation  <==> a*1=a '''
        # Arrange
        sut= Taschenrechner()
        input = 5
        # Act
        result = sut.multiplikation(input, 1)
        # Assert
        assert result == input

    @pytest.mark.parametrize("summand1,summand2,expected,beschreibung"
        , [
                                 (1, 2, 2, 'positiv * positiv'),
                                 (-1, 1, -1, 'negativ*positiv'),
                                 (-1, -1, 1, 'negativ*negativ'),
                                 (-11111111, -22222222, 246913575308642, 'Grosse Negative Zahlen'),
                                 (1111111, 2222222, 2469135308642, 'Grosse positive Zahlen')])
    def test_verschiedene_werte(self, summand1, summand2, expected, beschreibung):
        '''Testet in verschiedenen Szenarien, dass die richtigen Werte berechnet werden. asdfasdfasdf werwer sdfwer sdfsdwerwer '''
        #Arrange
        sut= Taschenrechner()
        #Act
        result = sut.multiplikation(summand1,summand2)
        #Assert
        assert result == expected

    class TestFalscheInputs():
        '''Multiplikation gibt valueErrors zurück wenn der input sich nicht sauber zu einer Zahl verarbeiten lásst'''
        def test_falscher_input_zuerst(self):
            #Arrange
            sut = Taschenrechner()
            input1 = 'wurst'
            input2 = 1
            #Act & Assert
            with pytest.raises(ValueError):
                result = sut.multiplikation(input1,input2)

        def test_falscher_input_als_zweites(self):
            #Arrange
            sut = Taschenrechner()
            input1 = 1
            input2 = 'input'
            #Act & Assert
            with pytest.raises(ValueError):
                result = sut.multiplikation(input1,input2)

        def test_beide_inputs_falsch(self):
            # Arrange
            sut = Taschenrechner()
            input1 = 'wurst'
            input2 = 'käse'
            # Act & Assert
            with pytest.raises(ValueError):
                result = sut.multiplikation(input1, input2)