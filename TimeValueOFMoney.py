PV = 1000
r = 0.05
n = 1

FV = PV * ((1+r) ** n) # Formula for calculating Future Value

print (FV)


FV = 1050
r = 0.05
n = 1

PV = FV / ((1 + r) ** n) # Formula for calculating Present Value

print (PV)


#compounding
PV = 1000
r = 0.05
n = 2 # number of periods = 2 since bond makes semiannual payments
t = 1 # number of years

FV = PV * ((1+(r/n)) ** (n*t)) # Formula for compounding

print (FV)

r = 0.1
n = 3
PV = 0
FV = 9476.96

AP = (FV * r) / (((1 + r) ** n - 1)*(1+r)) # Formula for Annuity payments, given Future Value

print (AP)


r = 0.1
n = 5
AP = 2500

PV = (AP * (1 - ((1 + r) ** -n))) / r # Formula for PV, given Annuity payments

print (PV)

r = 0.08
n = 45
AP1 = 30000

PV = (AP1 * (1 - ((1 + r) ** -n))) / r # Formula for PV, given Annuity payments

print (PV)

r = 0.15
n = 25
PV = 0
FV = 363252.045095

AP = (FV * r) / (((1 + r) ** n - 1)*(1+r)) # Formula to calculate Annuity Payments, given FV

#AP = (r * PV) / (1 - ((1 + r) ** -n)) # Formula to calculate Annuity Payments, given PV

print (AP)
