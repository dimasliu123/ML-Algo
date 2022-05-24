import numpy as np

class Activation:
    def __init__(self, inputs):
        self.inputs = inputs

class ReLU:
    def __init__(self, inputs):
        super().__init__(inputs)
        self.inputs = inputs

	def forward(self): # f(x) = {inputs <= 0, z > 0 = z}
		self.out = np.maximum(0, self.inputs)

	def backward(self): # f'(x) = = {inputs <= 0 = 0, z > 0 = 1}
        inputs = self.inputs
		inputs[inputs<=0] = 0
		inputs[inputs>0] = 1
		return inputs

class Sigmoid:
    def __init__(self, inputs):
        super().__init__(inputs)
        self.inputs = inputs
	def forward(self): # f(x)  = 1 / ( 1 + e^-x)
		self.out = 1 / (1 + np.exp(-self.inputs))

	def backward(self): # f'(x) = f(x) - (1 - f(x))
		return self.forward() - ( 1 - self.forward())

class Tanh:
    def __init__(self, inputs):
        super().__init__(inputs)
        self.inputs = inputs

	def forward(self): # f(x) = (e^x - e^-x) / (e^x + e^-x)
		self.out = (np.exp(inputs) - np.exp(-inputs)) / (np.exp(inputs) + np.exp(-inputs)) 

	def backward(self): # f'(x) = 1 - f(x)^2
		self.out = 1. - self.forward(inputs) ** 2

class Softmax:
    def __init__(self, inputs):
        super().__init__(inputs)
        self.inputs = inputs

    def forward(self): # f(x) = e(x) / ∑e(x)
        exp_inputs = np.exp(self.inputs)
        self.out = exp_inputs / np.sum(exp_z)
    
    def backward(self):
        inputs_flat = self.out.reshape(-1, 1)
        inputs_diag = np.diagflat(self.out)
        return inputs_diag - np.dot(inputs_flat, inputs_flat.T)
