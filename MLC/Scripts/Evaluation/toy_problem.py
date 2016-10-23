import numpy as np
import MLC.Log.log as lg
import matplotlib.pyplot as plt
import sys

from MLC.matlab_engine import MatlabEngine
from MLC.mlc_parameters.mlc_parameters import Config


def individual_data(indiv):
    x = np.arange(-10, 10 + 0.1, 0.1)
    # FIXME: Numpy precision it's driving me up the wall. It doesn't put a zero
    # in the middle element of the array (put a extremely small number instead).
    # That generates problems with the division operation
    x[len(x) / 2] = 0
    y = np.tanh(x**3 - x**2 - 1)

    eng = MatlabEngine.engine()
    config = Config.get_instance()
    # artificial_noise = self._config.getint('EVALUATOR', 'artificialnoise')

    # In this test we have no noise by config file. But, if this were the
    # case, we would a have problem because the random of MATLAB is not
    # the random of Python :(
    # WORKAROUND: Generate the noise in matlab and process it in python

    # MAKE SOME NOISE!!!
    # noise = eng.eval('rand(length(zeros(1, ' + str(len(x)) + ')))-0.5')
    # np_noise = np.array([s for s in noise[0]])
    # y2 = y + np_noise * 500 * artificial_noise

    y2 = y

    if isinstance(indiv.get_formal(), str):
        formal = indiv.get_formal().replace('S0', 'x')
    else:
        # toy problem support for multiple controls
        formal = indiv.get_formal()[0].replace('S0', 'x')

    eng.workspace['x'] = eng.eval('-10:0.1:10')
    eng.workspace['formal'] = formal

    # Calculate J like the sum of the square difference of the
    # functions in every point

    lg.logger_.debug('[POP][TOY_PROBLEM] Individual Formal: ' + formal)
    eng.workspace['y3'] = eng.eval('zeros(1, ' + str(len(x)) + ')')
    eng.eval('eval([formal])')
    y3 = eng.eval('eval([formal])')

    try:
        np_y3 = np.array([s for s in y3[0]])
    except TypeError:
        np_y3 = np.repeat(y3, len(x))

    return x, y, y2, np_y3


def cost(indiv):
    x, y, y2, np_y3 = individual_data(indiv)
    cost_np_y3 = float(np.sum((np_y3 - y2)**2))
    return cost_np_y3


def show_best(index, indiv, block=True):
    x, y, y2, np_y3 = individual_data(indiv)
    # FIXME: Absolute only makes sense if we're working with complex numbers. It's not the case...
    y4 = np.sqrt((y - np_y3)**2 / (1 + np.absolute(x**2)))

    plt.clf()
    plt.suptitle("Individual N#{0} - Cost: {1}".format(index, indiv.get_cost()))
    plt.subplot(2, 1, 1)
    plt.plot(x, y, x, y2, '*', x, np_y3)

    plt.subplot(2, 1, 2)
    plt.plot(x, y4, '*r')
    plt.yscale('log')
    plt.show(block=block)
