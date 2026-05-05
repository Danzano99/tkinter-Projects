class TemperatureModel:
    def fahrenheit_to_celsius(self, fahrenheit_text):
        """
        Converts Fahrenheit input into Celsius.
        If input is invalid, returns None, and asks for valid number
        """
        try:
            fahrenheit = float(fahrenheit_text)
            celsius = (fahrenheit - 32) * 5 / 9
            return fahrenheit, celsius

        except ValueError:
            return None