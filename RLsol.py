#Grupo 2: André Fonseca (84698), Leonor Loureiro (84736)
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 20:31:54 2017

@author: mlopes
"""
import numpy as np

def Q2pol(Q, eta=1):
    ''' simplification of epsilon greedy algorithm
        eta = epsilon; the chance of selecting the max value
        should be a value between 0 and 1
    '''
    pol = np.zeros((Q.shape[0], Q.shape[1]))

    for line in range(Q.shape[0]):
        temp_chance = np.random.random()
        if temp_chance >= eta:
            index = np.random.randint(0, Q.shape[1]) #random column
        else:
            index = np.argmax(Q[line])

        pol[line, index] = 1
    return pol

class myRL:

    def __init__(self, nS, nA, gamma):
        self.nS = nS
        self.nA = nA
        self.gamma = gamma
        self.Q = np.zeros((nS, nA))
        
    def traces2Q(self, trace):
        self.Q = np.zeros((self.nS, self.nA))
        tempQ = np.zeros((self.nS, self.nA))
        diff = True
        alpha = 0.2  # learning rate

        while diff:
            for line in trace:
                ini_state = int(line[0])
                action = int(line[1])
                next_sate = int(line[2])
                reward = int(line[3])

                old_value = self.Q[ini_state, action] # calculate old value of Q
                estimated_future_value = max(self.Q[next_sate, :]) # max(next states) --> selects 'optimal'
                learned_value = reward + self.gamma * estimated_future_value

                self.Q[ini_state, action] = (1 - alpha) * old_value + alpha * learned_value

            # np.allclose -> Returns True if two arrays are element - wise equal within a tolerance.
            diff = not np.allclose(tempQ, self.Q)
            tempQ = np.copy(self.Q)

        return self.Q



