import conversions
import unittest

"""
test conversion celsius to kelvin 
"""
class CelsiusToKelvin(unittest.TestCase):

	def testConvertCelsiusToKelvin_default(self):
		result = conversion.convertCelsiusToKelvin(300.00)
		self.assertEqual(573.15, result)

	def testConvertCelsiusToKelvin_zeroCelsius(self):
		result = conversion.convertCelsiusToKelvin(0.00)
		self.assertEqual(273.15, result)

	def testConvertCelsiusToKelvin_decimalValues(self):
		result = conversion.convertCelsiusToKelvin(0.02)
		self.assertEqual(273.17, result)

	def testConvertCelsiusToKelvin_negativeValues(self):
		result = conversion.convertCelsiusToKelvin(-280.00)
		self.assertEqual(-6.85, result)

	def testConvertCelsiusToKelvin_largeNumber(self):
		result = conversion.convertCelsiusToKelvin(2345670)
		self.assertEqual(2345943.15, result)

"""
test conversion kelvin to celsius
"""
class KelvinToCelsius(unittest.TestCase):

	def testConvertKelvinToCelsius_default(self):
		result = conversion.convertKelvinToCelsius(573.15)
		self.assertEqual(300.00, result)

	def testConvertKelvinToCelsius_zeroCelsius(self):
		result = conversion.convertKelvinToCelsius(273.15)
		self.assertEqual(0.00, result)

	def testConvertKelvinToCelsius_decimalValues(self):
		result = conversion.convertKelvinToCelsius(273.17)
		self.assertEqual(0.02, result)

	def testConvertKelvinToCelsius_negativeValues(self):
		result = conversion.convertKelvinToCelsius(-6.85)
		self.assertEqual(-280.00, result)

	def testConvertKelvinToCelsius_largeNumber(self):
		result = conversion.convertKelvinToCelsius(2345943.15)
		self.assertEqual(2345670, result)


"""
test conversion celsius to fahrenheit
"""
class CelsiusToFahrenheit(unittest.TestCase):
    
	def testCelsiusToFahrenheit_default(self):
		result = conversion.convertCelsiusToFahrenheit(300.00)
		self.assertEqual(572.00, result)

	def testCelsiusToFahrenheit_zeroCelsius(self):
		result = conversion.convertCelsiusToFahrenheit(0.00)
		self.assertEqual(32.00, result)

	def testCelsiusToFahrenheit_decimalValues(self):
		result = conversion.convertCelsiusToFahrenheit(15.5)
		self.assertEqual(59.9, result)

	def testCelsiusToFahrenheit_negativeValues(self):
		result = conversion.convertCelsiusToFahrenheit(-55.00)
		self.assertEqual(-67.00, result)

	def testCelsiusToFahrenheit_largeNumber(self):
		result = conversion.convertCelsiusToFahrenheit(2345670)
		self.assertEqual(4222238.00, result)


"""
test conversion fahrenheit to celsius
"""
class FahrenheitToCelsius(unittest.TestCase):
    
	def testFahrenheitToCelsius_default(self):
		result = conversion.convertFahrenheitToCelsius(572.00)
		self.assertEqual(300.00, result)

	def testFahrenheitToCelsius_zeroCelsius(self):
		result = conversion.convertFahrenheitToCelsius(32.00)
		self.assertEqual(0.00, result)

	def testFahrenheitToCelsius_decimalValues(self):
		result = conversion.convertFahrenheitToCelsius(59.9)
		self.assertEqual(15.5, result)

	def testFahrenheitToCelsius_negativeValues(self):
		result = conversion.convertFahrenheitToCelsius(-67.00)
		self.assertEqual(-55.00, result)

	def testFahrenheitToCelsius_largeNumber(self):
		result = conversion.convertFahrenheitToCelsius(4222238.00)
		self.assertEqual(2345670, result)

"""
test conversion kelvin to fahrenheit
"""
class KelvinToFahrenheit(unittest.TestCase):

	def testKelvinToFahrenheit_default(self):
		result = conversion.convertKelvinToFahrenheit(300.00)
		self.assertEqual(80.33, result)

	def testKelvinToFahrenheit_zeroKelvin(self):
		result = conversion.convertKelvinToFahrenheit(0.00)
		self.assertEqual(-459.67, result)

	def testKelvinToFahrenheit_decimalValues(self):
		result = conversion.convertKelvinToFahrenheit(305.35)
		self.assertEqual(89.96, result)

	def testKelvinToFahrenheit_negativeValues(self):
		result = conversion.convertKelvinToFahrenheit(-30.35)
		self.assertEqual(-514.3, result)

	def testKelvinToFahrenheit_largeNumber(self):
		result = conversion.convertKelvinToFahrenheit(4222238.00)
		self.assertEqual(7599568.73, result)

"""
test conversion fahrenheit to kelvin 
"""
class FahrenheitToKelvin(unittest.TestCase):

	def testFahrenheitToKelvin_default(self):
		result = conversion.convertFahrenheitToKelvin(80.33)
		self.assertEqual(300.00, result)

	def testFahrenheitToKelvin_zeroKelvin(self):
		result = conversion.convertFahrenheitToKelvin(-459.67)
		self.assertEqual(0.00, result)

	def testFahrenheitToKelvin_decimalValues(self):
		result = conversion.convertFahrenheitToKelvin(89.96)
		self.assertEqual(305.35, result)

	def testFahrenheitToKelvin_negativeValues(self):
		result = conversion.convertFahrenheitToKelvin(-514.3)
		self.assertEqual(-30.35, result)

	def testFahrenheitToKelvin_largeNumber(self):
		result = conversion.convertFahrenheitToKelvin(7599568.73)
		self.assertEqual(4222238.00, result)


if __name__ == "__main__":
    unittest.main()