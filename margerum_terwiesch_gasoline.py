Python 2.7.9 (default, Dec 10 2014, 12:24:55) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> gas gallons = (raw_input('Please enter the number of gallons of gasoline:  '))
SyntaxError: invalid syntax
>>> gas_gallons = (raw_input('Please enter the number of gallons of gasoline:  '))
Please enter the number of gallons of gasoline:  26
>>> carbon_dioxide_pounds = gas_gallons*19.64

Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    carbon_dioxide_pounds = gas_gallons*19.64
TypeError: can't multiply sequence by non-int of type 'float'
>>> gas_gallons = float(raw_input('Please enter the number of gallons of gasoline:  '))
Please enter the number of gallons of gasoline:  26.5
>>> carbon_dioxide_pounds = gas_gallons*19.64
>>> print gas_gallons, 'gallons of gasoline produces approximately', carbon_dioxide_pounds, 'pounds of carbon dioxide'
26.5 gallons of gasoline produces approximately 520.46 pounds of carbon dioxide
>>> ================================ RESTART ================================
>>> 
Please enter the number of gallons of gasoline:  26
26.0 gallons of gasoline produces approximately 510.64 pounds of carbon dioxide
>>> 
>>> barrels_of_crude = float(raw_input('Please enter the number of barrels of crude:  '))
gas_gallons = barrels_of_crude*19
Please enter the number of barrels of crude:  5
>>> print barrels_of_crude, 'barrels of crude produce approximately', gas_gallons, 'gas gallons'
5.0 barrels of crude produce approximately 26.0 gas gallons
>>> ================================ RESTART ================================
>>> 
Please enter the number of gallons of gasoline:  
>>> ================================ RESTART ================================
>>> 
Please enter the number of gallons of gasoline:  26
26.0 gallons of gasoline produces approximately 510.64 pounds of carbon dioxide
1.36842105263 barrels of crude produce approximately 26.0 gas gallons
>>> ================================ RESTART ================================
>>> 
Please enter the number of gallons of gasoline:  26
26.0 gallons of gasoline produces approximately 510.64 pounds of carbon dioxide and
1.36842105263 barrels of crude produce approximately 26.0 gas gallons
>>> ================================ RESTART ================================
>>> 
Please enter the number of gallons of gasoline:  26
26.0 gallons of gasoline produces approximately 510.64 pounds of carbon dioxide and
1.36842105263 barrels of crude are required to produce approximately 26.0 gas gallons
>>> ================================ RESTART ================================
>>> 
Please enter the number of gallons of gasoline:  26
26.0 gallons of gasoline produces approximately 510.64 pounds of carbon dioxide and
1.36842105263 barrels of crude are required to produce approximately 26.0 gas gallons
and the average cost of 26.0 is 67.08 dollars
>>> ================================ RESTART ================================
>>> 
Please enter the number of gallons of gasoline:  26
26.0\ gallons of gasoline produces approximately 510.64 pounds of carbon dioxide and
1.36842105263 barrels of crude are required to produce approximately 26.0 gas gallons
and the average cost of 26.0 gas gallons is 67.08 dollars
>>> ================================ RESTART ================================
>>> 
Please enter the number of gallons of gasoline:  30
30.0 gallons of gasoline produces approximately 589.2 pounds of carbon dioxide and
1.57894736842 barrels of crude are required to produce approximately 30.0 gas gallons
and the average cost of 30.0 gas gallons is 77.4 dollars
>>> ================================ RESTART ================================
>>> 
Please enter the number of gallons of gasoline:  30
30.0 gallons of gasoline produce approximately 589.2 pounds of carbon dioxide, and
1.57894736842 barrels of crude are required to produce approximately 30.0 gas gallons, 
and the average cost of 30.0 gas gallons is 77.4 dollars
>>> 
