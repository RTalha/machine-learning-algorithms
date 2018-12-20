#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 21:38:11 2018

@author: rana
"""


import matplotlib.pyplot as plt
import sklearn as skt
import numpy as np
import pandas as pd

def calculate_theta(theta_1,m,data_set):
    #derivative of slop also
    theta_1_new = 0
    for i in range(m):
        theta_1_new +=((theta_1*data_set[i][0]-data_set[i][1])*data_set[i][0])/m
        
    return (theta_1_new)
def gradient_descent():
    
    theta1 = 0
    alpha = 0.08
    m=0
    counter = 0
    list_1_gradient = []
    theta_1_values = []
    #loaddata set
    housing = pd.read_csv('/home/rana/Documents/housing.csv')
    data_set = pd.iloc[:,:]
    X = pd.iloc[:,-1]
    Y = pd.iloc[:,1]
    m = len(X)
    housing.head()
    
    while True:
        theta_values = calculate_theta(theta1,m,data_set)
        print(theta_values)
        theta1-= alpha*theta_values
        counter+=1
        theta_1_values.append(theta1)
        list_1_gradient.append(abs(theta1))
        
        if theta_values < 0.01:
            print ("Goal achieved")
            print ("values of theta_1 are",theta1)
            b = np.asarray(list_1_gradient)
            theta_1_values = np.asarray(theta_1_values)
            
            c = np.arange(counter)
            plt.plot(c, theta_1_values,'x',label = "theta_1")
            plt.legend(loc = "best")
            plt.title("visualization of Theta_0 and Theta_1 values")
            plt.xlabel("Iteration")
            plt.ylabel("thetas values")
            plt.show()

            break
gradient_descent()