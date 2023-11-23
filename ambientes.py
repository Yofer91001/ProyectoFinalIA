import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.offsetbox import AnnotationBbox, OffsetImage

class ABC():
    
    def __init__(self):
        self.nA = 2
        self.action_space = [0,1]
        self.nS = 3
        self.A = 0
        self.B = 1
        self.C = 2
        self.LEFT = 0
        self.RIGHT = 1
        self.P = self.set_P()
        self.dict_acciones = {self.LEFT:'LEFT', self.RIGHT:'RIGHT'}
        self.dict_states = {self.A:'A', self.B:'B', self.C:'C'}
        self.p_right = 0.9
        self.state = self.A

    def set_P(self):
        P = {}
        P[self.A] = {a:[] for a in range(self.nA)}
        P[self.B] = {a:[] for a in range(self.nA)}
        P[self.C] = {a:[] for a in range(self.nA)}
        # AQUÍ SU CÓDIGO
        P[self.A][self.LEFT] = [(1,0,-1,False)]
        P[self.A][self.RIGHT] = [(0.1,0,-1,False), (0.9,1,-1,False)]
        P[self.B][self.LEFT] = [(1,0,-1,False)]
        P[self.B][self.RIGHT] = [(0.1,1,-1,False), (0.9,2,10,True)]
        # HASTA AQUÍ SU CÓDIGO
        return P

    def reset(self):
        self.state = self.A
        return self.state
    
    def step(self, action):
        state = self.state
        next_state_probabilities = self.P[state][action]
        n = len(next_state_probabilities)
        indice = np.random.choice(range(n), p=[x[0] for x in next_state_probabilities])
        next_state = next_state_probabilities[indice][1]
        self.state = next_state
        reward = next_state_probabilities[indice][2]
        done = next_state_probabilities[indice][3]
        return next_state, reward, done    

    def render(self):
        str(f'Estado: {self.state}')

    def __str__(self):
        string = ''
        for s in range(self.nS):
            string += '\n'+'-'*20
            string += f'\nState: {self.dict_states[s]}'
            for a in range(self.nA):
                string += f'\nAction:{self.dict_acciones[a]}'
                for x in self.P[s][a]:
                    string += f'\n| probability:{x[0]}, '
                    string += f'new_state:{self.dict_states[x[1]]}, '
                    string += f'reward:{x[2]}, '
                    string += f'done?:{x[3]} |'
        return string

