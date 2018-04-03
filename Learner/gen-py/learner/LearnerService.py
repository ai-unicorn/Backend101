#
# Autogenerated by Thrift Compiler (0.11.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
from thrift.TRecursive import fix_spec

import sys
import logging
from .ttypes import *
from thrift.Thrift import TProcessor
from thrift.transport import TTransport
all_structs = []


class Iface(object):
    def hello(self, identity):
        """
        Parameters:
         - identity
        """
        pass

    def logisticRegression(self, xTrain, yTrain, penalty, dual, tol, C, fitIntercept, interceptScaling, classWeight, randomState, solver, maxIter, multiClass, verbose, warmStart, nJobs):
        """
        Parameters:
         - xTrain
         - yTrain
         - penalty
         - dual
         - tol
         - C
         - fitIntercept
         - interceptScaling
         - classWeight
         - randomState
         - solver
         - maxIter
         - multiClass
         - verbose
         - warmStart
         - nJobs
        """
        pass


class Client(Iface):
    def __init__(self, iprot, oprot=None):
        self._iprot = self._oprot = iprot
        if oprot is not None:
            self._oprot = oprot
        self._seqid = 0

    def hello(self, identity):
        """
        Parameters:
         - identity
        """
        self.send_hello(identity)
        return self.recv_hello()

    def send_hello(self, identity):
        self._oprot.writeMessageBegin('hello', TMessageType.CALL, self._seqid)
        args = hello_args()
        args.identity = identity
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_hello(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = hello_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "hello failed: unknown result")

    def logisticRegression(self, xTrain, yTrain, penalty, dual, tol, C, fitIntercept, interceptScaling, classWeight, randomState, solver, maxIter, multiClass, verbose, warmStart, nJobs):
        """
        Parameters:
         - xTrain
         - yTrain
         - penalty
         - dual
         - tol
         - C
         - fitIntercept
         - interceptScaling
         - classWeight
         - randomState
         - solver
         - maxIter
         - multiClass
         - verbose
         - warmStart
         - nJobs
        """
        self.send_logisticRegression(xTrain, yTrain, penalty, dual, tol, C, fitIntercept, interceptScaling, classWeight, randomState, solver, maxIter, multiClass, verbose, warmStart, nJobs)
        return self.recv_logisticRegression()

    def send_logisticRegression(self, xTrain, yTrain, penalty, dual, tol, C, fitIntercept, interceptScaling, classWeight, randomState, solver, maxIter, multiClass, verbose, warmStart, nJobs):
        self._oprot.writeMessageBegin('logisticRegression', TMessageType.CALL, self._seqid)
        args = logisticRegression_args()
        args.xTrain = xTrain
        args.yTrain = yTrain
        args.penalty = penalty
        args.dual = dual
        args.tol = tol
        args.C = C
        args.fitIntercept = fitIntercept
        args.interceptScaling = interceptScaling
        args.classWeight = classWeight
        args.randomState = randomState
        args.solver = solver
        args.maxIter = maxIter
        args.multiClass = multiClass
        args.verbose = verbose
        args.warmStart = warmStart
        args.nJobs = nJobs
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_logisticRegression(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = logisticRegression_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "logisticRegression failed: unknown result")


class Processor(Iface, TProcessor):
    def __init__(self, handler):
        self._handler = handler
        self._processMap = {}
        self._processMap["hello"] = Processor.process_hello
        self._processMap["logisticRegression"] = Processor.process_logisticRegression

    def process(self, iprot, oprot):
        (name, type, seqid) = iprot.readMessageBegin()
        if name not in self._processMap:
            iprot.skip(TType.STRUCT)
            iprot.readMessageEnd()
            x = TApplicationException(TApplicationException.UNKNOWN_METHOD, 'Unknown function %s' % (name))
            oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
            x.write(oprot)
            oprot.writeMessageEnd()
            oprot.trans.flush()
            return
        else:
            self._processMap[name](self, seqid, iprot, oprot)
        return True

    def process_hello(self, seqid, iprot, oprot):
        args = hello_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = hello_result()
        try:
            result.success = self._handler.hello(args.identity)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except LearnerException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("hello", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_logisticRegression(self, seqid, iprot, oprot):
        args = logisticRegression_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = logisticRegression_result()
        try:
            result.success = self._handler.logisticRegression(args.xTrain, args.yTrain, args.penalty, args.dual, args.tol, args.C, args.fitIntercept, args.interceptScaling, args.classWeight, args.randomState, args.solver, args.maxIter, args.multiClass, args.verbose, args.warmStart, args.nJobs)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except LearnerException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("logisticRegression", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

# HELPER FUNCTIONS AND STRUCTURES


class hello_args(object):
    """
    Attributes:
     - identity
    """


    def __init__(self, identity=None,):
        self.identity = identity

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.identity = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('hello_args')
        if self.identity is not None:
            oprot.writeFieldBegin('identity', TType.STRING, 1)
            oprot.writeString(self.identity.encode('utf-8') if sys.version_info[0] == 2 else self.identity)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(hello_args)
hello_args.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'identity', 'UTF8', None, ),  # 1
)


