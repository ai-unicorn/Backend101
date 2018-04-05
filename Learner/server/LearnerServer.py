import sys
import os
sys.path.append(os.path.abspath('../gen-py'))

# Thrift related functionality
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

from argparse import ArgumentParser

from learner import LearnerService
from learner.ttypes import *

from sklearn.linear_model import LogisticRegression

import numpy as np


class LearnerHandler(LearnerService.Iface):

    def __init__(self):
        pass


    def hello(self, identity):
        print(identity)
        return identity

    def logisticRegression(
        self, xTrain, yTrain, penalty, dual, tol, C, fitIntercept,
        interceptScaling, classWeight, randomState, solver, maxIter,
        multiClass, verbose, warmStart, nJobs,
    ):
        if len(classWeight) == 0:
            classWeight = 'balanced'

        if randomState is not None:
          if len(randomState) == 0:
              randomState = None
          elif len(randomState) == 1:
             randomState = randomState[0]
          elif len(randomState) > 1:
             # https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.RandomState.html
             randomeState = np.random.RandomState(randomState)

        if not solver in ["newton-cg", "lbfgs", "liblinear", "sag", "saga"]:
            ex = LearnerException()
            ex.errorCode = LearnErrorCode.RUNTIME_ERROR
            ex.message = "wrong solver!"
            raise ex
        if not multiClass in ["ovr", "multinomial"]:
            ex = LearnerException()
            ex.errorCode = LearnErrorCode.RUNTIME_ERROR
            ex.message = "wrong multi_class!"
            raise ex
        logistic = LogisticRegression(penalty, dual, tol, C, fitIntercept,
                                      interceptScaling, classWeight,
                                      randomState, solver, maxIter, multiClass,
                                      verbose, warmStart, nJobs)
        logistic.fit(xTrain, yTrain)
        attributes = LogisticRegressionAttributes(
            logistic.coef_, logistic.intercept_, logistic.n_iter_)
        return attributes



def parse_args():
    parser = ArgumentParser()
    parser.add_argument('-p', '--port', type=int, dest='port', default=30303,
                        required=False, help='The server port')
    return parser.parse_args()


def main():
    sys.stdout.write('Learner server is starting...')
    options = parse_args()
    sys.stdout.write('port: ' + str(options.port) + '\n')

    handler = LearnerHandler()
    processor = LearnerService.Processor(handler)
    transport = TSocket.TServerSocket('localhost', options.port)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
    server.serve()


if __name__ == '__main__':
    rc = main()
    sys.exit(rc)
