import numpy as np
from timeit import default_timer as timer
from matplotlib import pyplot
import math
from numba import vectorize
from numba.cuda import random
from numba import cuda

@vectorize(['float64(float64, float64, float64, float64, float64)'], target='cuda')
def step(price, dt, c0, c1, noise):
    return price * math.exp(c0 * dt + c1 * noise)

def montecarlo(rng_states, paths, dt, interest, volatility):
    c0 = interest - 0.5 * volatility ** 2
    c1 = volatility * np.sqrt(dt)

    threadId = cuda.grid(1) # this does not work needs the @cuda_jit decorator
                            # but the cuda compiler does not seem to work well
                            # with numpy arrays
    prng = random.xoroshiro128p_uniform_float32(rng_states, threadId)

    noises = np.zeros(paths.shape[0])

    for j in range(1, paths.shape[1]): # for each time step
        prices = paths[:, j - 1]       # last prices
        # gaussian noises for simulation
        #noises = np.random.normal(0., 1., prices.size)
        prng.normal(noises, 0., 1.)
        # simulate
        paths[:, j] = step(prices, dt, c0, c1, noises)

# Stock information parameters
StockPrice = 20.83
StrikePrice = 21.50
Volatility = 0.021
InterestRate = 0.20
Maturity = 5. / 12.

# monte carlo simulation parameters
numPath = 3000000
NumStep = 100

# plotting
MAX_PATH_IN_PLOT = 50

def driver(pricer, do_plot=False):
    paths = np.zeros((numPath, NumStep + 1), order='F')
    paths[:, 0] = StockPrice
    DT = Maturity / NumStep

    ts = timer()
    threads_per_block = 64
    blocks = 24
    rng_states = random.create_xoroshiro128p_states(threads_per_block * blocks, seed=1)
    pricer(rng_states,paths, DT, InterestRate, Volatility)
    te = timer()
    elapsed = te - ts

    ST = paths[:, -1]
    PaidOff = np.maximum(paths[:,-1] - StrikePrice, 0)
    print("Result")
    print(f"Stock price: {np.mean(ST)}")
    print(f"Standard error: {np.std(ST)/np.sqrt(numPath)}")
    print(f"Paid off: {np.mean(PaidOff)}")
    optionPrice = np.mean(PaidOff) * np.exp(-InterestRate * Maturity)
    print(f"Option price: {optionPrice}")

    print("Performance")
    NumCompute = numPath * NumStep
    print(f"Mstep/second = {NumCompute/elapsed/1e6:.2f}")
    print(f"Time elapsed = {elapsed:.3f}")

    if do_plot:
        pathct = min(numPath, MAX_PATH_IN_PLOT)
        for i in range(pathct):
            pyplot.plot(paths[i])
        print(f"Plotting {pathct}/{numPath} paths")
        pyplot.show()


import cProfile as profile
profile.run("driver(montecarlo, do_plot=True)", sort="time")
