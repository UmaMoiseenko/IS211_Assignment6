from decimal import Decimal

"""
Takes in a float representing a Celsius measurement, and returns that
temperature converted into Kelvins
"""
def convertCelsiusToKelvin(floatVal):
    return float(floatVal) + 273.15

"""
Takes in a float representing a Celsius measurement, and returns
that temperature converted into Fahrenheit
"""
def convertCelsiusToFahrenheit(floatVal):
    return float(floatVal) * 9/5 + 32

"""
Takes in a float representing a Fahrenheit measurement, and returns
that temperature converted into Celsius
"""
def convertFahrenheitToCelsius(floatVal):
    return round( (floatVal - 32) * 5/9)

"""
Takes in a float representing a Fahrenheit measurement, and returns
that temperature converted into Kelvin
"""
def convertFahrenheitToKelvin(floatVal):
    return (float(floatVal) + 459.67) * 5/9

"""
Takes in a float representing a Kelvin measurement, and returns
that temperature converted into Celsius
"""
def convertKelvinToCelsius(floatVal):
    return float(floatVal) - 273.15

"""
Takes in a float representing a Kelvin measurement, and returns
that temperature converted into Fahrenheit
"""
def convertKelvinToFahrenheit(floatVal):
    result = Decimal(float(floatVal)  * 9/5 - 459.67)
    return round(result,2)
