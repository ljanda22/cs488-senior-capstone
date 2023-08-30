import random
import numpy as np

# Function to generate the synthetic samples
def populate(N, i, nnarray, Sample, Synthetic):
    numattrs = Sample.shape[1]
    newindex = 0
    while N != 0:
        nn = random.randint(1, k)
        for attr in range(numattrs):
            dif = Sample[nnarray[i][nn], attr] - Sample[i, attr]
            gap = random.uniform(0, 1)
            Synthetic[newindex, attr] = Sample[i, attr] + gap * dif
        newindex += 1
        N -= 1

# Main code
N = 100
if N < 100:
    T = 100
    Randomize_T = random.sample(range(T), int(N/100*T))
    Sample = Sample[Randomize_T]
    T = len(Randomize_T)
else:
    T = Sample.shape[0]
T = int(N/100 * T)
N = int(N/100)

k = 5
Sample = np.array([[1,2,3],[4,5,6],[7,8,9]]) # example data
nnarray = np.array([[1,2,0,1,2],[2,0,1,2,0],[1,2,0,1,2]]) # example nearest neighbors
Synthetic = np.zeros((N*T, Sample.shape[1]))

for i in range(T):
    populate(N, i, nnarray, Sample, Synthetic)

