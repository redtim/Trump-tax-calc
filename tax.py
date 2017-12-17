#A simple tax calculator to compare the 2017 tax rates to the proposed trump tax plan for 2018
# I don't have kids, soooooo if you do, please add in the child credit stuff and make a PR
# also any other complicated tax situations are appreciated


#### 2018 proposed tax brackets

#10 percent: $0 to $9,525
#12 percent: $9,525 to $38,700
#22 percent: $38,700 to $82,500
#24 percent: $82,500 to $157,500
#32 percent: $157,500 to $200,000
#35 percent: $200,000 to $500,000
#37 percent: $500,000 and above

from var import *

def calculateTax(income, brackets):
    tax = 0.0         
    lastLev=0.0
    for rate, level  in iter(sorted(brackets.iteritems())):
        if income > level:
            tax = tax + (level-lastLev)*rate/100
            ##uncomment to see the "tax brackets"
            #print "tax {:f} rate {:f} level {:f}".format(tax,rate,level)
            lastLev=level
        else:
            tax = tax + (income - lastLev)*rate/100
            ##uncomment to see the "excess above last tax bracker"
            #print "excess tax {:f}".format((TaxableIncome - lastLev)*rate/100)
            break
    return tax


newLevs = {10:9525.0, 12:38700.0, 22:82500.0, 24:157500.0, 32:200000.0, 35:500000.0, 37:9999999999999999999999999999.0}
oldLevs ={10:9325.0, 15:37950.0, 25:91900.0, 28:191650.0, 33:416700.0,35:418400.0,39:999999999999999999999999.0}

######################## Input Your Info in vars.py ########################

######################### OLD TAX PLAN ###################################
TaxableIncome= salary - PropertyTax - StateIncomeTax - MortgageInterest - Retirement - OtherDeductions
tax = calculateTax(TaxableIncome,oldLevs)
print "2017 what you should pay"
print "old tax is {:f}\n\n".format(tax)



######################### NEW TAX PLAN ###################################
tax = 0.0         
lastLev=0.0
if PropertyTax + StateIncomeTax > 10000:
    StateTax=10000
else:
    StateTax = PropertyTax + StateIncomeTax
if MortgageInterest > 10000:
    MortgageInterest=10000

TaxableIncome = salary - StateTax - MortgageInterest - Retirement - OtherDeductions
tax = calculateTax(TaxableIncome,newLevs)

print "2018 what you would pay under new tax plan"
print "new tax is {:f}\n\n".format(tax)

