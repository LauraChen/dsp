# Hint:  use Google to find python function

from datetime import datetime

def days_between(d1, d2):
    return abs((d2 - d1).days)

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   
d1 = datetime.strptime(date_start, "%m-%d-%Y")
d2 = datetime.strptime(date_stop, "%m-%d-%Y")
print("The answer to part A is: "+ str(days_between(d1,d2)))
      
####b)  
date_start = '12312013'  
date_stop = '05282015'
d1 = datetime.strptime(date_start, "%m%d%Y")
d2 = datetime.strptime(date_stop, "%m%d%Y")
print("The answer to part B is: "+ str(days_between(d1,d2)))

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  
d1 = datetime.strptime(date_start, "%d-%b-%Y")
d2 = datetime.strptime(date_stop, "%d-%b-%Y")
print("The answer to part B is: "+ str(days_between(d1,d2)))
