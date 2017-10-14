import numpy as np
from scipy.special import erfinv
import unittest
import matplotlib.pyplot as plt
import math
###########################################
# Problem 1
###########################################

def inverse_normal_cdf(u,mu,sigma2):
    #get X from inverse normal CDF 
    inverseError= erfinv(2*u-1)               #inverse erf function
    res = mu + math.sqrt(2*sigma2)*inverseError
    return res
    
###########################################
# Problem 2
###########################################

def normal_sampler(n_samples,mu,sigma2):
    #normal distribution use inverse CDF
    u = np.random.uniform(0, 1, n_samples)             #sample from uniform first
    
    normalX= inverse_normal_cdf(u, mu, sigma2)
    plt.hist(normalX, normed=True, bins=30)
    plt.xlabel('x');
    plt.ylabel('Count');
    plt.title('Histogram of samples for normal distribution')
    plt.show(block = False) 
    
    return normalX

###########################################
# Problem 3
###########################################

def mcev(fun,n_samples,mu,sigma2):
    ## estimated function fun's expected value by monte carlo simulation
    sampleX =  normal_sampler(n_samples, mu, sigma2)

    fx = fun(sampleX)    
    print ("fx: ", type(fx))     #get CDF
    return np.ndarray.mean(fx)


##########test############
    
#normal_sampler(1000,0, 2)

def fun(x):
    return x**2      # x, x**3

print ("test mcev", mcev(fun, 1000, 0.0, 2.0))