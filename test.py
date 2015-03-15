import conversion
import unittest

"""
test conversion celsius to kelvin and kelivn to celsius
"""
class CelsiusAndKelvin(unittest.TestCase):

	values = ( 
		(300.00, 573.15),
		(150.00, 423.15),
		(115.00, 388.15) )

	
	def testConvertCelsiusToKelvin(self):
		for celsius, kelvin in self.values:
			result = conversion.convertCelsiusToKelvin(celsius)
			self.assertEqual(kelvin, result)

	def testConvertKelvinToCelsius(self):
		for celsius, kelvin in self.values:
			result = conversion.convertKelvinToCelsius(kelvin)
			self.assertEqual(celsius, result)

"""
test conversion celsius to fahrenheit and fahrenheit to celsius
"""
class CelsiusAndFahrenheit(unittest.TestCase):
    
    values = ( 
    	(300.00, 572.00),
		(215.00, 419.00),
		(150.00, 302.00))

    def testConvertCelsiusToFahrenheit(self):
    	for celsius, fahrenheit in self.values:
    		result = conversion.convertCelsiusToFahrenheit(celsius)
    		self.assertEqual(fahrenheit, result)
    
    def testConvertFahrenheitToCelsius(self):
    	for celsius, fahrenheit in self.values:
    		result = conversion.convertFahrenheitToCelsius(fahrenheit)
    		self.assertEqual(celsius, result)

"""
test conversion celsius to fahrenheit and fahrenheit to celsius
"""
class CelsiusAndFahrenheit(unittest.TestCase):
    
    values = ( 
    	(300.00, 572.00),
		(215.00, 419.00),
		(150.00, 302.00))

    def testConvertCelsiusToFahrenheit(self):
    	for celsius, fahrenheit in self.values:
    		result = conversion.convertCelsiusToFahrenheit(celsius)
    		self.assertEqual(fahrenheit, result)
    
    def testConvertFahrenheitToCelsius(self):
    	for celsius, fahrenheit in self.values:
    		result = conversion.convertFahrenheitToCelsius(fahrenheit)
    		self.assertEqual(celsius, result)


"""
test conversion kelvin to fahrenheit and fahrenheit to kelvin 
"""
class KelvinAndFahrenheit(unittest.TestCase):
    
    values = ( 
        (300.00, 80.33),
        (215.00, -72.67),
        (150.00, -189.67))

    def testConvertKelvinToFahrenheit(self):
    	for kelvin, fahrenheit in self.values:
    		result = conversion.convertKelvinToFahrenheit(kelvin)
    		self.assertEqual(fahrenheit, result)

    def testConvertFahrenheitToKelvin(self):
    	for kelvin, fahrenheit in self.values:
    		result = conversion.convertFahrenheitToKelvin(fahrenheit)
    		self.assertEqual(kelvin, result)


if __name__ == "__main__":
    unittest.main()