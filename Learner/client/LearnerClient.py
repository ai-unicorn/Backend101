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


try:
    transport = TSocket.TSocket('localhost', 30303)
    transport = TTransport.TBufferedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)

    client = LearnerService.Client(protocol)
    transport.open()

    res = client.hello('lingguang')
    print(res)
    transport.close()
except LearnerException, ex:
    print ex.message
