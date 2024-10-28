import time 
  
def convert(seconds): 
    return time.strftime("%H:%M:%S", time.gmtime(n)) 
      
n = 45625
print(convert(n))