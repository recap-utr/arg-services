module.exports = {
  aduProto: require("./arg_services/adu/v1/adu_pb"),
  aduService: require("./arg_services/adu/v1/AduServiceClientPb"),
  baseProto: require("./arg_services/base/v1/base_pb"),
  entailmentProto: require("./arg_services/entailment/v1/entailment_pb"),
  entailmentService: require("./arg_services/entailment/v1/EntailmentServiceClientPb"),
  graphProto: require("./arg_services/graph/v1/graph_pb"),
  retrievalProto: require("./arg_services/retrieval/v1/retrieval_pb"),
  retrievalService: require("./arg_services/retrieval/v1/RetrievalServiceClientPb"),
};
