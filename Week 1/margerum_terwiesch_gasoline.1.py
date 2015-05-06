
while True:
    gas_gallons = raw_input('Please enter the number of gallons of gasoline:  ')
    try:
        gas_gallons = float(gas_gallons)
        break
    except ValueError:
        print gas_gallons, 'is not a valid entry'

carbon_dioxide_pounds = gas_gallons*19.64
print gas_gallons,'gallons of gasoline produce approximately',
carbon_dioxide_pounds, 'pounds of carbon dioxide, and'

barrels_of_crude_oil = gas_gallons/19
print barrels_of_crude_oil, 'barrels of crude are required to produce approximately'\
        , gas_gallons, 'gas gallons,'

average_cost = gas_gallons*2.580
print 'and the average cost of', gas_gallons, 'gas gallons is', average_cost, 'dollars'

