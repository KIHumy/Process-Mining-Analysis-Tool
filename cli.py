import requests
import time
import json
import subprocess
import pathlib

def serverHealthcheck():
    while True:
        try:
            healthcheck = requests.get("http://localhost:60321/healthcheck")
            if healthcheck.status_code == 200:
                return
        except:
            print("Server is still starting up.")
            time.sleep(5)

def main():
    serverHealthcheck()

    initialServerMessage = requests.get("http://localhost:60321/")
    iniServMessage = initialServerMessage.json()
    print(iniServMessage)

    print("The analysis tool is starting. Awaiting instructions.")
    while True:
        instruction = input()

        if instruction == "help":
            print("The current commands are: close (closes the program) \n help (shows the available commands)")

        if instruction == "close":
            requests.post("http://localhost:60321/instruction", json= {"instruction":"shutdown"})
            print("The analysis tool will close now")
            subprocess.run(["docker", "compose", "down"])
            return
        
        if instruction == "comparison":
            userContinue = "yes"
            while userContinue == "yes":
                print("please enter the file name.")
                fileName = input()
                print("do you want to load additional files? If yes type yes.")
                userContinue = input()

        if instruction == "startNTest":
            print("Starting network test for the docker network.")
            serverNTRequestAnswer = requests.post("http://localhost:60321/instruction", json= {"instruction":"start_n_test"})
            print(serverNTRequestAnswer.json())
            ongoing = True
            while ongoing == True:
                time.sleep(5)
                answer = requests.post("http://localhost:60321/client/result/status", json= {"task":"network_test"})
                if answer.json() == {"status":"finished"}:
                    print("N test was successfull.")
                    ongoing = False
                elif answer.json() == {"status":"no_connected_workers"}:
                    print("No connected workers.")
                    ongoing = False
                else:
                    print(answer.json())

        if instruction == "returnSystemRequirements":
            print("Requesting system requirements.")
            requirements = requests.get("http://localhost:60321/system/requirements")
            print(json.dumps(requirements.json(), indent=3))
            openFile= open("netRequirements/netRequirements.json", "w")
            json.dump(requirements.json(), openFile, indent=3)

        if instruction == "uploadTask":
            print("Please provide a valid file name excluding the data type that exists in the netTasks directory. \n For example if you want to upload task1.json type task1.")
            taskFile = input()
            taskFilePath = pathlib.Path("netTasks/" + taskFile + ".json")
            print("Try to upload task.")
            if pathlib.Path.exists(taskFilePath):
                print("File found begin up-load.")
                openFile= open(taskFilePath, "r")
                jsonTaskInstructions = json.load(openFile)
                try:
                    messageStat = requests.post("http://localhost:60321/system/task/", json=jsonTaskInstructions)
                    messageStat.raise_for_status()
                    print("Upload was successful.")
                except:
                    print("Your template was rejected please submit a template that matches the requirements.")
                    print(messageStat.json())
            else:
                print("Your specified file does not exist, is not part of the directory netTasks or is not a .json file.")
                continue

        if instruction == "getComparisonTemplate":
            print("Requesting template from API server.")
            receivedTemplate = requests.post("http://localhost:60321/instruction", json= {"instruction":"send_template_for_workers"})
            print(receivedTemplate)
            print(json.dumps(receivedTemplate.json(), indent=3))
            openFile= open("netTasks/networkTaskTemplate.json", "w")
            json.dump(receivedTemplate.json(), openFile, indent=3)
                
if __name__ == "__main__":
    main()