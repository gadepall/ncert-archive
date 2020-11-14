#Given total principal amount Prin,Interest rate Ir1 of 1st bond and Ir2 of 2nd bond,makeInvestment calculates how much to invest in first bond and how much to invest in 2nd bond to get total interest of Interest in a year. 
def makeInvestment(Prin,Ir1,Ir2,Interest):
    maxInt1 = (Prin*Ir1)/100;#Interest recieved if all of prin is invested in first bond
    maxInt2 = (Prin*Ir2)/100;#Interest recieved if all of prin is invested in second bond
    if Interest < maxInt1 and Interest < maxInt2: #case (30000,5,7,1000).trust will get minimum interest of 1500
        return "This principle "+str(Prin)+" cannot get so low Interest="+str(Interest)
    elif Interest > maxInt1 and Interest > maxInt2: # case (30000,5,7,3000).trust can get maximum interest of 2100.3000 is not possible
        return "This principle "+str(Prin)+" cannot get so high Interest="+str(Interest)
    elif Interest == maxInt1:
        return "Invest "+str(Prin)+" in first fund having interest rate "+str(Ir1)+"% and 0 in second fund having interest rate "+str(Ir2)+"% to get total interest of "+str(Interest)
    else:
        #prin1 is amount invested in 1st bond,prin2 = (prin-prin1) in 2nd.then total interest revieved would be Interest = prin1*Ir1+prin2*Ir2.calculating we get prin1 and prin2
        prin1 = (100*(Interest-maxInt2))/(Ir1-Ir2)
        prin2 = Prin-prin1
        return "Invest "+str(prin1)+" in first fund having interest rate "+str(Ir1)+"% and "+str(prin2)+" in second fund having interest rate "+str(Ir2)+"% to get total interest of "+str(Interest)

print(makeInvestment(30000,5,7,1800))
print(makeInvestment(30000,5,7,2000))
