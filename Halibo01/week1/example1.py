# Example pytorch usage for python
import torch as tc

# This is a convolution 2d example for a image
kernel = [
    [-1, -2, -1],
    [0, 0, 0],
    [1, 2, 1]
        ]

kernel = tc.tensor(kernel)
kernel = kernel.squeeze()
print(kernel)
print(tc.__version__)