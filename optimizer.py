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



Update 15 March: from scipy beginners guide to optimization
You can set your constraints as a function. ex: if you know that x[1] should == 4:
def constraint1(x):
	return 4-x (or x-4) so that it is 0

then when you add to the optimizer:
cons1 = {'type': 'ineq', 'fun':constraint1}
and then make it into a list
cons = [cons1,cons2,cons3,cons_n]


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
C = np.asarray(C)
C[C == 0] = 0.00000000000001
np.random.seed(1)
CL = np.random.rand(2, np.shape(C)[1])  #make the CL guess array, it's as wide as as many samples as we have, and 2 tall, one for each cell type (pretending we have two for now)
P = np.random.rand(np.shape(C)[0], 2)   #make the P guess array, it's 2 wide, one for each cell type and it's as long as we have proteins

#get shapes to make variable change easier
CL_shape = np.shape(CL)
P_shape = np.shape(P)

##########################
##optimizer part
#######################

warnings.filterwarnings('ignore')  #this can be dangerous so it might not be good to have here but res likes to get mad when the array is variable values

def objective(tot):
	#get back original arrays, res only works off one guess
	CL_reshaped, P_reshaped = np.split(tot, [len(CL)])

	#first reshape CL and P. I know it's a lot of variables but lenCL makes it that way
	CL_reshaped = np.reshape(CL_reshaped, CL_shape)
	P_reshaped = np.reshape(P_reshaped, P_shape)

	#get an array for each cell line so we can make Cguess
	CL1 = CL_reshaped[0][np.newaxis] #same shape as TCL_for_c1 (just more samples). Is wider than is tall which is what we want
	CL2 = CL_reshaped[1][np.newaxis]
	P1 = P_reshaped[:,0][np.newaxis].transpose()
	P2 = P_reshaped[:,1][np.newaxis].transpose()

	Cguess = (CL1 * P1) + (CL2 * P2)
	return np.mean(abs(np.log10(Cguess/C)))   #we have the mean in here because res does not like to have an array as the output
	#return Cguess


#this is for the minimizer input 
CL = CL.flatten()
P = P.flatten()   
tot = np.concatenate([CL, P])

res = minimize(objective, tot, method = 'nelder-mead')
print res        #right now there is no change between x and res x 









