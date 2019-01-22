##############################################################################
## Code to anaylyze information gain from a a small dataset:

import pandas as pd
import numpy as np

## Just checking what every line is about:
## with open('bugs_data.txt', 'r') as data_txt:
##    print(data_txt.readlines())

data_bugs= pd.read_csv('bugs_data.csv', delimiter=',',header=0)

### Split by color:
data_bugs_brown= data_bugs[data_bugs['Color'] == 'Brown']
data_bugs_blue= data_bugs[data_bugs['Color'] == 'Blue']
data_bugs_green= data_bugs[data_bugs['Color'] == 'Green']

# Compute entropy:
# Write a function to compute entropy:
def entropy(y):
    '''
    Calculates probabilities and log-base2 to compute Entropy by group
    '''
    n_obs= len(y)
    n_Mobug= len(y[y == 'Mobug'])
    n_Lobug= len(y[y == 'Lobug'])
    
    p_Mobug= n_Mobug/n_obs
    p_Lobug= n_Lobug/n_obs
    
    log_Mobug= np.log2(p_Mobug)
    log_Lobug= np.log2(p_Lobug)
    
    # Formula:
    #return [n_Mobug, n_Lobug, n_obs]
    E= round(np.sum(np.array([-p_Mobug*log_Mobug, -p_Lobug*log_Lobug])), 3)
    return E

print(entropy(data_bugs_brown.Species))

## Prepare new dataset:
def length_group_17(x):
     return 1 if x < 17.0 else 0

def length_group_20(x):
     return 1 if x < 20.0 else 0

data_bugs['less_20'] = data_bugs['Length (mm)'].apply(length_group_20)
data_bugs['less_17'] = data_bugs['Length (mm)'].apply(length_group_17)

###### 

data_bugs_17= data_bugs[data_bugs['less_17'] == 1]
data_bugs_no17= data_bugs[data_bugs['less_17'] == 0]

#data_bugs_20= data_bugs[data_bugs['less_20'] == 1]




