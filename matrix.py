from numpy import *

m1 = matrix ('1 2 3; 4 5 6')      

m2 = matrix ('7 8 ; 9 10 ; 11 12')      


m3 = (m1*m2)

print (m3.reshape(2,2))
