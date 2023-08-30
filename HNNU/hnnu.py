import numpy as np
from sklearn.neighbors import DistanceMetric
from sklearn.neural_network import MLPRegressor

# Function to train autoencoder
def train_autoencoder(samples):
    # Define autoencoder architecture and train on samples
    model = MLPRegressor(hidden_layer_sizes=(100,50,100), activation='relu', solver='adam', max_iter=500)
    model.fit(samples, samples)
    return model

# Function to train simple ANN
def train_simpleANN(samples):
    # Define simple ANN architecture and train on samples
    model = MLPRegressor(hidden_layer_sizes=(100,50), activation='relu', solver='adam', max_iter=500)
    model.fit(samples, samples)
    return model

# Main code
n1 = 100 # number of minority class samples
n2 = 1000 # number of majority class samples
m = 10 # number of attributes
threshold = 100 # threshold for deciding whether to use autoencoder or simple ANN

majSamples = np.random.rand(n2, m) # example majority class samples
minSamples = np.random.rand(n1, m) # example minority class samples

if m > threshold:
    model = train_autoencoder(minSamples)
else:
    model = train_simpleANN(minSamples)

dist = DistanceMetric.get_metric('euclidean')
distArray = {}
for i in range(n2):
    x = majSamples[i]
    x0 = model.predict(x.reshape(1,-1))[0]
    d = dist.pairwise(x.reshape(1,-1), x0.reshape(1,-1))[0][0]
    index = i
    distArray[index] = d

sortedList = sorted(distArray.items(), key=lambda x: x[1], reverse=True)
selectedIndices = [x[0] for x in sortedList[:n1]]
X1 = majSamples[selectedIndices]

finalData = np.vstack((X1, minSamples))

