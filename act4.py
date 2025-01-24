#math module with conditional
import math  

x = float('nan') #not a number
if math.isnan(x): 
    print('Not a number')


x = float('inf')

if math.isinf(x): #infinite
    print('Infinity')


xy=10
print(math.isfinite(xy)) 
print(math.isnan(xy))
