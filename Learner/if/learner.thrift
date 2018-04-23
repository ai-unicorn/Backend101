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

struct DecisionTreeAttributes {
  1: list<list<double>> classes,
  2: list<double> feature_importances,
  3: i32 max_features,
  4: list<double> n_classes,
  5: i32 n_features,
  6: i32 n_outputs,
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

  DecisionTreeAttributes decisionTreeClassifier(
    1: required list<list<double>> xTrain,
    2: required list<double> yTrain,
    3: list<double> sample_weight,
    4: bool check_input,
    5: list<double> x_idx_sorted,
    6: string criterion,
    7: string splitter,
    8: string max_depth,
    9: string min_samples_split,
    10: string min_samples_leaf,
    11: double min_weight_fraction_leaf,
    12: string max_features,
    13: list<i32> randomState,
    14: string max_leaf_nodes,
    15: double min_impurity_decrease,
    16: double min_impurity_split,
    17: list<map<string, string>> class_weight,
    18: bool presort,
  ) throws (1: LearnerException e);
}
