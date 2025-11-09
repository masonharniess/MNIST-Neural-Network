import numpy as np

class Network(object):
  def __init__(self, sizes):
    # The number of layers in the network.
    self.num_layers = len(sizes)
    # The number of neurons in the respective layers.
    self.sizes = sizes 
    # Initialise the bias vectors for each layer.
    self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
    # Initialise the weight matricies for each layer-to-layer connection.
    self.weights = [np.random.randn(y, x) for x, y in zip(sizes[:-1], sizes[1:])]


