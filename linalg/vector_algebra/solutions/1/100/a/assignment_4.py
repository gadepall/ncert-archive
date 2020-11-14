# GIVEN :: ABC is a triangle with AD as median and AM is perp to BC. 
# How to give inputs : ac can be any integer value. Make sur other inputs satisfy the triangle properties and given conditions.
import math
def calculate_LHS(ac):
    return ac**2

def calculate_RHS(adsq,bc,dm):
    return adsq +bc*dm + (bc/2)**2

ac = float((input("Enter LHS : ")))
ad, bc, dm = input("Enter RHS values (ad,bc,dm) respectively : ").split()

lhs = calculate_LHS(ac)
rhs = calculate_RHS(float(ad),float(bc),float(dm))

if lhs == rhs:
    print("LHS = RHS. Hence proved.")
else:
    print("Incorrect input. Please re-check!")