class hello_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRING:
                    self.success = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = LearnerException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('hello_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRING, 0)
            oprot.writeString(self.success.encode('utf-8') if sys.version_info[0] == 2 else self.success)
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(hello_result)
hello_result.thrift_spec = (
    (0, TType.STRING, 'success', 'UTF8', None, ),  # 0
    (1, TType.STRUCT, 'e', [LearnerException, None], None, ),  # 1
)


class logisticRegression_args(object):
    """
    Attributes:
     - xTrain
     - yTrain
     - penalty
     - dual
     - tol
     - C
     - fitIntercept
     - interceptScaling
     - classWeight
     - randomState
     - solver
     - maxIter
     - multiClass
     - verbose
     - warmStart
     - nJobs
    """


    def __init__(self, xTrain=None, yTrain=None, penalty="l2", dual=False, tol=0.0001, C=1, fitIntercept=True, interceptScaling=1, classWeight={
    }, randomState=[
    ], solver="liblinear", maxIter=100, multiClass="ovr", verbose=0, warmStart=False, nJobs=1,):
        self.xTrain = xTrain
        self.yTrain = yTrain
        self.penalty = penalty
        self.dual = dual
        self.tol = tol
        self.C = C
        self.fitIntercept = fitIntercept
        self.interceptScaling = interceptScaling
        if classWeight is self.thrift_spec[9][4]:
            classWeight = {
            }
        self.classWeight = classWeight
        if randomState is self.thrift_spec[10][4]:
            randomState = [
            ]
        self.randomState = randomState
        self.solver = solver
        self.maxIter = maxIter
        self.multiClass = multiClass
        self.verbose = verbose
        self.warmStart = warmStart
        self.nJobs = nJobs

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.LIST:
                    self.xTrain = []
                    (_etype3, _size0) = iprot.readListBegin()
                    for _i4 in range(_size0):
                        _elem5 = []
                        (_etype9, _size6) = iprot.readListBegin()
                        for _i10 in range(_size6):
                            _elem11 = iprot.readDouble()
                            _elem5.append(_elem11)
                        iprot.readListEnd()
                        self.xTrain.append(_elem5)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.LIST:
                    self.yTrain = []
                    (_etype15, _size12) = iprot.readListBegin()
                    for _i16 in range(_size12):
                        _elem17 = iprot.readDouble()
                        self.yTrain.append(_elem17)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.penalty = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.BOOL:
                    self.dual = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.DOUBLE:
                    self.tol = iprot.readDouble()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.DOUBLE:
                    self.C = iprot.readDouble()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.BOOL:
                    self.fitIntercept = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.DOUBLE:
                    self.interceptScaling = iprot.readDouble()
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.MAP:
                    self.classWeight = {}
                    (_ktype19, _vtype20, _size18) = iprot.readMapBegin()
                    for _i22 in range(_size18):
                        _key23 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        _val24 = iprot.readDouble()
                        self.classWeight[_key23] = _val24
                    iprot.readMapEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.LIST:
                    self.randomState = []
                    (_etype28, _size25) = iprot.readListBegin()
                    for _i29 in range(_size25):
                        _elem30 = iprot.readI32()
                        self.randomState.append(_elem30)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 11:
                if ftype == TType.STRING:
                    self.solver = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 12:
                if ftype == TType.I32:
                    self.maxIter = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 13:
                if ftype == TType.STRING:
                    self.multiClass = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 14:
                if ftype == TType.I32:
                    self.verbose = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 15:
                if ftype == TType.BOOL:
                    self.warmStart = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 16:
                if ftype == TType.I32:
                    self.nJobs = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('logisticRegression_args')
        if self.xTrain is not None:
            oprot.writeFieldBegin('xTrain', TType.LIST, 1)
            oprot.writeListBegin(TType.LIST, len(self.xTrain))
            for iter31 in self.xTrain:
                oprot.writeListBegin(TType.DOUBLE, len(iter31))
                for iter32 in iter31:
                    oprot.writeDouble(iter32)
                oprot.writeListEnd()
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.yTrain is not None:
            oprot.writeFieldBegin('yTrain', TType.LIST, 2)
            oprot.writeListBegin(TType.DOUBLE, len(self.yTrain))
            for iter33 in self.yTrain:
                oprot.writeDouble(iter33)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.penalty is not None:
            oprot.writeFieldBegin('penalty', TType.STRING, 3)
            oprot.writeString(self.penalty.encode('utf-8') if sys.version_info[0] == 2 else self.penalty)
            oprot.writeFieldEnd()
        if self.dual is not None:
            oprot.writeFieldBegin('dual', TType.BOOL, 4)
            oprot.writeBool(self.dual)
            oprot.writeFieldEnd()
        if self.tol is not None:
            oprot.writeFieldBegin('tol', TType.DOUBLE, 5)
            oprot.writeDouble(self.tol)
            oprot.writeFieldEnd()
        if self.C is not None:
            oprot.writeFieldBegin('C', TType.DOUBLE, 6)
            oprot.writeDouble(self.C)
            oprot.writeFieldEnd()
        if self.fitIntercept is not None:
            oprot.writeFieldBegin('fitIntercept', TType.BOOL, 7)
            oprot.writeBool(self.fitIntercept)
            oprot.writeFieldEnd()
        if self.interceptScaling is not None:
            oprot.writeFieldBegin('interceptScaling', TType.DOUBLE, 8)
            oprot.writeDouble(self.interceptScaling)
            oprot.writeFieldEnd()
        if self.classWeight is not None:
            oprot.writeFieldBegin('classWeight', TType.MAP, 9)
            oprot.writeMapBegin(TType.STRING, TType.DOUBLE, len(self.classWeight))
            for kiter34, viter35 in self.classWeight.items():
                oprot.writeString(kiter34.encode('utf-8') if sys.version_info[0] == 2 else kiter34)
                oprot.writeDouble(viter35)
            oprot.writeMapEnd()
            oprot.writeFieldEnd()
        if self.randomState is not None:
            oprot.writeFieldBegin('randomState', TType.LIST, 10)
            oprot.writeListBegin(TType.I32, len(self.randomState))
            for iter36 in self.randomState:
                oprot.writeI32(iter36)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.solver is not None:
            oprot.writeFieldBegin('solver', TType.STRING, 11)
            oprot.writeString(self.solver.encode('utf-8') if sys.version_info[0] == 2 else self.solver)
            oprot.writeFieldEnd()
        if self.maxIter is not None:
            oprot.writeFieldBegin('maxIter', TType.I32, 12)
            oprot.writeI32(self.maxIter)
            oprot.writeFieldEnd()
        if self.multiClass is not None:
            oprot.writeFieldBegin('multiClass', TType.STRING, 13)
            oprot.writeString(self.multiClass.encode('utf-8') if sys.version_info[0] == 2 else self.multiClass)
            oprot.writeFieldEnd()
        if self.verbose is not None:
            oprot.writeFieldBegin('verbose', TType.I32, 14)
            oprot.writeI32(self.verbose)
            oprot.writeFieldEnd()
        if self.warmStart is not None:
            oprot.writeFieldBegin('warmStart', TType.BOOL, 15)
            oprot.writeBool(self.warmStart)
            oprot.writeFieldEnd()
        if self.nJobs is not None:
            oprot.writeFieldBegin('nJobs', TType.I32, 16)
            oprot.writeI32(self.nJobs)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(logisticRegression_args)
logisticRegression_args.thrift_spec = (
    None,  # 0
    (1, TType.LIST, 'xTrain', (TType.LIST, (TType.DOUBLE, None, False), False), None, ),  # 1
    (2, TType.LIST, 'yTrain', (TType.DOUBLE, None, False), None, ),  # 2
    (3, TType.STRING, 'penalty', 'UTF8', "l2", ),  # 3
    (4, TType.BOOL, 'dual', None, False, ),  # 4
    (5, TType.DOUBLE, 'tol', None, 0.0001, ),  # 5
    (6, TType.DOUBLE, 'C', None, 1, ),  # 6
    (7, TType.BOOL, 'fitIntercept', None, True, ),  # 7
    (8, TType.DOUBLE, 'interceptScaling', None, 1, ),  # 8
    (9, TType.MAP, 'classWeight', (TType.STRING, 'UTF8', TType.DOUBLE, None, False), {
    }, ),  # 9
    (10, TType.LIST, 'randomState', (TType.I32, None, False), [
    ], ),  # 10
    (11, TType.STRING, 'solver', 'UTF8', "liblinear", ),  # 11
    (12, TType.I32, 'maxIter', None, 100, ),  # 12
    (13, TType.STRING, 'multiClass', 'UTF8', "ovr", ),  # 13
    (14, TType.I32, 'verbose', None, 0, ),  # 14
    (15, TType.BOOL, 'warmStart', None, False, ),  # 15
    (16, TType.I32, 'nJobs', None, 1, ),  # 16
)


class logisticRegression_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.LIST:
                    self.success = []
                    (_etype40, _size37) = iprot.readListBegin()
                    for _i41 in range(_size37):
                        _elem42 = iprot.readDouble()
                        self.success.append(_elem42)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = LearnerException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('logisticRegression_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.DOUBLE, len(self.success))
            for iter43 in self.success:
                oprot.writeDouble(iter43)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(logisticRegression_result)
logisticRegression_result.thrift_spec = (
    (0, TType.LIST, 'success', (TType.DOUBLE, None, False), None, ),  # 0
    (1, TType.STRUCT, 'e', [LearnerException, None], None, ),  # 1
)
fix_spec(all_structs)
del all_structs

