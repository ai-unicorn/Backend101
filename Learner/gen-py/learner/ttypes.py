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

from thrift.transport import TTransport
all_structs = []


class LearnErrorCode(object):
    RUNTIME_ERROR = 0

    _VALUES_TO_NAMES = {
        0: "RUNTIME_ERROR",
    }

    _NAMES_TO_VALUES = {
        "RUNTIME_ERROR": 0,
    }


class LearnerException(TException):
    """
    Attributes:
     - errorCode
     - message
    """


    def __init__(self, errorCode=None, message=None,):
        self.errorCode = errorCode
        self.message = message

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
                if ftype == TType.I32:
                    self.errorCode = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.message = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('LearnerException')
        if self.errorCode is not None:
            oprot.writeFieldBegin('errorCode', TType.I32, 1)
            oprot.writeI32(self.errorCode)
            oprot.writeFieldEnd()
        if self.message is not None:
            oprot.writeFieldBegin('message', TType.STRING, 2)
            oprot.writeString(self.message.encode('utf-8') if sys.version_info[0] == 2 else self.message)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __str__(self):
        return repr(self)

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class LogisticRegressionAttributes(object):
    """
    Attributes:
     - coef
     - intercept
     - n_iter
    """


    def __init__(self, coef=None, intercept=None, n_iter=None,):
        self.coef = coef
        self.intercept = intercept
        self.n_iter = n_iter

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
                    self.coef = []
                    (_etype3, _size0) = iprot.readListBegin()
                    for _i4 in range(_size0):
                        _elem5 = []
                        (_etype9, _size6) = iprot.readListBegin()
                        for _i10 in range(_size6):
                            _elem11 = iprot.readDouble()
                            _elem5.append(_elem11)
                        iprot.readListEnd()
                        self.coef.append(_elem5)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.LIST:
                    self.intercept = []
                    (_etype15, _size12) = iprot.readListBegin()
                    for _i16 in range(_size12):
                        _elem17 = iprot.readDouble()
                        self.intercept.append(_elem17)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.LIST:
                    self.n_iter = []
                    (_etype21, _size18) = iprot.readListBegin()
                    for _i22 in range(_size18):
                        _elem23 = iprot.readDouble()
                        self.n_iter.append(_elem23)
                    iprot.readListEnd()
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
        oprot.writeStructBegin('LogisticRegressionAttributes')
        if self.coef is not None:
            oprot.writeFieldBegin('coef', TType.LIST, 1)
            oprot.writeListBegin(TType.LIST, len(self.coef))
            for iter24 in self.coef:
                oprot.writeListBegin(TType.DOUBLE, len(iter24))
                for iter25 in iter24:
                    oprot.writeDouble(iter25)
                oprot.writeListEnd()
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.intercept is not None:
            oprot.writeFieldBegin('intercept', TType.LIST, 2)
            oprot.writeListBegin(TType.DOUBLE, len(self.intercept))
            for iter26 in self.intercept:
                oprot.writeDouble(iter26)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.n_iter is not None:
            oprot.writeFieldBegin('n_iter', TType.LIST, 3)
            oprot.writeListBegin(TType.DOUBLE, len(self.n_iter))
            for iter27 in self.n_iter:
                oprot.writeDouble(iter27)
            oprot.writeListEnd()
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


class DecisionTreeAttributes(object):
    """
    Attributes:
     - classes
     - feature_importances
     - max_features
     - n_classes
     - n_features
     - n_outputs
    """


    def __init__(self, classes=None, feature_importances=None, max_features=None, n_classes=None, n_features=None, n_outputs=None,):
        self.classes = classes
        self.feature_importances = feature_importances
        self.max_features = max_features
        self.n_classes = n_classes
        self.n_features = n_features
        self.n_outputs = n_outputs

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
                    self.classes = []
                    (_etype31, _size28) = iprot.readListBegin()
                    for _i32 in range(_size28):
                        _elem33 = []
                        (_etype37, _size34) = iprot.readListBegin()
                        for _i38 in range(_size34):
                            _elem39 = iprot.readDouble()
                            _elem33.append(_elem39)
                        iprot.readListEnd()
                        self.classes.append(_elem33)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.LIST:
                    self.feature_importances = []
                    (_etype43, _size40) = iprot.readListBegin()
                    for _i44 in range(_size40):
                        _elem45 = iprot.readDouble()
                        self.feature_importances.append(_elem45)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.max_features = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.LIST:
                    self.n_classes = []
                    (_etype49, _size46) = iprot.readListBegin()
                    for _i50 in range(_size46):
                        _elem51 = iprot.readDouble()
                        self.n_classes.append(_elem51)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.n_features = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I32:
                    self.n_outputs = iprot.readI32()
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
        oprot.writeStructBegin('DecisionTreeAttributes')
        if self.classes is not None:
            oprot.writeFieldBegin('classes', TType.LIST, 1)
            oprot.writeListBegin(TType.LIST, len(self.classes))
            for iter52 in self.classes:
                oprot.writeListBegin(TType.DOUBLE, len(iter52))
                for iter53 in iter52:
                    oprot.writeDouble(iter53)
                oprot.writeListEnd()
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.feature_importances is not None:
            oprot.writeFieldBegin('feature_importances', TType.LIST, 2)
            oprot.writeListBegin(TType.DOUBLE, len(self.feature_importances))
            for iter54 in self.feature_importances:
                oprot.writeDouble(iter54)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.max_features is not None:
            oprot.writeFieldBegin('max_features', TType.I32, 3)
            oprot.writeI32(self.max_features)
            oprot.writeFieldEnd()
        if self.n_classes is not None:
            oprot.writeFieldBegin('n_classes', TType.LIST, 4)
            oprot.writeListBegin(TType.DOUBLE, len(self.n_classes))
            for iter55 in self.n_classes:
                oprot.writeDouble(iter55)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.n_features is not None:
            oprot.writeFieldBegin('n_features', TType.I32, 5)
            oprot.writeI32(self.n_features)
            oprot.writeFieldEnd()
        if self.n_outputs is not None:
            oprot.writeFieldBegin('n_outputs', TType.I32, 6)
            oprot.writeI32(self.n_outputs)
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
all_structs.append(LearnerException)
LearnerException.thrift_spec = (
    None,  # 0
    (1, TType.I32, 'errorCode', None, None, ),  # 1
    (2, TType.STRING, 'message', 'UTF8', None, ),  # 2
)
all_structs.append(LogisticRegressionAttributes)
LogisticRegressionAttributes.thrift_spec = (
    None,  # 0
    (1, TType.LIST, 'coef', (TType.LIST, (TType.DOUBLE, None, False), False), None, ),  # 1
    (2, TType.LIST, 'intercept', (TType.DOUBLE, None, False), None, ),  # 2
    (3, TType.LIST, 'n_iter', (TType.DOUBLE, None, False), None, ),  # 3
)
all_structs.append(DecisionTreeAttributes)
DecisionTreeAttributes.thrift_spec = (
    None,  # 0
    (1, TType.LIST, 'classes', (TType.LIST, (TType.DOUBLE, None, False), False), None, ),  # 1
    (2, TType.LIST, 'feature_importances', (TType.DOUBLE, None, False), None, ),  # 2
    (3, TType.I32, 'max_features', None, None, ),  # 3
    (4, TType.LIST, 'n_classes', (TType.DOUBLE, None, False), None, ),  # 4
    (5, TType.I32, 'n_features', None, None, ),  # 5
    (6, TType.I32, 'n_outputs', None, None, ),  # 6
)
fix_spec(all_structs)
del all_structs
