from modulos import *

class Validadores:
    def validate_entry2(self, text):
        if text == "": return True
        try:
            value = int(text)
        except ValueError:  # oops, couldn't convert to int

            return False
        return 0 <= value <= 100
    def validate_entry20(self, text):
        if text == "": return True
        try:
            value = int(text)
        except ValueError:  # oops, couldn't convert to int

            return False
        return 0 <= value <= 100000000000000000000
    
    def validate_entry11(self, text):
        if text == "": return True
        try:
            value = int(text)
        except ValueError:  # oops, couldn't convert to int

            return False
        return 0 <= value <= 100000000000

    def validate_entry2float(self, text):
        if text == "": return True
        try:
            value = float(text)
        except ValueError:  # oops, couldn't convert to int

            return False
        return len(text) < 4
    def validate_entry9float(self, text):
        if text == "": return True
        try:
            value = float(text)
        except ValueError:  # oops, couldn't convert to int

            return False
        return len(text) < 10