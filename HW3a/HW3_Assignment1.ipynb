#LIbraries

from __future__ import print_function
__author__= 'fmz'

import numpy as np
import matplotlib.pyplot as pl
import json
from scipy.stats import norm
import matplotlib.mlab as mlab

#Definition

s = json.load(open('fmz_matplotlibr.json'))
pl.rcParams.update(s)

distributions = ['chisq','normal', 'binomial', 'poisson', 'lognormal', 'pareto']

mymean=500 #population mean
samples=100 #number of samples to be generated

df = 100 #degrees of freedon for the CHI-SQUARE DISTRIBUITION

sig=1 #Standard deviation for the NORMAL DISTRIBUITION

myp=0.95 # p from the BINORMAL DISTRIBUITION
myn=mymean/myp # n from the BINORMAL DISTRIBUITION
#n*p=mean

#n trials and p probability of success where n an integer >= 0 and p is in the interval [0,1]




mysizeN=2000/(np.array(range(1,100)+[10]))

# CHI-SQ 
#numpy.random.chisquare(df, size=None)

chsq={}
df = mymean

chsq['chisq'] = np.random.chisquare(df, samples)

chsq['chisq']={} 

for n in mysizeN:
    chsq['chisq'][n] = np.random.chisquare(df, size=n)
    
CHISQmeans={}
CHISQmeans['chisq'] = {}
fig_mu_N = pl.figure(figsize=(10,10))
axchisq_mu_n = fig_mu_N.add_subplot(111)
for nn in chsq['chisq'].iterkeys():
    CHISQmeans['chisq'][nn] = chsq['chisq'][nn].mean()
    #and plot it
    axchisq_mu_n.plot(nn, CHISQmeans['chisq'][nn], 'o')
    axchisq_mu_n.set_xlabel('sample size')
    axchisq_mu_n.set_ylabel('sample mean')
    axchisq_mu_n.set_title('CHI SQUARE DISTRIBUTION')
    axchisq_mu_n.plot([min(mysizeN), max(mysizeN)],[df,df], 'k')

allmeans=[]
for n in CHISQmeans['chisq']:
    allmeans.append(CHISQmeans['chisq'][n])
    
  #  print (CHISQmeans)
    
    # NORMAL DISTRIBUITION
#numpy.random.normal(loc=0.0, scale=1.0, size=None)
nrml={}

nrml['normal']={}

for n in mysizeN:
    nrml['normal'][n] = np.random.normal(mymean,sig,n)
    
NRMLmeans = {}
NRMLmeans['normal'] = {}
fig_mu_N = pl.figure(figsize=(10,10))
axnormal_mu_n = fig_mu_N.add_subplot(111)
for nn in nrml['normal'].iterkeys():
    NRMLmeans['normal'][nn] = nrml['normal'][nn].mean()
    #and plot it
    axnormal_mu_n.plot(nn, NRMLmeans['normal'][nn], 'o')
    axnormal_mu_n.set_xlabel('sample size')
    axnormal_mu_n.set_ylabel('sample mean')
    axnormal_mu_n.set_title('NORMAL DISTRIBUTION')
    axnormal_mu_n.plot([min(mysizeN), max(mysizeN)],[mymean,mymean], 'k')

for n in NRMLmeans['normal']:
    allmeans.append(NRMLmeans['normal'][n])
    
 #   print (NRMLmeans)
    
    #BINOMIAL
#numpy.random.binomial(n, p, size=None)where n trials and p probability of success where n an integer >= 0 and p is in the interval [0,1]
bnml={}

bnml['binomial']={}

for n in mysizeN:
    bnml['binomial'][n] = np.random.binomial(myn,myp,n)

BNMLmeans = {}
BNMLmeans['binomial'] = {}
BNMLmeans['binomial'] = {}
fig_mu_N = pl.figure(figsize=(10,10))
axbinomial_mu_n = fig_mu_N.add_subplot(111)
for nn in bnml['binomial'].iterkeys():
    BNMLmeans['binomial'][nn] = bnml['binomial'][nn].mean()
    #and plot it
    axbinomial_mu_n.plot(nn, BNMLmeans['binomial'][nn], 'o')
    axbinomial_mu_n.set_xlabel('sample size')
    axbinomial_mu_n.set_ylabel('sample mean')
    axbinomial_mu_n.set_title('BINOMIAL DISTRIBUTION')
    axbinomial_mu_n.plot([min(mysizeN), max(mysizeN)],[mymean,mymean], 'k') 

for n in BNMLmeans['binomial']:
    allmeans.append(BNMLmeans['binomial'][n])

