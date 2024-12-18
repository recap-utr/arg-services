# Argumentation Microservices

This project contains Protobuf definitions for building complex argumentation machines.
The idea is to facilitate a microservice-oriented architecture where individual parts can be swapped out easily.
Along with the Protobuf files, the project also contains code for generating libraries for multiple programming languages that are released as packages in their respective registries:

- [Python](https://pypi.org/project/arg-services/)
- [TypeScript](https://www.npmjs.com/package/arg-services)
- [Java](https://search.maven.org/artifact/de.uni-trier.recap/arg-services)

Documentation can be found at the [Buf Schema Registry](https://buf.build/recap/arg-services).

## Recommended Service Ports

- NLP: 50100
- Retrieval: 50200
- Adaptation: 50300
- Mining: 50500

## Useful Links and References

- AIFdb all schemes: <https://aifdb.org/schemes/all>
- AIFdb scheme: <https://aifdb.org/schemes/$ID>
- AIFdb descriptor: <https://aifdb.org/descriptors/$ID>
