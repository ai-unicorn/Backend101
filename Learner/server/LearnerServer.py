import sys
import os
sys.path.append(os.path.abspath('../gen-py'))

# Thrift related functionality
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

from learner import LearnerService

from argparse import ArgumentParser


class LearnerHandler(LearnerService.Iface):

    def __init__(self):
        pass


    def hello(self, identity):
        print(identity)
        return identity


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
