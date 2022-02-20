# Protocol Documentation
<a name="top"></a>

## Table of Contents

- [arg_services/adu/v1/adu.proto](#arg_services_adu_v1_adu-proto)
    - [ClassificationRequest](#arg_services-adu-v1-ClassificationRequest)
    - [ClassificationResponse](#arg_services-adu-v1-ClassificationResponse)
    - [ClassifiedSegment](#arg_services-adu-v1-ClassifiedSegment)
    - [SegmentationRequest](#arg_services-adu-v1-SegmentationRequest)
    - [SegmentationResponse](#arg_services-adu-v1-SegmentationResponse)
  
    - [Classifier](#arg_services-adu-v1-Classifier)
    - [Granularity](#arg_services-adu-v1-Granularity)
  
    - [AduService](#arg_services-adu-v1-AduService)
  
- [arg_services/base/v1/base.proto](#arg_services_base_v1_base-proto)
- [arg_services/entailment/v1/entailment.proto](#arg_services_entailment_v1_entailment-proto)
    - [Detail](#arg_services-entailment-v1-Detail)
    - [EntailmentRequest](#arg_services-entailment-v1-EntailmentRequest)
    - [EntailmentResponse](#arg_services-entailment-v1-EntailmentResponse)
    - [EntailmentsRequest](#arg_services-entailment-v1-EntailmentsRequest)
    - [EntailmentsResponse](#arg_services-entailment-v1-EntailmentsResponse)
  
    - [Prediction](#arg_services-entailment-v1-Prediction)
  
    - [EntailmentService](#arg_services-entailment-v1-EntailmentService)
  
- [arg_services/graph/v1/graph.proto](#arg_services_graph_v1_graph-proto)
    - [AtomNode](#arg_services-graph-v1-AtomNode)
    - [Edge](#arg_services-graph-v1-Edge)
    - [Graph](#arg_services-graph-v1-Graph)
    - [Graph.EdgesEntry](#arg_services-graph-v1-Graph-EdgesEntry)
    - [Graph.NodesEntry](#arg_services-graph-v1-Graph-NodesEntry)
    - [Graph.ParticipantsEntry](#arg_services-graph-v1-Graph-ParticipantsEntry)
    - [Graph.ResourcesEntry](#arg_services-graph-v1-Graph-ResourcesEntry)
    - [Node](#arg_services-graph-v1-Node)
    - [Participant](#arg_services-graph-v1-Participant)
    - [Reference](#arg_services-graph-v1-Reference)
    - [Resource](#arg_services-graph-v1-Resource)
    - [SchemeNode](#arg_services-graph-v1-SchemeNode)
  
    - [Scheme](#arg_services-graph-v1-Scheme)
    - [SchemeType](#arg_services-graph-v1-SchemeType)
  
- [arg_services/nlp/v1/nlp.proto](#arg_services_nlp_v1_nlp-proto)
    - [DocBinRequest](#arg_services-nlp-v1-DocBinRequest)
    - [DocBinResponse](#arg_services-nlp-v1-DocBinResponse)
    - [EmbeddingModel](#arg_services-nlp-v1-EmbeddingModel)
    - [NlpConfig](#arg_services-nlp-v1-NlpConfig)
    - [SimilaritiesRequest](#arg_services-nlp-v1-SimilaritiesRequest)
    - [SimilaritiesResponse](#arg_services-nlp-v1-SimilaritiesResponse)
    - [Strings](#arg_services-nlp-v1-Strings)
    - [TextTuple](#arg_services-nlp-v1-TextTuple)
    - [Vector](#arg_services-nlp-v1-Vector)
    - [VectorResponse](#arg_services-nlp-v1-VectorResponse)
    - [VectorsRequest](#arg_services-nlp-v1-VectorsRequest)
    - [VectorsResponse](#arg_services-nlp-v1-VectorsResponse)
  
    - [EmbeddingLevel](#arg_services-nlp-v1-EmbeddingLevel)
    - [EmbeddingType](#arg_services-nlp-v1-EmbeddingType)
    - [Pooling](#arg_services-nlp-v1-Pooling)
    - [SimilarityMethod](#arg_services-nlp-v1-SimilarityMethod)
  
    - [NlpService](#arg_services-nlp-v1-NlpService)
  
- [arg_services/retrieval/v1/retrieval.proto](#arg_services_retrieval_v1_retrieval-proto)
    - [Mapping](#arg_services-retrieval-v1-Mapping)
    - [RetrieveRequest](#arg_services-retrieval-v1-RetrieveRequest)
    - [RetrieveRequest.CasesEntry](#arg_services-retrieval-v1-RetrieveRequest-CasesEntry)
    - [RetrieveResponse](#arg_services-retrieval-v1-RetrieveResponse)
    - [RetrievedCase](#arg_services-retrieval-v1-RetrievedCase)
    - [RetrievedMapping](#arg_services-retrieval-v1-RetrievedMapping)
  
    - [MappingAlgorithm](#arg_services-retrieval-v1-MappingAlgorithm)
  
    - [RetrievalService](#arg_services-retrieval-v1-RetrievalService)
  
- [arg_services/topic_modeling/v1/topic_modeling.proto](#arg_services_topic_modeling_v1_topic_modeling-proto)
    - [Term](#arg_services-topic_modeling-v1-Term)
    - [Topic](#arg_services-topic_modeling-v1-Topic)
    - [TopicsRequest](#arg_services-topic_modeling-v1-TopicsRequest)
    - [TopicsResponse](#arg_services-topic_modeling-v1-TopicsResponse)
  
    - [TopicModelingService](#arg_services-topic_modeling-v1-TopicModelingService)
  
- [Scalar Value Types](#scalar-value-types)



<a name="arg_services_adu_v1_adu-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## arg_services/adu/v1/adu.proto



<a name="arg_services-adu-v1-ClassificationRequest"></a>

### ClassificationRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| segments | [string](#string) | repeated |  |
| classifier | [Classifier](#arg_services-adu-v1-Classifier) |  |  |






<a name="arg_services-adu-v1-ClassificationResponse"></a>

### ClassificationResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| segments | [ClassifiedSegment](#arg_services-adu-v1-ClassifiedSegment) | repeated |  |






<a name="arg_services-adu-v1-ClassifiedSegment"></a>

### ClassifiedSegment



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| text | [string](#string) |  |  |
| adu | [bool](#bool) |  |  |
| claim | [bool](#bool) |  |  |
| premise | [bool](#bool) |  |  |






<a name="arg_services-adu-v1-SegmentationRequest"></a>

### SegmentationRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| text | [string](#string) |  |  |
| granularity | [Granularity](#arg_services-adu-v1-Granularity) |  |  |






<a name="arg_services-adu-v1-SegmentationResponse"></a>

### SegmentationResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| segments | [string](#string) | repeated |  |





 


<a name="arg_services-adu-v1-Classifier"></a>

### Classifier


| Name | Number | Description |
| ---- | ------ | ----------- |
| CLASSIFIER_UNSPECIFIED | 0 |  |
| CLASSIFIER_TWO_WAY | 1 |  |
| CLASSIFIER_THREE_WAY | 2 |  |
| CLASSIFIER_SEQUENTIAL | 3 |  |



<a name="arg_services-adu-v1-Granularity"></a>

### Granularity


| Name | Number | Description |
| ---- | ------ | ----------- |
| GRANULARITY_UNSPECIFIED | 0 |  |
| GRANULARITY_SENTENCE | 1 |  |
| GRANULARITY_SUBSENTENCE | 2 |  |
| GRANULARITY_PARAGRAPH | 3 |  |


 

 


<a name="arg_services-adu-v1-AduService"></a>

### AduService


| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| Segmentation | [SegmentationRequest](#arg_services-adu-v1-SegmentationRequest) | [SegmentationResponse](#arg_services-adu-v1-SegmentationResponse) |  |
| Classification | [ClassificationRequest](#arg_services-adu-v1-ClassificationRequest) | [ClassificationResponse](#arg_services-adu-v1-ClassificationResponse) | rpc TwoWay (TwoWayRequest) returns (TwoWayResponse); rpc ThreeWay (ThreeWayRequest) returns (ThreeWayResponse); rpc Sequential (SequentialRequest) returns (SequentialResponse); |

 



<a name="arg_services_base_v1_base-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## arg_services/base/v1/base.proto


 

 

 

 



<a name="arg_services_entailment_v1_entailment-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## arg_services/entailment/v1/entailment.proto



<a name="arg_services-entailment-v1-Detail"></a>

### Detail



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| probability | [double](#double) |  |  |
| prediction | [Prediction](#arg_services-entailment-v1-Prediction) |  |  |






<a name="arg_services-entailment-v1-EntailmentRequest"></a>

### EntailmentRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| language | [string](#string) |  |  |
| premise | [string](#string) |  |  |
| claim | [string](#string) |  |  |






<a name="arg_services-entailment-v1-EntailmentResponse"></a>

### EntailmentResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| prediction | [Prediction](#arg_services-entailment-v1-Prediction) |  |  |
| details | [Detail](#arg_services-entailment-v1-Detail) | repeated |  |






<a name="arg_services-entailment-v1-EntailmentsRequest"></a>

### EntailmentsRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| queries | [EntailmentRequest](#arg_services-entailment-v1-EntailmentRequest) | repeated |  |






<a name="arg_services-entailment-v1-EntailmentsResponse"></a>

### EntailmentsResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| results | [EntailmentResponse](#arg_services-entailment-v1-EntailmentResponse) | repeated |  |





 


<a name="arg_services-entailment-v1-Prediction"></a>

### Prediction


| Name | Number | Description |
| ---- | ------ | ----------- |
| PREDICTION_UNSPECIFIED | 0 |  |
| PREDICTION_ENTAILMENT | 1 |  |
| PREDICTION_CONTRADICTION | 2 |  |
| PREDICTION_NEUTRAL | 3 |  |


 

 


<a name="arg_services-entailment-v1-EntailmentService"></a>

### EntailmentService


| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| Entailment | [EntailmentRequest](#arg_services-entailment-v1-EntailmentRequest) | [EntailmentResponse](#arg_services-entailment-v1-EntailmentResponse) |  |
| Entailments | [EntailmentsRequest](#arg_services-entailment-v1-EntailmentsRequest) | [EntailmentsResponse](#arg_services-entailment-v1-EntailmentsResponse) |  |

 



<a name="arg_services_graph_v1_graph-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## arg_services/graph/v1/graph.proto



<a name="arg_services-graph-v1-AtomNode"></a>

### AtomNode



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| text | [string](#string) |  |  |
| reference | [Reference](#arg_services-graph-v1-Reference) | optional |  |
| participant | [string](#string) | optional |  |






<a name="arg_services-graph-v1-Edge"></a>

### Edge



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| source | [string](#string) |  | string id = 1; |
| target | [string](#string) |  |  |
| created | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  |  |
| updated | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  |  |
| metadata | [google.protobuf.Struct](#google-protobuf-Struct) |  |  |






<a name="arg_services-graph-v1-Graph"></a>

### Graph



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| nodes | [Graph.NodesEntry](#arg_services-graph-v1-Graph-NodesEntry) | repeated | string id = 1; |
| edges | [Graph.EdgesEntry](#arg_services-graph-v1-Graph-EdgesEntry) | repeated |  |
| resources | [Graph.ResourcesEntry](#arg_services-graph-v1-Graph-ResourcesEntry) | repeated |  |
| participants | [Graph.ParticipantsEntry](#arg_services-graph-v1-Graph-ParticipantsEntry) | repeated |  |
| major_claim | [string](#string) | optional |  |
| analysts | [Participant](#arg_services-graph-v1-Participant) | repeated |  |
| version | [string](#string) |  |  |
| created | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  |  |
| updated | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  |  |
| metadata | [google.protobuf.Struct](#google-protobuf-Struct) |  |  |






<a name="arg_services-graph-v1-Graph-EdgesEntry"></a>

### Graph.EdgesEntry



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [string](#string) |  |  |
| value | [Edge](#arg_services-graph-v1-Edge) |  |  |






<a name="arg_services-graph-v1-Graph-NodesEntry"></a>

### Graph.NodesEntry



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [string](#string) |  |  |
| value | [Node](#arg_services-graph-v1-Node) |  |  |






<a name="arg_services-graph-v1-Graph-ParticipantsEntry"></a>

### Graph.ParticipantsEntry



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [string](#string) |  |  |
| value | [Participant](#arg_services-graph-v1-Participant) |  |  |






<a name="arg_services-graph-v1-Graph-ResourcesEntry"></a>

### Graph.ResourcesEntry



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [string](#string) |  |  |
| value | [Resource](#arg_services-graph-v1-Resource) |  |  |






<a name="arg_services-graph-v1-Node"></a>

### Node



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| atom | [AtomNode](#arg_services-graph-v1-AtomNode) |  |  |
| scheme | [SchemeNode](#arg_services-graph-v1-SchemeNode) |  |  |
| created | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  |  |
| updated | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  |  |
| metadata | [google.protobuf.Struct](#google-protobuf-Struct) |  |  |






<a name="arg_services-graph-v1-Participant"></a>

### Participant



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](#string) |  | string id = 1; |
| username | [string](#string) |  |  |
| email | [string](#string) |  |  |
| url | [string](#string) |  |  |
| location | [string](#string) |  |  |
| description | [string](#string) |  |  |
| created | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  |  |
| updated | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  |  |
| metadata | [google.protobuf.Struct](#google-protobuf-Struct) |  |  |






<a name="arg_services-graph-v1-Reference"></a>

### Reference



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| resource | [string](#string) |  | string id = 1; |
| offset | [int64](#int64) |  |  |
| text | [string](#string) |  |  |
| metadata | [google.protobuf.Struct](#google-protobuf-Struct) |  |  |






<a name="arg_services-graph-v1-Resource"></a>

### Resource



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| text | [string](#string) |  | string id = 1; |
| title | [string](#string) |  |  |
| source | [string](#string) |  |  |
| created | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  |  |
| updated | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  |  |
| metadata | [google.protobuf.Struct](#google-protobuf-Struct) |  |  |






<a name="arg_services-graph-v1-SchemeNode"></a>

### SchemeNode



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [SchemeType](#arg_services-graph-v1-SchemeType) | optional |  |
| argumentation_scheme | [Scheme](#arg_services-graph-v1-Scheme) | optional |  |
| descriptors | [google.protobuf.Struct](#google-protobuf-Struct) |  |  |





 


<a name="arg_services-graph-v1-Scheme"></a>

### Scheme


| Name | Number | Description |
| ---- | ------ | ----------- |
| SCHEME_UNSPECIFIED | 0 |  |
| SCHEME_AD_HOMINEM | 1 |  |
| SCHEME_ALTERNATIVE_MEANS | 2 |  |
| SCHEME_ALTERNATIVES | 3 |  |
| SCHEME_ANALOGY | 4 |  |
| SCHEME_ARBITRARY_VERBAL_CLASSIFICATION | 5 |  |
| SCHEME_AUTHORITY | 6 |  |
| SCHEME_BIAS | 7 |  |
| SCHEME_BIASED_CLASSIFICATION | 8 |  |
| SCHEME_CALLING_OUT | 9 |  |
| SCHEME_CAUSAL_SLIPPERY_SLOPE | 10 |  |
| SCHEME_CAUSE_TO_EFFECT | 11 |  |
| SCHEME_CIRCUMSTANTIAL_AD_HOMINEM | 12 |  |
| SCHEME_COMMITMENT_EXCEPTION | 13 |  |
| SCHEME_COMMITMENT | 14 |  |
| SCHEME_COMPOSITION | 15 |  |
| SCHEME_CONFLICTING_GOALS | 16 |  |
| SCHEME_CONSEQUENCES | 17 |  |
| SCHEME_CORRELATION_TO_CAUSE | 18 |  |
| SCHEME_DANGER_APPEAL | 19 |  |
| SCHEME_DEFINITION_TO_VERBAL_CLASSIFICATION | 20 |  |
| SCHEME_DIFFERENCES_UNDERMINE_SIMILARITY | 21 |  |
| SCHEME_DILEMMA | 22 |  |
| SCHEME_DIRECT_AD_HOMINEM | 23 |  |
| SCHEME_DIVISION | 24 |  |
| SCHEME_ESTABLISHED_RULE | 25 |  |
| SCHEME_ETHOTIC | 26 |  |
| SCHEME_EVIDENCE_TO_HYPOTHESIS | 27 |  |
| SCHEME_EXAMPLE | 28 |  |
| SCHEME_EXCEPTION_SIMILARITY_CASE | 29 |  |
| SCHEME_EXCEPTIONAL_CASE | 30 |  |
| SCHEME_EXPERT_OPINION | 31 |  |
| SCHEME_EXPERTISE_INCONSISTENCY | 32 |  |
| SCHEME_FAIRNESS | 33 |  |
| SCHEME_FALSIFICATION_OF_HYPOTHESIS | 34 |  |
| SCHEME_FEAR_APPEAL | 35 |  |
| SCHEME_FULL_SLIPPERY_SLOPE | 36 |  |
| SCHEME_GENERAL_ACCEPTANCE_DOUBT | 37 |  |
| SCHEME_GENERIC_AD_HOMINEM | 38 |  |
| SCHEME_GOODWILL | 39 |  |
| SCHEME_GRADUALISM | 40 |  |
| SCHEME_IGNORANCE | 41 |  |
| SCHEME_INCONSISTENT_COMMITMENT | 42 |  |
| SCHEME_INFORMANT_REPORT | 43 |  |
| SCHEME_INTERACTION_OF_ACT_AND_PERSON | 44 |  |
| SCHEME_IRRATIONAL_FEAR_APPEAL | 45 |  |
| SCHEME_LACK_OF_COMPLETE_KNOWLEDGE | 46 |  |
| SCHEME_LACK_OF_EXPERT_RELIABILITY | 47 |  |
| SCHEME_LOGICAL | 48 |  |
| SCHEME_MISPLACED_PRIORITIES | 49 |  |
| SCHEME_MODUS_PONENS | 50 |  |
| SCHEME_MORAL_VIRTUE | 51 |  |
| SCHEME_NEED_FOR_HELP | 52 |  |
| SCHEME_NEGATIVE_CONSEQUENCES | 53 |  |
| SCHEME_OPPOSED_COMMITMENT | 54 |  |
| SCHEME_OPPOSITIONS | 55 |  |
| SCHEME_CAUSAL_FACTORS_INVOLVED | 56 |  |
| SCHEME_PARAPHRASE | 57 |  |
| SCHEME_PERCEPTION | 58 |  |
| SCHEME_POPULAR_OPINION | 59 |  |
| SCHEME_POPULAR_PRACTICE | 60 |  |
| SCHEME_POSITION_TO_KNOW | 61 |  |
| SCHEME_POSITIVE_CONSEQUENCES | 62 |  |
| SCHEME_PRACTICAL_REASONING_FROM_ANALOGY | 63 |  |
| SCHEME_PRACTICAL_REASONING | 64 |  |
| SCHEME_PRACTICAL_WISDOM | 65 |  |
| SCHEME_PRAGMATIC_ALTERNATIVES | 66 |  |
| SCHEME_PRAGMATIC_INCONSISTENCY | 67 |  |
| SCHEME_PRECEDENT_SLIPPERY_SLOPE | 68 |  |
| SCHEME_PROPERTY_NOT_EXISTANT | 69 |  |
| SCHEME_REFRAMING | 70 |  |
| SCHEME_REQUIRED_STEPS | 71 |  |
| SCHEME_RESOLVING_INCONSISTENCY | 72 |  |
| SCHEME_RULE | 73 |  |
| SCHEME_RULES | 74 |  |
| SCHEME_SIGN_FROM_OTHER_EVENTS | 75 |  |
| SCHEME_SIGN | 76 |  |
| SCHEME_TWO_PERSON_PRACTICAL_REASONING | 77 |  |
| SCHEME_UNFAIRNESS | 78 |  |
| SCHEME_VAGUE_VERBAL_CLASSIFICATION | 79 |  |
| SCHEME_VAGUENESS_OF_VERBAL_CLASSIFICATION | 80 |  |
| SCHEME_VALUE_BASED_PRACTICAL_REASONING | 81 |  |
| SCHEME_VALUES | 82 |  |
| SCHEME_VERBAL_CLASSIFICATION | 83 |  |
| SCHEME_VERBAL_SLIPPERY_SLOPE | 84 |  |
| SCHEME_VESTED_INTEREST | 85 |  |
| SCHEME_VIRTUE_GOODWILL | 86 |  |
| SCHEME_WASTE | 87 |  |
| SCHEME_WEAKEST_LINK | 88 |  |
| SCHEME_WISDOM_GOODWILL | 89 |  |
| SCHEME_WISDOM_VIRTUE | 90 |  |
| SCHEME_WISDOM_VIRTUE_GOODWILL | 91 |  |
| SCHEME_WITNESS_TESTIMONY | 92 |  |



<a name="arg_services-graph-v1-SchemeType"></a>

### SchemeType


| Name | Number | Description |
| ---- | ------ | ----------- |
| SCHEME_TYPE_UNSPECIFIED | 0 |  |
| SCHEME_TYPE_SUPPORT | 1 |  |
| SCHEME_TYPE_ATTACK | 2 |  |
| SCHEME_TYPE_REPHRASE | 3 |  |
| SCHEME_TYPE_TRANSITION | 4 |  |
| SCHEME_TYPE_PREFERENCE | 5 |  |
| SCHEME_TYPE_ASSERTION | 6 |  |


 

 

 



<a name="arg_services_nlp_v1_nlp-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## arg_services/nlp/v1/nlp.proto



<a name="arg_services-nlp-v1-DocBinRequest"></a>

### DocBinRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| config | [NlpConfig](#arg_services-nlp-v1-NlpConfig) |  | Spacy config. |
| texts | [string](#string) | repeated | List of strings to be processed. |
| attributes | [Strings](#arg_services-nlp-v1-Strings) | optional | Attributes that shall be included in the DocBin object. Defaults to `(&#34;ORTH&#34;, &#34;TAG&#34;, &#34;HEAD&#34;, &#34;DEP&#34;, &#34;ENT_IOB&#34;, &#34;ENT_TYPE&#34;, &#34;ENT_KB_ID&#34;, &#34;LEMMA&#34;, &#34;MORPH&#34;, &#34;POS&#34;)`. Possible values: `(&#34;IS_ALPHA&#34;, &#34;IS_ASCII&#34;, &#34;IS_DIGIT&#34;, &#34;IS_LOWER&#34;, &#34;IS_PUNCT&#34;, &#34;IS_SPACE&#34;, &#34;IS_TITLE&#34;, &#34;IS_UPPER&#34;, &#34;LIKE_URL&#34;, &#34;LIKE_NUM&#34;, &#34;LIKE_EMAIL&#34;, &#34;IS_STOP&#34;, &#34;IS_OOV_DEPRECATED&#34;, &#34;IS_BRACKET&#34;, &#34;IS_QUOTE&#34;, &#34;IS_LEFT_PUNCT&#34;, &#34;IS_RIGHT_PUNCT&#34;, &#34;IS_CURRENCY&#34;, &#34;ID&#34;, &#34;ORTH&#34;, &#34;LOWER&#34;, &#34;NORM&#34;, &#34;SHAPE&#34;, &#34;PREFIX&#34;, &#34;SUFFIX&#34;, &#34;LENGTH&#34;, &#34;CLUSTER&#34;, &#34;LEMMA&#34;, &#34;POS&#34;, &#34;TAG&#34;, &#34;DEP&#34;, &#34;ENT_IOB&#34;, &#34;ENT_TYPE&#34;, &#34;ENT_ID&#34;, &#34;ENT_KB_ID&#34;, &#34;HEAD&#34;, &#34;SENT_START&#34;, &#34;SENT_END&#34;, &#34;SPACY&#34;, &#34;PROB&#34;, &#34;LANG&#34;, &#34;MORPH&#34;, &#34;IDX&#34;)`. [Documentation](https://spacy.io/api/token#attributes). |
| enabled_pipes | [Strings](#arg_services-nlp-v1-Strings) |  |  |
| disabled_pipes | [Strings](#arg_services-nlp-v1-Strings) |  |  |
| embedding_levels | [EmbeddingLevel](#arg_services-nlp-v1-EmbeddingLevel) | repeated | List of vectors that shall be saved in the `DocBin` object. The computation is time-consuming, so you should only specify the embeddings you actually use! |






<a name="arg_services-nlp-v1-DocBinResponse"></a>

### DocBinResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| docbin | [bytes](#bytes) |  | Serialized [`DocBin`](https://spacy.io/api/docbin) object |






<a name="arg_services-nlp-v1-EmbeddingModel"></a>

### EmbeddingModel
Specification of one model that is used to generate embeddings for strings.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| model_type | [EmbeddingType](#arg_services-nlp-v1-EmbeddingType) |  | Each embedding has to be implemented, thus this enum is used to select the correct one. |
| model_name | [string](#string) |  | You have to specify the name of the model that should be used by the selected impelemtation (i.e., `model_type`). We provide links to exemplary models for each implementation in the documentation of `EmbeddingType`. |
| pooling_type | [Pooling](#arg_services-nlp-v1-Pooling) |  | Standard pooling functions like mean, min, max. |
| pmean | [double](#double) |  | Power mean (or generalized mean). This method allows you to alter the computation of the mean representation. Special cases include arithmetic mean (p = 1), geometric mean (p = 0), harmonic mean (p = -1), minimum (p = -∞), maximum (p = ∞). [Wikipedia](https://en.wikipedia.org/wiki/Generalized_mean). |






<a name="arg_services-nlp-v1-NlpConfig"></a>

### NlpConfig
Common message for configuring spacy.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| language | [string](#string) |  | Any language supported by spacy (e.g., `en`). [Reference](https://spacy.io/usage/models#languages). |
| spacy_model | [string](#string) |  | Name of the trained spacy pipeline (e.g., `en_core_web_lg`). If empty, a blank spacy model will be used (e.g., if you only need embeddings and provide custom `embedding_models`. [Example: English models](https://spacy.io/models/en). |
| embedding_models | [EmbeddingModel](#arg_services-nlp-v1-EmbeddingModel) | repeated | List of embeddings to use for computing word/sentence vectors. If given, these embeddings will **override** the embeddings of the specified `spacy_model`. Multiple models are concatenated to each other, increasing the length of the resulting vector. |
| similarity_method | [SimilarityMethod](#arg_services-nlp-v1-SimilarityMethod) |  | Mathematical function to determine a similarity score given two strings. |






<a name="arg_services-nlp-v1-SimilaritiesRequest"></a>

### SimilaritiesRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| config | [NlpConfig](#arg_services-nlp-v1-NlpConfig) |  | Spacy config. |
| text_tuples | [TextTuple](#arg_services-nlp-v1-TextTuple) | repeated | List of string pairs to compare. |






<a name="arg_services-nlp-v1-SimilaritiesResponse"></a>

### SimilaritiesResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| similarities | [double](#double) | repeated | List of similarities ordered just like the original `text_tuples`. |






<a name="arg_services-nlp-v1-Strings"></a>

### Strings
Wrapper message to encode a list of strings that can also be `null`.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| values | [string](#string) | repeated |  |






<a name="arg_services-nlp-v1-TextTuple"></a>

### TextTuple
Store a pair of strings.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| text1 | [string](#string) |  |  |
| text2 | [string](#string) |  |  |






<a name="arg_services-nlp-v1-Vector"></a>

### Vector
Container for storing a vector as a list of floats.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| vector | [double](#double) | repeated |  |






<a name="arg_services-nlp-v1-VectorResponse"></a>

### VectorResponse
Container object that includes vectors for all levels specified in `embedding_levels`.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| document | [Vector](#arg_services-nlp-v1-Vector) |  | One vector for the whole string. |
| tokens | [Vector](#arg_services-nlp-v1-Vector) | repeated | Vectors for all tokens in the string. |
| sentences | [Vector](#arg_services-nlp-v1-Vector) | repeated | Vectors for all sentences found in the string. |






<a name="arg_services-nlp-v1-VectorsRequest"></a>

### VectorsRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| config | [NlpConfig](#arg_services-nlp-v1-NlpConfig) |  | Spacy config. |
| texts | [string](#string) | repeated | List of strings that shall be embedded (i.e., converted to vectors). |
| embedding_levels | [EmbeddingLevel](#arg_services-nlp-v1-EmbeddingLevel) | repeated | List of vectors that shall be returned. The computation is time-consuming, so you should only specify the embeddings you actually use! |






<a name="arg_services-nlp-v1-VectorsResponse"></a>

### VectorsResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| vectors | [VectorResponse](#arg_services-nlp-v1-VectorResponse) | repeated | List of vectors whose order corresponds to the one of `texts`. |





 


<a name="arg_services-nlp-v1-EmbeddingLevel"></a>

### EmbeddingLevel


| Name | Number | Description |
| ---- | ------ | ----------- |
| EMBEDDING_LEVEL_UNSPECIFIED | 0 | In the default case, no vector is computed. |
| EMBEDDING_LEVEL_DOCUMENT | 1 | Compute one vector for the whole string. |
| EMBEDDING_LEVEL_TOKENS | 2 | Compute vectors for all tokens in the string. |
| EMBEDDING_LEVEL_SENTENCES | 3 | Compute vectors for all sentences found in the string. |



<a name="arg_services-nlp-v1-EmbeddingType"></a>

### EmbeddingType


| Name | Number | Description |
| ---- | ------ | ----------- |
| EMBEDDING_TYPE_UNSPECIFIED | 0 | In the default case, no embedding is computed. |
| EMBEDDING_TYPE_SPACY | 1 | [Spacy](https://spacy.io/models). |
| EMBEDDING_TYPE_TRANSFORMERS | 2 | [HuggingFace Transformers](https://huggingface.co/models). |
| EMBEDDING_TYPE_SENTENCE_TRANSFORMERS | 3 | [UKPLab Sentence Transformers](https://www.sbert.net/docs/pretrained_models.html) |
| EMBEDDING_TYPE_TENSORFLOW_HUB | 4 | Tensorflow Hub. Example: [Universal Sentence Encoder](https://tfhub.dev/google/universal-sentence-encoder/4). |



<a name="arg_services-nlp-v1-Pooling"></a>

### Pooling


| Name | Number | Description |
| ---- | ------ | ----------- |
| POOLING_UNSPECIFIED | 0 | IN the default case, the arithmetic mean should be used. |
| POOLING_MEAN | 1 | Arithmetic mean of all elements. [Wikipedia](https://en.wikipedia.org/wiki/Arithmetic_mean). |
| POOLING_MAX | 2 | Maximum element of vector. [Wikipedia](https://en.wikipedia.org/wiki/Maximum). |
| POOLING_MIN | 3 | Minimum element of vector. [Wikipedia](https://en.wikipedia.org/wiki/Minimum). |
| POOLING_SUM | 4 | Sum of all elements. |
| POOLING_FIRST | 5 | First element of vector. |
| POOLING_LAST | 6 | Last element of vector. |
| POOLING_MEDIAN | 7 | Median element of vector. [Wikipedia](https://en.wikipedia.org/wiki/Median). |
| POOLING_GMEAN | 8 | Geometirc mean of all elements. [Wikipedia](https://en.wikipedia.org/wiki/Geometric_mean). |
| POOLING_HMEAN | 9 | Harmonic mean of all elements. [Wikipedia](https://en.wikipedia.org/wiki/Harmonic_mean). |



<a name="arg_services-nlp-v1-SimilarityMethod"></a>

### SimilarityMethod
Possible methods to compute the similarity between two vectors.

| Name | Number | Description |
| ---- | ------ | ----------- |
| SIMILARITY_METHOD_UNSPECIFIED | 0 | If not given, the implementation defaults to cosine similarity. |
| SIMILARITY_METHOD_COSINE | 1 | Cosine similarity. [Wikipedia](https://en.wikipedia.org/wiki/Cosine_similarity). |
| SIMILARITY_METHOD_DYNAMAX_JACCARD | 2 | DynaMax Jaccard. [Paper](https://arxiv.org/abs/1904.13264), [Code](https://github.com/babylonhealth/fuzzymax/blob/master/similarity/fuzzy.py). |
| SIMILARITY_METHOD_MAXPOOL_JACCARD | 3 | MaxPool Jaccard. [Paper](https://arxiv.org/abs/1904.13264), [Code](https://github.com/babylonhealth/fuzzymax/blob/master/similarity/fuzzy.py). |
| SIMILARITY_METHOD_DYNAMAX_DICE | 4 | DynaMax Dice. [Paper](https://arxiv.org/abs/1904.13264), [Code](https://github.com/babylonhealth/fuzzymax/blob/master/similarity/fuzzy.py). |
| SIMILARITY_METHOD_DYNAMAX_OTSUKA | 5 | DynaMax Otsuka. [Paper](https://arxiv.org/abs/1904.13264), [Code](https://github.com/babylonhealth/fuzzymax/blob/master/similarity/fuzzy.py). |
| SIMILARITY_METHOD_WMD | 6 | Word Mover&#39;s Distance [Gensim Tutorial](https://radimrehurek.com/gensim/auto_examples/tutorials/run_wmd.html). |
| SIMILARITY_METHOD_EDIT | 7 | Levenshtein distance. [Wikipedia](https://en.wikipedia.org/wiki/Levenshtein_distance). |
| SIMILARITY_METHOD_JACCARD | 8 | Jaccard similarity. [Wikipedia](https://en.wikipedia.org/wiki/Jaccard_index). |
| SIMILARITY_METHOD_ANGULAR | 9 | Angular distance. [Wikipedia](https://en.wikipedia.org/wiki/Angular_distance). |


 

 


<a name="arg_services-nlp-v1-NlpService"></a>

### NlpService
Service for offloading computationally complex NLP tasks.

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| Vectors | [VectorsRequest](#arg_services-nlp-v1-VectorsRequest) | [VectorsResponse](#arg_services-nlp-v1-VectorsResponse) | Compute embeddings (i.e., vectors) for strings. |
| Similarities | [SimilaritiesRequest](#arg_services-nlp-v1-SimilaritiesRequest) | [SimilaritiesResponse](#arg_services-nlp-v1-SimilaritiesResponse) | Compute the similarity score between two strings. |
| DocBin | [DocBinRequest](#arg_services-nlp-v1-DocBinRequest) | [DocBinResponse](#arg_services-nlp-v1-DocBinResponse) | Process strings by spacy and return them as [binary data](https://spacy.io/api/docbin). Locally, spacy can restore this data **without** loading the underlying NLP models into the main memory. Allows one to retrieve all computed attributes (e.g., POS tags, sentences), but can only be used by Python programs. |

 



<a name="arg_services_retrieval_v1_retrieval-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## arg_services/retrieval/v1/retrieval.proto



<a name="arg_services-retrieval-v1-Mapping"></a>

### Mapping



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| query_id | [string](#string) |  |  |
| case_id | [string](#string) |  |  |
| similarity | [double](#double) |  |  |






<a name="arg_services-retrieval-v1-RetrieveRequest"></a>

### RetrieveRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| cases | [RetrieveRequest.CasesEntry](#arg_services-retrieval-v1-RetrieveRequest-CasesEntry) | repeated |  |
| query_graph | [arg_services.graph.v1.Graph](#arg_services-graph-v1-Graph) |  |  |
| query_text | [string](#string) |  |  |
| nlp_config | [arg_services.nlp.v1.NlpConfig](#arg_services-nlp-v1-NlpConfig) |  |  |
| limit | [int32](#int32) |  |  |
| mac_phase | [bool](#bool) |  |  |
| fac_phase | [bool](#bool) |  |  |
| mapping_algorithm | [MappingAlgorithm](#arg_services-retrieval-v1-MappingAlgorithm) |  |  |
| use_scheme_ontology | [bool](#bool) |  |  |
| enforce_scheme_types | [bool](#bool) |  |  |






<a name="arg_services-retrieval-v1-RetrieveRequest-CasesEntry"></a>

### RetrieveRequest.CasesEntry



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [string](#string) |  |  |
| value | [arg_services.graph.v1.Graph](#arg_services-graph-v1-Graph) |  |  |






<a name="arg_services-retrieval-v1-RetrieveResponse"></a>

### RetrieveResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| ranking | [RetrievedCase](#arg_services-retrieval-v1-RetrievedCase) | repeated |  |
| mac_ranking | [RetrievedCase](#arg_services-retrieval-v1-RetrievedCase) | repeated |  |
| fac_ranking | [RetrievedMapping](#arg_services-retrieval-v1-RetrievedMapping) | repeated |  |






<a name="arg_services-retrieval-v1-RetrievedCase"></a>

### RetrievedCase



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| similarity | [double](#double) |  |  |






<a name="arg_services-retrieval-v1-RetrievedMapping"></a>

### RetrievedMapping



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| case | [RetrievedCase](#arg_services-retrieval-v1-RetrievedCase) |  |  |
| node_mappings | [Mapping](#arg_services-retrieval-v1-Mapping) | repeated |  |





 


<a name="arg_services-retrieval-v1-MappingAlgorithm"></a>

### MappingAlgorithm


| Name | Number | Description |
| ---- | ------ | ----------- |
| MAPPING_ALGORITHM_UNSPECIFIED | 0 |  |
| MAPPING_ALGORITHM_ASTAR | 1 |  |
| MAPPING_ALGORITHM_ISOMORPHISM | 2 |  |


 

 


<a name="arg_services-retrieval-v1-RetrievalService"></a>

### RetrievalService


| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| Retrieve | [RetrieveRequest](#arg_services-retrieval-v1-RetrieveRequest) | [RetrieveResponse](#arg_services-retrieval-v1-RetrieveResponse) |  |

 



<a name="arg_services_topic_modeling_v1_topic_modeling-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## arg_services/topic_modeling/v1/topic_modeling.proto



<a name="arg_services-topic_modeling-v1-Term"></a>

### Term



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| text | [string](#string) |  |  |
| score | [float](#float) |  |  |






<a name="arg_services-topic_modeling-v1-Topic"></a>

### Topic



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| count | [int64](#int64) |  |  |
| terms | [Term](#arg_services-topic_modeling-v1-Term) | repeated |  |






<a name="arg_services-topic_modeling-v1-TopicsRequest"></a>

### TopicsRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| documents | [string](#string) | repeated |  |
| config | [arg_services.nlp.v1.NlpConfig](#arg_services-nlp-v1-NlpConfig) |  |  |






<a name="arg_services-topic_modeling-v1-TopicsResponse"></a>

### TopicsResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| outliers | [Topic](#arg_services-topic_modeling-v1-Topic) |  |  |
| topics | [Topic](#arg_services-topic_modeling-v1-Topic) | repeated |  |





 

 

 


<a name="arg_services-topic_modeling-v1-TopicModelingService"></a>

### TopicModelingService


| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| Topics | [TopicsRequest](#arg_services-topic_modeling-v1-TopicsRequest) | [TopicsResponse](#arg_services-topic_modeling-v1-TopicsResponse) |  |

 



## Scalar Value Types

| .proto Type | Notes | C++ | Java | Python | Go | C# | PHP | Ruby |
| ----------- | ----- | --- | ---- | ------ | -- | -- | --- | ---- |
| <a name="double" /> double |  | double | double | float | float64 | double | float | Float |
| <a name="float" /> float |  | float | float | float | float32 | float | float | Float |
| <a name="int32" /> int32 | Uses variable-length encoding. Inefficient for encoding negative numbers – if your field is likely to have negative values, use sint32 instead. | int32 | int | int | int32 | int | integer | Bignum or Fixnum (as required) |
| <a name="int64" /> int64 | Uses variable-length encoding. Inefficient for encoding negative numbers – if your field is likely to have negative values, use sint64 instead. | int64 | long | int/long | int64 | long | integer/string | Bignum |
| <a name="uint32" /> uint32 | Uses variable-length encoding. | uint32 | int | int/long | uint32 | uint | integer | Bignum or Fixnum (as required) |
| <a name="uint64" /> uint64 | Uses variable-length encoding. | uint64 | long | int/long | uint64 | ulong | integer/string | Bignum or Fixnum (as required) |
| <a name="sint32" /> sint32 | Uses variable-length encoding. Signed int value. These more efficiently encode negative numbers than regular int32s. | int32 | int | int | int32 | int | integer | Bignum or Fixnum (as required) |
| <a name="sint64" /> sint64 | Uses variable-length encoding. Signed int value. These more efficiently encode negative numbers than regular int64s. | int64 | long | int/long | int64 | long | integer/string | Bignum |
| <a name="fixed32" /> fixed32 | Always four bytes. More efficient than uint32 if values are often greater than 2^28. | uint32 | int | int | uint32 | uint | integer | Bignum or Fixnum (as required) |
| <a name="fixed64" /> fixed64 | Always eight bytes. More efficient than uint64 if values are often greater than 2^56. | uint64 | long | int/long | uint64 | ulong | integer/string | Bignum |
| <a name="sfixed32" /> sfixed32 | Always four bytes. | int32 | int | int | int32 | int | integer | Bignum or Fixnum (as required) |
| <a name="sfixed64" /> sfixed64 | Always eight bytes. | int64 | long | int/long | int64 | long | integer/string | Bignum |
| <a name="bool" /> bool |  | bool | boolean | boolean | bool | bool | boolean | TrueClass/FalseClass |
| <a name="string" /> string | A string must always contain UTF-8 encoded or 7-bit ASCII text. | string | String | str/unicode | string | string | string | String (UTF-8) |
| <a name="bytes" /> bytes | May contain any arbitrary sequence of bytes. | string | ByteString | str | []byte | ByteString | string | String (ASCII-8BIT) |

