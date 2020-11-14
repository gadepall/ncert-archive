import random

#Question:
#A die is thrown. If E is the event ”the number appearing is a multiple of 3” and F be the event ”the number appearing is even” then find whether E and F are independent ?
print("E: The number appearing is a multiple of 3")
print("F: The number appearing is even","\n")

#Simulation
N = 7000
count_number_of_even = 0
count_number_of_mul_of_3 = 0
count_number_of_even_and_mul_of_3 = 0
for i in range(0,N):
    x = random.randint(1,6)
    if(x%2 == 0 and x%3 == 0):
        count_number_of_even_and_mul_of_3=count_number_of_even_and_mul_of_3+1;
    if(x%2 == 0):
        count_number_of_even=count_number_of_even+1;
    if(x%3 == 0):
        count_number_of_mul_of_3=count_number_of_mul_of_3+1;

print("Pr(E) using simulation = ",count_number_of_mul_of_3/N)    
print("Pr(F) using simulation = ",count_number_of_even/N)
print("Pr(E intersection F) using simulation = ",count_number_of_even_and_mul_of_3/N)
print("Pr(E)*Pr(F) using simulation = ",(count_number_of_mul_of_3/N)*(count_number_of_even/N))
