import pandas as pd 
import numpy as np 
from scipy.optimize import minimize 
import warnings 

### we want to minimize the |log(a/b)| which will be the absolute value of the fold change 

'''
def function (x):
	f(x) = |log(a/b)|
obviously a and b is not as simple as that.... 

CL * P
______  

  C

=> a == CL * P
and b == C


CL is what we are guessing. C we know (is data) and P we know some of (is markers info). 
so we need to be able to do matrix multiplication

To actually do the optimization....

#nelder_meld is the simplex method 
x0 = np.array(guess)
res = minimize(function, x0, method = 'nelder_meld', constraints = {constraints: blahblah, constraints: blahblah})

the output of res will be the same shape as x0. X0 for us will be our concentrations data. Then it will return the concentrations 
data to get as close as possible to our actual copy numbers osv



Update 14 March:
def minimize_function (x):
	return abs(np.log10(x))

this is how the example at minimize explains it. So X would be Cguess/ C. Maybe we can figure out CL and P from this?  
Or maybe could have in Cguess and C 


practice code:
CL * P = np.dot. Numpy dot formula = matrix multiplication of these two values, like khan acacemy video
np.dot(a, b)

TCL = np.array([[5,5], [2,8],[1,9]])
TCL_for_c1 = TCL[:,0][np.newaxis] #(will make it so that its (0,4) instead of just a list of 4 int)
TCL_for_c2 = TCL[:,1][np.newaxis]

TP = np.array([[100,0], [50,50], [0,10], [40,80]])
TP_for_c1 = TP[:,0][np.newaxis].transpose()
TP_for_c2 = TP[:,1][np.newaxis].transpose()


TC = (TCL_for_c1 * TP_for_c1) + (TCL_for_c2 * TP_for_c2)
'''










#actual start of script



C = pd.read_csv('~/Desktop/Masters_Thesis/data/liver_data/optimizer_small_data_liver.csv', index_col = 0)
CL = np.random.rand(2, np.shape(C)[1])  #make the CL guess array, it's as wide as as many samples as we have, and 2 tall, one for each cell type (pretending we have two for now)
P = np.random.rand(np.shape(C)[0], 2)   #make the P guess array, it's 2 wide, one for each cell type and it's as long as we have proteins

#add more here if you use more cell lines
CL1 = CL[0][np.newaxis] #same shape as TCL_for_c1 (just more samples). Is wider than is tall which is what we want
CL2 = CL[1][np.newaxis]

P1 = P[:,0][np.newaxis].transpose()
P2 = P[:,1][np.newaxis].transpose()

warnings.filterwarnings('ignore')  #this can be dangerous so it might not be good to have here but res likes to get mad when the array is variable values
def min_func(x):
	return np.mean(abs(np.log10(x)))   #we have the mean in here because res does not like to have an array as the output

C = np.asarray(C)
Cguess= (CL1 * P1) + (CL2 * P2)   # I have checked to see that the matrix multiplication is done correctly and it is!! 
x = Cguess/ C    #what we actually want
x = x.flatten()   # has to be flat shape or res yells
x = np.nan_to_num(x) # right now this replaces the inf, but SHOULD FIX TO REFLECT SOMETHING DIV BY 0, RIGHT NOW IT IS A HUGE NUMBER ( X * 10 **308)

res = minimize(min_func, x, method = 'nelder-mead')
print res.x        #right now there is no change between x and res x 










