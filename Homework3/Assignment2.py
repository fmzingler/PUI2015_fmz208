# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 20:18:26 2015

@author: Fernando
"""
from __future__ import print_function
__author__= 'fmz'

import numpy as np

alpha=0.05
#we like fractions better then percentages. as a rule of thumb, either use fractions or counts
var0=27.2
var1=28.2
P_0=var0*0.01 
P_1=var1*0.01

n_0=409
n_1=564

#lets get the counts by multiplying by the sample size
Nt_0=P_0*n_0
Nt_1=P_1*n_1

#define the sample proportion first
sp=(P_0*n_0+P_1*n_1)/(n_1+n_0)
print (sp)


# i am goonna create a little one line function to calculate the standard dev, it is not really needed, but just to show you how you do such a thing
sp_stdev= lambda p, n: np.sqrt( p * ( 1 - p ) /n[0] +  p * ( 1 - p )/n[1]  )


sp_stdev_2y=sp_stdev((P_0+P_1),[n_0,n_1])

print (P_0, n_0, n_1, sp_stdev_2y)


zscore = lambda p0, p1, s : (p0-p1)/s
z_2y = zscore(P_1, P_0, sp_stdev_2y)
print (z_2y)


##p-value for employment after 2 years
p_2y=1-0.6217

print (p_2y)

def report_result(p,a):
    print ('is the p value {0:.2f} smaller than the critical value {1:.2f}? '.format(p,a))
    if p<a:
        print ("YES!")
    else: print ("NO!")
    
    print ('the Null hypothesis is {}'.format( 'rejected' if p<a  else 'not rejected') )

    
report_result(p_2y,alpha)


Ntot = 973
expected = 564*409*270.296*702.704
sample_values = [[var0*5.64,(1-var0)*5.64],[var1*4.09,(1-var1)*4.09]]
 
chisqstat= lambda N, values, expect : N*((values[0][0]*values[1][1]-values[0][1]*values[1][0])**2)/(expect)

print (chisqstat(Ntot,  sample_values, expected))