// include "fb303.thrift"

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

service LearnerService { // extends fb303.FacebookService {

  string hello(
    1: string identity,
  ) throws (1: LearnerException e);

}
