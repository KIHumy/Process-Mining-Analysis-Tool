import subprocess
import sys

subprocess.run(["docker", "compose", "up", "-d"])
subprocess.run([sys.executable, "cli.py"])