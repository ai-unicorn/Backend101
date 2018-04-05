namespace cpp learner
namespace java learner
namespace py learner


enum LearnErrorCode {
  RUNTIME_ERROR = 0,
}

exception LearnerException {
  1: LearnErrorCode errorCode,
  2: string message,
}

struct LogisticRegressionAttributes {
  1: list<list<double>> coef,
  2: list<double> intercept,
  3: list<double> n_iter,
}

service LearnerService {

  string hello(
    1: string identity,
  ) throws (1: LearnerException e);

  // TODO: investigate why the default value doesn't work
  //       may have to use another fork
  LogisticRegressionAttributes logisticRegression(
    1: required list<list<double>> xTrain,
    2: required list<double> yTrain,
    3: optional string penalty = "l2",
    4: optional bool dual = false,
    5: optional double tol = 0.0001,
    6: optional double C = 1.0,
    7: optional bool fitIntercept = true,
    8: optional double interceptScaling = 1,
    // if classWeight is an empty map, use 'balanced' mode
    9: optional map<string, double> classWeight = None,
    // randomState is used when solver == ‘sag’ or ‘liblinear’
    10: optional list<i32> randomState = None,
    // {‘newton-cg’, ‘lbfgs’, ‘liblinear’, ‘sag’, ‘saga’} for solver
    11: optional string solver = "liblinear",
    12: optional i32 maxIter = 100,
    // {‘ovr’, ‘multinomial’} for multiClass
    13: optional string multiClass = "ovr",
    14: optional i32 verbose = 0,
    15: optional bool warmStart = false,
    16: optional i32 nJobs = 1,
  ) throws (1: LearnerException e);

}
