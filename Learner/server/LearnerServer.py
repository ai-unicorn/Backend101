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
from sklearn.tree import DecisionTreeClassifier

import numpy as np

import ast


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


    def decisionTreeClassifier(
        self, xTrain, yTrain, sample_weight=None, check_input=True,
        x_idx_sorted=None, criterion="gini", splitter="best", max_depth=None,
        min_samples_split="2", min_samples_leaf="1", min_weight_fraction_leaf=0,
        max_features=None, randomState=None,
        max_leaf_nodes=None, min_impurity_decrease=0, min_impurity_split=1,
        class_weight=None, presort=False,
    ):
        min_samples_split = ast.literal_eval(min_samples_split)
        min_samples_leaf = ast.literal_eval(min_samples_leaf)
        try:
            if max_features is not None:
                max_features = ast.literal_eval(max_features)
        except:
            pass

        if randomState is not None:
          if len(randomState) == 0:
              randomState = None
          elif len(randomState) == 1:
             randomState = randomState[0]
          elif len(randomState) > 1:
             # https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.RandomState.html
             randomeState = np.random.RandomState(randomState)

        if max_leaf_nodes is not None:
            max_leaf_nodes = ast.literal_eval(max_leaf_nodes)

        if class_weight is not None:
            if len(class_weight) == 0:
                class_weight = "balanced"
            elif len(class_weight) > 0:
                typed_class_weight = {}
                for d in class_weight:
                    for k, v in d:
                        k = ast.literal_eval(k)
                        v = ast.literal_eval(v)
                        typed_class_weight[k] = v
                class_weight = typed_class_weight

        clf = DecisionTreeClassifier(
            criterion, splitter, max_depth, min_samples_split,
            min_samples_leaf, min_weight_fraction_leaf, max_features,
            randomState, max_leaf_nodes, min_impurity_decrease,
            min_impurity_split, class_weight, presort,
        )
        clf.fit(xTrain, yTrain, sample_weight, check_input, x_idx_sorted)
        return DecisionTreeAttributes(clf.classes_, clf.feature_importances_,
            clf.max_features_, cls.n_classes_, cls.n_features_,
            cls.n_outputs_)


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
