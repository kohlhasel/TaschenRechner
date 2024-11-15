from pydantic import BaseModel


class StringKonverter(BaseModel):
    def str_to_int(self, zahl: int):
        try:
            return int(zahl)
        except:
            raise ValueError(f'{zahl} lies sich nicht zu int konvertieren ')


class Taschenrechner(BaseModel):
    converter: StringKonverter = StringKonverter()

    def addition(self, a, b):
        return self.converter.str_to_int(a) + self.converter.str_to_int(b)

    def subtraktion(self, a, b):
        return self.converter.str_to_int(a) - self.converter.str_to_int(b)

    def multiplikation(self, a, b):
        return self.converter.str_to_int(a) * self.converter.str_to_int(b)
