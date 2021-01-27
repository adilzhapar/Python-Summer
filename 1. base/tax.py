def electr(x, y, debt):
    elec = (x - y) * 17.79 + debt
    elec = float("{:.2f}".format(elec))
    return elec


def fungas(x, y, debt):
    gas = (x - y) * 29.44 + debt
    gas = float("{:.2f}".format(gas))
    return gas


last = float(input("Last for electricity: "))
pre = float(input("Previous for electricity: "))
print("Difference in electricity: {:.2f}".format(last - pre))
debt = float(input("Debt for electricity: "))
over = float(input("Overpay for electricity: "))

elec = electr(last, pre, debt)
s = input("Include overpay?(Yes or No) ")
if s == "Yes":
    elec -= over
    elec = float("{:.2f}".format(elec))

glast = float(input("Last for gas: "))
gpre = float(input("Previous for gas: "))
print("Difference in gas: {:.2f}".format(glast - gpre))
gdebt = float(input("Debt for gas: "))
gover = float(input("Overpay for gas: "))

gas = fungas(glast, gpre, gdebt)
s = input("Include overpay?(Yes or No) ")
if s == "Yes":
    gas -= gover
    gas = float("{:.2f}".format(gas))

water = float(input("Water: "))
dwater = float(input("Debt for water: "))

trash = 3318.24
vdgo = 225
phone = 5899
cost = elec + gas + water + dwater + trash + vdgo + phone
cost = float("{:.2f}".format(cost))
print("The electricity costs: ", elec)
print("The gas costs: ", gas)
print("The cost is: ", cost)



