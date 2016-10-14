#!/usr/bin/env python2

import sys
import numpy as np
import pickle
from loadTestCases import *

from A3Part1 import minimizeEnergySpreadDFT
from A3Part2 import optimalZeropad
from A3Part3 import testRealEven
from A3Part4 import suppressFreqDFTmodel
from A3Part5 import zpFFTsizeExpt

functions = {
    "A3-part-1" : minimizeEnergySpreadDFT,
    "A3-part-2" : optimalZeropad,
    "A3-part-3" : testRealEven,
    "A3-part-4" : suppressFreqDFTmodel,
    "A3-part-5" : zpFFTsizeExpt
}

if __name__ == "__main__":
    data = pickle.load(open('testInput%s.pkl'%PA,'r'))

    partIds = data["exampleInputs"].keys()
    for partId in partIds:
        inputs = data["exampleInputs"][partId]
        outputs = data["exampleOutputs"][partId]
        fun = functions[partId]
        print "Running test for %s" % partId
        for _input, _output in zip(inputs, outputs):
            results = fun(**_input)
            for expected, actual in zip(_output, results):
                if isinstance(expected, (np.ndarray, np.generic)):
                    if not np.all(np.isclose(expected, actual)):
                        print "Failed running test for %s (comparing numpy arrays)" % partId
                        print "expected:", expected
                        print "actual:", actual
                else:
                    if expected != actual:
                        print "Failed running test for %s" % partId
                        print "expected:", expected
                        print "actual:", actual
