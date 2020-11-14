def median(n_num): 
	n = len(n_num) 
	n_num.sort() 
  
	if n % 2 == 0: 
    		median1 = n_num[n/2] 
   		#median2 = n_num[n/2 - 1] 
    		median = (median1 )/2
	else: 
    		median = n_num[n//2] 
	print("Median is: " median) 
	
def mean(n_num):
	n= len(n_num)
	get_sum = sum(n_num) 
	mean = get_sum / n 
  
	print("Mean / Average is: " + str(mean)) 
	
def mode(n_num):
	n = len(n_num) 
  
	data = Counter(n_num) 
	get_mode = dict(data) 
	mode = [k for k, v in get_mode.items() if v == max(list(data.values()))] 
  
	if len(mode) == n: 
    		get_mode = "No mode found"
	else: 
    		get_mode = "Mode is / are: " + ', '.join(map(str, mode)) 
      		print("Mode is: " get_mode) 
