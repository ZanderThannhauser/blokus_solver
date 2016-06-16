import numpy as np
file = open("layers_1/hidden_layers", "w");
x = 50;
y = 50;
z = 5;
a1 = np.random.rand(x, y * z) - 0.5;
for i in range(0, y * z):
	for j in range(0, x):
		file.write(str(a1[j][i]));
		file.write(" ")
	file.write("\n")
file.close();
