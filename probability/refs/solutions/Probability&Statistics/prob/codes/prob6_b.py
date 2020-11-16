import random 
  
  
x = "y"
throws=1
event_sim=0
   
while x == "y": 
      
    # Gnenerates a random number 
    # between 1 and 6 (including 
    # both 1 and 6) 
    no = random.randint(1,6) 
      
    if no == 1: 
        print("[-----]") 
        print("[     ]") 
        print("[  0  ]") 
        print("[     ]") 
        print("[-----]") 
    if no == 2: 
        print("[-----]") 
        print("[ 0   ]") 
        print("[     ]") 
        print("[   0 ]") 
        print("[-----]") 
    if no == 3: 
        print("[-----]") 
        print("[     ]") 
        print("[0 0 0]") 
        print("[     ]") 
        print("[-----]") 
    if no == 4: 
        print("[-----]") 
        print("[0   0]") 
        print("[     ]") 
        print("[0   0]") 
        print("[-----]") 
    if no == 5: 
        print("[-----]") 
        print("[0   0]") 
        print("[  0  ]") 
        print("[0   0]") 
        print("[-----]") 
    if no == 6: 
        print("[-----]") 
        print("[0 0 0]") 
        print("[     ]") 
        print("[0 0 0]") 
        print("[-----]") 
          
    sample=6
    event_size=3
    prob=event_size/sample
    if(no%2==1):
    	event_sim=event_sim+1
    	sim=event_sim/throws
    else:
    	sim=event_sim/throws
    throws=throws+1
    print(sim,prob)
    x=input("press y to roll again and n to exit:") 
    print("\n") 
