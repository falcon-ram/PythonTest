import numpy as np
from timeit import default_timer as timer
from numba import vectorize


# Vectorize the Vector add function
# below is a python decorator which is used to compile the python code
# to Cuda code for the GPU
@vectorize(["float32(float32, float32)"], target='cuda')
def VectorAdd(a, b):
    return a + b

N = 32000000 # number of elements per Array
A = np.ones(N, dtype=np.float32)
B = np.ones(N, dtype=np.float32)
C = np.zeros(N, dtype=np.float32)

start = timer()
C = VectorAdd(A, B) # return C instead of passing as a parameter
vectoradd_timer = timer() - start

print("C[:5] = " + str(C[:5]))
print("C[-5:] = " + str(C[-5:]))

print("VectorAdd took " + str(vectoradd_timer) + " seconds")