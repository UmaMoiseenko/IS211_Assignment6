from decimal import Decimal


def convert(fromUnit, toUnit, value):
    """
        m = yd/1.0936 - yard  to meter
        m = mi/0.00062137 - mile to meter

        mi = yd * 0.00056818 - yard to mile
        mi = m * 0.00062137 - meter to mile

        yd =m * 1.0936 - meter to Yard
        yd = mi * 1760  - mile to Yard

     =>   result = val/from * to 
    """
    dist_convert_values = {
        'Mile': (0.00062137),
        'Yard': (1.0936),
        'Meter': (1)
    }

    temp_convert_values = {
        'Celsius': (1, 0),
        'Fahrenheit': ( 1.8, 32),
        'Kelvin': (1, 273.15)
    }

    if ( temp_convert_values.viewkeys() >= {fromUnit} and dist_convert_values.viewkeys() >= { toUnit}) \
        or ( temp_convert_values.viewkeys() >= {toUnit} and dist_convert_values.viewkeys() >= { fromUnit}):
        raise ConversionNotPossible("Conversion is not possible")

    elif dist_convert_values.viewkeys() >= {fromUnit, toUnit}:
        devisor = dist_convert_values[fromUnit]
        multiplier = dist_convert_values[toUnit]

        result =  Decimal( float(value)/devisor * multiplier )
        return round(result,7)

    elif temp_convert_values.viewkeys() >= {fromUnit, toUnit}:
        fromUnit = temp_convert_values[fromUnit]
        toUnit = temp_convert_values[toUnit]

        devisor = fromUnit[0]
        substract = fromUnit[1]
        divident = toUnit[0]
        addent = toUnit[1]

        result =  Decimal( (float(value) - substract) * divident / devisor  + addent)
        return round(result,7)


class ConversionNotPossible(Exception):
    """ Exception """
    pass

    