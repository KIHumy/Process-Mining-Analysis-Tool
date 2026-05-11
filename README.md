# Process-Mining-Analysis-Tool
This is the infrastructure repo to built this Process Mining analysis tool.

# Usage
To run this tool you need a certain type of file structure. The structure should be as follows:

someDirectoryName/
├── PMATinfra/
├── PMATSystem/
├── PMATdependencies/
├── DPIM-as-docker-service/
├── extTLKC-as-docker-service/
├── PRETSA-as-docker-service/
└── SaCoFa-as-docker-service/

The name of the main directory can be chosen arbitrarily. However, the names of the other directories mus be exactly like in the docker compose file von PMATinfra.

To run the tool use the following command: python runProMinAnaToo.py
Note: It might be necessary to activate venv in the directory someDirectoryName and it might be that some additional requirements need to be installed over pip install. However most repos this service consist of have there own requirements lists. If there is still some import missing you need to install it.

If you want to execute the mentioned process mining algorithms use uploadTask in the cli. The cli asks you then to specify a task file. This task file is a json file with a specifc structure. If you want to see the structure type getComparisonTemplate in the cli. You can then insert you variables in this template and upload it to the network with uploadTask.

To give the workers (the process mining algorithms) an event log to process you need to find there input directory in the dockerNetworkDirectory of this repo. For example to send extTLKC-as-docker-service an event log make sure this event log is in dockerNetworkDirectory/workerFiles/extTLKC/input/.
Note: Do not rename any directorys in the dockerNetworkDirectory and do not rename dockerNetworkDirectory or docker compose might fail. And only type uploadTask in the cli ones the file you gave over the fileName variable really exists in the input directory.
