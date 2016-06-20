import numpy as np;
import math





def sigmoid(x):
    return 1 / (1 + math.exp(-x));
def sigmoid_pri(x):
    return sigmoid(x)*(1-sigmoid(x));

def activation(input, first_layer, hidden_layers, final_layer):
    layers = np.zeros((6, 50))
    layers[0] = np.dot(input, first_layer);
    for j in range(0, 50):
        layers[0][j] = sigmoid(layers[0][j]);
    for i in range(0, 5):
        hidden_layer = hidden_layers[(i*50) : ( (i+1) * 50 ) ];
        layers[i+1] = np.dot(layers[i].T, hidden_layer);
        for j in range(0, 50):
            layers[i+1][j] = sigmoid(layers[i+1][j]);
    output = np.dot(layers[5], final_layer);
    output = sigmoid(output);
    return output;











if(False):
	if(False):
		first_layer = np.ones((400, 50));
		hidden_layers =  np.ones((250, 50));
		final_layer =  np.ones((50));
	else:
		first_layer = np.genfromtxt("layers_1/first_layer", delimiter=" ")
		hidden_layers =  np.genfromtxt("layers_1/hidden_layers", delimiter=" ");
		final_layer =  np.genfromtxt("layers_1/final_layer", delimiter=" ")

	input = np.ones((400));
	print activation(input, first_layer, hidden_layers, final_layer);
