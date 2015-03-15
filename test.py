import conversion
import unittest


class CelsiusToKelvin(unittest.TestCase):

	celsiusToKelvin = ( (300.00, 573.15),
					    (150.00, 423.15),
					    (115.00, 388.15),
	                    (96.00, 369.15),
	                    (40.00, 313.15) )

	
	def testConvertCelsiusToKelvin(self):
		for celsius, kelvin in self.celsiusToKelvin:
			result = conversion.convertCelsiusToKelvin(celsius)
			self.assertEqual(kelvin, result)


class CelsiusToFahrenheit(unittest.TestCase):
    
    celsiusToFahrenheit = ( (300.00, 572.00),
    						(215.00, 419.00),
							(150.00, 302.00),
							(96.00, 204.80),
							(40.00, 104.00) )

    def testConvertCelsiusToFahrenheit(self):
    	for celsius, fahrenheit in self.celsiusToFahrenheit:
    		print fahrenheit
    		result = conversion.convertCelsiusToFahrenheit(celsius)
    		self.assertEqual(fahrenheit, result)


if __name__ == "__main__":
    unittest.main()