# Process-Mining-Analysis-Tool
This is the infrastructure repo to built this Process Mining analysis tool.

# Usage
To run this tool you need a certain type of file structure. The structure should be as follows:

```text
someDirectoryName/
├── PMATinfra/ https://github.com/KIHumy/Process-Mining-Analysis-Tool
├── PMATSystem/ https://github.com/KIHumy/Process-Mining-Analysis-Tool-Analyser
├── PMATdependencies/ https://github.com/KIHumy/Process-Mining-Analysis-Tool-Process-Mining-Services-Dependencies
├── DPIM-as-docker-service/ https://github.com/KIHumy/DPIM-as-docker-service
├── extTLKC-as-docker-service/ https://github.com/KIHumy/TLKC-Privacy-Ext-as-docker-service
├── PRETSA-as-docker-service/ https://github.com/KIHumy/PRETSA-as-docker-service
└── SaCoFa-as-docker-service/ https://github.com/KIHumy/SaCoFa-as-docker-service
```

The name of the main directory can be chosen arbitrarily. However, the names of the other directories mus be exactly like in the docker compose file of PMATinfra. The URLs behind the directories show which repo has to be where. Use initially docker compose up --build to build all container images after this just use our start command. To end the first execution use strg+c this should end the first run after build.

To run the tool use the following command: python runProMinAnaToo.py
Note: It might be necessary to activate venv in the directory someDirectoryName and it might be that some additional requirements need to be installed over pip install. However most repos this service consist of have there own requirements lists. If there is still some import missing you need to install it.

If you want to execute the mentioned process mining algorithms use uploadTask or uploadAutoTask in the cli depending on wether you wish for a single run or an automated comparison. The cli asks you then to specify a task file. This task file is a json file with a specifc structure. If you want to see the structure type getComparisonTemplate in the cli. You can also type getComparisonTemplateForAutoComparison to receive a template for an automated comparison. You can then insert you variables in this template and upload it to the network with uploadTask or uploadAutoTask depending on what you want to execute.

To give the workers (the process mining algorithms) an event log to process you need to find the input directory of the network in the dockerNetworkDirectory of this repo. dockerNetworkDirectory/input/.
Note: Don't rely on the help command of the cli its not up to date.
Note: If you include DPIM it might crash and its not supported for privacy analysis anyway so please remove it from the template before you send it to the network.
Note: Do not rename any directorys in the dockerNetworkDirectory and do not rename dockerNetworkDirectory or docker compose might fail. And only type uploadTask or uploadAutoTask in the cli once the file you gave over the fileName variable really exists in the input directory.

For the usage of the programm to start the programm run the following file: runProMinAnaToo.py
then you can request a template over: getComparisonTemplate or getComparisonTemplateForAutoComparison
You can then fill in the template your run parameters but for the getComparisonTemplate make sure not to close the program or the template becomes unusable.
Then you can start a comparison with either: uploadTask or uploadAutoTask depending on your chosen template.
If you want to close the programm type close. If you want to look further in the instructions take a look at cli.py. But note some of these functions are old and not functional or they are incomplete and therfore without effect.
