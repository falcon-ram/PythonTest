# pure python code
import numpy as np
from timeit import default_timer as timer

def VectorAdd(a, b, c):
    for i in range(a.size):
        c[i] = a[i] + b[i]

N = 32000000 # number of elements per Array
A = np.ones(N, dtype=np.float32)
B = np.ones(N, dtype=np.float32)
C = np.zeros(N, dtype=np.float32)

start = timer()
VectorAdd(A, B, C)
vectoradd_timer = timer() - start

print("C[:5] = " + str(C[:5]))
print("C[-5:] = " + str(C[-5:]))

print("VectorAdd took " + str(vectoradd_timer) + " seconds")
