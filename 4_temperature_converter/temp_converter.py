def convert_temp(value, unit):
    unit = unit.upper()
    if unit == "F":
        result = (value-32)*5/9
    elif unit == "C":
        result = (value*9/5)+32
    else:
        return "Error: Unit must be 'C' or 'F'."
    return round(result, 2)


print(convert_temp(125, 'c'))
"""
Converts temperatures between Celsius and Fahrenheit.
    
 Args:
     value (float): The temperature value to convert
    unit (str): The unit of the input value ('C' for Celsius, 'F' for Fahrenheit)
    
Returns:
    float: The converted temperature value, rounded to 2 decimal places
    str: Error message if unit is invalid
    
Example:
     >>> convert_temp(32, 'F')
     0.0
    >>> convert_temp(100, 'C') 
    212.0
    >>> convert_temp(25, 'X')
    'Error: Unit must be 'C' or 'F'.'
"""

