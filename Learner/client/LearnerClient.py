import sys
import os
sys.path.append(os.path.abspath('../gen-py'))

# Thrift related functionality
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

from learner import LearnerService
from learner.ttypes import *

from sklearn import datasets, neighbors, linear_model

try:
    transport = TSocket.TSocket('localhost', 30303)
    transport = TTransport.TBufferedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)

    client = LearnerService.Client(protocol)
    transport.open()

    res = client.hello('lingguang')
    print(res)

    digits = datasets.load_digits()
    X_digits = digits.data
    y_digits = digits.target
    n_samples = len(X_digits)
    X_train = X_digits[:int(.9 * n_samples)]
    y_train = y_digits[:int(.9 * n_samples)]

    res = client.logisticRegression(
        xTrain=X_train, yTrain=y_train, penalty='l2', dual=False, tol=0.0001,
        C=1.0, fitIntercept=1, interceptScaling=1, classWeight=None,
        randomState=None, solver='liblinear', maxIter=100, multiClass='ovr',
        verbose=0, warmStart=False, nJobs=1,
    )
    print(res.coef)
    print(res.intercept)
    print(res.n_iter)

    transport.close()
except LearnerException, ex:
    print ex.message
