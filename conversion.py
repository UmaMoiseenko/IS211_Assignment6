"""
Takes in a float representing a Celsius measurement, and returns that
temperature converted into Kelvins
"""
def convertCelsiusToKelvin(floatVal):
    celsius = float(floatVal) + 273.15
    return celsius

"""
Takes in a float representing a Celsius measurement, and returns
that temperature converted into Fahrenheit
"""
def convertCelsiusToFahrenheit(floatVal):
    fahrenheit = float(floatVal) * 9/5 + 32
    return fahrenheit



# print convertCelsiusToFahrenheit(300.00)
# print convertCelsiusToFahrenheit(150.00)
print convertCelsiusToFahrenheit(215.00)
# print convertCelsiusToFahrenheit(96.00)
# print convertCelsiusToFahrenheit(40.00)
