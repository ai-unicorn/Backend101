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

service LearnerService {

  string hello(
    1: string identity,
  ) throws (1: LearnerException e);

  list<double> logisticRegression(
    1: list<list<double>> xTrain,
    2: list<double> yTrain,
    3: string penalty = "l2",
    4: bool dual = false,
    5: double tol = 0.0001,
    6: double C = 1.0,
    7: bool fitIntercept = true,
    8: double interceptScaling = 1,
    // if classWeight is an empty map, use 'balanced' mode
    9: map<string, double> classWeight = None,
    // randomState is used when solver == ‘sag’ or ‘liblinear’
    10: list<i32> randomState = None,
    // {‘newton-cg’, ‘lbfgs’, ‘liblinear’, ‘sag’, ‘saga’} for solver
    11: string solver = "liblinear",
    12: i32 maxIter = 100,
    // {‘ovr’, ‘multinomial’} for multiClass
    13: string multiClass = "ovr",
    14: i32 verbose = 0,
    15: bool warmStart = false,
    16: i32 nJobs = 1,
  ) throws (1: LearnerException e);

}
