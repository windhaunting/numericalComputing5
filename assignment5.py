import numpy as np
from scipy.special import erfinv
import unittest
import matplotlib.pyplot as plt
import math
###########################################
# Problem 1
###########################################

def inverse_normal_cdf(u,mu,sigma2):
    ## Add code here ##
    
    inverseError= erfinv(2*u-1)               #inverse erf function
    res = mu + math.sqrt(2*sigma2)*inverseError
    return res
    
###########################################
# Problem 2
###########################################

def normal_sampler(n_samples,mu,sigma2):
    ## Add code here ##
    
    u = np.random.uniform(0, 1, n_samples)             #sample from uniform first
    #print ("u: ",u)
    
    normalX= inverse_normal_cdf(u, mu, sigma2)
    plt.hist(normalX, normed=True, bins=30)
    plt.xlabel('x');
    plt.ylabel('Probability of normal distribution');
    plt.show() 
###########################################
# Problem 3
###########################################

def mcev(fun,n_samples,mu,sigma2):
    ## Add code here ##
    return -1



##########test############
    
normal_sampler(1000,0, 2)