#print (BNMLmeans)


#POISSON
#numpy.random.poisson(lam=1.0, size=None)
pssn={}

pssn['poisson']={}
ld=mymean
for n in mysizeN:
    pssn['poisson'][n] = np.random.poisson(mymean,n)
    
PSSNmeans = {}
PSSNmeans['poisson'] = {}
    
PSSNmeans['poisson'] = {}
fig_mu_N = pl.figure(figsize=(10,10))
axpoisson_mu_n = fig_mu_N.add_subplot(111)
for nn in pssn['poisson'].iterkeys():
    PSSNmeans['poisson'][nn] = pssn['poisson'][nn].mean()
    #and plot it
    axpoisson_mu_n.plot(nn, PSSNmeans['poisson'][nn], 'o')
    axpoisson_mu_n.set_xlabel('sample size')
    axpoisson_mu_n.set_ylabel('sample mean')
    axpoisson_mu_n.set_title('POISSON DISTRIBUTION')
    axpoisson_mu_n.plot([min(mysizeN), max(mysizeN)],[mymean,mymean], 'k')

for n in PSSNmeans['poisson']:
    allmeans.append(PSSNmeans['poisson'][n])

#print (PSSNmeans)
   
    
    ##EXPONENTIAL
#np.random.exponential(bt,size)
expo={}

expo['exponential']={}
for n in mysizeN:
    expo['exponential'][n] = np.random.exponential(mymean,n)
    #np.exp(-(np.log(n)-mymean)**2/(2*LGsig**2))/(n*LGsig*np.sqrt(2*np.pi))
   # pdf = (np.exp(-(np.log(x) - mu)**2 / (2 * sigma**2))
#...        / (x * sigma * np.sqrt(2 * np.pi)))
    #

EXPOmeans = {}
EXPOmeans['exponential'] = {}
fig_mu_N = pl.figure(figsize=(10,10))
axlognormal_mu_n = fig_mu_N.add_subplot(111)
for nn in expo['exponential'].iterkeys():
    EXPOmeans['exponential'][nn] = expo['exponential'][nn].mean()
    #and plot it
    axlognormal_mu_n.plot(nn, EXPOmeans['exponential'][nn], 'o')
    axlognormal_mu_n.set_xlabel('sample size')
    axlognormal_mu_n.set_ylabel('sample mean')
    axlognormal_mu_n.set_title('EXPONENTIAL DISTRIBUTION')
    axlognormal_mu_n.plot([min(mysizeN), max(mysizeN)],[mymean,mymean], 'k')

for n in EXPOmeans['exponential']:
    allmeans.append(EXPOmeans['exponential'][n])
    
#print (EXPOmeans)
   
    
    #LOGISTIC
#numpy.random.logistic(loc=0.0, scale=1.0, size=None)¶

logs={}

logs['logistic']={}

m=mymean

for n in mysizeN:
    logs['logistic'][n] = np.random.logistic(mymean, sig, n)
    
LOGSmeans = {}
LOGSmeans['logistic'] = {}
fig_mu_N = pl.figure(figsize=(10,10))
axpareto_mu_n = fig_mu_N.add_subplot(111)
for nn in logs['logistic'].iterkeys():
    LOGSmeans['logistic'][nn] = logs['logistic'][nn].mean()
    #and plot it
    axpareto_mu_n.plot(nn, LOGSmeans['logistic'][nn], 'o')
    axpareto_mu_n.set_xlabel('sample size')
    axpareto_mu_n.set_ylabel('sample mean')
    axpareto_mu_n.set_title('LOGISTIC DISTRIBUTION')
    axpareto_mu_n.plot([min(mysizeN), max(mysizeN)],[mymean,mymean], 'k')

for n in LOGSmeans['logistic']:
    allmeans.append(LOGSmeans['logistic'][n])
#print (PRTOmeans)
    
#PLOT ALL SAMPLE MEANS

pl.figure(figsize=(10,10))
pl.hist(allmeans, normed=1,alpha=0.5, bins=30)
pl.xlabel('sample mean')
pl.ylabel('N')
pl.title('ALL SAMPLE MEANS')


#FIT A GAUSSIAN

(mu, sigma) = norm.fit(allmeans)
pl.figure(figsize=(10,10))
pl.xlabel('sample mean')
pl.ylabel('N')
pl.title('ALL SAMPLE MEANS WITH GAUSSIAN')
n, bins, patches=pl.hist(allmeans,normed=1,bins=50, alpha=0.3)
y = mlab.normpdf( bins, mu, sigma)
l = pl.plot(bins, y, 'r', linewidth=2)
