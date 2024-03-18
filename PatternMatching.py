import random
import math



# return appropriate N that satisfies the error bounds
def findN(eps,m):
	return ((2*m/eps * math.log(26,2))*math.log( (2*m/eps * math.log(26,2)),2))//1 + 1
''' proof - let p be the value of pattern and x be the value of text string which matches
so q gives same mod value with p and x and thus q divides |p-x|
for a  false positive  probability is :p() =  no of such prime qs such that it divides |p-x|/no of primes less than N
we need p()<=eps
max value of |p-x| = (26^m -1)*25/(26-1) obtained by putting one string as zzzz... and other as aaaa...
and no of primes less than N >= N/(2* log2 N)
using this we obtain 
N/log2 N >= 2*m* (log2 26)/eps
and on further solving and approximations 
we get the above expression
'''



# Now we assign values as instructed to the alphabets
A=0
B=1
C=2
D=3
E=4
F=5
G=6
H=7
I=8
J=9
K=10
L=11
M=12
N=13
O=14
P=15
Q=16
R=17
S=18
T=19
U=20
V=21
W=22
X=23
Y=24
Z=25

# Return sorted list of starting indices where p matches x
def modPatternMatch(q,p,x):
    report_indices = [] #contains the indices where the pattern matches with the text
    value_of_p_string = 0 #will store the value of pattern
    for i in range (0,len(p)):
        value_of_p_string = (26* value_of_p_string + eval(p[i]))%q #writing the polynomial using horner's rule 
        #time complexity - O(log(q))
        #since the loop is executed m times, where m is len(p) , TC =O(m*log(q))
        #space complexity  = O(log(q)) to store the value of p_string
    check_string_x = 0
    for i in  range (0,len(p)):
        check_string_x = (26 * check_string_x + eval(x[i]))%q  # O(log(q))
        #since the loop is executed m times, where m is len(p) , TC =O(m*log(q))
        #space complexity  = O(log(q)) to store the value of check_string whiich is not more than q bits + O(m) max space to store  i  = O(m+logq)

    j=0 
    t=len(p) 
    while j+len(p) <=len(x): # condition to check untill the last possible string
        if value_of_p_string == check_string_x : #O(1)
            #if match found append  the index
            report_indices.append(j) #O(1)
            #if no of indices= k then SC =O(k)
            j+=1
            
        else: 
            j+=1
        if t<len(x):
            add_value = (eval(x[t])) %q #O(logq) time and space
            subtract_value = (26**(len(p)-1) * eval(x[t- len(p)]))%q  #O(logq) time and space
            
            check_string_x=( 26*(check_string_x -subtract_value) + add_value)%q #O(logq) time and space
            
            
            t+=1
        # since the wile loop is executed (n-m+1) times , time complexity  = O((n-m)logq)
        # log(n-m) max space is required to store j and log(n) max space is reuired to store t 
        # SC =O(logq + logn) + O(k)
        
    return(report_indices)
    # TC = O((n-m)logq) + O(mlogq) = O((n+m)logq)
    # SC = O(logq + logn) + O(logq + logm) + O(k) = O(logq + logm + logn + k) = O(logq+logn+ k)

# Return sorted list of starting indices where p matches x    
def modPatternMatchWildcard(q,p,x):

    report_indices_wildcard = []

    value_of_p_string_wild = 0 #will store the value of pattern
    i=0 
    while i< len(p):
        if p[i]== '?':
            ind = i 
            value_of_p_string_wild =(26*value_of_p_string_wild)%q #O(logq)time and space
            i+=1
        else:
            value_of_p_string_wild = (26* value_of_p_string_wild + eval(p[i])) % q  #O(logq)time and space
            i+=1
        #since the loop is executed m times, where m is len(p) , TC =O(m*log(q))
        #space complexity  = O(log(q)) to store the value of value of p string whiich is not more than q bits + O(m) max space to store  i  = O(m+logq)


    j=0
    check_string_x_wild = 0
    while j < len(p):
        if j == ind :
            check_string_x_wild = (26*check_string_x_wild)%q #O(logq)time and space
            j+=1
        else: 
            check_string_x_wild = (26* check_string_x_wild + eval(x[j])) % q  #O(logq)time and space
            j+=1
        #since the loop is executed m times, where m is len(p) , TC =O(m*log(q))
        #space complexity  = O(log(q)) to store the value of check_string whiich is not more than q bits + O(m) max space to store  j  = O(m+logq)

    j_wild =0

    t_wild = len(p)

    while j_wild+len(p) <= len(x):
        if value_of_p_string_wild == check_string_x_wild : # O(1) time
            report_indices_wildcard.append(j_wild) #O(1) time
            #if no of indices= k then SC =O(k)
            j_wild+=1

        else:
            j_wild+=1

        if t_wild < len(x) :
            add_value = (eval(x[t_wild]))%q #O(logq)time and space

            subtract_value = (26**(len(p)-1) * eval(x[t_wild - len(p)]))%q  #O(logq)time and space

            add_wild  = (26**(len(p)-(ind))* eval(x[j_wild-1+ind]))%q  #O(logq)time and space

            subtract_wild  = (26**(len(p)-1-(ind)-1) * eval(x[j_wild+ind]))%q  #O(logq)time and space
Instructor
| 11/12 at 2:28 pm
Grading comment:
Here every time you are computing 26** some constant can be stored outside the loop. it takes O(m) times as multiple of O(len(x)-len(p)-j_wild) in over all T.C of this while loop, which could be optimized.


            if ind== 0:
                check_string_x_wild = (26*(check_string_x_wild - subtract_wild ) + add_value)%q  #O(logq)time and space

            elif ind==len(p)-1 :
                check_string_x_wild = (26*(check_string_x_wild + - subtract_value)+add_wild)%q #O(logq)time and space

            else:
                check_string_x_wild = (26*(check_string_x_wild +  - subtract_value - subtract_wild) +add_wild+ add_value)%q #O(logq)time and space
            t_wild+=1

        # since the wile loop is executed (n-m+1) times , time complexity  = O((n-m)logq)
        # log(n-m) max space is required to store j_wild and log(n) max space is reuired to store t_wild
        # SC =O(logq + logn) + O(k)


    return report_indices_wildcard  
    # TC = O((n-m)logq) + O(mlogq) = O((n+m)logq)
    # SC = O(logq + logn) + O(logq + logm) + O(k) = O(logq + logm + logn + k) = O(logq+logn+ k)     
                        
            
#To generate random prime less than N
def randPrime(N):
	primes = []
	for q in range(2,N+1):
		if(isPrime(q)):
			primes.append(q)
	return primes[random.randint(0,len(primes)-1)]

# To check if a number is prime
def isPrime(q):
	if(q > 1):
		for i in range(2, int(math.sqrt(q)) + 1):
			if (q % i == 0):
				return False
		return True
	else:
		return False

#pattern matching
def randPatternMatch(eps,p,x):
	N = findN(eps,len(p))
	q = randPrime(N)
	return modPatternMatch(q,p,x)

#pattern matching with wildcard
def randPatternMatchWildcard(eps,p,x):
	N = findN(eps,len(p))
	q = randPrime(N)
	return modPatternMatchWildcard(q,p,x)        