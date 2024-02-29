from matplotlib.pylab import f
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

def p_value(x0, x1):
    _, p = ttest_ind(x0, x1, equal_var=False)

    return p

x0 = [ 0.37573001,  0.21247917, -0.67124648,  0.2374745,  -1.45603413, -0.25755043,  -0.11001962,  0.37688537, -1.1212683,   1.01799572]

x1 = [-0.2426411,-1.77085777,-2.89941971,-2.11527647,-1.36233166,-1.55094782,1.37423683,-1.13154447,-0.02978513,-2.0079708 ]

p = p_value(x0, x1)
print(f"Question 1: {p}")

x0 = [ 2.94014422,  3.04439738, -0.94101418, -0.92752818, -0.46969084,  3.05078551, 1.75493175,  2.31201154, 6.19113954, -0.64650055]

x1 = [ 3.01754857,  4.68259652,  5.462443,    1.28730691,  0.77273338, -1.67701899, -0.8889576,  -0.63605098, -4.4283456,   0.26754374]

p = p_value(x0, x1)
print(f"Question 2: {p}")

x0=[ 1.61440259,1.67138762,-0.01637776, 0.83468138, 1.10434472,1.51214375,1.81918826, 0.64452334,2.21594525, 1.6284409 ]
x1=[2.05921024, 1.19243816, 2.98865825, 1.78041892, 0.65840815, 2.39363351, 2.34263727, 1.89973928, 2.90954834, 2.8325926 ]
p = p_value(x0, x1)
print(f"Question 3: {p}")

from scipy.special import erf

def event_probability(x, mu, s):
    # x is the value of the event
    # mu is the gaussian mean (default 0.0)
    # s is the gaussian std dev (default 1.0)
    # z is how many sigma away x is from mean
    z = np.fabs((x-mu)/s)
    return 1.0 - erf(z/np.sqrt(2))

x = [ 1.40796533, 0.29104673, 1.74539197, -0.17648601, 0.60321751, 2.90038798, 2.06495026, 1.37243758, 0.93980907, -0.04161072]
x = np.random.normal(0.0,1.0,1000)
mean = np.mean(x)
std = np.std(x)
print(std)
print(f"{event_probability(9, mean, std)}")