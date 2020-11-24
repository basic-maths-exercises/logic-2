import numpy as np

def numberLessThan( data, n ) : 
  # You need to write code here
  
def numberMoreThan( data, n ) : 
  # You need to write code here
  
def numberLessThanOrEqualTo( data, n ) :
  # You need to write code here
  
def numberGreaterThanOrEqualTo( data, n ) :
  # You need to write code here


# This code allows you to see if your functions are working correctly
data = np.loadtxt("mydata.dat")
print( numberLessThan(data,5), "of the integers in mydata.dat are less than 5" )
print( numberMoreThan(data,5), "of the integers in mydata.dat are more than 5" )
print( numberLessThanOrEqualTo(data,5), "of the integers in mydata.dat are less than or equal to 5" )
print( numberGreaterThanOrEqualTo(data,5), "of the integers in mydata.dat are greater than or equal to 5" )
